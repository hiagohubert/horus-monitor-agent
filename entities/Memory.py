class Memory(object):
    total = 0.0
    used = 0.0
    free = 0.0

    def __init__(self, total, used, free):
        self.total = total
        self.used = used
        self.free = free
    