import subprocess
import shlex
import psutil
import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from entities.CPU import CPU

class SysCPU(object):

    def getModelName(self):
        proc1 = subprocess.Popen(shlex.split('lscpu'), stdout=subprocess.PIPE)
        proc2 = subprocess.Popen(shlex.split('grep \"Model name\"'), stdin=proc1.stdout,
                                 stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        proc1.stdout.close()
        out, err = proc2.communicate()
        model_name = out.split(":")
        return model_name[1].strip()

    def getVendorID(self):
        proc1 = subprocess.Popen(shlex.split('lscpu'), stdout=subprocess.PIPE)
        proc2 = subprocess.Popen(shlex.split('grep \"Vendor ID\"'), stdin=proc1.stdout,
                                 stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        proc1.stdout.close()
        out, err = proc2.communicate()
        vendor_id = out.split(":")
        return vendor_id[1].strip()

    def getArchitecture(self):
        proc1 = subprocess.Popen(shlex.split('lscpu'), stdout=subprocess.PIPE)
        proc2 = subprocess.Popen(shlex.split('grep \"Architecture\"'), stdin=proc1.stdout,
                                 stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        proc1.stdout.close()
        out, err = proc2.communicate()
        architecture = out.split(":")
        return architecture[1].strip()

    def getCPUCores(self):
        proc1 = subprocess.Popen(shlex.split('cat /proc/cpuinfo'), stdout=subprocess.PIPE)
        proc2 = subprocess.Popen(shlex.split('grep \"model name\"'), stdin=proc1.stdout,
                                 stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        proc3 = subprocess.Popen(shlex.split('wc -l'), stdin=proc2.stdout,
                                 stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        proc1.stdout.close()
        proc2.stdout.close()
        out, err = proc3.communicate()
        return out.strip()

    def getPercentUsed(self):
        return psutil.cpu_percent(interval=1)


    def CPUinfo(self):
        cpu = CPU(self.getArchitecture(), self.getVendorID(), self.getModelName(), self.getCPUCores(), self.getPercentUsed())
        return cpu.percent_used




