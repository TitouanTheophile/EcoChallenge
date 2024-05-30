import builtins

def abs(x):
    if x > 0:
        return x
    else:
        return -x

def aiter(async_iterable):
    # return aiter()
    pass

def all(iterable):
    for element in iterable:
        if not element:
            return False
    return True

def anext(async_iterator):
    # return anext()
    pass

def any(iterable):
    for element in iterable:
        if element:
            return True
    return False

def ascii(object):
    # return ascii()
    pass

def bin(x):
    # return bin()
    pass

def bool(x=False):
    if x:
        return True
    else:
        return False
    
def breakpoint(*args, **kws):
    # return breakpoint()
    pass

def bytearray(source=b''):
    # return bytearray()
    pass

def bytes(source=b''):
    # return bytes()
    pass

def callable(object):
    # return callable()
    pass

def chr(i):
    # return chr()
    pass

# def classmethod():
    # return classmethod()
    # pass

def compile(source, filename, mode, flags=0, dont_inherit=False, optimize=-1):
    # return compile()
    pass

def complex(real=0, imag=0):
    # return complex()
    pass

def delattr(object, name):
    # return delattr()
    pass

def dict(**kwarg):
    # return dict()
    pass

def dir(object):
    # return dir()
    pass

def divmod(a, b):
    d = int(a / b)
    m = a % b
    return (d, m)

def enumerate(iterable, start=0):
    n = start
    for elem in iterable:
        yield n, elem
        n += 1

def eval(expression, globals=None, locals=None):
    # return eval()
    pass

def exec(object, globals=None, locals=None, /, *, closure=None):
    # return exec()
    pass

def filter(function, iterable):
    # return filter()
    pass

def float(x=0.0):
    # return float()
    pass

def format(value, format_spec=''):
    # return format()
    pass

def frozenset(iterable=set()):
    # return frozenset()
    pass

def getattr(object, name):
    # return getattr()
    pass

def globals():
    # return globals()
    pass

def hasattr(object, name):
    # return hasattr()
    pass

def hash(object):
    # return hash()
    pass

def help():
    # return help()
    pass

def hex(x):
    if not isinstance(x, int):
        raise TypeError("an integer is required")
    hex_digits = "0123456789abcdef"
    result = ""
    while x > 0:
        x = x / 16
        remainder = x % 16
        result = hex_digits[remainder] + result
    return "0x" + result if result else "0x0"

def id(object):
    # return id()
    pass

def input():
    # return input()
    pass

def int(x=0):
    # return int()
    pass

def isinstance(object, classinfo):
    # return isinstance()
    pass

# def issubclass(class, classinfo):
    # return issubclass()
    pass

def iter(object):
    # return iter()
    pass

def len(s):
    lenght = 0
    for _ in s:
        lenght = lenght + 1

    return lenght

def list():
    # return list()
    pass

def locals():
    # return locals()
    pass

def map(function, iterable, *iterables):
    # return map()
    pass

def max(iterable, *, key=None):
    # return max()
    pass

def memoryview(object):
    # return memoryview()
    pass

def min(iterable):
    lenght = builtins.len(iterable)
    if lenght == 0:
        raise  ValueError("Iterable is empty.")

    m = iterable[0]

    for i in builtins.range(1, lenght):
        if iterable[i] < m:
            m = iterable[i]
    return m

def next(iterator):
    # return next()
    pass

def object():
    # return object()
    pass

def oct(x):
    # return oct()
    pass

def open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None):
    # return open()
    pass

def ord(c):
    # return ord()
    pass

def pow(base, exp, mod=None):
    # return pow()
    pass

def print(*objects, sep=' ', end='\n', file=None, flush=False):
    # return print()
    pass

def property(fget=None, fset=None, fdel=None, doc=None):
    # return property()
    pass

def range(stop):
    # return range()
    pass

def repr(object):
    # return repr()
    pass

def reversed(seq):
    # return reversed()
    pass

def round(number, ndigits=None):
    # return round()
    pass

def set():
    # return set()
    pass

def setattr(object, name, value):
    # return setattr()
    pass

def slice(stop):
    # return slice()
    pass

def sorted(iterable, /, *, key=None, reverse=False):
    # return sorted()
    pass

# def staticmethod():
#     # return staticmethod()
#     pass

def str(object=''):
    # return str()
    pass

def sum(iterable):
    s = 0
    for v in iterable:
        s = s + v
    
    return s

def super():
    # return super()
    pass

def tuple():
    # return tuple()
    pass

def type():
    # return type()
    pass

def vars():
    # return vars()
    pass

def zip(*iterables, strict=False):
    # return zip()
    pass

# def import():
    # return import()  pass
    # pass
