# This file is part of whatsthis. See LICENSE file for license information.
"""TODO."""

import os


class Distro:
    """TODO."""

    def __init__(self, data_dir='/'):
        """TODO."""
        self.data_dir = data_dir
        self.paths = {}

    def query(self, key, index, attribute):
        """TODO."""
        file_path = self.paths[key].format(index=index, attribute=attribute)
        return self.read(file_path)

    def read(self, file_path):
        """TODO."""
        with open(os.path.join(self.data_dir, file_path), 'r') as target:
            string = target.read()

        return string.rstrip()
