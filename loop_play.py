import pygame
# Initialize the mixer
pygame.mixer.init()
# Load two sounds

# Play the sounds; these will play simultaneously

def s1():
    snd1 = pygame.mixer.Sound('file1.wav')
    snd1.play(-1)
def s2():
    snd2 = pygame.mixer.Sound('file2.wav')
    snd2.play(-1)
def s3():
    snd3 = pygame.mixer.Sound('file3.wav')
    snd3.play(-1)
