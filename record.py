import pyaudio
import wave
import time
import loop_play
f = open('bpm.txt','r')
bpm = int(round(float(f.read())))
f.close()
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = (240/bpm)*4
WAVE_OUTPUT_FILENAME_CHANNEL1 = "file1.wav"
WAVE_OUTPUT_FILENAME_CHANNEL2 = "file2.wav"
WAVE_OUTPUT_FILENAME_CHANNEL3 = "file3.wav"
audio = pyaudio.PyAudio()

def channel1(frames,stream):
    print "Recorded in channel 1..."
    waveFile = wave.open(WAVE_OUTPUT_FILENAME_CHANNEL1, 'wb')
    waveFile.setnchannels(CHANNELS)
    waveFile.setsampwidth(audio.get_sample_size(FORMAT))
    waveFile.setframerate(RATE)
    waveFile.writeframes(b''.join(frames))
    waveFile.close()
def channel2(frames,stream):
    print "Recorded in channel 2..."
    waveFile = wave.open(WAVE_OUTPUT_FILENAME_CHANNEL2, 'wb')
    waveFile.setnchannels(CHANNELS)
    waveFile.setsampwidth(audio.get_sample_size(FORMAT))
    waveFile.setframerate(RATE)
    waveFile.writeframes(b''.join(frames))
    waveFile.close()
def channel3(frames,stream):
    print "Recorded in channel 3..."
    waveFile = wave.open(WAVE_OUTPUT_FILENAME_CHANNEL3, 'wb')
    waveFile.setnchannels(CHANNELS)
    waveFile.setsampwidth(audio.get_sample_size(FORMAT))
    waveFile.setframerate(RATE)
    waveFile.writeframes(b''.join(frames))
    waveFile.close()
    stream.stop_stream()
    stream.close()
    audio.terminate()
def rec(counter): 
# start Recording

    raw_input("Start Recording")
    print "4"
    time.sleep(240/(4*bpm))
    print "3"
    time.sleep(240/(4*bpm))
    print "2"
    time.sleep(240/(4*bpm))
    print "1"
    time.sleep(240/(4*bpm))
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                rate=RATE, input=True,
                frames_per_buffer=CHUNK)
    
    print "recording..."
    frames = []
 
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)
    print "finished recording"
    if counter==1:
        channel1(frames,stream)
        loop_play.s1()
        print "looping channel 1..."

    elif counter==2:
        channel2(frames,stream)
        loop_play.s2()
        print "looping channel 2..."
    elif counter==3:
        channel3(frames,stream)
        loop_play.s2()
        print "looping channel 3..."
        print "All Channels are full"
        while True:
            pass
    del frames[ 0:len(frames) ]
# stop Recording
    

def main():

    counter=0    
    while True:
        counter+=1
        rec(counter)
       
main()
