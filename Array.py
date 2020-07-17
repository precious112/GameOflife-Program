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