import sys
sys.path.insert(1, '../')
from pymv.mv import Mv

mov = Mv()
mov.Input('filename.mkv') \
    .MapAll() \
    .Video.Codec('h264') \
        .Bitrate('1M')
mov.Audio.Codec('ac3', streamIndex=0) \
    .Codec('aac', streamIndex=1) \
    .Channels(2, streamIndex=1) \
    .Bitrate('512k', streamIndex=0) \
    .Bitrate('192k', streamIndex=1)
mov.Output('output.mkv')
print(mov.get_command())