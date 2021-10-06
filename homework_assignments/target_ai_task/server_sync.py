"""
ServerSync
"""

import os
import logging

import asyncio
import bson

from file_system import FileSystem


class ServerSync:
    """
    Server Sync class
    """

    def __init__(self, host: str, port: int, destination: str,
                 loop: bool = None) -> None:
        """
        Initialize the class.  Add some detail here.

        :param host: Host address
        :param port: Port number
        :param destination: The directory to which the results will be stored
        :param loop: Event loop
        """
        self.host = host
        self.port = port
        self.destination = destination
        self._loop = loop or asyncio.get_event_loop()
        self._server = asyncio.start_server(
            client_connected_cb=self._handle_echo,
            host=host,
            port=port,
            loop=self._loop
        )

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self.host}, {self.port})'

    def start(self, loop: bool = True) -> None:
        """
        Start sync server.

        :param loop: Run the sync server until stop() is called
        """
        logging.info('SyncServer is started')

        self._server = self._loop.run_until_complete(self._server)

        logging.info(f'Listening established on: '
                     f'{self._server.sockets[0].getsockname()}')

        if loop:
            self._loop.run_forever()

    def stop(self, loop: bool = True) -> None:
        """
        Stop sync server.

        :param loop: Close the loop
        """

        self._server.close()

        if loop:
            self._loop.close()

        logging.info('SyncServer has been stopped')

    async def _handle_echo(self, reader, writer):
        """
        Callback.

        :param reader: a StreamReader object
        :param writer: a StreamWriter object
        """
        peer_name = writer.get_extra_info('peername')
        logging.info(f'Accepted connection from {peer_name}')

        received_data = await reader.read()

        # parse information from the received data
        data_frame = bson.loads(received_data)

        FileSystem.chunk_merging(
            data_frame=data_frame,
            destination_path=self.destination
        )

        writer.close()
