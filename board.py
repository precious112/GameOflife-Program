import cell
import Array2D
import random
BOARD_NUM = 10
GRID_NUM = 10
DEAD_CELL= 0
LIVE_CELL = 1
class Board:
 def __init__(self,BOARD_NUM,GRID_NUM,DEAD_CELL,LIVE_CELL):
 	self._board= Array2D(BOARD_NUM,GRID_NUM)
 	self._Grids= Cell("deadcell")
 #clear all the Grids to value zero	
 def clearArray(self):
   grid = self._Grids
   self._board.clear(grid)
 #set some Grids to live grids	
 
 def setLiveGrids(self):
   alive = self._Grids("livecell")
 	for i in range(4):
 		for j in range(4):
 			i= random.randint(0,5)
 			j=random.randint(0,5)
 			self._board[i,j] = alive
 			
 				

 def playGame(self):
   setLiveGrids()
 	#rules to change a dead cell to live cell
 	i = random.randint(10)
 	j = random.randint(10)
 	L= self._Grids.SetCell("livecell")
 	L= self._board[i,j]
 	while i <= self.BOARD_NUM:
 		while j <= self.GRID_NUM:
 			if self.board[i-1,j-1] == self._Grids.isAlive and self.board[i-1,j+1]== self._Grids.isAlive:
 				L = self._Grids.SetCell("livecell)
 			elif self.board[i,j-1] == self._Grids.isAlive and self.board[i,j+1] == self._Grids.isAlive:
 				L= self._Grids.SetCell("livecell)
 			elif self.board[i+1,j-1] == self._Grids.isAlive and self.board[i+1,j+1] == self._Grids.isAlive:
 				L= self._Grids.SetCell("livecell)
 			elif self.board[i-1,j]== self._Grids.isAlive and self.board[i+1,j] == self._Grids.isAlive:
 				L= self._Grids.SetCell("livecell)
 			else:
 				L = self._Grids.SetCell("deadcell")
 				
 	
 def main():
 
   if __name__== "__main__":
     playGame()