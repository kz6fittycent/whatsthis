# This file is part of whatsthis. See LICENSE file for license information.
"""TODO."""

import json

from whatsthis.compositors import Compositor


class JSONCompositor(Compositor):
    """TODO."""

    def __init__(self, data):
        """TODO."""
        self.data = data

    def print(self):
        """TODO."""
        print('json output')
        print(json.dumps(self.data, indent=4, sort_keys=True))
