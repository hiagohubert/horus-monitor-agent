import subprocess
import shlex
import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from entities.OS import OS

class SysOS(object):

    def getDistributorID(self):
        proc1 = subprocess.Popen(shlex.split('lsb_release --id'), stdout=subprocess.PIPE)
        out, err = proc1.communicate()
        distributor_id = out.split(":")
        return distributor_id[1].strip()

    def getRelease(self):
        proc1 = subprocess.Popen(shlex.split('lsb_release -r'), stdout=subprocess.PIPE)
        out, err = proc1.communicate()
        release = out.split(":")
        return release[1].strip()

    def getCodeName(self):
        proc1 = subprocess.Popen(shlex.split('lsb_release -c'), stdout=subprocess.PIPE)
        out, err = proc1.communicate()
        codename = out.split(":")
        return codename[1].strip()

    def getDescription(self):
        proc1 = subprocess.Popen(shlex.split('lsb_release -d'), stdout=subprocess.PIPE)
        out, err = proc1.communicate()
        description = out.split(":")
        return description[1].strip()

    def OSinfo(self):
        os = OS(self.getDistributorID(), self.getRelease(), self.getCodeName(), self.getDescription())
        return os

