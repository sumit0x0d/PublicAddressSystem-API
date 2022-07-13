from typing import List
import alsaaudio
import time
import audioop

import socket

IP_ADDR = '127.0.0.1'

SEND_PORT = 8888
RECV_PORT = 8888

PERIOD_SIZE = 1024
FORMAT = alsaaudio.PCM_FORMAT_S16_LE
CHANNELS = 1
RATE=8000
DEVICE = "default"

allData = []
count = 0

output_audio = alsaaudio.PCM(alsaaudio.PCM_PLAYBACK, alsaaudio.PCM_NORMAL,
    channels = CHANNELS,
    rate = RATE,
    format = FORMAT,
    periodsize = PERIOD_SIZE,
    device = DEVICE)

recv_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
recv_sock.bind((IP_ADDR, RECV_PORT))

allData = bytearray()
count = 0

while count != 4000:
    msg, _ = recv_sock.recvfrom(1024)
    for i in msg:
        allData.append(i)
    count = count + 1
    # output_audio.write(msg)

list1 = [allData[i:i+PERIOD_SIZE] for i in range(0, len(allData), PERIOD_SIZE)]

for arr in list1:
    output_audio.write(arr)
