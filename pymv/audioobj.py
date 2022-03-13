from __future__ import annotations  # needed for -> AudioObj

from typing import Union
from pymv.streamType import StreamType
from pymv.baseobj import BaseObj
from pymv.commandbuilder import CommandBuilder

class AudioObj(BaseObj):
    def __init__(self, mov_obj: CommandBuilder):
        self._streamType = StreamType.Audio     # Use for distinction in base class
        
        super().__init__(mov_obj)

    def Channels(self, numOfChannels: int, stream_specifier: int=None) -> AudioObj:
        if stream_specifier != -1:
            self._parent.add_command((f'-ac:{stream_specifier}', str(numOfChannels)))
        else:
            self._parent.add_command(('-ac', str(numOfChannels)))
        return self