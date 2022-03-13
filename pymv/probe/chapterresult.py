from .tags import Tags

# {'id': 2, 'time_base': '1/1000000000', 'start': 139056000000, 'start_time': '139.056000', 'end': 172422000000, 'end_time': '172.422000', 'tags': {'title': '00:02:19.056'}}
class ChapterResult:
    __raw_chapter_obj = None
    tags = None
    id = None
    time_base = None
    start = None
    end = None
    start_time = None
    end_time = None

    def __init__(self, chapter_obj):
        self.__raw_chapter_obj = chapter_obj
        self.id = self['id']
        self.time_base = self['time_base']
        self.start = self['start']
        self.end = self['end']
        self.start_time = self['start_time']
        self.end_time = self['end_time']
        self.tags = self['tags']

    def __getitem__(self, key):
        return self.__raw_chapter_obj[key]

    def _print_debug(self):
        print(f"Id: {self.id}, time_base: {self.time_base}")
        print(f"start_time: {self.start_time}, end_time: {self.end_time}")
        print("Tags:")
        for tag in self.tags.keys():
            print(f"{tag} = {self.tags[tag]}")