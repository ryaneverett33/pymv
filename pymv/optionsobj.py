from pymv.commandbuilder import CommandBuilder
from pymv.hwAccelMethod import HwAccelMethod

from typing import Union

class OptionsObj:
    def __init__(self, builder: CommandBuilder):
        self.__builder: CommandBuilder = builder
        self.__options_flags: dict[str, bool] = dict()

    def Duration(self, duration: str) -> "OptionsObj":
        # TODO make duration a timecode object
        self.__builder.add_command(('-t', str(duration)))
        return self

    def Seek(self, duration: Union[int, float]) -> "OptionsObj":
        # TODO maybe make this a timecode object
        self.__builder.add_command(('-ss', str(duration)))
        return self

    def Overwrite(self) -> "OptionsObj":
        if 'overwrite' not in self.__options_flags:
            self.__builder.add_command(('-y'))
            self.__options_flags['overwrite'] = True
        return self

    def Silent(self) -> "OptionsObj":
        if 'silent' not in self.__options_flags:
            self.__builder.add_command(('-loglevel', 'error', '-stats'), initial_command=True)
            self.__options_flags['silent'] = True
        return self