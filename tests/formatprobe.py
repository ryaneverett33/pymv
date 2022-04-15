import sys
sys.path.insert(1, '../')
from pymv.mv import Mv

mov = Mv()
result = mov.Probe.probe('filename.mkv')
print(result.format.get_duration())
print(result.format.get_size())
result.format._print_debug()
for chapter in result.chapters:
    chapter._print_debug()
for stream in result.streams:
    stream._print_debug()