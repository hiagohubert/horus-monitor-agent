#!-*- coding: utf8 -*-
import requests, json
import subprocess
import shlex
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from rest.Rest import Rest

class Tasks(object):

    rest = Rest()
    local_app = os.getcwd()

    def saveToken(self, token):
        f = open('data/token.dat', 'w')
        f.write(str(token))
        f.close()

    def OSInfo(self):
        print "Capturando informações do sistema operacional..."
        self.rest.saveOSInfo()

    def initWithSystem(self):
        f = open('/etc/rc.local', 'w')
        f.write("python "+self.local_app+ "/monitor.py\nexit 0 ")
        f.close()

    def runMonitor(self):
        proc1 = subprocess.Popen(shlex.split('python '+self.local_app+'/monitor.py'))
