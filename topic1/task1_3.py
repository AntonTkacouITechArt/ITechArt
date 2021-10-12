class FibIterator:
    def __init__(self):
        self.counter = 0
        self.limit = 100
        self.prev = 0
        self.next = 1

    def __next__(self):
        if self.counter < self.limit:
            self.counter += 1
            buff1 = self.prev
            buff2 = self.next
            self.next += self.prev
            self.prev = buff2
            return buff1
        else:
            raise StopIteration

    def __iter__(self):
        self.counter = 0
        self.prev = 0
        self.next = 1
        return self


def fib_generator():
    prev = 0
    next = 1
    for _ in range(0, 100):
        yield prev
        buff = prev + next
        prev = next
        next = buff


def strange_decorator(func):
    def wrapper(*args, **kwargs):
        if (len(args) + len(kwargs)) > 10:
            raise ValueError
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if type(v) is bool:
                    raise TypeError
        a = func(*args, **kwargs)
        if type(a) is int:
            a += 13
        return a

    return wrapper
