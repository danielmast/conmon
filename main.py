import csv
import datetime
import sys
import time

import speedtest

import ping

print('Start monitoring connection')
s = speedtest.Speedtest()
file = sys.argv[1]

while True:
    t = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    try:
        down = round(s.download()/1024/1024, 1)
        up = round(s.upload()/1024/1024, 1)
        packet_loss = ping.packet_loss()

        print(t, ':', 'Download:', down, 'Mbps', ', Upload:', up, 'Mbps', ', Packet loss:', packet_loss, '%')

        values = [t, down, up, packet_loss]
    except:
        values = [t, '', '', '']
        print('exception')

    with open(file, 'a') as f:
        writer = csv.writer(f)
        writer.writerow(values)
    time.sleep(60*30)
