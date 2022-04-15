from __future__ import annotations
import typing

class Tags(dict):
    def __init__(self, tag_obj: dict):
        super().__init__(tag_obj)

    def __getitem__(self, key: str) -> typing.Any:
        if key in self:
            return super().__getitem__(key)
        return None

    def title(self) -> str:
        return self['title']

    def language(self) -> str:
        return self['language']

    def _print_debug(self):
        print("Tags:")
        for tag in self.keys():
            print(f"\t{tag} = {self[tag]}")