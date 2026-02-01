import pygame as pg
from copy import deepcopy
import random
import struct

import gameDefs

class GameLogic:
    def __init__(self, gameAudio):
        self.gameAudio = gameAudio
        self.gameNetworking = None
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
        self.inventory = [gameDefs.InventoryItem.EMPTY.value, gameDefs.InventoryItem.EMPTY.value]
        self.deskItemCount = 0
        self.maxDeskItemCount = 0
        self.pickedFrom = -1
        self.pickUpCounter = 0
        self.startTime = 60 # 1 minute
        self.gameResult = gameDefs.GameResult.PLAYING.value
        self.playedGameResultAudio = False
        self.whoWon = [None] * 4
        
        self.returnAreaCounter = 0
        self.returnAreaCounterMax = 300
        self.spawnItemCounter = 0
        self.spawnItemCounterMax = 100
        
        self.playersStartPos = [
            [100, 300],
            [300, 400],
            [400, 500],
            [500, 600]
        ]
        self.playersPos = deepcopy(self.playersStartPos)
        
        self.desks = []
        self.playersRect = [None] * 4
        self.deskRects = []
        self.returnTaskLeftRect = pg.Rect(100, 450 - 75, 80, 160)
        self.returnTaskRightRect = pg.Rect(1420, 450 - 75, 80, 160)
        
        self.resetGame()
        self.playersConnected[gameDefs.PlayerConnected.PLAYER2.value] = False
        self.playersConnected[gameDefs.PlayerConnected.PLAYER3.value] = False
        self.playersConnected[gameDefs.PlayerConnected.PLAYER4.value] = False
        
    def resetGame(self):        
        self.playerScores[gameDefs.PlayerScore.PLAYER1.value] = 0
        self.playerScores[gameDefs.PlayerScore.PLAYER2.value] = 0
        self.playerScores[gameDefs.PlayerScore.PLAYER3.value] = 0
        self.playerScores[gameDefs.PlayerScore.PLAYER4.value] = 0
        self.playedGameResultAudio = False
        self.whoWon[gameDefs.PlayerScore.PLAYER1.value] = False
        self.whoWon[gameDefs.PlayerScore.PLAYER2.value] = False
        self.whoWon[gameDefs.PlayerScore.PLAYER3.value] = False
        self.whoWon[gameDefs.PlayerScore.PLAYER4.value] = False
        self.inventory = [gameDefs.InventoryItem.EMPTY.value, gameDefs.InventoryItem.EMPTY.value]
        self.deskItemCount = 0
        self.playersPos = deepcopy(self.playersStartPos)
        
        self.desks = []
        self.playersRect = [None] * 4
        self.addDesks()
        
        self.returnTaskLeftActive = False
        self.returnTaskRightActive = False
        self.randDesk = -1
        
        self.remainingTime = self.startTime
        self.gameStartTicks = pg.time.get_ticks()
        
    def addDesks(self):
        self.deskRects.append(pg.Rect(400, 400, 96, 96))
        self.deskRects.append(pg.Rect(800, 600, 96, 96))
        self.deskRects.append(pg.Rect(600, 200, 96, 96))
        self.deskRects.append(pg.Rect(1200, 300, 96, 96))
        self.deskRects.append(pg.Rect(1100, 600, 96, 96))
        self.deskRects.append(pg.Rect(750, 400, 96, 96))
        self.deskRects.append(pg.Rect(300, 600, 96, 96))
        self.desks.append([400, 400, gameDefs.InventoryItem.EMPTY.value, self.deskRects[0], False])
        self.desks.append([800, 600, gameDefs.InventoryItem.EMPTY.value, self.deskRects[1], False])
        self.desks.append([600, 200, gameDefs.InventoryItem.EMPTY.value, self.deskRects[2], False])
        self.desks.append([1100, 300, gameDefs.InventoryItem.EMPTY.value, self.deskRects[3], False])
        self.desks.append([1100, 600, gameDefs.InventoryItem.EMPTY.value, self.deskRects[4], False])
        self.desks.append([750, 400, gameDefs.InventoryItem.EMPTY.value, self.deskRects[5], False])
        self.desks.append([300, 600, gameDefs.InventoryItem.EMPTY.value, self.deskRects[6], False])
        
    def updatePlayerRect(self):
        for i in range(len(self.playersRect)):
            self.playersRect[i] = pg.Rect(self.playersPos[i][0], self.playersPos[i][1], 96, 96)
        
    def checkCollisions(self):
        keys = pg.key.get_pressed()
        self.pickUpCounter += 1
        
        for desk in self.desks:
            if self.playersRect[self.playerID].colliderect(desk[3]):
                if keys[pg.K_e]:
                    if desk[2] != gameDefs.InventoryItem.EMPTY.value:
                        if self.pickUpCounter > 50:
                            self.spawnItemCounter = 0
                            self.deskItemCount -= 1
                            
                            if not self.playerIsHost:
                                for i in range(len(self.desks)):
                                    if desk == self.desks[i]:
                                        self.pickedFrom = i
                            
                            if self.inventory[0] == gameDefs.InventoryItem.EMPTY.value:
                                self.setInventory(0, desk[2])
                                desk[2] = gameDefs.InventoryItem.EMPTY.value
                                desk[4] = False
                                self.gameAudio.playPickupSound()
                                
                            elif self.inventory[1] == gameDefs.InventoryItem.EMPTY.value:
                                self.setInventory(1, desk[2])
                                desk[2] = gameDefs.InventoryItem.EMPTY.value
                                desk[4] = False
                                self.gameAudio.playPickupSound()
                                
                            self.pickUpCounter = 0
        
        if self.returnTaskLeftActive and self.playersRect[self.playerID].colliderect(self.returnTaskLeftRect):
            if keys[pg.K_q]:
                if self.inventory[0] == gameDefs.InventoryItem.TASK.value:
                    self.setInventory(0, gameDefs.InventoryItem.EMPTY.value)
                    self.playerScores[self.playerID] += 1
                    self.gameAudio.playReturnTaskSound()
                    
            if keys[pg.K_e]:
                if self.inventory[1] == gameDefs.InventoryItem.TASK.value:
                    self.setInventory(1, gameDefs.InventoryItem.EMPTY.value)
                    self.playerScores[self.playerID] += 1
                    self.gameAudio.playReturnTaskSound()
            
        if self.returnTaskRightActive and self.playersRect[self.playerID].colliderect(self.returnTaskRightRect):
            if keys[pg.K_q]:
                if self.inventory[0] == gameDefs.InventoryItem.TASK.value:
                    self.setInventory(0, gameDefs.InventoryItem.EMPTY.value)
                    self.playerScores[self.playerID] += 1
                    self.gameAudio.playReturnTaskSound()
                    
            if keys[pg.K_e]:        
                if self.inventory[1] == gameDefs.InventoryItem.TASK.value:
                    self.setInventory(1, gameDefs.InventoryItem.EMPTY.value)
                    self.playerScores[self.playerID] += 1
                    self.gameAudio.playReturnTaskSound()
            
    def activateReturnAreas(self):
        if self.returnAreaCounter < self.returnAreaCounterMax:
            self.returnAreaCounter += 1
        else:
            self.returnTaskLeftActive = not self.returnTaskLeftActive
            self.returnTaskRightActive = not self.returnTaskRightActive
                
            self.returnAreaCounter = 0
            
    def spawnItems(self):
        self.randDesk = random.randint(0, len(self.desks) - 1)
        randItem = gameDefs.InventoryItem.TASK.value
        
        if self.deskItemCount < self.maxDeskItemCount:
            self.spawnItemCounter += 1
        
        if self.spawnItemCounter >= self.spawnItemCounterMax:
            if self.desks[self.randDesk][2] == gameDefs.InventoryItem.EMPTY.value and not self.desks[self.randDesk][4]:
                self.desks[self.randDesk][2] = randItem
                self.desks[self.randDesk][4] = True
                
                self.deskItemCount += 1
                self.spawnItemCounter = 0
                
    def checkWaterBottleUsed(self):
        keys = pg.key.get_pressed()
        
        if keys[pg.K_q]:
            if self.inventory[0] == gameDefs.InventoryItem.WATER_BOTTLE.value:
                self.setInventory(0, gameDefs.InventoryItem.EMPTY.value)
        if keys[pg.K_e]:
            if self.inventory[1] == gameDefs.InventoryItem.WATER_BOTTLE.value:
                self.setInventory(1, gameDefs.InventoryItem.EMPTY.value)
            
    def loop(self):
        self.pickedFrom = -1
        self.updatePlayerRect()
        self.checkCollisions()
        if self.playerIsHost:
            self.activateReturnAreas()
            self.maxDeskItemCount = sum(self.playersConnected) + 1
            self.spawnItems()
            
        self.checkWaterBottleUsed()
        
        if not self.playerIsHost:
            data = struct.pack("5i", 0, self.playersPos[self.playerID][0], self.playersPos[self.playerID][1], self.playerScores[self.playerID], self.pickedFrom)
            try:
                self.gameNetworking.tcp.send(data)
            except:
                self.scene = gameDefs.Scene.MAIN_MENU.value
                self.gameNetworking.disconnect()
        
    def setInventory(self, slotNum, item):
        self.inventory[slotNum] = item
    
    def getRemainingTime(self):
        if self.playerIsHost:
            elapsedSeconds = (pg.time.get_ticks() - self.gameStartTicks) // 1000
            remaining = max(0, self.startTime - elapsedSeconds)
            return remaining
        else:
            return self.remainingTime
    
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
            
        if not self.playedGameResultAudio:
            if self.gameResult == gameDefs.GameResult.WON.value:
                self.gameAudio.playGameResultWin()
            elif self.gameResult == gameDefs.GameResult.DRAW.value:
                self.gameAudio.playGameResultDraw()
            elif self.gameResult == gameDefs.GameResult.LOST.value:
                self.gameAudio.playGameResultLose()
                
            self.playedGameResultAudio = True
    
    def endGame(self):
        self.paused = False
        self.decideGameResult()
    