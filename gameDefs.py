import enum

class ErrorCode(enum.Enum):
    SUCCESS = 0
    JOIN_GAME = 1

class Scene(enum.Enum):
    MAIN_MENU = 0
    JOIN_GAME = 1
    WAITING_ROOM = 2
    GAME = 3
    
class PlayerConnected(enum.Enum):
    # No PlAYER1, because it is the host which is always connected.
    PLAYER2 = 0
    PLAYER3 = 1
    PLAYER4 = 2
    
class PlayerScore(enum.Enum):
    PLAYER1 = 0
    PLAYER2 = 1
    PLAYER3 = 2
    PLAYER4 = 3
    
class PlayerPos(enum.Enum):
    PLAYER1 = 0
    PLAYER2 = 1
    PLAYER3 = 2
    PLAYER4 = 3
    
class InventoryItem(enum.Enum):
    EMPTY = 0
    TASK = 1
    WATER_BOTTLE = 2
    
class InventorySlot(enum.Enum):
    SLOT1 = 0
    SLOT2 = 1
    
class GameResult(enum.Enum):
    PLAYING = 0
    WON = 1
    LOST = 2
    DRAW = 3
    