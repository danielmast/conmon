import time

import speedtest

import ping

s = speedtest.Speedtest()

while True:
    print(time.ctime())
    try:
        down = s.download()/1024/1024
        up = s.upload()/1024/1024
        packet_loss = ping.packet_loss()
        print('Download:', round(down, 1), 'Mbps')
        print('Upload:', round(up, 1), 'Mbps')
        print('Packet loss:', packet_loss, '%')
    except:
        print('exception')
    time.sleep(60*5)