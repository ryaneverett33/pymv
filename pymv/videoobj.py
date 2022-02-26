from __future__ import annotations  # needed for -> VideoObj

from typing import Union
from pymv.streamType import StreamType
from pymv.baseobj import BaseObj
from pymv.commandbuilder import CommandBuilder

class VideoObj(BaseObj):
    _streamType = StreamType.Video     # Use for distinction in base class

    def __init__(self, mov_obj : CommandBuilder):
        super().__init__(mov_obj)

    def Maxrate(self, rate: Union[int, str]) -> VideoObj:
        self._parent.add_command(('-maxrate', rate))
        return self

    def Minrate(self, rate: Union[int, str]) -> VideoObj:
        self._parent.add_command(('-minrate', rate))
        return self

    def Bufsize(self, size: str) -> VideoObj:
        self._parent.add_command(('-bufsize', size))
        return self

    def Crf(self, rate: Union[int, float]) -> VideoObj:
        self._parent.add_command(('-crf', rate))
        return self

    def Preset(self, preset: str) -> VideoObj:
        self._parent.add_command(('-preset', preset))
        return self