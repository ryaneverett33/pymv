import subprocess
import sys

class runner():
    arguments = None
    executable = None

    def __init__(self, arguments, executable):
        self.arguments = arguments
        self.executable = executable

    def run(self):
        argCopy = [self.executable]
        argCopy.extend(self.arguments)
        subprocess.run(argCopy, stdout=sys.stdout)
