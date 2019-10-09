from enum import Enum

class StreamType(Enum):
    Video = 10
    Audio = 20
    Subtitle = 30
    
    def get_stream_qualifier(self):
        if self is StreamType.Video:
            return 'v'
        elif self is StreamType.Audio:
            return 'a'
        elif self is StreamType.Subtitle:
            return 's'
