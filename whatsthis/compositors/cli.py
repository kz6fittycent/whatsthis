# This file is part of whatsthis. See LICENSE file for license information.
"""TODO."""

from whatsthis.compositors import Compositor


class CLICompositor(Compositor):
    """TODO."""

    def __init__(self, data):
        """TODO."""
        self.data = data

    def print(self):
        """TODO."""
        print('cli output')
        print(self.data)
