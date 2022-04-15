import typing

from . import parse_type, safe_get

class CodecInfo:
    def __init__(self, stream_info:dict):
        self._raw_stream_info:dict = stream_info
        self.name:str = parse_type(safe_get(stream_info, 'codec_name'), str)
        self.long_name:str = parse_type(safe_get(stream_info, 'codec_long_name'), str)
        self.type:str = parse_type(safe_get(stream_info, 'codec_type'), str)
        self.time_base:str = parse_type(safe_get(stream_info, 'codec_time_base'), str)
        self.tag_string:str = parse_type(safe_get(stream_info, 'codec_tag_string'), str)
        self.tag:str = parse_type(safe_get(stream_info, 'codec_tag'), str)

    def __getitem__(self, key:str) -> typing.Any:
        return self._raw_stream_obj[key]

    def is_video_stream(self) -> bool:
        return self.type == "video"
    
    def is_audio_stream(self) -> bool:
        return self.type == "audio"
    
    def is_subtitle_stream(self) -> bool:
        return self.type == "subtitle"

    def _print_debug(self):
        print("Codec Info:")
        print(f"\tName: {self.name}, Long Name: {self.long_name}")
        print(f"\tType: {self.type}, Tag: {self.tag}, Tag String: {self.tag_string}, Time Base: {self.time_base},")