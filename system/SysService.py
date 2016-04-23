import subprocess
import shlex
import sys
import os.path

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from entities.Service import Service
from entities.ServiceStatus import ServiceStatus

class SysService(object):
    service_list = []

    def __init__(self):
        self.getAllServices()

    def getAllServices(self):
        proc1 = subprocess.Popen(shlex.split('service --status-all'), stdout=subprocess.PIPE)

        out, err = proc1.communicate()
        out_lines = out.splitlines()
        size = len(out_lines)

        for i in range(1, size):
            service_str = out_lines[i]
            service = service_str.split()
            serviceobj = None

            if service[1] == "+":
                serviceobj = Service(service[3], ServiceStatus.RUNNING)
            else:
                serviceobj = Service(service[3], ServiceStatus.STOPPED)


            self.service_list.append(serviceobj)







