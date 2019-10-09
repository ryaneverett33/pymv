import sys
sys.path.insert(1, '../pymv')
from pymv import mv

mov = mv()
mov.Input('filename.mkv') \
.Map(0,0).Map(0,1)
# mov.Codec().Copy()
mov.Codec().Video('copy') \
.Audio('copy')
mov.Output('test.mkv') \
.run()