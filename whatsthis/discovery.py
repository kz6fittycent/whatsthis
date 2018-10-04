# This file is part of whatsthis. See LICENSE file for license information.
"""TODO."""

import logging

from whatsthis.compositors.cli import CLICompositor
from whatsthis.compositors.json import JSONCompositor
from whatsthis.instance import Instance


class Discovery:
    """TODO."""

    def __init__(self, output_formatter='cli', data_dir=None):
        """TODO."""
        self._log = logging.getLogger(__name__)

        self.data = {}
        self.instance = Instance(data_dir)

        discovery_objects = [
            self.cloud,
            self.compute,
            self.container,
            self.distro,
            self.io,
            self.virtualization,
        ]
        for method in discovery_objects:
            method()

        if output_formatter == 'json':
            compositor = JSONCompositor(self.data)
        elif output_formatter == 'cli':
            compositor = CLICompositor(self.data)

        compositor.print()

    def cloud(self):
        """TODO."""
        pass

    def compute(self):
        """TODO."""
        compute = instance.compute()

    def container(self):
        """TODO."""
        pass

    def distro(self):
        """TODO."""
        pass

    def io(self):
        """TODO."""
        pass

    def virtualization(self):
        """TODO."""
        pass
