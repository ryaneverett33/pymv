from pymv.tags import Tags
import datetime
import math

class Format:
    raw_format_obj = None
    
    # Raw Fields
    filename = None
    nb_streams = 0
    nb_programs = 0
    format_name = None
    format_long_name = None
    start_time = None
    duration = None
    size = None
    bit_rate = None
    probe_score = 0

    tags = None

    def __init__(self, format_obj):
        self.raw_format_obj = format_obj
        self._parse_format(format_obj)

    def _parse_format(self, format_obj):
        if format_obj['filename']:
            self.filename = format_obj['filename']
        if format_obj['nb_streams']:
            self.nb_streams = int(format_obj['nb_streams'])
        if format_obj['nb_programs']:
            self.nb_programs = int(format_obj['nb_programs'])
        if format_obj['format_name']:
            self.format_name = format_obj['format_name']
        if format_obj['format_long_name']:
            self.format_long_name = format_obj['format_long_name']
        if format_obj['start_time']:
            self.start_time = float(format_obj['start_time'])
        if format_obj['duration']:
            self.duration = float(format_obj['duration'])
        if format_obj['size']:
            self.size = int(format_obj['size'])
        if format_obj['bit_rate']:
            self.bit_rate = int(format_obj['bit_rate'])
        if format_obj['probe_score']:
            self.probe_score = int(format_obj['probe_score'])
        if format_obj['tags']:
            self.tags = Tags(format_obj['tags'])

    # Get a time object with the duration parsed
    # If date_time, return a datetime object instead of a time object
    def duration_obj(self, date_time=True):
        if self.duration is None:
            return None
        minutes = self.duration / 3600
        frac, hours = math.modf(minutes)
        seconds, minutes = math.modf(frac * 60)
        milliseconds, seconds = math.modf(seconds * 60)
        milliseconds = int(milliseconds * 1000)
        if date_time:
            return datetime.datetime(year=1, month=1, day=1, hour=int(hours), minute=int(minutes),
                                        second=int(seconds), microsecond=int(milliseconds * 1000))
        return datetime.time(int(hours), int(minutes), int(seconds), int(milliseconds * 1000))

    # Get the file size in a friendly format
    # Use bibytes to get the same size as MediaInfo
    # BUG bibytes not returning proper value
    def size_str(self, bibytes=False):
        if self.size is None:
            return None
        size = self.size
        if bibytes:
            size = size / 1.024
        mb, gb = math.modf(size / (1024*1e6) if bibytes else size / 1e9)
        if gb > 0:
            return "{0}.{1} G{2}B".format(int(gb), int(mb * 1000), 'i' if bibytes else '')
        kb, mb = math.modf(size / (1024*1e3) if bibytes else size / 1e6)
        if mb > 0:
            return "{0}.{1} M{2}B".format(int(mb), int(kb * 1000), 'i' if bibytes else '')
        b, kb = math.modf(size / 1024 if bibytes else size / 1e3)
        return "{0}.{1} K{2}B".format(int(kb), int(b * 1000), 'i' if bibytes else '')