"""
Server
"""

import logging

import click

from server_sync import ServerSync


@click.command()
@click.option('--host',
              default='127.0.0.1',
              prompt='Enter host addr',
              type=str)
@click.option('--port',
              default='10001',
              prompt='Enter port',
              type=int)
@click.option('--destination',
              prompt='Enter destination directory',
              type=str)
@click.option('--debug', is_flag=True)
def server_app(host: str, port: int, destination: str, debug: bool):
    if debug:
        logging.basicConfig(level=logging.DEBUG)

    server = ServerSync(
        host=host,
        port=port,
        destination=destination,
    )
    try:
        server.start()
    except KeyboardInterrupt:
        pass
    finally:
        server.stop()


if __name__ == '__main__':
    server_app()
