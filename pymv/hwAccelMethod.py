from enum import Enum

class HwAccelMethod(Enum):
    # https://trac.ffmpeg.org/wiki/HWAccelIntro
    cuda = 1
    cuvid = 2
    qsv = 4                 # https://trac.ffmpeg.org/wiki/Hardware/QuickSync
    vdpau = 8
    vaapi = 16              # https://trac.ffmpeg.org/wiki/Hardware/VAAPI
    dxva2 = 32
    videotoolbox = 64
    Unknown = 8

    def __str__(self) -> str:
        if self.value == 'cuda':
            return 'cuda'
        elif self.value == 'cuvid':
            return 'cuvid'
        elif self.value == 'qsv':
            return 'qsv'
        elif self.value == 'vdpau':
            return 'vdpau'
        elif self.value == 'vaapi':
            return 'vaapi'
        elif self.value == 'dxva2':
            return 'dxva2'
        elif self.value == 'videotoolbox':
            return 'videotoolbox'
        return ''