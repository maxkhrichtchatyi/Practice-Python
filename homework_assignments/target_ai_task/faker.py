"""
Faker
"""

import logging

import click

from file_generator import FileGenerator
from file_system import FileSystem


@click.command()
@click.option('--destination',
              prompt='Enter the destination directory',
              type=str)
@click.option('--file_size',
              prompt='Enter the fake file size in Mb',
              type=int)
@click.option('--chunk_size',
              prompt='Enter a chunk size in Kb',
              type=int)
@click.option('--debug', is_flag=True)
def app(destination: str, file_size: int, chunk_size: int, debug=False):
    """
    Simple program that creates fake a file, splits the file into chunks
    and makes lock file.
    """
    if debug:
        logging.basicConfig(level=logging.DEBUG)

    file_name = 'data'

    # Generate a fake file
    FileGenerator.gen_fake_file(
        file_path=destination,
        file_name=file_name,
        size=file_size,
    )

    # Generate a lock file
    FileGenerator.gen_lock_file(
        file_path=destination,
        file_name=file_name,
    )

    # Split the fake file into chunks
    FileSystem.split_equal(
        file_name=file_name,
        source_path=destination,
        destination_path=destination,
        chunk_size=chunk_size,
    )


if __name__ == '__main__':
    app()
