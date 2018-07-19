# This file is part of whatsthis. See LICENSE file for license information.
"""TODO."""

from whatsthis.distro import Distro


class Sysfs(Distro):
    """TODO."""

    def __init__(self):
        """TODO."""
        super().__init__()

        self.paths = {
            'cpu': 'sys/devices/system/cpu/cpu{index}/{attribute}',
            'cpu_cache': 'sys/devices/system/cpu/cpu{index}/cache/{attribute}',
            'node': 'sys/devices/system/node/node{index}/{attribute}',
        }
