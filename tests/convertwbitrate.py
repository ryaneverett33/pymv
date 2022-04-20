import sys
sys.path.insert(1, '../')
from pymv import Pymv

mov = Pymv()
mov.Input('filename.mkv') \
    .MapAll() \
    .Video.Codec('h264') \
        .Bitrate('1M')
mov.Audio.Codec('ac3', stream_specifier=0) \
    .Codec('aac', stream_specifier=1) \
    .Channels(2, stream_specifier=1) \
    .Bitrate('512k', stream_specifier=0) \
    .Bitrate('192k', stream_specifier=1)
mov.Output('output.mkv')
mov.print_command()