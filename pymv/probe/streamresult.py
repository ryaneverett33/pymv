import typing

from .tags import Tags
from .streaminfo import *
from .codecinfo import CodecInfo
from .dispositioninfo import DispositionInfo
from . import parse_type, safe_get

class StreamResult:
    def __init__(self, stream_obj):
        self._raw_stream_obj:dict = stream_obj
        self.index:int = parse_type(stream_obj['index'], int)
        self.codec_info:CodecInfo = CodecInfo(stream_obj)
        self.stream_info:StreamInfo = None
        if self.is_audio_stream():
            self.stream_info = AudioStreamInfo(stream_obj)
        elif self.is_video_stream():
            self.stream_info = VideoStreamInfo(stream_obj)
        else:
            self.stream_info = SubtitleStreamInfo(stream_obj)
        self.start_pts:int = parse_type(safe_get(stream_obj, 'start_pts'), int)
        self.start_time:str = parse_type(safe_get(stream_obj, 'start_time'), str)
        self.duration_ts:int = parse_type(safe_get(stream_obj, 'duration_ts'), int)
        self.duration:str = parse_type(safe_get(stream_obj, 'duration'), str)
        self.disposition:DispositionInfo = DispositionInfo(stream_obj)
        self.tags:Tags = Tags(safe_get(stream_obj, 'tags'))

    def __getitem__(self, key:str) -> typing.Any:
        return self._raw_stream_obj[key]

    def is_video_stream(self) -> bool:
        return self.codec_info.is_video_stream()
    
    def is_audio_stream(self) -> bool:
        return self.codec_info.is_audio_stream()
    
    def is_subtitle_stream(self) -> bool:
        return self.codec_info.is_subtitle_stream()

    def _print_debug(self):
        print(f"Index: {self.index}")
        print(f"start_pts: {self.start_pts}, start_time: {self.start_time}, duration_ts: {self.duration_ts}, duration: {self.duration}")
        self.codec_info._print_debug()
        self.stream_info._print_debug()
        self.disposition._print_debug()
        self.tags._print_debug()