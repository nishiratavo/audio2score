import pyaudio
import aubio
import numpy as np

FRAME = 2048 
SR = 44100
RUNNING_TIME = 10 #seconds

# setup pitch
tolerance = 0.8
win_s = 4096 # fft size
hop_s = FRAME # hop size
pitch_algo = aubio.pitch("default", win_s, hop_s, SR)
pitch_algo.set_unit("midi")
pitch_algo.set_tolerance(tolerance)

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paFloat32,channels=1,rate=SR,input=True,
              frames_per_buffer=FRAME)

for i in range(int(RUNNING_TIME*SR/FRAME)): #go for RUNNING_TIME few seconds
    data = np.fromstring(stream.read(FRAME),dtype=np.float32)
    pitch = pitch_algo(data)[0]
    confidence = pitch_algo.get_confidence()
    print("{} / {}".format(pitch,confidence))

stream.stop_stream()
stream.close()
p.terminate()