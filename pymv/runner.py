import subprocess
import sys

class runner():
    arguments = None
    executable = None

    def __init__(self, arguments, executable):
        self.arguments = arguments
        self.executable = executable

    # Return a tuple of returncode, stdout (if captured), and stderr (if captured)
    def run(self, capture_stdout=False, capture_stderr=False) -> tuple:
        argCopy = [self.executable]
        argCopy.extend(self.arguments)
        process = subprocess.run(argCopy, stdout=subprocess.PIPE if capture_stdout else sys.stdout,
                                stderr=subprocess.PIPE if capture_stderr else sys.stderr)
        return process.returncode, process.stdout, process.stderr
