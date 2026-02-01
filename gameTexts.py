import enum

import gameDefs

class MainMenuText(enum.Enum):
    TITLE = 0
    
class JoinGameMenuText(enum.Enum):
    TEXTBOX_IP = 0
    
class WaitingRoomText(enum.Enum):
    WAIT_FOR_GAME_START = 0
    PLAYER1 = 1
    PLAYER2 = 2
    PLAYER3 = 3
    PLAYER4 = 4

class GameText(enum.Enum):
    TIMER = 0
    PLAYER1 = 1
    PLAYER2 = 2
    PLAYER3 = 3
    PLAYER4 = 4
    PLAYER1_SCORE = 5
    PLAYER2_SCORE = 6
    PLAYER3_SCORE = 7
    PLAYER4_SCORE = 8
    GAME_RESULT = 9

class TextProp(enum.Enum):
    TEXT_OBJ = 0
    POS_X = 1
    POS_Y = 2

class GameTexts:
    def __init__(self, pygame, gameLogic, windowWidth, windowHeight):
        self.pg = pygame
        self.gameLogic = gameLogic
        self.windowWidth = windowWidth
        self.windowHeight = windowHeight
        self.mainMenuTexts = []
        self.joinGameMenuTexts = []
        self.waitingRoomTexts = []
        self.joinErrorText = [None, None, None]
        self.gameMapTexts = []
        self.gameResultText = [None, None, None]
        
        self.bigFont = None
        self.smallFont = None
        self.initFonts()
        self.initTexts()
        
    def initFonts(self):
        self.pg.font.init()
        self.bigFont = self.pg.font.Font('res/font/Habbo.ttf', 70)
        self.smallFont = self.pg.font.Font('res/font/Habbo.ttf', 45)
        
    def initTexts(self):
        self.mainMenuTexts.append([
            self.bigFont.render("Student Rush", False, (255, 255, 255)),
            None, None
        ])
        self.mainMenuTexts[MainMenuText.TITLE.value][TextProp.POS_X.value] = self.windowWidth/2 - self.mainMenuTexts[MainMenuText.TITLE.value][TextProp.TEXT_OBJ.value].get_width()/2
        self.mainMenuTexts[MainMenuText.TITLE.value][TextProp.POS_Y.value] = 100
        
        self.joinGameMenuTexts.append([
            self.bigFont.render('Wpisz adres IP serwera', False, (255, 255, 255)),
            None, None
        ])
        self.joinGameMenuTexts[JoinGameMenuText.TEXTBOX_IP.value][TextProp.POS_X.value] = self.windowWidth/2 - self.joinGameMenuTexts[JoinGameMenuText.TEXTBOX_IP.value][TextProp.TEXT_OBJ.value].get_width()/2
        self.joinGameMenuTexts[JoinGameMenuText.TEXTBOX_IP.value][TextProp.POS_Y.value] = 100
        
        self.joinErrorText[TextProp.TEXT_OBJ.value] = self.smallFont.render('Nie udalo sie polaczyc z serwerem', False, (255, 255, 255))
        self.joinErrorText[TextProp.POS_X.value] = self.windowWidth/2 - self.joinErrorText[0].get_width()/2
        self.joinErrorText[TextProp.POS_Y.value] = self.joinGameMenuTexts[JoinGameMenuText.TEXTBOX_IP.value][TextProp.POS_Y.value] + 100
        
        self.waitingRoomTexts.append([
            self.bigFont.render('Czekanie na rozpoczecie gry', False, (255, 255, 255)),
            None, None
        ])
        self.waitingRoomTexts[WaitingRoomText.WAIT_FOR_GAME_START.value][TextProp.POS_X.value] = self.windowWidth/2 - self.waitingRoomTexts[WaitingRoomText.WAIT_FOR_GAME_START.value][TextProp.TEXT_OBJ.value].get_width()/2
        self.waitingRoomTexts[WaitingRoomText.WAIT_FOR_GAME_START.value][TextProp.POS_Y.value] = 100
        
        self.waitingRoomTexts.append([
            self.smallFont.render('', False, (255, 255, 255)),
            None, None
        ])
        self.waitingRoomTexts[WaitingRoomText.PLAYER1.value][TextProp.POS_X.value] = self.windowWidth/2 - 350
        self.waitingRoomTexts[WaitingRoomText.PLAYER1.value][TextProp.POS_Y.value] = self.windowHeight - 370
        
        self.waitingRoomTexts.append([
            self.smallFont.render('', False, (255, 255, 255)),
            None, None
        ])
        self.waitingRoomTexts[WaitingRoomText.PLAYER2.value][TextProp.POS_X.value] = self.windowWidth/2 - 350 + 200
        self.waitingRoomTexts[WaitingRoomText.PLAYER2.value][TextProp.POS_Y.value] = self.windowHeight - 370
        
        self.waitingRoomTexts.append([
            self.smallFont.render('', False, (255, 255, 255)),
            None, None
        ])
        self.waitingRoomTexts[WaitingRoomText.PLAYER3.value][TextProp.POS_X.value] = self.windowWidth/2 - 350 + 400
        self.waitingRoomTexts[WaitingRoomText.PLAYER3.value][TextProp.POS_Y.value] = self.windowHeight - 370
        
        self.waitingRoomTexts.append([
            self.smallFont.render('', False, (255, 255, 255)),
            None, None
        ])
        self.waitingRoomTexts[WaitingRoomText.PLAYER4.value][TextProp.POS_X.value] = self.windowWidth/2 - 350 + 600
        self.waitingRoomTexts[WaitingRoomText.PLAYER4.value][TextProp.POS_Y.value] = self.windowHeight - 370
        
        self.gameMapTexts.append([
            self.bigFont.render('5:00', False, (255, 255, 255)),
            None, None
        ])
        self.gameMapTexts[GameText.TIMER.value][TextProp.POS_X.value] = self.windowWidth/2 - self.gameMapTexts[GameText.TIMER.value][TextProp.TEXT_OBJ.value].get_width()/2
        self.gameMapTexts[GameText.TIMER.value][TextProp.POS_Y.value] = 35
        
        self.gameMapTexts.append([
            self.smallFont.render('Player1', False, (255, 255, 255)),
            None, None
        ])
        self.gameMapTexts[GameText.PLAYER1.value][TextProp.POS_X.value] = self.gameMapTexts[GameText.TIMER.value][TextProp.POS_X.value] - 615
        self.gameMapTexts[GameText.PLAYER1.value][TextProp.POS_Y.value] = 100
        
        self.gameMapTexts.append([
            self.smallFont.render('Player2', False, (255, 255, 255)),
            None, None
        ])
        self.gameMapTexts[GameText.PLAYER2.value][TextProp.POS_X.value] = self.gameMapTexts[GameText.TIMER.value][TextProp.POS_X.value] - 315
        self.gameMapTexts[GameText.PLAYER2.value][TextProp.POS_Y.value] = 100
        
        self.gameMapTexts.append([
            self.smallFont.render('Player3', False, (255, 255, 255)),
            None, None
        ])
        self.gameMapTexts[GameText.PLAYER3.value][TextProp.POS_X.value] = self.gameMapTexts[GameText.TIMER.value][TextProp.POS_X.value] + 285
        self.gameMapTexts[GameText.PLAYER3.value][TextProp.POS_Y.value] = 100
        
        self.gameMapTexts.append([
            self.smallFont.render('Player4', False, (255, 255, 255)),
            None, None
        ])
        self.gameMapTexts[GameText.PLAYER4.value][TextProp.POS_X.value] = self.gameMapTexts[GameText.TIMER.value][TextProp.POS_X.value] + 585
        self.gameMapTexts[GameText.PLAYER4.value][TextProp.POS_Y.value] = 100
        
        self.gameMapTexts.append([
            self.smallFont.render('0', False, (255, 255, 255)),
            None, None
        ])
        self.gameMapTexts[GameText.PLAYER1_SCORE.value][TextProp.POS_X.value] = self.gameMapTexts[GameText.PLAYER1.value][TextProp.POS_X.value] + self.gameMapTexts[GameText.PLAYER1.value][TextProp.TEXT_OBJ.value].get_width() + 55
        self.gameMapTexts[GameText.PLAYER1_SCORE.value][TextProp.POS_Y.value] = 100
        
        self.gameMapTexts.append([
            self.smallFont.render('0', False, (255, 255, 255)),
            None, None
        ])
        self.gameMapTexts[GameText.PLAYER2_SCORE.value][TextProp.POS_X.value] = self.gameMapTexts[GameText.PLAYER2.value][TextProp.POS_X.value] + self.gameMapTexts[GameText.PLAYER2.value][TextProp.TEXT_OBJ.value].get_width() + 55
        self.gameMapTexts[GameText.PLAYER2_SCORE.value][TextProp.POS_Y.value] = 100
        
        self.gameMapTexts.append([
            self.smallFont.render('0', False, (255, 255, 255)),
            None, None
        ])
        self.gameMapTexts[GameText.PLAYER3_SCORE.value][TextProp.POS_X.value] = self.gameMapTexts[GameText.PLAYER3.value][TextProp.POS_X.value] + self.gameMapTexts[GameText.PLAYER3.value][TextProp.TEXT_OBJ.value].get_width() + 55
        self.gameMapTexts[GameText.PLAYER3_SCORE.value][TextProp.POS_Y.value] = 100
        
        self.gameMapTexts.append([
            self.smallFont.render('0', False, (255, 255, 255)),
            None, None
        ])
        self.gameMapTexts[GameText.PLAYER4_SCORE.value][TextProp.POS_X.value] = self.gameMapTexts[GameText.PLAYER4.value][TextProp.POS_X.value] + self.gameMapTexts[GameText.PLAYER4.value][TextProp.TEXT_OBJ.value].get_width() + 55
        self.gameMapTexts[GameText.PLAYER4_SCORE.value][TextProp.POS_Y.value] = 100
        
        self.gameResultText[TextProp.TEXT_OBJ.value] = self.bigFont.render('Game result', False, (255, 255, 255))
        self.gameResultText[TextProp.POS_X.value] = self.windowWidth/2 - self.gameResultText[TextProp.TEXT_OBJ.value].get_width()/2
        self.gameResultText[TextProp.POS_Y.value] = 300
        
    def changeGameResultText(self, text):
        self.gameResultText[TextProp.TEXT_OBJ.value] = self.bigFont.render(text, False, (255, 255, 255))
        self.gameResultText[TextProp.POS_X.value] = self.windowWidth/2 - self.gameResultText[TextProp.TEXT_OBJ.value].get_width()/2
        
    def checkGameResultForText(self):
        if self.gameLogic.gameResult == gameDefs.GameResult.WON.value:
            self.changeGameResultText("Wygrales")
        elif self.gameLogic.gameResult == gameDefs.GameResult.LOST.value:
            self.changeGameResultText("Przegrales")
        elif self.gameLogic.gameResult == gameDefs.GameResult.DRAW.value:
            self.changeGameResultText("Remis")
        elif self.gameLogic.gameResult == gameDefs.GameResult.PLAYING.value:
            self.changeGameResultText("")
            