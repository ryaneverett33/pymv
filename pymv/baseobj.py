from pymv.streamType import StreamType
from pymv.commandbuilder import CommandBuilder
from pymv.metadataobj import MetadataObj

class BaseObj:
    def __init__(self, mov_obj):
        self._streamType: StreamType = StreamType.Unknown           # Set in child class
        self._parent: CommandBuilder = mov_obj
        
        self.Metadata: MetadataObj = MetadataObj(self._parent, streamType=self._streamType)

    def Codec(self, *args, **kwargs):
        if self._streamType == StreamType.Unknown:
            self._parent.add_command(('-codec', args[0]))
        else:
            codecType = self._streamType.get_stream_qualifier()
            if 'stream_specifier' in kwargs:
                self._parent.add_command((f"-c:{codecType}:{kwargs['stream_specifier']}", args[0]))
            else:
                self._parent.add_command((f"-{codecType}codec", args[0]))
        return self

    def Bitrate(self, *args, **kwargs):
        codecType = self._streamType.get_stream_qualifier()
        if 'stream_specifier' in kwargs:
            self._parent.add_command((f"-b:{codecType}:{kwargs['stream_specifier']}", args[0]))
        else:
            self._parent.add_command((f"-b:{codecType}", args[0]))
        return self