from __future__ import annotations # needed for -> Mv

import warnings
import typing

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
from .inputobj import InputObj

class Mv(CommandBuilder, BaseObj, MetadataObj):
    def __init__(self, ffmpeg_path="ffmpeg", ffprobe_path="ffprobe"):
        CommandBuilder.__init__(self, ffmpeg_path=ffmpeg_path, ffprobe_path=ffprobe_path)
        BaseObj.__init__(self, self)
        self.Probe: prober = prober(self._ffprobe_path)
        self.Lookup: Lookup = Lookup()
        self.Video: VideoObj = VideoObj(self)
        self.Audio: AudioObj = AudioObj(self)
        self.Subtitle: SubtitleObj = SubtitleObj(self)
        self.Metadata: MetadataObj = MetadataObj(self)
        self.Options: OptionsObj = OptionsObj(self)

    def Input(self, input: str, format:str=None, offset:str=None, scale:str=None, pix_fmt:str=None) -> Mv:
        self.inputs.append(InputObj(input, format=format, offset=offset, scale=scale, pix_fmt=pix_fmt))
        return self

    def Output(self, filename: str) -> Mv:
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

    def get_command(self) -> str:
        arguments = self._get_arguments()
        arguments = [str(argument) for argument in arguments]
        return self._ffmpeg_path + " " + " ".join(arguments)

    def print_command(self) -> Mv:
        print(self.get_command())
        return self

    def Run(self, capture_stdout: bool=False, capture_stderr: bool=False) -> typing.Tuple[int, str, str]:
        run = runner(self._get_arguments(), self._ffmpeg_path)
        return run.run(capture_stdout=capture_stdout, capture_stderr=capture_stderr)