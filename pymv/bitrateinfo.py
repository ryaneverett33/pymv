from pymv.ffcommand import ffcommand
from pymv.StreamType import StreamType

class bitrateinfo(ffcommand):
    bitrates = None         # Dictionary of either str or list
    crf = None
    preset = None

    def __init__(self):
        self.bitrates = dict()

    def Video(self, bitrate, stream_specifier=None):
        if stream_specifier is None:
            return self.set_value(StreamType.Video, bitrate)
        else:
            return self.set_value_of_stream(StreamType.Video, bitrate, stream_specifier)

    def Audio(self, bitrate, stream_specifier=None):
        if stream_specifier is None:
            return self.set_value(StreamType.Audio, bitrate)
        else:
            return self.set_value_of_stream(StreamType.Audio, bitrate, stream_specifier)
    
    def Crf(self, crf):
        self.crf = str(crf)
        return self

    def Preset(self, preset):
        self.preset = preset
        return self

    def set_value(self, streamType, bitrate):
        if streamType in self.bitrates:
            if isinstance(self.bitrates, list):
                raise Exception('Setting bitrate would overwrite existing stream settings')
            else:
                raise Exception('Setting bitrate would overwrite existing value')
        self.bitrates[streamType] = bitrate
        return self

    def set_value_of_stream(self, streamType, bitrate, stream_specifier=None):
        if streamType in self.bitrates:
            if isinstance(self.bitrates, str):
                raise Exception('Setting stream settigns would overwrite existing bitrate value')
        else:
            self.bitrates[streamType] = list()
        self.bitrates[streamType].append(Bitrate(stream_specifier, bitrate))
        sorted(self.bitrates[streamType], key=lambda bitrate: bitrate.stream_specifier)
        return self

    def to_args(self):
        args = []
        # assemble crf and preset
        if self.crf is not None:
            args.append('-crf')
            args.append(self.crf)
        if self.preset is not None:
            args.append('-preset')
            args.append(self.preset)
        # assemble bitrates
        for streamType in self.bitrates.keys():
            if isinstance(self.bitrates[streamType], list):
                for bitrate in self.bitrates[streamType]:
                    args.append('-b:{0}:{1}'.format(streamType.get_stream_qualifier(), bitrate.stream_specifier))
                    args.append(bitrate.bitrate)
            elif isinstance(self.bitrates[streamType], str):
                args.append('-b:{0}'.format(streamType.get_stream_qualifier()))
                args.append(self.bitrates[streamType])
        return args

class Bitrate():
    stream_specifier = None
    bitrate = None

    def __init__(self, stream_specifier, bitrate):
        self.stream_specifier = stream_specifier
        self.bitrate = bitrate