Aby mozna bylo uruchomic gre, nalezy zainstalowac pygame_widgets

jak uruchomic:
python3 game.py

serwer jest zawsze Player1 i ma playerID = 0

Aby zaprogramowac istniejace przyciski nalezy zmienic kod w pliku gameWidgetsLogic.py i
w odpowiadajacym roznym przyciskom metodach, przyklad: zeby zmienic zachowanie programu przy wcisnieciu przycisku
zaloz gre, trzeba zmienic kod w metodzie createGameButton w pliku gameWidgetsLogic.py

Uwaga:
kod jest w wiekszosci plikow trudny do zrozumienia i moze byc niezoptymalizowany.
jesli chcesz zrozumiec calosc projektu zacznij czytac kod od pliku game.py.
jesli starczy czasu po zrobieniu wszystkich punktow ponizej mozna zrobic kod
czytelniejszy.

do zrobienia:
- po kliknieciu zaloz gre, stworz serwer, ktory moze przyjmowac do 3 graczy
  (serwer nie jest oddzielnym skryptem, czyli wykonuje sie w tym samym programie gry na
   oddzielnym watku)
   
- po kliknieciu dolacz do gry, wpisaniu ip i kliknieciu dolacz:
  polacz sie z serwerem,
  
  (playerID dla PLAYER1 = 0,
   playerID dla PLAYER2 = 1,
   playerID dla PLAYER3 = 2,
   playerID dla PLAYER4 = 3)
  
  odbierz od serwera playerID i go ustaw na kliencie, klient wysyla z powrotem informacje ze dostal playerID,
  wtedy na serwerze ustaw self.gameLogic.playersConnected[gameDefs.PlayerConnected.PLAYER#.value] = True,
  gdzie # to liczba od 2 do 4
  (wyslij playerID, czyli po stronie serwera pierszy wolny self.gameLogic.playersConnected[gameDefs.PlayerConnected.PLAYER#.value],
  ktory jest False, przyklad: jesli self.gameLogic.playersConnected[gameDefs.PlayerConnected.PLAYER3.value] == False, to wyslij
  do klienta playerID = 2)
  
- po kliknieciu start w poczekalni przez serwer:
  ustaw startowa pozycje graczy:
  self.gameLogic.playersPos[gameDefs.PlayerPos.PLAYER#.value] = (posX, posY),
  gdzie # to liczba od 1 do 4
  
- poruszanie sie graczy, (przyklad renderowania: zeby zmienic pozycje renderowania dla gracza 2 na x=300, y=400:
  self.gameLogic.playersPos[gameDefs.PlayerPos.PLAYER2.value] = (300, 400))
  
- kolizje, np. nie mozna przejsc przez lawke, wykryj gdy:
  gracz jest obok lawki
  gracz jest obok punktu odbioru zadan,
  gracz jest obok innego gracza,
  gracz nie moze wyjsc poza plansze
  
- renderuj kilka lawek na planszy za pomoca metody drawDesk w metodzie drawDesks:
  self.drawDesk(posX, posY, itemOnDesk) (przyklad: self.drawDesk(400, 400, gameDefs.InventoryItem.TASK.value)),
  to wyrenderuje lawke z zadaniem

- jesli gracz jest obok lawki na ktorej jest zadanie i trzyma jakis przycisk przez, np. 3 sekundy to dodaj do wolnego slotu w ekwipunku
  przedmiot TASK: setInventory(gameDefs.InventorySlot.SLOT#.value, gameDefs.InventoryItem.TASK.value),
  gdzie # to liczba od 1 do 2
  slot w ekwipunku jest wolny jesli self.gameLogic.inventory[gameDefs.InventorySlot.SLOT#.value] == gameDefs.InventoryItem.EMPTY.value

- jesli gracz jest obok lawki na ktorej jest butelka wody i wcisnie jakis przycisk to dodaj do wolnego slotu w ekwipunku
  przedmiot WATER_BOTTLE: setInventory(gameDefs.InventorySlot.SLOT#.value, gameDefs.InventoryItem.WATER_BOTTLE.value),
  gdzie # to liczba od 1 do 2
  
- wybierz przedmiot, ktory jest w ekwipunku klawiszami 1 i 2, przyklad:
  na slot2 jest butelka wody, wiec po wcisnieciu klawisza 2 jest ona gotowa do uzycia
  
- gdy butelka wody jest w ekwipunku i gotowa do uzycia mozna ja rozlac na podloge co daje efekt:
  znikniecia z ekwipunku (self.gameLogic.inventory[gameDefs.InventorySlot.SLOT#.value] == gameDefs.InventoryItem.EMPTY.value)
  jesli jakis gracz wejdzie na obszar na ktorej stal gracz przy uzyciu butelki, to przez, np. sekunde nie moze sie ruszac i
  wylatuje im z ekwipunku zadania ktore posiada
  
- gracz moze oddac zadania w punkcie odbioru, ktory sie pojawia po lewej lub prawej stronie planszy.
  punkt odbioru pojawia sie co, np. 30 sekund i znika po 5 sekundach.
  zeby punkt odbioru sie renderowal nalezy ustawic:
  self.gameLogic.returnTaskLeftActive = True dla lewego punktu odbioru
  self.gameLogic.returnTaskRightActive = True dla prawego punktu odbioru
  
- pojawianie sie przedmiotow na lawkach jak opisane w prezentacji ProjectProposal na Teams

- jesli jakis gracz sie rozlaczy ustaw na serwerze self.gameLogic.playersConnected[gameDefs.PlayerConnected.PLAYER#.value] = False,
  wyslij ta informacje do klientow i na klientach rowniez ustaw self.gameLogic.playersConnected[gameDefs.PlayerConnected.PLAYER#.value] = False

- jesli serwer sie rozlaczyl to powiadom klientow i po stronie klienta wywolaj metode self.gameLogic.endGame()

- po oddaniu zadania przez gracza wyslij do innych nowa liczbe punktow gracza
  self.gameLogic.playerScores[gameDefs.PlayerScore.PLAYER#.value]
  
- uderzanie innych graczy, gdy jest sie w ich poblizu

- po skonczeniu gry (licznik jest 00:00) zaprogramuj wylaczenie serwera w metodzie endGame w pliku gameLogic.py

- inne punkty, ktore nie podalem a sa w pliku ProjectProposal na Teams
