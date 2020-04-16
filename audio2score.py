import pyaudio
import numpy as np

FRAME = 2048 
RATE = 44100
RUNNING_TIME = 10 #seconds

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16,channels=1,rate=RATE,input=True,
              frames_per_buffer=FRAME)

for i in range(int(RUNNING_TIME*RATE/FRAME)): #go for RUNNING_TIME few seconds
    data = np.fromstring(stream.read(FRAME),dtype=np.int16)
    peak=np.average(np.abs(data))*2
    print(peak)

stream.stop_stream()
stream.close()
p.terminate()