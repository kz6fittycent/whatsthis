# This file is part of whatsthis. See LICENSE file for license information.
"""TODO."""

from whatsthis.distro import Distro


class Command(Distro):
    """TODO."""

    def __init__(self):
        """TODO."""
        super().__init__()

        self.paths = {
            'cpuinfo': 'proc/cpuinfo',
            'meminfo': 'proc/meminfo',
        }

    @property
    def arch(self):
        """TODO."""
        pass
