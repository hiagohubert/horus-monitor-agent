import requests, json, sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from system.SysCPU import SysCPU
from system.SysService import SysService
from system.SysOS import SysOS
from system.SysDisc import SysDisc
from system.SysMemory import SysMemory

class Rest(object):

    def saveServiceInfo(self):
        services = SysService()
        data = []
        for service in services.service_list:
            service_dict = {"service": service.name, "status": str(service.status)}
            data.append(service_dict)

        requests.post("http://rest", data=data) #TODO

    def saveOSInfo(self):
        os = SysOS()
        os_info = os.OSinfo()
        data = {"distributor_id": os_info.distributor_id, "release": os_info.release,
                "codename": os_info.codename, "description": os_info.description}
        requests.post("http://rest", data=data) #TODO

    def saveDiscInfo(self):
        disc = SysDisc()
        data = []
        for disc_info in disc.discs:
            disc_dict = {"file_system": disc_info.file_system, "size": disc_info.size, "used": disc_info.used,
                         "free": disc_info.free, "free_percent": disc_info.free_percent, "mounted_in": disc_info.mounted_in}
            data.append(disc_dict)

        requests.post("http://rest", data=data) #TODO

    def saveMemoryInfo(self):
        memory = SysMemory()
        data = {"free": memory.memory.free, "percent_used": memory.memory.percent_used, "total": memory.memory.total, "used": memory.memory.used }
        requests.post("http://rest", data=data)

    def saveCPUInfo(self):
        cpu = SysCPU()
        cpu_info = cpu.CPUinfo()
        data = {"architecture": cpu_info.architecture, "vendor_id": cpu_info.vendor_id, "model_name": cpu_info.model_name,
                "cpu_cores": cpu_info.cpu_cores, "percent_used": cpu_info.percent_used }
        requests.post("http://rest", data=data) #TODO

