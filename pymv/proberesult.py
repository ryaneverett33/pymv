from pymv.chapterresult import ChapterResult
from pymv.streamresult import StreamResult
from pymv.format import Format

class ProbeResult:
    raw_json = None     # The orginal json object to create the object
    streams = None      # Array of StreamResult objects
    chapters = None     # Array of ChapterResult objects
    format = None       # Format object or None

    def __init__(self, jsonobj):
        if jsonobj is None:
            raise AttributeError("jsonobj is None")
        self.raw_json = jsonobj
        raw_streams = jsonobj["streams"]
        raw_chapters = jsonobj['chapters']
        raw_format = jsonobj['format']

        if raw_streams is not None:
            self.streams = []
            self._parse_streams(raw_streams)
        if raw_chapters is not None:
            self.chapters = []
            self._parse_chapters(raw_chapters)
        if raw_format is not None:
            self.format = Format(raw_format)

    def _parse_streams(self, raw_streams):
        for stream in raw_streams:
            self.streams.append(StreamResult(stream))

    def _parse_chapters(self, raw_chapters):
        for chapter in raw_chapters:
            self.chapters.append(ChapterResult(chapter))

    