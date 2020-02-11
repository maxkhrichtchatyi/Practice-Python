import time
import logging

import click

from file_system import FileSystem
from client_sync import ClientSync


@click.command()
@click.option('--host',
              default='127.0.0.1',
              prompt='Enter host addr',
              type=str)
@click.option('--port',
              default='10001',
              prompt='Enter port',
              type=int)
@click.option('--source',
              prompt='Enter source directory',
              type=str)
@click.option('--debug', is_flag=True)
def client_app(host: str, port: int, source: str, debug: bool):
    if debug:
        logging.basicConfig(level=logging.DEBUG)

    while True:
        if FileSystem.check_file_by_extension(source, '.done'):
            client = ClientSync(
                host=host,
                port=port,
                source=source,
            )
            try:
                client.start()
            except KeyboardInterrupt:
                pass
            finally:
                client.stop()

            break

        time.sleep(2)

        logging.info('Waiting for .done')


if __name__ == '__main__':
    client_app()
