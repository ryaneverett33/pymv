from pymv.probe.proberesult import ProbeResult
import os
import subprocess
import json

class prober():
    def __init__(self, executable: str="ffprobe"):
        self.executable: str = executable

    def probe(self, filename: str):
        if not os.path.isfile(filename):
            raise Exception("File does not exist")
        args = [self.executable, '-v', 'quiet', '-print_format', 'json',
        '-show_format', '-show_streams', '-show_chapters', filename]
        # result.stdout && result.stderr
        result = subprocess.run(args, capture_output=True)
        if len(result.stdout) == 0:
            raise Exception("Unable to probe file, error occurred")
        jsonobj = None
        try:
            jsonobj = json.loads(result.stdout)
        except ValueError:
            raise Exception("Unable to probe file, failure occuring parsing result")
        return ProbeResult(jsonobj)