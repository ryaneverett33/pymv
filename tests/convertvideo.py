import sys
sys.path.insert(0, '../')
from pymv.mv import Mv

mov = Mv()
mov.Input('filename.mkv') \
    .Map(0, 0) \
    .Map(0, 1) \
    .Map(0, 2) \
    .Video.Codec('h264') \
        .Crf(18) \
        .Preset('fast')
mov.Audio.Codec('ac3', streamIndex=0) \
        .Codec('aac', streamIndex=1) \
        .Bitrate('512k', streamIndex=0) \
        .Bitrate('192k', streamIndex=1) \
        .Metadata.Title('Surround', streamIndex=0) \
            .Title('Stereo', streamIndex=1)
mov.Metadata.Title('ConvertVideoTestOut')
mov.Output('output.mkv')
print(mov.get_command())