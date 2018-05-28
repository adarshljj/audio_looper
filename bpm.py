import time as time
raw_input("Tap 1")
c = float(time.time())
raw_input("Tap 2")
raw_input("Tap 3")
raw_input("Tap 4")
f=float(time.time())

def bpm():
    diff=(float (f)-float (c))
    #factor=diff*27
    #bpm = (1.0/(diff/60.0))

    bpm=float(float(60*float(4/float(diff)))*(float(3)/float(4)))
    print("time for 4 beats is ", float(diff))
    print("Beats per minute is ", float(bpm))
    return bpm
bpm()
