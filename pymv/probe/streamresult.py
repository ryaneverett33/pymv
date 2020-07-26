from pymv.tags import Tags

class StreamResult:
    raw_stream_obj = None
    tags = None

    def __init__(self, stream_obj):
        self.raw_stream_obj = stream_obj