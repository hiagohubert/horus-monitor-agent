import time
import threading
from rest.Rest import Rest
import config

rest = Rest()

def monitorCPU():
    print "Iniciando monitoramento de CPU..."
    while True:
        rest.saveCPUInfo()
        time.sleep(config.DELAY_BETWEEN_REQUESTS)

def monitorMemory():
    print "Iniciando monitoramento de memoria..."
    while True:
        rest.saveMemoryInfo()
        time.sleep(config.DELAY_BETWEEN_REQUESTS)

def monitorDisc():
    print "Iniciando monitoramento de disco..."
    while True:
        rest.saveDiscInfo()
        time.sleep(config.DELAY_BETWEEN_REQUESTS)

def core():
    try:
        threading.Thread(target=monitorCPU).start()
        threading.Thread(target=monitorMemory).start()
        threading.Thread(target=monitorDisc).start()
    except:
        print "Problema ao iniciar thread"


core()