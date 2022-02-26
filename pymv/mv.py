from __future__ import annotations
from lib2to3.pytree import Base  # needed for -> Mv

import warnings
import typing

from pymv.proberesult import ProbeResult
from .streamType import StreamType
from .commandbuilder import CommandBuilder
from .runner import runner
from .prober import prober
from .lookup import Lookup
from .videoobj import VideoObj
from .audioobj import AudioObj
from .subtitleobj import SubtitleObj
from .metadataobj import MetadataObj
from .optionsobj import OptionsObj
from .baseobj import BaseObj

class Mv(CommandBuilder, BaseObj, MetadataObj):
    Probe = None
    Lookup = None
    Video = None
    Audio = None
    Subtitle = None
    Metadata = None
    HwAccel = None
    Options = None

    def __init__(self, ffmpeg_path="ffmpeg", ffprobe_path="ffprobe"):
        CommandBuilder.__init__(self, ffmpeg_path=ffmpeg_path, ffprobe_path=ffprobe_path)
        BaseObj.__init__(self, self)
        self.Probe = prober(self._ffprobe_path)
        self.Lookup = Lookup()
        self.Video = VideoObj(self)
        self.Audio = AudioObj(self)
        self.Subtitle = SubtitleObj(self)
        self.Metadata = MetadataObj(self)
        self.Options = OptionsObj(self)

    def Input(self, filename) -> Mv:
        self.inputs.append(filename)
        return self

    def Output(self, filename) -> Mv:
        self.outputs.append(filename)
        return self

    def Map(self, *args) -> Mv:
        # https://ffmpeg.org/ffmpeg-all.html#Advanced-options
        mapCommand = ""

        for i in range(0, len(args)):
            # We could attempt to understand the mappings but there's a lot of ffmpeg
            # logic to map back into here.
            arg = args[i]

            if not isinstance(arg, int) and not isinstance(arg, str):
                raise ValueError(f"{arg} is of invalid type {type(arg)}, acceptable values [str, int]")
            mapCommand += str(arg) if isinstance(arg, int) else arg
            if i + 1 < len(args):
                mapCommand += ":"

        self.add_command(('-map', mapCommand))
        return self

    def MapAll(self) -> Mv:
        return self.Map(0)

    def get_command(self) -> Mv:
        arguments = self._get_arguments()
        arguments = [str(argument) for argument in arguments]
        return self._ffmpeg_path + " " + " ".join(arguments)

    def run(self, capture_stdout=False, capture_stderr=False) -> tuple:
        run = runner(self._get_arguments(), self._ffmpeg_path)
        return run.run(capture_stdout=capture_stdout, capture_stderr=capture_stderr)