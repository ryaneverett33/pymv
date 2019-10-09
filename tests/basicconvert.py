import sys
sys.path.insert(1, '../pymv')
from pymv import mv

mov = mv()
mov.Input('filename.mkv')
mov.Map(0,0)
mov.Map(0,1)
# mov.Codec().Copy()
mov.Codec().Video('copy')
mov.Codec().Audio('copy')
mov.Output('test.mkv')
print(mov.get_command())