import typing

class Tags:
    raw_tag_obj = None
    _dict = None

    def __init__(self, tag_obj):
        self.raw_tag_obj = tag_obj
        self._dict = dict()
        for key in tag_obj.keys():
            self._dict[key] = tag_obj[key]

    def __getitem__(self, key: str) -> typing.Any:
        if key in self._dict:
            return self._dict[key]
        return None

    def title(self) -> str:
        return self._getter('title')

    def language(self) -> str:
        return self['language']