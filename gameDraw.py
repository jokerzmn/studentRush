import pygame as pg

import gameTextures
import gameTexts
import gameDefs

class GameDraw:
    def __init__(self, gameLogic, gameTextures, gTexts, windowWidth, windowHeight, screen):
        self.screen = screen
        self.gameLogic = gameLogic
        self.textures = gameTextures.textures
        self.gameTextures = gameTextures
        self.gameTexts = gTexts
        self.windowWidth = windowWidth
        self.windowHeight = windowHeight
        
    # Draw player heads with their names at the top of the screen during gameplay
    def drawPlayerHeads(self):
        self.screen.blit(
            self.textures[gameTextures.Texture.PLAYER1_HEAD.value],
            (self.gameTexts.gameMapTexts[gameTexts.GameText.TIMER.value][gameTexts.TextProp.POS_X.value] - 600, 30)
        )
        
        if self.gameLogic.playersConnected[gameDefs.PlayerConnected.PLAYER2.value]:  
            self.screen.blit(
                self.textures[gameTextures.Texture.PLAYER2_HEAD.value],
                (self.gameTexts.gameMapTexts[gameTexts.GameText.TIMER.value][gameTexts.TextProp.POS_X.value] - 300, 30)
            )
            self.gameTexts.gameMapTexts[gameTexts.GameText.PLAYER2.value][gameTexts.TextProp.TEXT_OBJ.value] = self.gameTexts.smallFont.render(
                "Player2", False, (255, 255, 255)
            )
        else:
            self.gameTexts.gameMapTexts[gameTexts.GameText.PLAYER2.value][gameTexts.TextProp.TEXT_OBJ.value] = self.gameTexts.smallFont.render(
                "", False, (255, 255, 255)
            )
            
        if self.gameLogic.playersConnected[gameDefs.PlayerConnected.PLAYER3.value]:  
            self.screen.blit(
                self.textures[gameTextures.Texture.PLAYER3_HEAD.value],
                (self.gameTexts.gameMapTexts[gameTexts.GameText.TIMER.value][gameTexts.TextProp.POS_X.value] + 300, 30)
            )
            self.gameTexts.gameMapTexts[gameTexts.GameText.PLAYER3.value][gameTexts.TextProp.TEXT_OBJ.value] = self.gameTexts.smallFont.render(
                "Player3", False, (255, 255, 255)
            )
        else:
            self.gameTexts.gameMapTexts[gameTexts.GameText.PLAYER3.value][gameTexts.TextProp.TEXT_OBJ.value] = self.gameTexts.smallFont.render(
                "", False, (255, 255, 255)
            )
            
        if self.gameLogic.playersConnected[gameDefs.PlayerConnected.PLAYER4.value]:  
            self.screen.blit(
                self.textures[gameTextures.Texture.PLAYER4_HEAD.value],
                (self.gameTexts.gameMapTexts[gameTexts.GameText.TIMER.value][gameTexts.TextProp.POS_X.value] + 600, 30)
            )
            self.gameTexts.gameMapTexts[gameTexts.GameText.PLAYER4.value][gameTexts.TextProp.TEXT_OBJ.value] = self.gameTexts.smallFont.render(
                "Player4", False, (255, 255, 255)
            )
        else:
            self.gameTexts.gameMapTexts[gameTexts.GameText.PLAYER4.value][gameTexts.TextProp.TEXT_OBJ.value] = self.gameTexts.smallFont.render(
                "", False, (255, 255, 255)
            )
        
    # Draw task textures with task count at the top of the screen during gampeplay
    def drawPLayersTaskCount(self):
        self.screen.blit(
            self.textures[gameTextures.Texture.TASK.value],
            (self.gameTexts.gameMapTexts[gameTexts.GameText.TIMER.value][gameTexts.TextProp.POS_X.value] - 500, 10)
        )
        self.gameTexts.gameMapTexts[gameTexts.GameText.PLAYER1_SCORE.value][gameTexts.TextProp.TEXT_OBJ.value] = self.gameTexts.smallFont.render(
            str(self.gameLogic.playerScores[gameDefs.PlayerScore.PLAYER1.value]), False, (255, 255, 255)
        )
        
        if self.gameLogic.playersConnected[gameDefs.PlayerConnected.PLAYER2.value]: 
            self.screen.blit(
                self.textures[gameTextures.Texture.TASK.value],
                (self.gameTexts.gameMapTexts[gameTexts.GameText.TIMER.value][gameTexts.TextProp.POS_X.value] - 200, 10)
            )
            self.gameTexts.gameMapTexts[gameTexts.GameText.PLAYER2_SCORE.value][gameTexts.TextProp.TEXT_OBJ.value] = self.gameTexts.smallFont.render(
                str(self.gameLogic.playerScores[gameDefs.PlayerScore.PLAYER2.value]), False, (255, 255, 255)
            )
        else:
            self.gameTexts.gameMapTexts[gameTexts.GameText.PLAYER2_SCORE.value][gameTexts.TextProp.TEXT_OBJ.value] = self.gameTexts.smallFont.render(
                "", False, (255, 255, 255)
            )
            
        if self.gameLogic.playersConnected[gameDefs.PlayerConnected.PLAYER3.value]: 
            self.screen.blit(
                self.textures[gameTextures.Texture.TASK.value],
                (self.gameTexts.gameMapTexts[gameTexts.GameText.TIMER.value][gameTexts.TextProp.POS_X.value] + 400, 10)
            )
            self.gameTexts.gameMapTexts[gameTexts.GameText.PLAYER3_SCORE.value][gameTexts.TextProp.TEXT_OBJ.value] = self.gameTexts.smallFont.render(
                str(self.gameLogic.playerScores[gameDefs.PlayerScore.PLAYER3.value]), False, (255, 255, 255)
            )
        else:
            self.gameTexts.gameMapTexts[gameTexts.GameText.PLAYER3_SCORE.value][gameTexts.TextProp.TEXT_OBJ.value] = self.gameTexts.smallFont.render(
                "", False, (255, 255, 255)
            )
            
        if self.gameLogic.playersConnected[gameDefs.PlayerConnected.PLAYER4.value]: 
            self.screen.blit(
                self.textures[gameTextures.Texture.TASK.value],
                (self.gameTexts.gameMapTexts[gameTexts.GameText.TIMER.value][gameTexts.TextProp.POS_X.value] + 700, 10)
            )
            self.gameTexts.gameMapTexts[gameTexts.GameText.PLAYER4_SCORE.value][gameTexts.TextProp.TEXT_OBJ.value] = self.gameTexts.smallFont.render(
                str(self.gameLogic.playerScores[gameDefs.PlayerScore.PLAYER4.value]), False, (255, 255, 255)
            )
        else:
            self.gameTexts.gameMapTexts[gameTexts.GameText.PLAYER4_SCORE.value][gameTexts.TextProp.TEXT_OBJ.value] = self.gameTexts.smallFont.render(
                "", False, (255, 255, 255)
            )
        
    def drawInventory(self):
        slotX = [None, None]
        slotX[0] = 100
        slotX[1] = 220
        
        # Draw empty inventory slots at the bottom of the screen
        self.screen.blit(
            self.textures[gameTextures.Texture.INVENTORY_SLOT.value],
            (slotX[0], self.windowHeight - self.textures[gameTextures.Texture.INVENTORY_SLOT.value].get_height() - 20)
        )
        self.screen.blit(
            self.textures[gameTextures.Texture.INVENTORY_SLOT.value],
            (slotX[1], self.windowHeight - self.textures[gameTextures.Texture.INVENTORY_SLOT.value].get_height() - 20)
        )
        
        # If player has any items draw them on the top of the empty inventory slots
        if self.gameLogic.inventory[gameDefs.InventorySlot.SLOT1.value] == gameDefs.InventoryItem.TASK.value:
            self.screen.blit(
                self.textures[gameTextures.Texture.TASK.value],
                (slotX[0] + 2, self.windowHeight - self.textures[gameTextures.Texture.INVENTORY_SLOT.value].get_height() - 18)
            )
        elif self.gameLogic.inventory[gameDefs.InventorySlot.SLOT1.value] == gameDefs.InventoryItem.WATTER_BOTTLE.value:
            self.screen.blit(
                self.textures[gameTextures.Texture.WATTER_BOTTLE.value],
                (slotX[0] + 2, self.windowHeight - self.textures[gameTextures.Texture.INVENTORY_SLOT.value].get_height() - 22)
            )
            
        if self.gameLogic.inventory[gameDefs.InventorySlot.SLOT2.value] == gameDefs.InventoryItem.TASK.value:
            self.screen.blit(
                self.textures[gameTextures.Texture.TASK.value],
                (slotX[1] + 2, self.windowHeight - self.textures[gameTextures.Texture.INVENTORY_SLOT.value].get_height() - 18)
            )
        elif self.gameLogic.inventory[gameDefs.InventorySlot.SLOT2.value] == gameDefs.InventoryItem.WATTER_BOTTLE.value:
            self.screen.blit(
                self.textures[gameTextures.Texture.WATTER_BOTTLE.value],
                (slotX[1] + 2, self.windowHeight - self.textures[gameTextures.Texture.INVENTORY_SLOT.value].get_height() - 22)
            )
            
    def drawTextGroup(self, textGroup):
        for text in textGroup:
            self.screen.blit(
                text[gameTexts.TextProp.TEXT_OBJ.value],
                (text[gameTexts.TextProp.POS_X.value], text[gameTexts.TextProp.POS_Y.value])
            )
            
    # Draw connected players and their names
    def drawPlayersWaitingRoom(self):
        self.screen.blit(
            self.textures[0],
            (self.windowWidth/2 - 350, self.windowHeight - 470)
        )
        self.gameTexts.waitingRoomTexts[gameTexts.WaitingRoomText.PLAYER1.value][gameTexts.TextProp.TEXT_OBJ.value] = self.gameTexts.smallFont.render(
            "Player1", False, (255, 255, 255)
        )
                
        for i in range(1, 4):
            if self.gameLogic.playersConnected[gameDefs.PlayerConnected.PLAYER2.value + i - 1]:
                self.screen.blit(
                    self.textures[i],
                    (self.windowWidth/2 - 350 + i * 200, self.windowHeight - 470)
                )
                self.gameTexts.waitingRoomTexts[gameTexts.WaitingRoomText.PLAYER2.value + i - 1][gameTexts.TextProp.TEXT_OBJ.value] = self.gameTexts.smallFont.render(
                    "Player"+str(i+1), False, (255, 255, 255)
                )
            # For not connected players make their name texts empty
            else:
                self.gameTexts.waitingRoomTexts[gameTexts.WaitingRoomText.PLAYER2.value + i - 1][gameTexts.TextProp.TEXT_OBJ.value] = self.gameTexts.smallFont.render(
                    "", False, (255, 255, 255)
                )
        
    def drawJoinError(self):
        self.screen.blit(
            self.gameTexts.joinErrorText[gameTexts.TextProp.TEXT_OBJ.value],
            (self.gameTexts.joinErrorText[gameTexts.TextProp.POS_X.value], self.gameTexts.joinErrorText[gameTexts.TextProp.POS_Y.value])
        )
        
    def drawGameResult(self):
       self.screen.blit(
            self.gameTexts.gameResultText[gameTexts.TextProp.TEXT_OBJ.value],
            (self.gameTexts.gameResultText[gameTexts.TextProp.POS_X.value], self.gameTexts.gameResultText[gameTexts.TextProp.POS_Y.value])
        ) 
    
    def drawReturnTaskIfActive(self):
        if self.gameLogic.returnTaskLeftActive:
            self.screen.blit(
                self.textures[gameTextures.Texture.RETURN_TASK.value],
                (100, self.windowHeight/2 - 75)
            )
        if self.gameLogic.returnTaskRightActive:
            self.screen.blit(
                pg.transform.flip(self.textures[gameTextures.Texture.RETURN_TASK.value], True, False),
                (1420, self.windowHeight/2 - 75)
            )
    
    def drawTimer(self):
        self.gameTexts.gameMapTexts[gameTexts.GameText.TIMER.value][gameTexts.TextProp.TEXT_OBJ.value] = self.gameTexts.bigFont.render(
            self.gameLogic.getRemainingTimeText(), False, (255, 255, 255)
        )
    
    def drawGameArea(self):
        self.screen.blit(
            self.textures[gameTextures.Texture.GAME_AREA.value],
            (100, 160)
        )
    
    def drawDesk(self, x, y, itemOnTop):
        self.screen.blit(
            self.textures[gameTextures.Texture.DESK.value],
            (x, y)
        )
        
        if itemOnTop == gameDefs.InventoryItem.TASK.value:
            self.textures[gameTextures.Texture.TASK.value] = pg.transform.scale(self.textures[gameTextures.Texture.TASK.value], (80, 80))
            self.screen.blit(
                self.textures[gameTextures.Texture.TASK.value],
                (x + 25, y + 15)
            ) 
            self.textures[gameTextures.Texture.TASK.value] = pg.transform.scale(self.textures[gameTextures.Texture.TASK.value], (96, 96))
            
        elif itemOnTop == gameDefs.InventoryItem.WATTER_BOTTLE.value:
            self.textures[gameTextures.Texture.WATTER_BOTTLE.value] = pg.transform.scale(self.textures[gameTextures.Texture.WATTER_BOTTLE.value], (80, 80))
            self.screen.blit(
                self.textures[gameTextures.Texture.WATTER_BOTTLE.value],
                (x + 25, y + 10)
            ) 
            self.textures[gameTextures.Texture.WATTER_BOTTLE.value] = pg.transform.scale(self.textures[gameTextures.Texture.WATTER_BOTTLE.value], (96, 96))
    
    def drawDesks(self):
        # Example of drawing desks with items on top of it
        self.drawDesk(400, 400, gameDefs.InventoryItem.TASK.value)
        self.drawDesk(800, 600, gameDefs.InventoryItem.WATTER_BOTTLE.value)
        self.drawDesk(600, 200, gameDefs.InventoryItem.EMPTY.value)
    
    def drawPlayers(self):
        self.screen.blit(
            self.textures[gameTextures.Texture.PLAYER1.value],
            self.gameLogic.playersPos[gameDefs.PlayerPos.PLAYER1.value]
        )
        if self.gameLogic.playersConnected[gameDefs.PlayerConnected.PLAYER2.value]:
            self.screen.blit(
                self.textures[gameTextures.Texture.PLAYER2.value],
                self.gameLogic.playersPos[gameDefs.PlayerPos.PLAYER2.value]
            )
        if self.gameLogic.playersConnected[gameDefs.PlayerConnected.PLAYER3.value]:
            self.screen.blit(
                self.textures[gameTextures.Texture.PLAYER3.value],
                self.gameLogic.playersPos[gameDefs.PlayerPos.PLAYER3.value]
            )
        if self.gameLogic.playersConnected[gameDefs.PlayerConnected.PLAYER4.value]:
            self.screen.blit(
                self.textures[gameTextures.Texture.PLAYER4.value],
                self.gameLogic.playersPos[gameDefs.PlayerPos.PLAYER4.value]
            )
    