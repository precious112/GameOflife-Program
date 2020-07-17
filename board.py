import ctypes
class Array:
 def __init__(self,size):
 	assert size>0,"Array size must be >0"
 	self._size=size
 	
 	PyArrayType=ctypes.py_object*size
 	self._elements= PyArrayType()
 	self.clear(None)
 	
 def __len__(self):
 	return self._size
 	
 def __getitem__(self,index):
 	assert index >=0 and index < len(self),"Array subscript out of range"
 	return self._elements[index]
 
 def __setitem__(self,index,value):
 	assert index <= 0 and index < len(self)
 	self._elements[index] = value
 
 def clear(self,value):
 	for i in range(len(self)):
 		self._elements[i] = value
 
 def __iter__(self):
 	return _Arrayiterator(self._elements)
 	
class _ArrayIterator :
 def __init__(self,theArray):
 	self._arrayRef=theArray
 	self._curNdx= 0
 
 def __iter__(self):
 	return self
 
 def __next__(self):
 	if self._curNdx < len(self._arrayRef):
 		entry = self._arrayRef[self._curNdx]
 		self.curNdx += 1
 		return entry
 	else:
 		raise StopIteration
class Array2D:
 def __init__(self,numRows,numCols):
 	self._theRows = Array(numRows)
 	for i in range(numRows):
 		self._theRows[i] = Array(numCols)
 
 def numRows(self):
 	return len(self._theRows)
 	
 def numCols(self):
 	return len(self._theRows[0])
 	
 def clear(self,value):
 	for row in range(self.numRows()):
 		row.clear(value)
 
 def __getitem__(self,ndxTuple):
 	assert len(ndxTuple) == 2, "invalid number of Array Subscript"
 	row=ndxTuple[0]
 	col=ndxTuple[1]
 	assert row >= 0 and row < self.numRows() \
 	      and col >= 0 and col < self.numCols(), \
 	      "Array subscript out of range"
 	 
 	theIdArray= self._theRows[row]
 	return theIdArray[col]
 
 def __setitem__(self,ndxTuple,value):
 	assert len(ndxTuple) == 2, "invalid number of Array Subscript"
 	row=ndxTuple[0]
 	col=ndxTuple[1]
 	assert row >= 0 and row < self.numRows() \
 	      and col >= 0 and col < self.numCols(), \
 	      "Array subscript out of range"
 	 
 	theIdArray= self._theRows[row]
 	theIdArray[col] = value
	 	
BOARD_NUM = 10
GRID_NUM = 10
DEAD_CELL= 0
LIVE_CELL = 1
class Board:
 def __init__(self,BOARD_NUM,GRID_NUM,DEAD_CELL,LIVE_CELL):
 	self._board= Array2D(BOARD_NUM,GRID_NUM)
 	self._Grids= Cell(DEAD_CELL,LIVE_CELL)
 #clear all the Grids to value zero	
 def clearArray(self):
 	self._board.clear(0)
 #set some Grids to live grids	
 def setLiveGrids(self):
 	
 	for i in range(4):
 		for j in range(4):
 			i= random.randint(0,5)
 			j=random.randint(0,5)
 			self._board.__setitem__((i,j),1)
 			
 			for i in self._board[i,j]:
 				for j in self._board[i,j]:
 					self._board.__getitem__((i,j))
 				

 def playGame(self):
 	#rules to change a dead cell to live cell
 	
 	L= self.DEAD_CELL
 	L= self._board[i,j]
 	while i <= self.BOARD_NUM:
 		while j <= self.GRID_NUM:
 			if self.board[i-1,j-1] == self.liveCell and self.board[i-1,j+1]== self.liveCell:
 				L = self.LIVE_CELL
 			elif self.board[i,j-1] == self.liveCell and self.board[i,j+1] == self.liveCell:
 				L= self.LIVE_CELL
 			elif self.board[i+1,j-1] == self.liveCell and self.board[i+1,j+1] == self.liveCell:
 				L= self.LIVE_CELL
 			elif self.board[i-1,j]== self.liveCell and self.board[i+1,j] == self.liveCell:
 				L= self.LIVE_CELL
 			else:
 				L = self.DEAD_CELL
 				
 	for i in self._board[i,j]:
 		for j in self._board[ i,j]:
 			self._board.__getitem__((i,j))
 			
 def main():
 
   if __name__== "__main__":
   	main()				