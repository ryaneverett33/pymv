from __future__ import annotations  # needed for -> SubtitleObj

from typing import Union
from pymv.streamType import StreamType
from pymv.baseobj import BaseObj
from pymv.commandbuilder import CommandBuilder

class SubtitleObj(BaseObj):
    def __init__(self, mov_obj : CommandBuilder):
        self._streamType = StreamType.Subtitle

        super().__init__(mov_obj)