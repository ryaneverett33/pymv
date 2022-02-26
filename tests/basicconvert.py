import sys
sys.path.insert(0, '../')
from pymv.mv import Mv

mov = Mv()
mov.Input('filename.mkv')
mov.Map(0,0).Map(0,1)
mov.Video.Codec('copy')
mov.Audio.Codec('copy')
mov.Output('test.mkv')
mov.run()