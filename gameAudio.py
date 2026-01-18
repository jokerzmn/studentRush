import pygame as pg

class GameAudio:
    def playButtonClickSound(self):
        pg.mixer.music.load("res/audio/buttonClick.wav")
        pg.mixer.music.play()
        