import socket, select
from threading import Thread
from copy import deepcopy
import struct

import gameDefs
import gameLogic

PORT = 1234
BUFFER_SIZE = 1024

class GameNetworking:
    def __init__(self, gameLogic):
        self.gameLogic = gameLogic
        self.gameWidgets = None
        self.tcp = None
        self.tcpRun = False
        self.conns = []
        self.tcpThread = None
        self.playerSockets = [None] * 3
        
    def startClient(self):
        self.conns.clear()
        self.tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.tcp.settimeout(0.1)
        self.tcpRun = True
        
        try:
            self.tcp.connect((self.gameWidgets.joinGameMenuWidgets[1].getText(), PORT))
        except:
            self.gameLogic.joinError = gameDefs.ErrorCode.JOIN_GAME
            return
            
        self.gameLogic.joinError = gameDefs.ErrorCode.SUCCESS
        self.gameLogic.scene = gameDefs.Scene.WAITING_ROOM.value
        self.tcpThread = Thread(target = self.clientThread)
        self.tcpThread.start()
        
    def startServer(self):
        self.conns.clear()
        self.tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.tcp.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.tcp.bind(("0.0.0.0", PORT))
        self.tcp.listen()
        
        self.tcpRun = True
        self.conns.append(self.tcp)
        self.tcpThread = Thread(target = self.serverThread)
        self.tcpThread.start()
        print("Server started")
        
    def disconnect(self):
        if self.tcpRun:
            self.tcpRun = False
            
            if self.tcpThread:
                self.tcpThread.join()
                self.tcpThread = None
                
            self.gameLogic.playersConnected[gameDefs.PlayerConnected.PLAYER2.value] = False
            self.gameLogic.playersConnected[gameDefs.PlayerConnected.PLAYER3.value] = False
            self.gameLogic.playersConnected[gameDefs.PlayerConnected.PLAYER4.value] = False
            self.gameLogic.playerID = 0
            self.gameLogic.playerScores[0] = 0
            self.gameLogic.playerScores[1] = 0
            self.gameLogic.playerScores[2] = 0
            self.gameLogic.playerScores[3] = 0
            self.gameLogic.playersPos = deepcopy(self.gameLogic.playersStartPos)
            print("Disconnected")
            
    def broadcastStartGame(self):
        data = struct.pack("25i", 3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)
        
        for conn in self.conns:
            if not conn == self.tcp:
                conn.send(data)
                
    def broadcastTCPInfo(self):
        data = struct.pack("25i", 4, self.gameLogic.playerScores[0], self.gameLogic.playerScores[1],
                            self.gameLogic.playerScores[2], self.gameLogic.playerScores[3],
                            self.gameLogic.getRemainingTime(), self.gameLogic.returnTaskLeftActive,
                            self.gameLogic.playersPos[0][0], self.gameLogic.playersPos[0][1],
                            self.gameLogic.playersPos[1][0], self.gameLogic.playersPos[1][1],
                            self.gameLogic.playersPos[2][0], self.gameLogic.playersPos[2][1],
                            self.gameLogic.playersPos[3][0], self.gameLogic.playersPos[3][1],
                            self.gameLogic.desks[0][2], self.gameLogic.desks[1][2], self.gameLogic.desks[2][2],
                            self.gameLogic.desks[3][2], self.gameLogic.desks[4][2], self.gameLogic.desks[5][2],
                            self.gameLogic.desks[6][2], self.gameLogic.playersConnected[0],
                            self.gameLogic.playersConnected[1], self.gameLogic.playersConnected[2])
        
        for conn in self.conns:
            if not conn == self.tcp:
                try:
                    conn.send(data)
                except:
                    pass
        
    def clientThread(self):
        while self.tcpRun:
            try:
                data = self.tcp.recv(BUFFER_SIZE)
                
                if not len(data) == 100:
                    continue
                
                if not data:
                    print("Server closed connection")
                    self.gameLogic.scene = gameDefs.Scene.MAIN_MENU.value
                    self.gameLogic.resetGame()
                    self.gameLogic.playersConnected[gameDefs.PlayerConnected.PLAYER2.value] = False
                    self.gameLogic.playersConnected[gameDefs.PlayerConnected.PLAYER3.value] = False
                    self.gameLogic.playersConnected[gameDefs.PlayerConnected.PLAYER4.value] = False
                    self.gameLogic.playerID = 0
                    self.tcpRun = False
                    break
                    
                data = struct.unpack("25i", data)
                id = data[0]
                
                if data:
                    if id < 3:
                        self.gameLogic.playersConnected[id - 1] = True
                        self.gameLogic.playerID = id
                    
                    elif id == 3:
                        self.gameLogic.scene = gameDefs.Scene.GAME.value
                    
                    elif id == 4:
                        self.gameLogic.remainingTime = data[5]
                        self.gameLogic.returnTaskLeftActive = data[6]
                        self.gameLogic.returnTaskRightActive = data[6]
                        
                        if not self.gameLogic.playerID == 0:
                            self.gameLogic.playerScores[0] = data[1]
                            self.gameLogic.playersPos[0][0] = data[7]
                            self.gameLogic.playersPos[0][1] = data[8]
                        if not self.gameLogic.playerID == 1:
                            self.gameLogic.playerScores[1] = data[2]
                            self.gameLogic.playersPos[1][0] = data[9]
                            self.gameLogic.playersPos[1][1] = data[10]
                        if not self.gameLogic.playerID == 2:
                            self.gameLogic.playerScores[2] = data[3]
                            self.gameLogic.playersPos[2][0] = data[11]
                            self.gameLogic.playersPos[2][1] = data[12]
                        if not self.gameLogic.playerID == 3:
                            self.gameLogic.playerScores[3] = data[4]
                            self.gameLogic.playersPos[3][0] = data[13]
                            self.gameLogic.playersPos[3][1] = data[14]
                            
                        self.gameLogic.desks[0][2] = data[15]
                        self.gameLogic.desks[1][2] = data[16]
                        self.gameLogic.desks[2][2] = data[17]
                        self.gameLogic.desks[3][2] = data[18]
                        self.gameLogic.desks[4][2] = data[19]
                        self.gameLogic.desks[5][2] = data[20]
                        self.gameLogic.desks[6][2] = data[21]
                        
                        self.gameLogic.playersConnected[gameDefs.PlayerConnected.PLAYER2.value] = data[22]
                        self.gameLogic.playersConnected[gameDefs.PlayerConnected.PLAYER3.value] = data[23]
                        self.gameLogic.playersConnected[gameDefs.PlayerConnected.PLAYER4.value] = data[24]
                        
            except:
                pass
            
        self.tcp.close()
      
    def serverThread(self):
        try:
            while self.tcpRun:
                read, write, error = select.select(self.conns, [], [], 0.1)
                self.broadcastTCPInfo()
                
                for socket in read:
                    # new connection
                    if socket == self.tcp:
                        if not self.gameLogic.scene == gameDefs.Scene.WAITING_ROOM.value:
                            sockfd, addr = self.tcp.accept()
                            sockfd.close()
                            return
                            
                        sockfd, addr = self.tcp.accept()
                        self.conns.append(sockfd)
                        
                        print(str(addr) + " connected")
                        
                        if not self.gameLogic.playersConnected[gameDefs.PlayerConnected.PLAYER2.value]:
                            data = struct.pack("25i", gameDefs.PlayerConnected.PLAYER2.value + 1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)
                            sockfd.send(data)
                            self.gameLogic.playersConnected[gameDefs.PlayerConnected.PLAYER2.value] = True
                            self.playerSockets[0] = sockfd
                            continue
                            
                        if not self.gameLogic.playersConnected[gameDefs.PlayerConnected.PLAYER3.value]:
                            data = struct.pack("25i", gameDefs.PlayerConnected.PLAYER3.value + 1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)
                            sockfd.send(data)
                            self.gameLogic.playersConnected[gameDefs.PlayerConnected.PLAYER3.value] = True
                            self.playerSockets[1] = sockfd
                            continue
                            
                        if not self.gameLogic.playersConnected[gameDefs.PlayerConnected.PLAYER4.value]:
                            data = struct.pack("25i", gameDefs.PlayerConnected.PLAYER4.value + 1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)
                            sockfd.send(data)
                            self.gameLogic.playersConnected[gameDefs.PlayerConnected.PLAYER4.value] = True
                            self.playerSockets[2] = sockfd
                            continue
                        
                    # from client
                    else:
                        try:
                        # data received
                            data = socket.recv(BUFFER_SIZE)
                            
                            if data:
                                data = struct.unpack("5i", data)
                                            
                                if data[0] == 0:
                                    for i in range(len(self.playerSockets)):
                                        if self.playerSockets[i] == socket:
                                            self.gameLogic.playersPos[i + 1][0] = data[1]
                                            self.gameLogic.playersPos[i + 1][1] = data[2]
                                            self.gameLogic.playerScores[i + 1] = data[3]
                                            if not data[4] == -1:
                                                self.gameLogic.desks[data[4]][2] = gameDefs.InventoryItem.EMPTY.value
                                                self.gameLogic.deskItemCount -= 1
                                                self.gameLogic.spawnItemCounter = 0
                                            continue
                                            
                                #self.gameLogic.playerID = int(data)
                            
                            # disconnected
                            if not data:
                                print(str(socket) + "disconnected")
                                
                                for i in range(len(self.playerSockets)):
                                    if self.playerSockets[i] == socket:
                                        self.gameLogic.playersConnected[i] = False
                                        
                                socket.close()
                                self.conns.remove(socket)
                                
                        # disconnected
                        except:
                            print(str(socket) + "disconnected")
                            
                            for i in range(len(self.playerSockets)):
                                    if self.playerSockets[i] == socket:
                                        self.gameLogic.playersConnected[i] = False
                                        
                            socket.close()
                            self.conns.remove(socket)
        finally:
            for sock in self.conns:
                try:
                    sock.close()
                except OSError:
                    pass
            self.conns.clear()
