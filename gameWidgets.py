from pygame_widgets.button import Button
from pygame_widgets.textbox import TextBox

import gameDefs
import gameWidgetsLogic

class GameWidgets:
    def __init__(self, gameWidgetsLogic, pygame, gameLogic, gameTexts, windowWidth, windowHeight, screen):
        self.gameWidgetsLogic = gameWidgetsLogic
        self.pg = pygame
        self.gameLogic = gameLogic
        self.gameTexts = gameTexts
        self.windowWidth = windowWidth
        self.windowHeight = windowHeight
        self.screen = screen
        self.mainMenuWidgets = []
        self.joinGameMenuWidgets = []
        self.waitingRoomWidgets = []
        self.pauseWidgets = []
        self.gameResultWidgets = []
        
        self.initWidgets()
        
    def initWidgets(self):
        self.mainMenuWidgets.append(Button(
            self.screen, self.windowWidth/2 - 175, 300, 350, 100, text='Zaloz gre',
            font=self.gameTexts.bigFont,
            fontSize=50, margin=20,
            inactiveColour=(150, 150, 150),
            borderThickness=4,
            borderColour=(0, 0, 0),
            pressedColour=(50, 50, 50), radius=0,
            onClick=self.gameWidgetsLogic.createGameButton
        ))
        self.mainMenuWidgets.append(Button(
            self.screen, self.windowWidth/2 - 175, 450, 350, 100, text='Dolacz do gry',
            font=self.gameTexts.bigFont,
            fontSize=50, margin=20,
            inactiveColour=(150, 150, 150),
            borderThickness=4,
            borderColour=(0, 0, 0),
            pressedColour=(50, 50, 50), radius=0,
            onClick=self.gameWidgetsLogic.joinGameButton
        ))
        self.mainMenuWidgets.append(Button(
            self.screen, self.windowWidth/2 - 175, 600, 350, 100, text='Wyjdz z gry',
            font=self.gameTexts.bigFont,
            fontSize=50, margin=20,
            inactiveColour=(150, 150, 150),
            borderThickness=4,
            borderColour=(0, 0, 0),
            pressedColour=(50, 50, 50), radius=0,
            onClick=self.gameWidgetsLogic.exitGameButton
        ))
        
        self.joinGameMenuWidgets.append(Button(
            self.screen, self.windowWidth/2 - 175, 450, 350, 100, text='Dolacz',
            font=self.gameTexts.bigFont,
            fontSize=50, margin=20,
            inactiveColour=(150, 150, 150),
            borderThickness=4,
            borderColour=(0, 0, 0),
            pressedColour=(50, 50, 50), radius=0,
            onClick=self.gameWidgetsLogic.ipTextBoxSubmit
        ))
        self.joinGameMenuWidgets.append(TextBox(
            self.screen,
            self.windowWidth/2 - 150, self.windowHeight/2 - 100, 300, 40,
            font=self.gameTexts.smallFont,
            fontSize=24,
            inactiveColour=(150, 150, 150),
            borderThickness=4,
            borderColour=(0, 0, 0),
            pressedColour=(50, 50, 50), radius=0,
            onSubmit=self.gameWidgetsLogic.ipTextBoxSubmit
        ))
        self.joinGameMenuWidgets.append(Button(
            self.screen, 50, self.windowHeight - 150, 350, 100, text='Wstecz',
            font=self.gameTexts.bigFont,
            fontSize=50, margin=20,
            inactiveColour=(150, 150, 150),
            borderThickness=4,
            borderColour=(0, 0, 0),
            pressedColour=(50, 50, 50), radius=0,
            onClick=self.gameWidgetsLogic.backToMenuButton
        ))
        
        self.waitingRoomWidgets.append(Button(
            self.screen, 50, self.windowHeight - 150, 350, 100, text='Wstecz',
            font=self.gameTexts.bigFont,
            fontSize=50, margin=20,
            inactiveColour=(150, 150, 150),
            borderThickness=4,
            borderColour=(0, 0, 0),
            pressedColour=(50, 50, 50), radius=0,
            onClick=self.gameWidgetsLogic.backToMenuButton
        ))
        self.waitingRoomWidgets.append(Button(
            self.screen, self.windowWidth - 400, self.windowHeight - 150, 350, 100, text='Start',
            font=self.gameTexts.bigFont,
            fontSize=50, margin=20,
            inactiveColour=(150, 150, 150),
            borderThickness=4,
            borderColour=(0, 0, 0),
            pressedColour=(50, 50, 50), radius=0,
            onClick=self.gameWidgetsLogic.startGameButton
        ))
        
        self.pauseWidgets.append(Button(
            self.screen, self.windowWidth/2 - 175, 300, 350, 100, text='Wznow gre',
            font=self.gameTexts.bigFont,
            fontSize=50, margin=20,
            inactiveColour=(150, 150, 150),
            borderThickness=4,
            borderColour=(0, 0, 0),
            pressedColour=(50, 50, 50), radius=0,
            onClick=self.gameWidgetsLogic.resumeButton
        ))
        self.pauseWidgets.append(Button(
            self.screen, self.windowWidth/2 - 175, 450, 350, 100, text='Rozlacz',
            font=self.gameTexts.bigFont,
            fontSize=50, margin=20,
            inactiveColour=(150, 150, 150),
            borderThickness=4,
            borderColour=(0, 0, 0),
            pressedColour=(50, 50, 50), radius=0,
            onClick=self.gameWidgetsLogic.disconnectButton
        ))
        
        self.gameResultWidgets.append(Button(
            self.screen, self.windowWidth/2 - 175, 420, 350, 100, text='Wroc do menu',
            font=self.gameTexts.bigFont,
            fontSize=50, margin=20,
            inactiveColour=(150, 150, 150),
            borderThickness=4,
            borderColour=(0, 0, 0),
            pressedColour=(50, 50, 50), radius=0,
            onClick=self.gameWidgetsLogic.backToMenuButton
        ))
        
    def hideJoinGameMenuWidgets(self):
        for widget in self.joinGameMenuWidgets:
            widget.hide()
            widget.disable()
            
    def hideMainMenuWidgets(self):
        for widget in self.mainMenuWidgets:
            widget.hide()
            widget.disable()
            
    def hideWaitingRoomWidgets(self):
        for widget in self.waitingRoomWidgets:
            widget.hide()
            widget.disable()
            
    def hidePauseWidgets(self):
        for widget in self.pauseWidgets:
            widget.hide()
            widget.disable()
            
    def hideGameResultWidgets(self):
        for widget in self.gameResultWidgets:
            widget.hide()
            widget.disable()
        
    def showMainMenuWidgets(self):
        self.hideWaitingRoomWidgets()
        self.hideJoinGameMenuWidgets()
        
        for widget in self.mainMenuWidgets:
            widget.show()
            widget.enable()
            
    def showJoinGameMenuWidgets(self):
        self.hideMainMenuWidgets()
        self.hideWaitingRoomWidgets()
        
        for widget in self.joinGameMenuWidgets:
            widget.show()
            widget.enable()
            
    def showWaitingRoomWidgets(self):
        self.hideMainMenuWidgets()
        self.hideJoinGameMenuWidgets()
        
        for widget in self.waitingRoomWidgets:
            # hide start button if player is not host
            if widget == self.waitingRoomWidgets[1]:
                if self.gameLogic.playerIsHost:
                    widget.show()
                    widget.enable()
                else:
                    widget.hide()
                    widget.disable()
            else:
                widget.show()
                widget.enable()
            
    def showGameMapWidgets(self):
        self.hideWaitingRoomWidgets()
        
    def showPauseWidgets(self):
        for widget in self.pauseWidgets:
            widget.show()
            widget.enable()
            
    def showGameResultWidgets(self):
        for widget in self.gameResultWidgets:
            widget.show()
            widget.enable()
        
    def showPauseWidgetsIfPaused(self):
        if not self.gameLogic.paused:
            self.hidePauseWidgets()
        else:
            self.showPauseWidgets()
    
    def showGameResultWidgetsIfGameEnded(self):
        if self.gameLogic.gameResult != gameDefs.GameResult.PLAYING.value and self.gameLogic.scene == gameDefs.Scene.GAME.value:
            self.showGameResultWidgets()
        else:
            self.hideGameResultWidgets()
        