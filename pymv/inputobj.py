from typing import Tuple
from .commandobj import CommandObj

class InputObj(CommandObj):
    def __init__(self, input: str, format: str=None, offset:str=None, scale:str=None, pix_fmt:str=None):
        # TODO handle input codec?
        super().__init__()

        self.input:str = input
        self.format:str = format
        self.offset:str = offset
        self.scale:str = scale
        self.pix_fmt:str = pix_fmt

    def get_commands(self) -> Tuple[Tuple, Tuple]:
        initial_commands = ()
        if self.format is not None:
            initial_commands = initial_commands + ('-f', self.format)
        if self.offset is not None:
            initial_commands = initial_commands + ('-itsoffset', self.offset)
        if self.scale is not None:
            initial_commands = initial_commands + ('-itsscale', self.scale)
        if self.pix_fmt is not None:
            # TODO Is this a valid flag?
            initial_commands = initial_commands + ('-pix_fmt', self.pix_fmt)
        
        initial_commands = initial_commands + ('-i', self.input)
        return (initial_commands, None)