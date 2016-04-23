class Disc(object):
    file_system = ""
    size = 0.0
    used = 0.0
    free = 0.0
    free_percent = 0.0
    mounted_in = ""

    def __init__(self, file_system, size, used, free, free_percent, mounted_in):
        self.file_system = file_system
        self.size = size
        self.used = used
        self.free = free
        self.mounted_in = mounted_in
        self.free_percent = str(100.0 - float( free_percent ))