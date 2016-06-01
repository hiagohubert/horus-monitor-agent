import subprocess
import shlex
import sys
import os.path
import re

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from entities.Disc import Disc

class SysDisc(object):
    discs = []

    def __init__(self):
        self.getDiscs()

    def getDiscs(self):
        number = re.compile(r'[^\d]+')
        proc1 = subprocess.Popen(shlex.split('df -h'), stdout=subprocess.PIPE)
        proc2 = subprocess.Popen(shlex.split('wc -l'), stdin=proc1.stdout,
                                 stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        proc1.stdout.close()
        out, err = proc2.communicate()
        num_disc = int(out) - 1

        for i in range(num_disc ,0, -1):
            proc1 = subprocess.Popen(shlex.split('df -h'), stdout=subprocess.PIPE)
            proc2 = subprocess.Popen(shlex.split('tail -n ' +str(i)), stdin=proc1.stdout,
                                     stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            proc3 = subprocess.Popen(shlex.split('head -n 1'), stdin=proc2.stdout,
                                     stdout=subprocess.PIPE, stderr=subprocess.PIPE)

            proc1.stdout.close()
            proc2.stdout.close()

            out, err = proc3.communicate()
            disco_info = out.split()

            disc = Disc(disco_info[0], disco_info[1], disco_info[2], disco_info[3], disco_info[4].replace("%", ""), disco_info[5])
            self.discs.append(disc)
