class myClass:
	def __init__(self,x,y):
		self.x = x
		self.y = y
	
	def lenX(self):
		return len(self.x)
	def lenY(self):
		return len(self.y)

	def insertX(self,val):
		self.x.append(val)
	
	def insertY(self,val):
		self.y.append(val)
	def getX(self):
		return self.x
	def getY(self):
		return self.y
