from __future__ import annotations  # needed for -> MetadataObj

from typing import Union

from pymv.streamType import StreamType
from pymv.commandbuilder import CommandBuilder

class MetadataObj:
    def __init__(self, builder: CommandBuilder, streamType: StreamType=StreamType.Unknown):
        self._streamType: StreamType = streamType
        self.__builder: CommandBuilder = builder

    def Title(self, title: str, stream_specifier: int=None) -> MetadataObj:
        return self.Set('title', title, stream_specifier=stream_specifier)

    def Language(self, lang: str, stream_specifier: int=None) -> MetadataObj:
        return self.Set('language', lang, stream_specifier=stream_specifier)

    def Set(self, field: str, value: str, stream_specifier: int=None) -> MetadataObj:
        if stream_specifier != None:
            self.__builder.add_command((f'-metadata:s:{self._streamType.get_stream_qualifier()}:{stream_specifier}',
                                        f'{field}={value}'))
        elif self._streamType == StreamType.Unknown:
            self.__builder.add_command(('-metadata', f'{field}={value}'))
        else:
            self.__builder.add_command((f'-metadata:s:{self._streamType.get_stream_qualifier()}',
                                        f'{field}={value}'))
        return self

    def MapMetadata(self, inputFile) -> MetadataObj:
        # TODO ffmpeg -i INPUT -i FFMETADATAFILE -map_metadata 1 -codec copy OUTPUT
        pass

    def ExtractMetadata(self, outputFile) -> MetadataObj:
        # TODO ffmpeg -i INPUT -f ffmetadata FFMETADATAFILE
        pass