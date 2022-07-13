import alsaaudio
import time

import socket

IP_ADDR = '127.0.0.1'

SEND_PORT = 8888
RECV_PORT = 8888

PERIOD_SIZE = 1024
FORMAT = alsaaudio.PCM_FORMAT_S16_LE
CHANNELS = 1
RATE=8000
DEVICE = "default"

input_audio = alsaaudio.PCM(alsaaudio.PCM_CAPTURE, alsaaudio.PCM_NONBLOCK,
    channels = CHANNELS,
    rate = RATE,
    format = FORMAT,
    periodsize = PERIOD_SIZE,
    device = DEVICE)

output_audio = alsaaudio.PCM(alsaaudio.PCM_PLAYBACK, alsaaudio.PCM_NORMAL,
    channels = CHANNELS,
    rate = RATE,
    format = FORMAT,
    periodsize = PERIOD_SIZE,
    device = DEVICE)

send_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def send(msg):
    send_sock.sendto(bytes(msg), (IP_ADDR, SEND_PORT))

allData = bytearray()
count = 0
while True:
    _, data = input_audio.read()
    for b in data:
        allData.append(b)

    count += 1
    if count == 4000:
        break

    time.sleep(.001)

for i in allData:
    print(i)
    send(bytes(i))
# list1 = [allData[i:i+PERIOD_SIZE] for i in range(0, len(allData), PERIOD_SIZE)]

#Writing the output
# for arr in list1:
#     # I tested writing the arr's to a wave file at this point
#     # and the wave file was fine
#     output_audio.write(arr)


# f = open("test.raw", 'wb')
# loops = 1000000
# while(loops > 0):
#     loops -= 1
#     # Read data from device
#     l, data = input_audio.read()

#     if l:
#         f.write(data)
#         time.sleep(.001)