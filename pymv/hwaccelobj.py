from __future__ import annotations  # needed for -> HwAccelObj

from pymv.commandbuilder import CommandBuilder
from pymv.hwAccelMethod import HwAccelMethod

class HwAccelObj:
    __builder : CommandBuilder = None

    def __init__(self, builder : CommandBuilder):
        self.__builder = builder

    def InputFormat(self, format : str):
        pass

    def Method(self, method : HwAccelMethod):
        pass

    def OutputFormat(self, format : str):
        pass

    def Device(self, device : str):
        pass

    def InitHwDevice(self, device : str):
        pass