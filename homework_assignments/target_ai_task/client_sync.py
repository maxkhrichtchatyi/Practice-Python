"""
ClientSync
"""

import os
import logging

import asyncio
import bson

from file_system import FileSystem


class ClientSync:
    """
    Client Sync class
    """

    def __init__(self, host: str, port: int, source: str,
                 loop: bool = None) -> None:
        """
        Initialize the class.  Add some detail here.

        :param host: Host address
        :param port: Port number
        :param loop: Event loop
        """
        self.host = host
        self.port = port
        self.source = source
        self._loop = loop or asyncio.get_event_loop()

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self.host}, {self.port})'

    async def task_builder(self):
        """
        Client tasks runner.
        """

        tasks = []

        # Select files for sending
        files = []

        for file_ in FileSystem.get_files_with_size(source_path=self.source):
            files.append({
                'name': file_['name'],
                'size': file_['size'],
            })

        meta = {
            'chunks': files
        }

        for file in files:
            task = asyncio.ensure_future(
                self.send_file(file_path=file['name'], **meta)
            )
            tasks.append(task)

        contents = await asyncio.gather(*tasks)

        return contents

    def start(self) -> None:
        """
        Start sync client.
        """

        logging.info('Client Sync is started')
        future = asyncio.ensure_future(self.task_builder())
        self._loop.run_until_complete(future)

    def stop(self) -> None:
        """
        Stop sync client.
        """

        self._loop.close()
        logging.info('Client Sync has been stopped')

    async def _echo(self, message):
        """
        Sender.

        :param message: Sending message
        """

        _, writer = await asyncio.open_connection(
            host=self.host,
            port=self.port,
            loop=self._loop
        )

        logging.info('Send the message')
        writer.write(message)
        await writer.drain()

        logging.info('Close the connection')
        writer.close()
        await writer.wait_closed()

    async def send_file(self, file_path: str, **meta):
        """
        Send file.

        :param file: Full file path
        :param meta: Meta information
        """
        full_file_path = os.path.join(self.source, file_path)

        with open(full_file_path, mode='rb') as f_handle:
            file_chunk = f_handle.read()

            # build data frame
            data_frame = {
                'data': file_chunk,
                'meta': {
                    'name': file_path,
                    'chunks': meta.get('chunks', [])
                }
            }

            # data frame to BSON
            bson_data_frame = bson.dumps(data_frame)

            await self._echo(bson_data_frame)
