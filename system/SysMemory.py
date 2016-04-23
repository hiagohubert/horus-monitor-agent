import subprocess
import shlex
import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from entities.Memory import Memory

class SysMemory(object):
    memory = None

    def __init__(self):
        self.getMemory()

    def getMemory(self):
        proc1 = subprocess.Popen(shlex.split('free -h'), stdout=subprocess.PIPE)
        proc2 = subprocess.Popen(shlex.split('tail -n 3'), stdin=proc1.stdout,
                                 stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        proc3 = subprocess.Popen(shlex.split('head -n 1'), stdin=proc2.stdout,
                                 stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        proc1.stdout.close()
        proc2.stdout.close()

        out, err = proc3.communicate()

        memory_data = out.split()

        memory = Memory(float(memory_data[1].replace("G", "").replace(",", ".")), float(memory_data[2].replace("G", "").replace(",", ".")), float(memory_data[3].replace("G", "").replace(",", ".")))

        self.memory = memory
