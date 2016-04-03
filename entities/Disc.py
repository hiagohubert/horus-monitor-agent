class Disc(object):
    file_system = ""
    size = 0.0
    used = 0.0
    free = 0.0
    mounted_in = ""

    def __init__(self, file_system, size, used, free, mounted_in):
        self.file_system = file_system
        self.size = size
        self.used = used
        self.free = free
        self.mounted_in = mounted_in