import gameDefs

class GameWidgetsLogic:
    def __init__(self, gameLogic, gameAudio):
        self.gameLogic = gameLogic
        self.gameAudio = gameAudio
        
    def exitGameButton(self):
        self.gameLogic.run = False
        
    def joinGameButton(self):
        self.gameAudio.playButtonClickSound()
        self.gameLogic.scene = gameDefs.Scene.JOIN_GAME.value
        
    def createGameButton(self):
        self.gameAudio.playButtonClickSound()
        self.gameLogic.playerIsHost = True
        self.gameLogic.scene = gameDefs.Scene.WAITING_ROOM.value
        
    def backToMenuButton(self):
        self.gameAudio.playButtonClickSound()
        self.gameLogic.gameResult = gameDefs.GameResult.PLAYING.value
        self.gameLogic.scene = gameDefs.Scene.MAIN_MENU.value
        
        # Reset error
        self.gameLogic.joinError = gameDefs.ErrorCode.SUCCESS
        
    def ipTextBoxSubmit(self):
        self.gameAudio.playButtonClickSound()
        self.gameLogic.playerIsHost = False
        # set to ErrorCode.JOIN_GAME on connection error
        self.gameLogic.joinError = gameDefs.ErrorCode.JOIN_GAME
        
    def startGameButton(self):
        self.gameAudio.playButtonClickSound()
        self.gameLogic.scene = gameDefs.Scene.GAME.value
        
        self.gameLogic.resetGame()
        
    def resumeButton(self):
        self.gameAudio.playButtonClickSound()
        self.gameLogic.paused = False
        
    def disconnectButton(self):
        self.gameAudio.playButtonClickSound()
        self.gameLogic.paused = False
        self.backToMenuButton()
        