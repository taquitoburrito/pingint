import os
import subprocess


def pingAll():
    c = 0
    while c < 256:
        fullIP = "192.168.86." + str(c)
        upDown = os.system("ping " + fullIP)
        c = c + 1
        output = str(subprocess.Popen(["ping.exe",fullIP],stdout = subprocess.PIPE).communicate()[0])
        if 'unreachable.' in output:
            upDown = 1
        response(upDown, fullIP)

def pingServers():
    baseIP = '192.168.86.'
    Server1 = '228'
    Server2 = '52'
    Server3 = '143'
    Server4 = '140'
    Server5 =  '166'
    Server6 = '43'
    n = 0
    list = [Server1, Server2, Server3, Server4, Server5, Server6]
    for i in list:
        fullIP = baseIP + list[n]
        upDown = os.system("ping -n 1 " + fullIP)
        output = str(subprocess.Popen(["ping.exe",fullIP],stdout = subprocess.PIPE).communicate()[0])
        if 'unreachable.' in output:
            upDown = 1

        response(upDown, fullIP)
        n = n + 1

        

def response(upDown, fullIP):
    if upDown == 0:
        print(fullIP +' is up!')
    else:
        print(fullIP + ' is down!')

ans = input('1. ping all (Takes a LONG time) or 2. ping servers? \n')
if ans == '1':
    pingAll()
elif ans == '2':
    pingServers()
else:
    pingServers()


