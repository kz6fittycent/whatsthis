# This file is part of whatsthis. See LICENSE file for license information.
"""TODO."""

from whatsthis.distro import Distro


class Proc(Distro):
    """TODO."""

    def __init__(self):
        """TODO."""
        super().__init__()

        self.paths = {
            'cpuinfo': 'proc/cpuinfo',
            'meminfo': 'proc/meminfo',
        }

    @property
    def cpuinfo(self):
        """TODO."""
        return self.read(self.paths['cpuinfo'])

    @property
    def meminfo(self):
        """TODO."""
        return self.read(self.paths['meminfo'])
