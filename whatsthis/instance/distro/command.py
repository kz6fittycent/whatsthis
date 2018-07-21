# This file is part of whatsthis. See LICENSE file for license information.
"""TODO."""

from whatsthis.instance.distro import Distro


class Command(Distro):
    """TODO."""

    def __init__(self, data_dir='/'):
        """TODO."""
        super().__init__()
        self.data_dir = data_dir

    @property
    def arch(self):
        """TODO."""
        self.execute('arch')
