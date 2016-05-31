import subprocess
import shlex
import sys
import os.path
import psutil
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from entities.Memory import Memory

class SysMemory(object):
    memory = None

    def __init__(self):
        self.getMemory()

    def convertToGB(self, num):
        num = round(float(num) / 2 ** 30, 2)
        return num

    def getMemory(self):

        values = psutil.virtual_memory()
        total = self.convertToGB(values.total)
        free = self.convertToGB(values.free)
        used = self.convertToGB(values.used)
        memory = Memory(total, used, free)

        self.memory = memory
