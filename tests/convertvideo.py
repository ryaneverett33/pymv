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
mov.Audio.Codec('ac3', stream_specifier=0) \
        .Codec('aac', stream_specifier=1) \
        .Bitrate('512k', stream_specifier=0) \
        .Bitrate('192k', stream_specifier=1) \
        .Metadata.Title('Surround', stream_specifier=0) \
            .Title('Stereo', stream_specifier=1)
mov.Metadata.Title('ConvertVideoTestOut')
mov.Output('output.mkv')
mov.print_command()