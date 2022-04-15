import datetime
import math
import typing

from .tags import Tags
from . import parse_type, safe_get

class Format:
    __SIZE_ARR = ['B', 'KB', 'MB', 'GB', 'TB', 'PB']

    def __init__(self, format_obj):
        self._raw_format_obj:dict = format_obj
        self.filename:str = parse_type(safe_get(format_obj, 'filename'), str)
        self.num_streams:int = parse_type(safe_get(format_obj, 'nb_streams'), int)
        self.num_programs:int = parse_type(safe_get(format_obj, 'nb_programs'), int)
        self.name:str = parse_type(safe_get(format_obj, 'format_name'), str)
        self.long_name:str = parse_type(safe_get(format_obj, 'format_long_name'), str)
        self.start_time:str = parse_type(safe_get(format_obj, 'start_time'), str)
        self.duration:str = parse_type(safe_get(format_obj, 'duration'), str)
        self.size:str = parse_type(safe_get(format_obj, 'size'), str)
        self.bit_rate:str = parse_type(safe_get(format_obj, 'bit_rate'), str)
        self.probe_score:int = parse_type(safe_get(format_obj, 'probe_score'), int)
        self.tags:Tags = Tags(safe_get(format_obj, 'tags'))

    def _print_debug(self):
        print(f"Format Info:")
        print(f"\tfilename: {self.filename}, size: {self.size}, number of streams: {self.num_streams}, number of programs: {self.num_programs}")
        print(f"\tname: {self.name}, long name: {self.long_name}, start time: {self.start_time}, duration: {self.duration}")
        print(f"\tBit rate: {self.bit_rate}, probe score: {self.probe_score}")
        self.tags._print_debug()

    def get_duration(self) -> typing.Union[None, datetime.time]:
        """Get duration as a time object"""
        if self.duration is None:
            return None
        duration_float = parse_type(self.duration, float)
        minutes, hours = math.modf(duration_float / 3600)
        seconds, minutes = math.modf(minutes * 60)
        ms, seconds = math.modf(seconds * 60)
        ms = ms * 1000
        return datetime.time(hour=int(hours), minute=int(minutes), second=int(seconds), microsecond=int(ms * 1000))

    def get_size(self) -> typing.Union[None, str]:
        """Get size of the file in a friendly format"""
        if self.size is None:
            return None

        steps = 0   # The number of times we've reduced the size
        current_size = parse_type(self.size, int)

        while current_size > 1e3:
            # Iteratively divide by a thousand until the number fits in a contained unit
            tmp_current_size = current_size / 1e3
            if tmp_current_size <= 1e3:
                # Don't convert to float until the end
                current_size = float(current_size) / 1e3
            else:
                current_size = tmp_current_size
            
            steps = steps + 1
        return f"{current_size:.3f} {Format.__SIZE_ARR[steps]}"
        