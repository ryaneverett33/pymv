from __future__ import annotations  # needed for -> MetadataObj

from typing import Union

from pymv.streamType import StreamType
from pymv.commandbuilder import CommandBuilder

class MetadataObj:
    _streamType : StreamType = StreamType.Unknown
    __builder : CommandBuilder = None

    def __init__(self, builder : CommandBuilder, streamType=StreamType.Unknown):
        self._streamType = streamType
        self.__builder = builder

    def Title(self, title, streamIndex=-1) -> MetadataObj:
        return self.Set('title', title, streamIndex=streamIndex)

    def Language(self, lang, streamIndex=-1) -> MetadataObj:
        return self.Set('language', lang, streamIndex=streamIndex)

    def Set(self, field, value, streamIndex=-1) -> MetadataObj:
        if streamIndex != -1:
            self.__builder.add_command((f'-metadata:s:{self._streamType.get_stream_qualifier()}:{streamIndex}',
                                        f'{field}={value}'))
        elif self._streamType == StreamType.Unknown:
            self.__builder.add_command(('-metadata', f'{field}={value}'))
        else:
            self.__builder.add_command((f'-metadata:s:{self._streamType.get_stream_qualifier()}',
                                        f'{field}={value}'))
        return self

    def MapMetadata(self, inputFile) -> MetadataObj:
        # ffmpeg -i INPUT -i FFMETADATAFILE -map_metadata 1 -codec copy OUTPUT
        pass

    def ExtractMetadata(self, outputFile) -> MetadataObj:
        # ffmpeg -i INPUT -f ffmetadata FFMETADATAFILE
        pass