class Cell:
 def __init__(self, cell_state):
 	self.cell_state = cell_state
 
 def SetCell(self, i):
 	if i == 'deadcell' :
 		self.cell_state=0
 	elif i == 'livecell':
 		self.cell_state=1
 	else:
 		raise RuntimeError("Unknown cell status ") 
 	
 	def isAlive(self):
 	  return self.cell_state
 	