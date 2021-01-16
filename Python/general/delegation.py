# Процесс делегирования в Python

class Upcase():
    def __init__(self, out):
        self._out = out

    def write(self, s):
        self._outfile = s.upper()

    def __getattr__(self, name):
        print('Looking up', name)
        return getattr(self._out, name)



class File():
    def __init__(self):
        self._outfile = 'test'

    def open(self):
        with open(self._outfile, 'w') as file:
            return file

    def write(self):
        self._outfile = 'test2'

file = File()
instance = Upcase(file)
instance.write('test')
instance.open()
print(instance._outfile)
#print(instance.hello())
#print(instance.hello())
#print(instance.write('test'))
#print(instance._outfile)
#print(instance.write('asd'))
#print(instance._outfile)
#print(instance._outfile)