"""
File Generator
"""

import os
import logging

from file_system import FileSystem


class FileGenerator(FileSystem):
    """
    File Generator
    """

    def __repr__(self) -> str:
        return f'{self.__class__.__name__})'

    @staticmethod
    def gen_lock_file(file_path: str, file_name: str):
        """
        Generate a lock file.

        :param file_path: Path of the fake file
        :param file_name: Name of the fake file
        """

        logging.info('The lock file generation had started')

        file_full_path = os.path.join(file_path, file_name)
        file_size = os.path.getsize(file_full_path)

        base_name, _ = os.path.splitext(os.path.basename(file_name))
        lock_file_name = f'{base_name}.done'

        lock_file_full_path = os.path.join(file_path, lock_file_name)

        with open(lock_file_full_path, 'w') as file_out:
            file_out.write(str(file_size))

        logging.info('The lock file generation is complete')

    @staticmethod
    def gen_fake_file(file_path: str, file_name: str, size: int) -> None:
        """
        Generate a fake file.

        :param file_path: Path of the fake file
        :param file_name: Name of the fake file
        :param size: Size of the fake file in megabytes
        """
        size = FileSystem.mb_to_bytes(size)
        file_full_path = os.path.join(file_path, file_name)

        logging.info('The fake file generation had started')

        with open(file_full_path, 'wb') as file_out:
            file_out.write(os.urandom(size))

        logging.info('The fake file generation is complete')
