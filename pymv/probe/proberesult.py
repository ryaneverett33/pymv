import typing

from .chapterresult import ChapterResult
from .streamresult import StreamResult
from .formatinfo import Format

class ProbeResult:
    def __init__(self, json_result: dict):
        if json_result is None:
            raise AttributeError("jsonobj is None")

        self._raw_json:dict = json_result
        self.streams:typing.List[StreamResult] = []
        self.chapters:typing.List[ChapterResult] = []
        self.format:Format = None

        if json_result["streams"] is not None:
            self._parse_streams(json_result["streams"])
        if json_result["chapters"] is not None:
            self._parse_chapters(json_result["chapters"])
        if json_result["format"] is not None:
            self.format = Format(json_result["format"])

    def _parse_streams(self, raw_streams):
        for stream in raw_streams:
            self.streams.append(StreamResult(stream))

    def _parse_chapters(self, raw_chapters):
        for chapter in raw_chapters:
            self.chapters.append(ChapterResult(chapter))

    def has_forced_subtitles(self) -> bool:
        pass