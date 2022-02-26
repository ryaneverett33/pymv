import sys
sys.path.insert(1, '../')
from pymv.mv import Mv

mov = Mv()
result = mov.Probe.probe('filename.mkv')
print(f"Filename: {result.format.filename}, size: {result.format.size_str()}")
duration = result.format.duration_obj()
print(f"Duration timecode: {duration}, minute segment: {duration.minute}, second segment: {duration.second}")