from pymv.fmap import fmap
from pymv.commandbuilder import commandbuilder
from pymv.runner import runner
from pymv.prober import prober

class mv(commandbuilder):
    prober = None

    def __init__(self):
        super().__init__()
        self.prober = prober(self.get_ffprobe())

    def Input(self, filename):
        self.inputs.append(filename)
        return self

    def Output(self, filename):
        self.outputs.append(filename)
        return self

    def Map(self, a, b):
        if not self.mapping is None and isinstance(self.mapping, fmap):
            raise Exception("Called Map when MapAll was already called")
        if self.mapping is None:
            self.mapping = []
        self.mapping.append(fmap(a, b))
        return self

    def MapAll(self):
        if not self.mapping is None or isinstance(self.mapping, list):
            raise Exception("Called MapAll when Map was already called")
        self.mapping = fmap.MapAll()
        return self

    def Metadata(self):
        return self.metadata_info

    def Codec(self):
        return self.codec_info

    def Bitrate(self):
        return self.bitrate_info

    def Duration(self, timecode):
        self.otheroptions.append('-t')
        self.otheroptions.append(timecode)
        return self

    def StartSeconds(self, timecode):
        self.otheroptions.append('-ss')
        self.otheroptions.append(timecode)
        return self

    def add_command(self, value):
        self.otheroptions.append(value)
        return self

    def get_command(self):
        arguments = self.get_arguments()
        command = self.get_executable() + ' '
        for i in range(0, len(arguments)):
            command = command + arguments[i]
            if i < len(arguments) - 1:
                command = command + ' '
        return command

    def probe(self, filename):
        return self.prober.probe(filename)

    def Input(self):
        return self.input_info

    def Output(self):
        return self.output_info

    def Video(self):
        return self.video_info

    def Audio(self):
        return self.audio_info

    def Subtitle(self):
        return self.subtitle_info

    def run(self):
        run = runner(self.get_arguments(), self.get_ffmpeg())
        run.run()