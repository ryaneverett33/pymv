import typing

from . import parse_type, safe_get

class StreamInfo:
    def __init__(self, stream_info: dict):
        self._raw_stream_info:dict = stream_info
        self.r_frame_rate:str = parse_type(safe_get(stream_info, "r_frame_rate"), str)
        self.avg_frame_rate:str = parse_type(safe_get(stream_info, "avg_frame_rate"), str)

    def __getitem__(self, key:str) -> typing.Any:
        return self._raw_stream_info[key]

    def _print_debug(self):
        if self == AudioStreamInfo:
            print("Audio Info:")
        elif self == VideoStreamInfo:
            print("Video Info:")
        elif self == SubtitleStreamInfo:
            print("Subtitle Info:")
        else:
            print("Stream Info:")
        print(f"\tr frame rate: {self.r_frame_rate}, average frame rate: {self.avg_frame_rate}")

class AudioStreamInfo(StreamInfo):
    def __init__(self, stream_info: dict):
        super().__init__(stream_info)
        self.sample_fmt:str = parse_type(safe_get(stream_info, "sample_fmt"), str)
        self.sample_rate:str = parse_type(safe_get(stream_info, "sample_rate"), str)
        self.channels:int = parse_type(safe_get(stream_info, "channels"), int)
        self.channel_layout:str = parse_type(safe_get(stream_info, "channel_layout"), str)
        self.bits_per_sample:int = parse_type(safe_get(stream_info, "bits_per_sample"), int)
        self.bits_per_raw_sample:str = parse_type(safe_get(stream_info, "bits_per_raw_sample"), int)

    def _print_debug(self):
        super()._print_debug()
        print(f"\tsample format: {self.sample_fmt}, sample rate: {self.sample_rate}")
        print(f"\tchannels: {self.channels}, channel layout: {self.channel_layout}")
        print(f"\tbits per sample: {self.bits_per_sample}, bits per raw sample: {self.bits_per_raw_sample}")

class VideoStreamInfo(StreamInfo):
    def __init__(self, stream_info: dict):
        super().__init__(stream_info)
        self.profile:str = parse_type(safe_get(stream_info, "profile"), str)
        self.width:int = parse_type(safe_get(stream_info, "width"), int)
        self.height:int = parse_type(safe_get(stream_info, "height"), int)
        self.coded_width:int = parse_type(safe_get(stream_info, "coded_width"), int)
        self.coded_height:int = parse_type(safe_get(stream_info, "coded_height"), int)
        self.has_b_frames:bool = parse_type(safe_get(stream_info, "has_b_frames"), bool)
        self.sample_aspect_ratio:str = parse_type(safe_get(stream_info, "sample_aspect_ratio"), str)
        self.display_aspect_ratio:str = parse_type(safe_get(stream_info, "display_aspect_ratio"), str)
        self.pix_fmt:str = parse_type(safe_get(stream_info, "pix_fmt"), str)
        self.level:int = parse_type(safe_get(stream_info, "level"), int)
        self.color_range:str = parse_type(safe_get(stream_info, "color_range"), str)
        self.color_space:str = parse_type(safe_get(stream_info, "color_space"), str)
        self.color_transfer:str = parse_type(safe_get(stream_info, "color_transfer"), str)
        self.color_primaries:str = parse_type(safe_get(stream_info, "color_primaries"), str)
        self.refs:int = parse_type(safe_get(stream_info, "refs"), int)

    def _print_debug(self):
        super()._print_debug()
        print(f"\tprofile: {self.profile}, level: {self.level}, refs: {self.refs}")
        print(f"\twidth: {self.width}, height: {self.height}, coded width: {self.coded_width}, coded height: {self.coded_height}")
        print(f"\tsample aspect ratio: {self.sample_aspect_ratio}, display aspect ratio: {self.display_aspect_ratio}, has b frames? {self.has_b_frames}")
        print(f"\tcolor range: {self.color_range}, color space: {self.color_space}, color transfer: {self.color_transfer}, color primaries: {self.color_primaries}")

class SubtitleStreamInfo(StreamInfo):
    def __init__(self, stream_info: dict):
        super().__init__(stream_info)

    def _print_debug(self):
        super()._print_debug()