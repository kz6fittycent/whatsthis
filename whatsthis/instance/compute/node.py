# This file is part of whatsthis. See LICENSE file for license information.
"""TODO."""

from whatsthis.instance.compute import Compute


class Node(Compute):
    """TODO."""

    def __init__(self, index):
        """TODO."""
        super().__init__()
        self.index = index

    @property
    def cpu(self):
        """TODO."""
        return self.sysfs.query('node', self.index, 'cpulist')

    @property
    def memory(self):
        """TODO."""
        return self.sysfs.query('node', self.index, 'meminfo')

    @property
    def numa_distance(self):
        """TODO."""
        return self.sysfs.query('node', self.index, 'distance')
