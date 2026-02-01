import pygame as pg

class GameAudio:
    def playButtonClickSound(self):
        pg.mixer.music.load("res/audio/buttonClick.wav")
        pg.mixer.music.play()
        
    def playPickupSound(self):
        pg.mixer.music.load("res/audio/pickupTask.wav")
        pg.mixer.music.play()
        
    def playReturnTaskSound(self):
        pg.mixer.music.load("res/audio/returnTask.wav")
        pg.mixer.music.play()
        
    def playGameResultWin(self):
        pg.mixer.music.load("res/audio/gameResultWin.wav")
        pg.mixer.music.play()
        
    def playGameResultDraw(self):
        pg.mixer.music.load("res/audio/gameResultDraw.wav")
        pg.mixer.music.play()
        
    def playGameResultLose(self):
        pg.mixer.music.load("res/audio/gameResultLose.wav")
        pg.mixer.music.play()
        