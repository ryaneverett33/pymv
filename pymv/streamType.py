import typing
from enum import Enum

class StreamType(Enum):
    Video = 1
    Audio = 2
    Subtitle = 4
    Unknown = 8
    
    def get_stream_qualifier(self):
        if self is StreamType.Video:
            return 'v'
        elif self is StreamType.Audio:
            return 'a'
        elif self is StreamType.Subtitle:
            return 's'
        else:
            return ''
