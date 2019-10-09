from pymv.ffcommand import ffcommand

class fmap(ffcommand):
    mapAll = False
    a = None
    b = None

    def __init__(self, a, b):
        self.a = a
        self.b = b

    @staticmethod
    def MapAll():
        obj = fmap(None, None)
        obj.mapAll = True
        return obj

    def to_args(self):
        if self.mapAll:
            return ['-map', '0']
        elif self.a is not None and self.b is not None:
            return ['-map', '{0}:{1}'.format(self.a, self.b)]
        else:
            raise Exception("Map object is empty, can't convert to arguments")