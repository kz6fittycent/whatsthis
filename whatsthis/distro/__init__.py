# This file is part of whatsthis. See LICENSE file for license information.
"""TODO."""

import os

LEXICON = {}


class Distro:
    """TODO."""

    def __init__(self, data_dir='/'):
        """TODO."""
        self.data_dir = data_dir

    def query(self, key, index, attribute):
        """TODO."""
        return self.read(LEXICON[key].format(index, attribute))

    def read(self, file_path):
        """TODO."""
        with open(os.path.join(self.data_dir, file_path), 'r') as target:
            string = target.read()

        return string.rstrip()
