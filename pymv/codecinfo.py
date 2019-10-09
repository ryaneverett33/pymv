from pymv.ffcommand import ffcommand

class codecinfo(ffcommand):
    copy = False                    # Whether to copy every codec from input to output
    videocodecs = None              # List of videocodecs to use
    audiocodecs = None              # List of audiocodecs to use
    subtitlecodecs = None           # List of subtitlecodecs to use

    def __init__(self):
        self.copy = False

    def __add_codec(self, videocodec=None, audiocodec=None, subtitlecodec=None):
        if videocodec is not None:
            self.videocodecs.append(videocodec)
            sorted(self.videocodecs, key=lambda acodec: acodec.index)
        elif audiocodec is not None:
            self.audiocodecs.append(audiocodec)
            sorted(self.audiocodecs, key=lambda acodec: acodec.index)
        elif subtitlecodec is not None:
            self.subtitlecodecs.append(subtitlecodec)
            sorted(self.subtitlecodecs, key=lambda acodec: acodec.index)
        else:
            raise Exception("__add_codec wasn't given the path to add the codec to")

    def Copy(self):
        self.copy = True
        return self
    
    def Video(self, codec, streamIndex=None):
        if streamIndex is None:
            if self.videocodecs is not None:
                if isinstance(self.videocodecs, list):
                    raise Exception('Setting video codec without stream index would overwrite previous codec mappings')
                elif isinstance(self.videocodecs, str):
                    raise Exception('Setting video codec would overwrite previous codec entry')
            self.videocodecs = codec
        else:
            if self.videocodecs is None:
                self.videocodecs = []
            if isinstance(self.videocodecs, str):
                raise Exception('Setting video codec would overwrite previous codec entry')
            else:
                self.__add_codec(videocodec=Codec(streamIndex, codec))
        return self

    def Audio(self, codec, streamIndex=None):
        if streamIndex is None:
            if self.audiocodecs is not None:
                if isinstance(self.audiocodecs, list):
                    raise Exception('Setting audio codec without stream index would overwrite previous codec mappings')
                elif isinstance(self.audiocodecs, str):
                    raise Exception('Setting audio codec would overwrite previous codec entry')
            self.audiocodecs = codec
        else:
            if self.audiocodecs is None:
                self.audiocodecs = []
            if isinstance(self.audiocodecs, str):
                raise Exception('Setting audio codec would overwrite previous codec entry')
            else:
                self.__add_codec(audiocodec=Codec(streamIndex, codec))
        return self

    def Subtitle(self, codec, streamIndex=None):
        if streamIndex is None:
            if self.subtitlecodecs is not None:
                if isinstance(self.subtitlecodecs, list):
                    raise Exception('Setting subtitle codec without stream index would overwrite previous codec mappings')
                elif isinstance(self.subtitlecodecs, str):
                    raise Exception('Setting subtitle codec would overwrite previous codec entry')
            self.subtitlecodecs = codec
        else:
            if self.subtitlecodecs is None:
                self.subtitlecodecs = []
            if isinstance(self.subtitlecodecs, str):
                raise Exception('Setting subtitle codec would overwrite previous codec entry')
            else:
                self.__add_codec(subtitlecodec=Codec(streamIndex, codec))
        return self

    def to_args(self):
        arguments = []
        if self.copy:
            arguments = ['-codec', 'copy']
        else:
            if self.videocodecs is not None:
                if isinstance(self.videocodecs, str):
                    arguments.append('-vcodec')
                    arguments.append(self.videocodecs)
                else:
                    for codec in self.videocodecs:
                        arguments.append('-c:v:{0}'.format(codec.index))
                        arguments.append(codec.name)
            if self.audiocodecs is not None:
                if isinstance(self.audiocodecs, str):
                    arguments.append('-acodec')
                    arguments.append(self.audiocodecs)
                else:
                    for codec in self.audiocodecs:
                        arguments.append('-c:a:{0}'.format(codec.index))
                        arguments.append(codec.name)
            if self.subtitlecodecs is not None:
                if isinstance(self.subtitlecodecs, str):
                    arguments.append('-scodec')
                    arguments.append(self.subtitlecodecs)
                else:
                    for codec in self.subtitlecodecs:
                        arguments.append('-c:s:{0}'.format(codec.index))
                        arguments.append(codec.name)
        return arguments


class Codec:
    index = 0           # Stream Index
    name = None         # Name of the codex to use

    def __init__(self, index, name):
        self.index = index
        self.name = name