# This file is part of whatsthis. See LICENSE file for license information.
"""TODO."""

from whatsthis.instance.compute import Compute


class Processor(Compute):
    """TODO."""

    def __init__(self, index):
        """TODO."""
        super().__init__()
        self.index = index

    @property
    def cache(self):
        """TODO."""
        cache = {}
        for level in self.sysfs.query('cpu', self.index, 'cache'):
            self.sysfs.query('cpu_cache', self.index, '%s/type' % level)
            self.sysfs.query('cpu_cache', self.index, '%s/size' % level)
            self.sysfs.query('cpu_cache', self.index, '%s/level' % level)

        return cache

    @property
    def cores(self):
        """TODO."""
        return self.sysfs.query('cpu', self.index, 'toplogy/cores')

    @property
    def flags(self):
        """TODO."""
        return self.proc.cpuinfo

    @property
    def ghz_max(self):
        """TODO."""
        return self.sysfs.query('cpu', self.index, 'cpufreq/cpuinfo_max_freq')

    @property
    def ghz_min(self):
        """TODO."""
        return self.sysfs.query('cpu', self.index, 'cpufreq/cpuinfo_min_freq')

    @property
    def model(self):
        """TODO."""
        return self.proc.cpuinfo

    @property
    def threads(self):
        """TODO."""
        return self.sysfs.query('cpu', self.index, 'toplogy/threads')
