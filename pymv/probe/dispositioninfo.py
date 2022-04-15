import typing
from . import parse_type, safe_get

class DispositionInfo:
    def __init__(self, stream_info:dict):
        self._raw_stream_info:dict = stream_info
        self.default:bool = parse_type(safe_get(stream_info, 'default'), bool)
        self.dub:bool = parse_type(safe_get(stream_info, 'dub'), bool)
        self.original:bool = parse_type(safe_get(stream_info, 'original'), bool)
        self.comment:bool = parse_type(safe_get(stream_info, 'comment'), bool)
        self.lyrics:bool = parse_type(safe_get(stream_info, 'lyrics'), bool)
        self.karaoke:bool = parse_type(safe_get(stream_info, 'karaoke'), bool)
        self.forced:bool = parse_type(safe_get(stream_info, 'forced'), bool)
        self.hearing_impaired:bool = parse_type(safe_get(stream_info, 'hearing_impaired'), bool)
        self.visual_impaired:bool = parse_type(safe_get(stream_info, 'visual_impaired'), bool)
        self.clean_effects:bool = parse_type(safe_get(stream_info, 'clean_effects'), bool)
        self.attached_pic:bool = parse_type(safe_get(stream_info, 'attached_pic'), bool)
        self.timed_thumbnails:bool = parse_type(safe_get(stream_info, 'timed_thumbnails'), bool)

    def __getitem__(self, key:str) -> typing.Any:
        return self._raw_stream_info[key]

    def _print_debug(self):
        print("Disposition Info:")
        print(f"\tDefault? {self.default} Dub? {self.dub} Original? {self.original} Comment? {self.comment} Lyrics? {self.lyrics}")
        print(f"\tKaraoke? {self.karaoke} Forced? {self.forced} Hearing Impaired? {self.hearing_impaired} Visual Impaired? {self.visual_impaired}")
        print(f"\tClean Effects? {self.clean_effects} Attached Picture? {self.attached_pic} Timed Thumbnails? {self.timed_thumbnails}")