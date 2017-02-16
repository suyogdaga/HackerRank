import sys

class Stack():
    def __init__(self):
        self._data = []

    def push(self, item):
        self._data.append(item)

    def is_empty(self):
        return len(self._data) == 0

    def pop(self):
        return self._data.pop()


def is_matched(expression):
    lefty ='{[('
    righty = '}])'

    s = Stack()

    for c in expression:
        if c in lefty:
            s.push(c)

        elif c in righty:
            if s.is_empty():
                return False
            elif righty.index(c) != lefty.index(s.pop()):
                return False

    return s.is_empty()

t = int(raw_input().strip())
for a0 in xrange(t):
    x = raw_input().strip()
    if is_matched(x):
        print 'YES'
    else:
        print 'NO'