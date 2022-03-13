import subprocess
import sys
import typing

class runner():
    arguments = None
    executable = None

    def __init__(self, arguments: typing.List[str], executable: str):
        self.arguments: typing.List[str] = arguments
        self.executable: str = executable

    # Return a tuple of returncode, stdout (if captured), and stderr (if captured)
    def run(self, capture_stdout: bool=False, capture_stderr: bool=False) -> typing.Tuple[int, str, str]:
        argCopy = [self.executable]
        argCopy.extend(self.arguments)
        process = subprocess.run(argCopy, stdout=subprocess.PIPE if capture_stdout else sys.stdout,
                                stderr=subprocess.PIPE if capture_stderr else sys.stderr)
        return process.returncode, process.stdout, process.stderr
