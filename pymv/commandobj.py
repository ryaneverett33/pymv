from abc import abstractmethod

from typing import Tuple

class CommandObj:
    def __init__(self):
        pass

    @abstractmethod
    def get_commands(self) -> Tuple[Tuple, Tuple]:
        """Gets the list of initial commands and a list of commands this object represents"""
        pass