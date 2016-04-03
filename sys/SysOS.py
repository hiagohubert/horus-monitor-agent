import subprocess
import shlex
from entities.OS import OS

class SysOS(object):

    def getDistributorID(self):
        proc1 = subprocess.Popen(shlex.split('lsb_release --id'), stdout=subprocess.PIPE)
        out, err = proc1.communicate()
        distributor_id = out.split(":")
        return distributor_id[1].strip()

    def get

teste = SysOS()
teste.getDistributorID()