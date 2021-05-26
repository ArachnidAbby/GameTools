class point:
    def __init__(self, x,y):
        self.x = x
        self.y = y
    
    def export(self):
        return [self.x,self.y]
    
    def change_Position(self,x,y):
        self.x=x
        self.y=y
    
class plane(point):
    def __init__(self, x,y,w,h):
        super().__init__(x,y)
        self.w = w
        self.h = h
    
    def export(self):
        return [self.x,self.y,self.w,self.h]
    
    def change_Dimensions(self,w,h):
        self.w = w
        self.h = h