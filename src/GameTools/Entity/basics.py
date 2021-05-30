class Entity:
	def __init__(self, plane):
		self.plane = plane
		self.currentPlane = plane
	def move(self,point):
		self.plane.change_Position(self.plane.x+point.x,self.plane.y+point.y)
	def change_Position(self, point):
		self.plane.change_Position(point.x,point.y)
	
	def draw(game):
		pass