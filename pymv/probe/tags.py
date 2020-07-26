class Tags:
    raw_tag_obj = None
    _dict = None

    def __init__(self, tag_obj):
        self.raw_tag_obj = tag_obj
        self._dict = dict()
        for key in tag_obj.keys():
            self._dict[key] = tag_obj[key]

    def _getter(self, key):
        if key in self._dict:
            return self._dict[key]
        return None

    def title(self):
        return self._getter('title')

    def language(self):
        return self._getter('language')