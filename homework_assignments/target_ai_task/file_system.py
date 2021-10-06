"""
File System
"""

import os
import logging
import gzip
import shutil
from typing import Generator


class FileSystem:
    """
    File System
    """

    def __init__(self, source_path, destination_path):
        self._source_path = source_path
        self._destination_path = destination_path

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self.host}, {self.port})'

    def _is_lock(self) -> bool:
        """
        Lock file checker.

        :return: True if the lock file exists, False otherwise
        """
        return os.path.isfile(
            os.path.join(
                self._source_path,
                'done',
            )
        )

    @staticmethod
    def mb_to_bytes(number_of_mb: int) -> int:
        """
        Converts megabytes to bytes.

        :param number_of_mb: Number of megabytes
        :return: Converted number of megabytes into number of bytes
        """
        return 1024 * 1024 * number_of_mb

    @staticmethod
    def kb_to_bytes(number_of_mb: int) -> int:
        """
        Converts kilobytes to bytes.

        :param number_of_mb: Number of kilobytes
        :return: Converted number of kilobytes into number of bytes
        """
        return 1024 * number_of_mb

    @staticmethod
    def to_gz(source_file: str, target_file: str) -> None:
        """
        Unzip gzip file

        :param source_file: Full path to the source file
        :param target_file: Full path to the destination gzip file
        """
        with open(source_file, 'rb') as file_in:
            with gzip.open(target_file, 'wb') as file_out:
                shutil.copyfileobj(file_in, file_out)

        return None

    @staticmethod
    def from_gz(source_file: str, target_file: str) -> None:
        """
        Unzip gzip file

        :param source_file: Full path to the source gzipped file
        :param target_file: Full path to the destination file
        """
        if not source_file.endswith('.gz'):
            return

        with gzip.open(source_file, 'rb') as file_in:
            with open(target_file, 'wb') as file_out:
                shutil.copyfileobj(file_in, file_out)

        return None

    @staticmethod
    def check_file_by_extension(source: str, extension: str) -> bool:
        for fname in os.listdir(f'{source}/.'):
            if fname.endswith(extension):
                return True

    @staticmethod
    def is_all_files_exist(source_path: str, files: list):
        for file_ in files:
            full_file_path = os.path.join(source_path, file_['name'])
            if not os.path.isfile(full_file_path) or os.path.getsize(full_file_path) != file_['size']:
                return False
        return True

    @staticmethod
    def get_files_with_size(source_path: str) -> Generator[str, None, None]:
        """

        :param source_path: Source path
        :return: File names
        """

        for entry in os.scandir(source_path):
            if not entry.name.startswith('.') and entry.is_file():
                yield {
                    'name': entry.name,
                    'size': os.path.getsize(os.path.join(source_path, entry.name))
                }

        return None

    @staticmethod
    def get_base_name_from_chunk_name(chunk_name: str) -> str:
        """
        Gets the base file name without extension.

        :param source_file: Full file path or file name
        :return: The base file name without extension
        """
        chunk_name = os.path.basename(chunk_name)
        chunk_name = os.path.splitext(chunk_name)[0]
        return '-'.join(chunk_name.split('-')[:-1])

    @staticmethod
    def split_equal(file_name: str, source_path: str, destination_path: str, chunk_size=1024) -> None:
        """
        Split a file into parts.

        :param file_name: File name
        :param source_path:
        :param destination_path:
        :param chunk_size: Size of the fake file in megabytes
        """
        chunk_size = FileSystem.kb_to_bytes(chunk_size)
        base_name, base_ext = os.path.splitext(os.path.basename(file_name))
        full_file_path = os.path.join(source_path, file_name)
        chunk_id = 0

        with open(full_file_path, 'rb') as file_read:
            while True:
                chunk = file_read.read(chunk_size)

                if not chunk:
                    break

                chunk_file_name = f'{base_name}-{chunk_id:07d}{base_ext}'
                chunk_file_name_gz = f'{base_name}-{chunk_id:07d}.gz'

                with open(os.path.join(destination_path, chunk_file_name), 'wb') as file_write:
                    file_write.write(chunk)

                # Archive the part of file
                FileSystem.to_gz(
                    source_file=os.path.join(source_path, chunk_file_name),
                    target_file=os.path.join(destination_path, chunk_file_name_gz)
                )

                # Remove the source part of file
                os.remove(os.path.join(source_path, chunk_file_name))

                chunk_id += 1

        os.remove(full_file_path)

        return None

    @staticmethod
    def chunk_merging(data_frame: bytes, destination_path: str):
        chunk_data = data_frame.get('data', b'')
        meta = data_frame.get('meta', {})
        chunk_name = meta.get('name', None)
        meta_chunks = meta.get('chunks', [])

        # get file name from the chunk name
        file_name = FileSystem.get_base_name_from_chunk_name(chunk_name)

        if chunk_name and chunk_data:
            logging.info(f'Received chunk: {chunk_name}')

            full_file_path = os.path.join(destination_path, chunk_name)

            with open(full_file_path, mode='wb') as f_handle:
                f_handle.write(chunk_data)

            if not FileSystem.is_all_files_exist(
                    source_path=destination_path,
                    files=meta_chunks
            ):
                return None

            logging.info('We got all the chunks of the file')

            with open(os.path.join(destination_path, file_name), 'wb') as f_out:
                for chunk in sorted(meta_chunks, key=lambda _: _['name']):
                    source_file = os.path.join(destination_path, chunk['name'])

                    if not source_file.endswith('.gz'):
                        continue

                    with gzip.open(source_file, 'rb') as f_in:
                        shutil.copyfileobj(f_in, f_out)

                    os.remove(source_file)
        return None
