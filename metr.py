import time
import pyaudio
import numpy as np
import tap
import threading
#import record


tap.main()
p = pyaudio.PyAudio()
f=open('bpm.txt','r')
bpm=int(round(float(f.read())))
f.close()       
volume = 0.3     # range [0.0, 1.0]
fs = 44100       # sampling rate, Hz, must be integer
duration = 0.4   # in seconds, may be float
f = 1760.0
f1 = 1318.5102276514797  # sine frequency, Hz, may be float


samples = (np.sin(2*np.pi*np.arange(fs*duration)*f/fs)).astype(np.float32)
samples1 = (np.sin(2*np.pi*np.arange(fs*duration)*f1/fs)).astype(np.float32)

stream = p.open(format=pyaudio.paFloat32,
                channels=1,
                rate=fs,
                output=True)

bpb=4

def play(counter,sleep):
    while True:
        counter += 1
        if counter % bpb:
            stream.write(volume*samples1)
        else:
            stream.write(volume*samples)
        time.sleep(sleep)
def main():
    sleep = 60.0 / bpm 
    counter = 0
    #t1=threading.Thread(target=play,args=(counter,sleep))
    play(counter,sleep)
    #t1.start()
    t2=threading.Thread(target=record.main,args=(counter,sleep))
    t2.start()
    print("Main function is here")
    
   # stream.stop_stream()
   # stream.close()
   # p.terminate()

main()
