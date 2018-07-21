# This file is part of whatsthis. See LICENSE file for license information.
"""TODO."""

from whatsthis.compositors import Compositor


class JSONCompositor(Compositor):
    """TODO."""

    def __init__(self, data):
        """TODO."""
        self.data = data

    def print(self):
        """TODO."""
        print('json output')
        print(self.data)
