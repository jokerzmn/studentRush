import enum

class Texture(enum.Enum):
    PLAYER1 = 0
    PLAYER2 = 1
    PLAYER3 = 2
    PLAYER4 = 3
    PLAYER1_HEAD = 4
    PLAYER2_HEAD = 5
    PLAYER3_HEAD = 6
    PLAYER4_HEAD = 7
    TASK = 8
    WATTER_BOTTLE = 9
    INVENTORY_SLOT = 10
    RETURN_TASK = 11
    GAME_AREA = 12
    DESK = 13
    
texturePaths = [
    "res/pngs/player1.png",
    "res/pngs/player2.png",
    "res/pngs/player3.png",
    "res/pngs/player4.png",
    "res/pngs/player1head.png",
    "res/pngs/player2head.png",
    "res/pngs/player3head.png",
    "res/pngs/player4head.png",
    "res/pngs/task.png",
    "res/pngs/waterBottle.png",
    "res/pngs/inventorySlot.png",
    "res/pngs/returnTask.png",
    "res/pngs/gameArea.png",
    "res/pngs/desk.png"
]

textureScales = [
    (96, 96),
    (96, 96),
    (96, 96),
    (96, 96),
    (80, 80),
    (80, 80),
    (80, 80),
    (80, 80),
    (96, 96),
    (96, 96),
    (100, 100),
    (80, 160),
    (1400, 600),
    (128, 128)
]
    
class GameTextures:
    def __init__(self, pygame):
        self.pg = pygame
        self.textures = [None] * len(Texture)
        self.initTextures()
        self.scaleTextures()
        
    def initTextures(self):
        for i in range(len(Texture)):
            self.textures[i] = self.pg.image.load(texturePaths[i]).convert_alpha()
        
    def scaleTextures(self):
        for i in range(len(Texture)):
            self.textures[i] = self.pg.transform.scale(self.textures[i], textureScales[i])
        