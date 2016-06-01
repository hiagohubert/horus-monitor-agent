#!-*- coding: utf8 -*-

import requests, json
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import tasks
import config

task = tasks.Tasks()
if not os.getuid() == 0:
    sys.exit('O setup deve ser executado como root!')

print " _    _    ____    _____    _    _    _____     __  __    ____    _   _   _____   _______    ____    _____"
print "| |  | |  / __ \  |  __ \  | |  | |  / ____|   |  \/  |  / __ \  | \ | | |_   _| |__   __|  / __ \  |  __ \\"
print "| |__| | | |  | | | |__) | | |  | | | (___     | \  / | | |  | | |  \| |   | |      | |    | |  | | | |__) |"
print "|  __  | | |  | | |  _  /  | |  | |  \___ \    | |\/| | | |  | | | . ` |   | |      | |    | |  | | |  _  /"
print "| |  | | | |__| | | | \ \  | |__| |  ____) |   | |  | | | |__| | | |\  |  _| |_     | |    | |__| | | | \ \\"
print "|_|  |_|  \____/  |_|  \_\  \____/  |_____/    |_|  |_|  \____/  |_| \_| |_____|    |_|     \____/  |_|  \_\\"
print "*************************************************************************************************************"


print "\n \nInforme o token do servidor:"

token = raw_input()

print "\n \nO token informado foi: "+token

test_token = requests.get(config.HOST+"/api/machine/"+token)

if test_token.status_code == 200:
    result = json.loads(test_token.content)
    print "Token validado com sucesso.\n\nO token fornecido referente ao servidor: " +result['name']

    task.saveToken(token)
    task.OSInfo()
    task.initWithSystem()
    task.runMonitor()

else:
    sys.exit("O token informado é inválido, verifique o código no seu Dashboard e tente novamente.")
