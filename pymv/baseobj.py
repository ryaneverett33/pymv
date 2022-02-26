from pymv.streamType import StreamType
from pymv.commandbuilder import CommandBuilder
from pymv.metadataobj import MetadataObj

class BaseObj:
    __parent : CommandBuilder = None
    _streamType = StreamType.Unknown           # Set in child class
    Metadata = None

    def __init__(self, mov_obj):
        self.__parent = mov_obj
        self.Metadata = MetadataObj(self.__parent, streamType=self._streamType)

    def Codec(self, *args, **kwargs):
        if self._streamType == StreamType.Unknown:
            self.__parent.add_command(('-codec', args[0]))
        else:
            codecType = self._streamType.get_stream_qualifier()
            if 'streamIndex' in kwargs:
                self.__parent.add_command((f"-c:{codecType}:{kwargs['streamIndex']}", args[0]))
            else:
                self.__parent.add_command((f"-{codecType}codec", args[0]))
        return self

    def Bitrate(self, *args, **kwargs):
        codecType = self._streamType.get_stream_qualifier()
        if 'streamIndex' in kwargs:
            self.__parent.add_command((f"-b:{codecType}:{kwargs['streamIndex']}", args[0]))
        else:
            self.__parent.add_command((f"-b:{codecType}", args[0]))
        return self