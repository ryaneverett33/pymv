from .tags import Tags

class StreamResult:
    _raw_stream_obj = None
    tags = None
    index = -1
    codec_type = None

    def __init__(self, stream_obj):
        self._raw_stream_obj = stream_obj

    def __getitem__(self, key):
        return self._raw_stream_obj[key]