# This file is part of whatsthis. See LICENSE file for license information.
"""TODO."""

from whatsthis.instance.compute import Compute
from whatsthis.instance.distro.command import Command
from whatsthis.instance.distro.proc import Proc
from whatsthis.instance.distro.sysfs import Sysfs


class Instance:
    """TODO."""

    def __init__(self, data_dir=''):
        """TODO."""
        self.cmd = Command(data_dir)
        self.proc = Proc(data_dir)
        self.sysfs = Sysfs(data_dir)

    @property
    def arch(self):
        """TODO."""
        return self.cmd.arch

    @property
    def memory(self):
        """TODO."""
        meminfo = self.proc.meminfo

        # MemTotal size in Kb
        total = meminfo[0].split(' ')[-2]

        return total

    @property
    def compute(self):
        """TODO."""
        compute = Compute()

        return compute.cores
