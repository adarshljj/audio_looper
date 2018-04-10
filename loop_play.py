import pygame
import sounddevice as sd
#fs=48000
duration = 10.5  # seconds
#myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=2)
file = 'file.wav'
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(file)
while 1:
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
