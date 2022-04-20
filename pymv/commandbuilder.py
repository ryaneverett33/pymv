import warnings
import typing

from .inputobj import InputObj

class CommandBuilder:
    def __init__(self, ffmpeg_path: str="ffmpeg", ffprobe_path: str="ffprobe"):
        self.inputs: typing.List[InputObj] = []
        self.outputs: typing.List[str] = []
        self._ffmpeg_path: str = ffmpeg_path
        self._ffprobe_path: str = ffprobe_path

        self.commands: typing.List[tuple] = list()
        self.initial_commands: typing.List[tuple] = list()

    def add_command(self, arguments: tuple, initial_command: bool=False):
        """Adds a command to be passed to the ffmpeg/probe invocation
            arguments: list of that encompass a command
                EX: ('-i', 'input.mkv')
            initial_command: Whether the command occurs before the main arguments
        """
        for item in arguments:
            if not isinstance(item, str):
                raise TypeError("Command tuple must only contain strings")
        if initial_command:
            self.initial_commands.append(arguments)
        else:
            self.commands.append(arguments)

    def _get_arguments(self):
        arguments = []
        # Error check
        if self.inputs is None:
            raise Exception("No Inputs given!")
        if self.outputs is None:
            raise Exception("No Outputs given!")
        # assemble initial options
        for initial_command in self.initial_commands:
            arguments = arguments + list(initial_command)
        # assemble input
        for input in self.inputs:
            initial_commands, _ = input.get_commands()
            arguments = arguments + list(initial_commands)
        # assemble options
        for command in self.commands:
            arguments = arguments + list(command)
        # assemble outputs
        for output in self.outputs:
            # Use a loop body because we may need to process outputs more smart later
            arguments.append(output)
        return arguments
