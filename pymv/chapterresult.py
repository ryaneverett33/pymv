from pymv.tags import Tags

class ChapterResult:
    raw_chapter_obj = None
    tags = None

    def __init__(self, chapter_obj):
        self.raw_chapter_obj = chapter_obj