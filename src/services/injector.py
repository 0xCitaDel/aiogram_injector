import random as rd
import os
import uuid

SRC_DIR_FILES = '/Users/0xcitadel/Applications/tempesta_bot/files'
DEST_DIR_FILES = '/Users/0xcitadel/Applications/tempesta_bot/files/tmp'

class Injector:
    def __init__(self, target_file: str, data):
        self.data: str = data
        self.target_file = target_file
        self.dest_file = str(rd.randint(1, 1000)) + self.target_file

    def inject_data(self):
        with open(self._get_file_path(SRC_DIR_FILES, self.target_file), 'rb') as binary:
            image_data = binary.read()
        new_dir = os.path.join(DEST_DIR_FILES, str(uuid.uuid4()))
        os.mkdir(new_dir)
        with open(os.path.join(new_dir, self.target_file), 'wb') as binary:
            binary.write(image_data + self._bytes_encode(self.data))

        return binary.name

    def _get_file_path(self, path, file):
        return os.path.join(path, file)

    def _get_new_file_name(self):
        return self._get_file_path(DEST_DIR_FILES, self.dest_file)

    def _bytes_encode(self, data: str):
        return data.encode('utf-8')
