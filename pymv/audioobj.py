from typing import Optional
from pymv.streamType import StreamType
from pymv.baseobj import BaseObj
from pymv.commandbuilder import CommandBuilder

class AudioObj(BaseObj):
    def __init__(self, mov_obj: CommandBuilder):
        self._streamType = StreamType.Audio     # Use for distinction in base class

        super().__init__(mov_obj, stream_type=self._streamType)

    def Channels(self, numOfChannels: int, stream_specifier: Optional[int]=None) -> "AudioObj":
        if stream_specifier != -1:
            self._parent.add_command((f'-ac:{stream_specifier}', str(numOfChannels)))
        else:
            self._parent.add_command(('-ac', str(numOfChannels)))
        return self