import sys
sys.path.insert(1, '../pymv')
from pymv import mv

mov = mv()
mov.Input('filename.mkv') \
    .Map(0,0) \
    .Map(0,1) \
    .Codec().Copy()
mov.Metadata() \
    .set_value('title', 'Some title') \
    .Audio('title', 'Surround', streamIndex=0) \
    .Video('title', '', streamIndex=0)
mov.Output('file2.mkv')
print(mov.get_command())