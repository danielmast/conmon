import subprocess
from subprocess import PIPE


def packet_loss():
    hostname = "8.8.8.8"
    process = subprocess.Popen(['ping', '-c', '20', hostname],
                               stdout=PIPE, stderr=PIPE)
    stdout, stderr = process.communicate()
    loss = float(
        [x for x in stdout.decode('utf-8').split('\n') if x.find('packet loss') != -1][0].split('%')[0].split(' ')[-1])
    return loss