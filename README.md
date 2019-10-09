# pymv
A basic wrapper library for the ffmpeg CLI tool.

## Example


This is a very basic example taking an input file (filename.mkv), selecting the streams for use, setting codec information, and finally running the command producing the output file (test.mkv).
```python
from pymv import mv

mov = mv()
mov.Input('filename.mkv') \
.Map(0,0).Map(0,1)
mov.Codec().Video('copy') \
.Audio('copy')
mov.Output('test.mkv') \
.run()
```

### More examples

More examples can be found in the [tests](/tests/) folder.

## TODO

There's a lot of work that needs to be done and can be found in the [TODO](/TODO) file.