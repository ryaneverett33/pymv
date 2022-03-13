from __future__ import annotations # needed for -> OptionsObj

import typing
from pymv.commandbuilder import CommandBuilder
from pymv.hwAccelMethod import HwAccelMethod

class OptionsObj:
    def __init__(self, builder : OptionsObj):
        self.__builder: CommandBuilder = builder
        self.__options_flags: typing.Dict[str, bool] = dict()

    def Duration(self, duration : str) -> OptionsObj:
        # TODO make duration a timecode object
        self.__builder.add_command(('-t', duration))
        return self

    def Seek(self, duration: typing.Union[int, float]) -> OptionsObj:
        # TODO maybe make this a timecode object
        self.__builder.add_command(('-ss', str(duration)))
        return self

    def Overwrite(self) -> OptionsObj:
        if 'overwrite' not in self.__options_flags:
            self.__builder.add_command(('-y'))
            self.__options_flags['overwrite'] = True
        return self

    def Silent(self) -> OptionsObj:
        if 'silent' not in self.__options_flags:
            self.__builder.add_command(('-loglevel', 'error', '-stats'), initial_command=True)
            self.__options_flags['silent'] = True
        return self