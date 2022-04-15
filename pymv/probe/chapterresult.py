import typing
from .tags import Tags
from . import parse_type, safe_get

class ChapterResult:
    def __init__(self, chapter_obj):
        self._raw_chapter_obj:dict = chapter_obj
        self.id:int = parse_type(safe_get(chapter_obj, 'id'), int)
        self.time_base:str = parse_type(safe_get(chapter_obj, 'time_base'), str)
        self.start:int = parse_type(safe_get(chapter_obj, 'start'), int)
        self.end:int = parse_type(safe_get(chapter_obj, 'end'), int)
        self.start_time:str = parse_type(safe_get(chapter_obj, 'start_time'), str)
        self.end_time:str = parse_type(safe_get(chapter_obj, 'end_time'), str)
        self.tags:Tags = Tags(safe_get(chapter_obj, 'tags'))

    def __getitem__(self, key: str) -> typing.Any:
        return self._raw_chapter_obj[key]

    def _print_debug(self):
        print("Chapter Info")
        print(f"\tId: {self.id}, time_base: {self.time_base}")
        print(f"\tstart_time: {self.start_time}, end_time: {self.end_time}")
        self.tags._print_debug()