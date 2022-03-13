from __future__ import annotations  # needed for -> HwAccelObj

from pymv.commandbuilder import CommandBuilder
from pymv.hwAccelMethod import HwAccelMethod

class HwAccelObj:
    def __init__(self, builder: CommandBuilder):
        self.__builder: CommandBuilder = builder

    def InputFormat(self, format: str):
        # TODO, add as option to mov.Input()
        pass

    def Method(self, method: HwAccelMethod, stream_specifier: int = None) -> HwAccelObj:
        arg_name = f'-hwaccel:{stream_specifier}' if stream_specifier is not None else '-hwaccel'
        self.__builder.add_command((arg_name, str(method)), initial_command=True)
        return self

    def OutputFormat(self, format: str) -> HwAccelObj:
        self.__builder.add_command(('-hwaccel_output_format', format), initial_command=True)
        return self

    def Device(self, device: str, stream_specifier: int = None) -> HwAccelObj:
        arg_name = f'-hwaccel_device:{stream_specifier}' if stream_specifier is not None else '-hwaccel_device'
        self.__builder.add_command((arg_name, device), initial_command=True)
        return self

    def InitHwDevice(self, device: str) -> HwAccelObj:
        self.__builder.add_command(('-init_hw_device', device), initial_command=True)
        return self