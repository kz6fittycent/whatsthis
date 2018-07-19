# This file is part of whatsthis. See LICENSE file for license information.
"""TODO."""

import os
import subprocess


class Distro:
    """TODO."""

    def __init__(self, data_dir='/'):
        """TODO."""
        self.data_dir = data_dir
        self.paths = {}

    @staticmethod
    def execute(args, data=None, env=None, shell=False):
        """Subprocess wrapper.

        Args:
            args: command to run
            data: data to pass
            env: optional env to use
            shell: optional shell to use

        Returns:
            Tuple of stdout, stderr, return code

        """
        if isinstance(args, str):
            args = args.split(' ')

        try:
            process = subprocess.Popen(
                args,
                env=env,
                shell=shell,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
        except FileNotFoundError:
            return '', 'No such file or directory', 1

        (out, err) = process.communicate(data)

        out = '' if not out else out.rstrip().decode("utf-8")
        err = '' if not err else err.rstrip().decode("utf-8")

        return out, err, process.returncode

    def query(self, key, index, attribute):
        """TODO."""
        file_path = self.paths[key].format(index=index, attribute=attribute)
        return self.read(file_path)

    def read(self, file_path):
        """TODO."""
        with open(os.path.join(self.data_dir, file_path), 'r') as target:
            string = target.read()

        return string.rstrip()
