import gameDefs
import gameNetworking

class GameWidgetsLogic:
    def __init__(self, gameLogic, gameAudio, gameNetworking):
        self.gameLogic = gameLogic
        self.gameAudio = gameAudio
        self.gameNetworking = gameNetworking
        
    def exitGameButton(self):
        self.gameLogic.run = False
        
    def joinGameButton(self):
        self.gameAudio.playButtonClickSound()
        self.gameLogic.scene = gameDefs.Scene.JOIN_GAME.value
        self.gameNetworking.gameWidgets.joinGameMenuWidgets[1].setText("")
        
    def createGameButton(self):
        self.gameAudio.playButtonClickSound()
        self.gameLogic.playerIsHost = True
        self.gameLogic.scene = gameDefs.Scene.WAITING_ROOM.value
        self.gameNetworking.startServer()
        
    def backToMenuButton(self):
        self.gameAudio.playButtonClickSound()
        self.gameLogic.gameResult = gameDefs.GameResult.PLAYING.value
        self.gameLogic.scene = gameDefs.Scene.MAIN_MENU.value
        
        self.gameNetworking.disconnect()
        # Reset error
        self.gameLogic.joinError = gameDefs.ErrorCode.SUCCESS
        
    def ipTextBoxSubmit(self):
        self.gameAudio.playButtonClickSound()
        
        if not self.gameNetworking.gameWidgets.joinGameMenuWidgets[1].getText():
            return
            
        self.gameLogic.playerIsHost = False
        self.gameNetworking.startClient()
        
    def startGameButton(self):
        self.gameAudio.playButtonClickSound()
        self.gameNetworking.broadcastStartGame()
        self.gameLogic.scene = gameDefs.Scene.GAME.value
        
        self.gameLogic.resetGame()
        
    def resumeButton(self):
        self.gameAudio.playButtonClickSound()
        self.gameLogic.paused = False
        
    def disconnectButton(self):
        self.gameAudio.playButtonClickSound()
        self.gameLogic.paused = False
        self.backToMenuButton()
        