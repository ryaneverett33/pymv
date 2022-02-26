import warnings
import typing

class CommandBuilder:
    inputs = None
    outputs = None
    commands : typing.List[tuple] = None
    initial_commands : typing.List[tuple] = None
    _ffmpeg_path : str = None
    _ffprobe_path : str = None       


    def __init__(self, ffmpeg_path="ffmpeg", ffprobe_path="ffprobe"):
        self.inputs = []
        self.outputs = []
        self._ffmpeg_path = ffmpeg_path
        self._ffprobe_path = ffprobe_path

        self.commands = list()
        self.initial_commands = list()

    def add_command(self, command: tuple, initial_command=False):
        if initial_command:
            self.initial_commands.append(command)
        else:
            self.commands.append(command)

    def _get_arguments(self):
        arguments = []
        # Error check
        if self.inputs is None:
            raise Exception("No Inputs given!")
        if self.outputs is None:
            raise Exception("No Outputs given!")
        # assemble initial options
        for initial_command in self.initial_commands:
            if isinstance(initial_command, tuple):
                arguments = arguments + list(initial_command)
            elif isinstance(initial_command, str):
                arguments.append(initial_command)
            else:
                raise TypeError(f"Unsupported comand type: {type(initial_command)}")
        # assemble input
        for input in self.inputs:
            arguments.append('-i')
            arguments.append(input)
        # assemble options
        for command in self.commands:
            if isinstance(command, tuple):
                arguments = arguments + list(command)
            elif isinstance(command, str):
                arguments.append(command)
            else:
                raise TypeError(f"Unsupported comand type: {type(command)}")
        # assemble outputs
        for output in self.outputs:
            # Use a loop body because we may need to process outputs more smart later
            arguments.append(output)
        return arguments
