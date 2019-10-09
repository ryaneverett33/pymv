from pymv.fmap import fmap
from pymv.commandbuilder import commandbuilder
from pymv.runner import runner

class mv(commandbuilder):
    def __init__(self):
        super().__init__()

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

    def get_command(self):
        arguments = self.get_arguments()
        command = self.get_executable() + ' '
        for i in range(0, len(arguments)):
            command = command + arguments[i]
            if i < len(arguments) - 1:
                command = command + ' '
        return command

    def run(self):
        run = runner(self.get_arguments(), self.get_executable())
        run.run()