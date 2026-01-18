import sys
import pygame as pg
import pygame_widgets as pw

import gameDefs
import gameLogic
import gameTextures
import gameTexts
import gameAudio
import gameWidgets
import gameWidgetsLogic
import gameDraw

class StudentRush:
    def __init__(self, fpsCap, windowWidth, windowHeight):
        self.fpsCap = fpsCap
        self.windowWidth = windowWidth
        self.windowHeight = windowHeight
        self.screen = None
        self.clock = None
        
        self.overlay = pg.Surface((windowWidth, windowHeight), pg.SRCALPHA)
        self.overlay.fill((0, 0, 0, 150))
        self.initPygame()
        
        self.gTextures = gameTextures.GameTextures(pg)
        self.gLogic = gameLogic.GameLogic()
        self.gTexts = gameTexts.GameTexts(pg, self.gLogic, self.windowWidth, self.windowHeight)

        self.gAudio = gameAudio.GameAudio()
        self.gWidgetsLogic = gameWidgetsLogic.GameWidgetsLogic(self.gLogic, self.gAudio)
        self.gWidgets = gameWidgets.GameWidgets(self.gWidgetsLogic, pg, self.gLogic, self.gTexts, self.windowWidth, self.windowHeight, self.screen)
        self.gDraw = gameDraw.GameDraw(self.gLogic, self.gTextures, self.gTexts, self.windowWidth, self.windowHeight, self.screen)
    
    def initPygame(self):
        pg.init()
        pg.display.set_caption("Student Rush")
        self.screen = pg.display.set_mode((self.windowWidth, self.windowHeight))
        self.clock = pg.time.Clock()
        
    def handleEvents(self, events):
        for event in events:
            if event.type == pg.QUIT:
                self.gLogic.run = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    if self.gLogic.scene == gameDefs.Scene.GAME.value and self.gLogic.gameResult == gameDefs.GameResult.PLAYING.value:
                        self.gLogic.paused = not self.gLogic.paused
    
    def loop(self):
        self.screen.fill((60, 60, 60))
        
        events = pg.event.get()
        self.handleEvents(events)
                    
        self.gWidgets.showPauseWidgetsIfPaused()
        self.gWidgets.showGameResultWidgetsIfGameEnded()
        
        match self.gLogic.scene:
            case gameDefs.Scene.MAIN_MENU.value:
                self.gDraw.drawTextGroup(self.gTexts.mainMenuTexts)
                self.gWidgets.showMainMenuWidgets()
            
            case gameDefs.Scene.JOIN_GAME.value:
                if self.gLogic.joinError == gameDefs.ErrorCode.JOIN_GAME:
                    self.gDraw.drawJoinError()
                
                self.gDraw.drawTextGroup(self.gTexts.joinGameMenuTexts)
                self.gWidgets.showJoinGameMenuWidgets()
                
            case gameDefs.Scene.WAITING_ROOM.value:
                self.gDraw.drawPlayersWaitingRoom()
                self.gDraw.drawTextGroup(self.gTexts.waitingRoomTexts)
                self.gWidgets.showWaitingRoomWidgets()
                
            case gameDefs.Scene.GAME.value:
                self.gDraw.drawGameArea()
                self.gDraw.drawDesks()
                
                self.gDraw.drawPlayerHeads()
                self.gDraw.drawPLayersTaskCount()
                self.gDraw.drawInventory()
                
                self.gDraw.drawPlayers()
                
                self.gDraw.drawTextGroup(self.gTexts.gameMapTexts)
                self.gWidgets.showGameMapWidgets()
                
                self.gDraw.drawReturnTaskIfActive()
                self.gDraw.drawTimer()
                
                if self.gLogic.getRemainingTime() <= 0:
                    self.gLogic.endGame()
                
                if self.gLogic.paused:
                    self.screen.blit(self.overlay, (0, 0))
                    
                if self.gLogic.gameResult != gameDefs.GameResult.PLAYING.value:
                    self.screen.blit(self.overlay, (0, 0))
                    self.gTexts.checkGameResultForText()
                    self.gDraw.drawGameResult()
        
        pw.update(events)
        pg.display.update()
        self.clock.tick(self.fpsCap)
        
game = StudentRush(60, 1600, 900)

while game.gLogic.run:
    game.loop()
