from __future__ import annotations  # needed for -> AudioObj

from typing import Union
from pymv.streamType import StreamType
from pymv.baseobj import BaseObj
from pymv.commandbuilder import CommandBuilder

class AudioObj(BaseObj):
    _streamType = StreamType.Audio     # Use for distinction in base class

    def __init__(self, mov_obj : CommandBuilder):
        super().__init__(mov_obj)

    def Channels(self, numOfChannels: int, streamIndex=-1) -> AudioObj:
        if streamIndex != -1:
            self.__parent.add_command((f'-ac:{streamIndex}', numOfChannels))
        else:
            self.__parent.add_command(('-ac', numOfChannels))
        return self