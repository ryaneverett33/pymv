from pymv.ffcommand import ffcommand
from pymv.StreamType import StreamType

class metadatainfo(ffcommand):
    base_data = None            # Metadata info for the container
    stream_data = None          # Dict of list of Metadata info (key/value) for streams


    def __init__(self):
        self.base_data = []
        self.stream_data = dict()

    def set_value(self, key, value):
        self.base_data.append(Info(key, value))
        return self

    def Video(self, key, value, streamIndex=None):
        return self.set_value_of_stream(key, value, StreamType.Video, streamIndex)

    def Audio(self, key, value, streamIndex=None):
        return self.set_value_of_stream(key, value, StreamType.Audio, streamIndex)

    def Subtitle(self, key, value, streamIndex=None):
        return self.set_value_of_stream(key, value, StreamType.Subtitle, streamIndex)

    def set_value_of_stream(self, key, value, streamType, streamIndex):
        if streamType is None or streamIndex is None:
            raise AttributeError('streamType or streamIndex attributes not given')
        if not isinstance(streamType, StreamType) or not isinstance(streamIndex, int):
            raise AttributeError('streamType must be a StreamType enum and streamIndex must be an int')
        if streamType not in self.stream_data:
            self.stream_data[streamType] = list()
        self.stream_data[streamType].append(StreamValue(streamIndex, Info(key, value)))
        sorted(self.stream_data[streamType], key=lambda value: value.index)
        return self

    def to_args(self):
        args = []
        if self.base_data is not None:
            for inf in self.base_data:
                args.append('-metadata')
                args.append("{0}={1}".format(inf.key, inf.value))
        if self.stream_data is not None:
            for stype in self.stream_data.keys():
                for value in self.stream_data[stype]:
                    args.append('-metadata:s:{0}:{1}'.format(stype.get_stream_qualifier(), value.index))
                    args.append("{0}={1}".format(value.info.key, value.info.value))
        return args


class StreamValue():
    index = None
    info = None

    def __init__(self, index, info):
        self.index = index
        self.info = info


class Info():
    key = None
    value = None

    def __init__(self, key, value):
        self.key = key
        self.value = value