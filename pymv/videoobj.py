from __future__ import annotations  # needed for -> VideoObj

from typing import Union
from pymv.streamType import StreamType
from pymv.baseobj import BaseObj
from pymv.commandbuilder import CommandBuilder

class VideoObj(BaseObj):
    _streamType = StreamType.Video     # Use for distinction in base class

    def __init__(self, mov_obj : CommandBuilder):
        super().__init__(mov_obj)

    def Maxrate(self, rate: int) -> VideoObj:
        self.__parent.add_command(('-maxrate', str(rate)))
        return self

    def Minrate(self, rate: int) -> VideoObj:
        self.__parent.add_command(('-minrate', str(rate)))
        return self

    def Bufsize(self, buffer: str) -> VideoObj:
        self.__parent.add_command(('-bufsize', buffer))
        return self