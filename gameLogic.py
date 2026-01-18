import pygame as pg

import gameDefs

class GameLogic:
    def __init__(self):
        self.scene = gameDefs.Scene.MAIN_MENU.value
        self.run = True
        self.playerIsHost = False
        self.playerID = 0
        self.paused = False
        self.joinError = gameDefs.ErrorCode.SUCCESS
        self.playersConnected = [None] * 3
        self.playerScores = [None] * 4
        self.returnTaskLeftActive = False
        self.returnTaskRightActive = False
        self.inventory = [gameDefs.InventoryItem.EMPTY, gameDefs.InventoryItem.EMPTY]
        self.startTime = 3 * 60 # 3 minutes
        self.gameResult = gameDefs.GameResult.PLAYING.value
        self.whoWon = [None] * 4
        
        # Example for start player positions
        self.playersPos = [
            (100, 300),
            (300, 400),
            (400, 500),
            (500, 600)
        ]
        
        self.resetGame()
        self.playersConnected[gameDefs.PlayerConnected.PLAYER2.value] = False
        self.playersConnected[gameDefs.PlayerConnected.PLAYER3.value] = False
        self.playersConnected[gameDefs.PlayerConnected.PLAYER4.value] = False
        
    def resetGame(self):        
        self.playerScores[gameDefs.PlayerScore.PLAYER1.value] = 0
        self.playerScores[gameDefs.PlayerScore.PLAYER2.value] = 0
        self.playerScores[gameDefs.PlayerScore.PLAYER3.value] = 0
        self.playerScores[gameDefs.PlayerScore.PLAYER4.value] = 0
        self.whoWon[gameDefs.PlayerScore.PLAYER1.value] = False
        self.whoWon[gameDefs.PlayerScore.PLAYER2.value] = False
        self.whoWon[gameDefs.PlayerScore.PLAYER3.value] = False
        self.whoWon[gameDefs.PlayerScore.PLAYER4.value] = False
        
        self.remainingTime = self.startTime
        self.gameStartTicks = pg.time.get_ticks()
        
    def setInventory(self, slotNum, item):
        self.inventory[slotNum] = item
    
    def getRemainingTime(self):
        elapsedSeconds = (pg.time.get_ticks() - self.gameStartTicks) // 1000
        remaining = max(0, self.startTime - elapsedSeconds)
        return remaining
    
    def getRemainingTimeText(self):
        remaining = self.getRemainingTime()
        minutes = remaining // 60
        seconds = remaining % 60
        return f"{minutes:02}:{seconds:02}"
        
    # show game result text
    def decideGameResult(self):
        maxScore = 0
        
        # get score from all players and set maxScore if player is still connected
        host = True
        for i in range(len(self.playerScores)):
            if not host:
                if self.playersConnected[gameDefs.PlayerConnected.PLAYER2.value + i - 1]:
                    if maxScore < self.playerScores[gameDefs.PlayerScore.PLAYER1.value + i]:
                        maxScore = self.playerScores[gameDefs.PlayerScore.PLAYER1.value + i]
            elif host:
                if maxScore < self.playerScores[gameDefs.PlayerScore.PLAYER1.value + i]:
                    maxScore = self.playerScores[gameDefs.PlayerScore.PLAYER1.value + i]
            host = False
        
        # set whoWon for players that have maxScore == their score
        for i in range(len(self.playerScores)):
            if maxScore == self.playerScores[gameDefs.PlayerScore.PLAYER1.value + i]:
                self.whoWon[gameDefs.PlayerScore.PLAYER1.value + i] = True
                
        # if player disconnected, they can't win
        if not self.playersConnected[gameDefs.PlayerConnected.PLAYER2.value]:
            self.whoWon[gameDefs.PlayerScore.PLAYER2.value] = False
        if not self.playersConnected[gameDefs.PlayerConnected.PLAYER3.value]:
            self.whoWon[gameDefs.PlayerScore.PLAYER3.value] = False
        if not self.playersConnected[gameDefs.PlayerConnected.PLAYER4.value]:
            self.whoWon[gameDefs.PlayerScore.PLAYER4.value] = False
                
        # set gameResult for player
        
        if self.whoWon[self.playerID]:
            anotherPlayerAlsoHasMaxScore = False
            
            for i in range(len(self.playerScores)):
                if i == self.playerID:
                    continue
                if self.whoWon[i]:
                    anotherPlayerAlsoHasMaxScore = True
                    break
            if anotherPlayerAlsoHasMaxScore:
                self.gameResult = gameDefs.GameResult.DRAW.value
            else:
                self.gameResult = gameDefs.GameResult.WON.value
        else:
            self.gameResult = gameDefs.GameResult.LOST.value
    
    def endGame(self):
        self.paused = False
        self.decideGameResult()
    