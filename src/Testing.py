'''
Testing project templates and other features
This is the Pygame Template
This is a pretty neet class based template
'''

from GameTools.Templates import ProjectTemplates
import GameTools, time,pygame
from GameTools import Templates, Entity,Tools
from GameTools.Tools import Math
from GameTools.Templates import ProjectTemplates

class myGame(ProjectTemplates.Pygame):
    def start(self):
        self.box = Entity.shapes.rectangle(Math.plane(0,0,Math.calculate_Coords(300,self),Math.calculate_Coords(300,self)),(0,0,0))
        GameTools.Tools.Messaging.send_Message("Default Message",None,TestKwarg='coolTest')
        self.direction=1
    
    def events(self, dt):
        pass

    def update(self, dt):
        self.box.move(Math.point(0.2*dt*self.direction,0))
        if self.box.touching_X(1):
            self.direction=-1
        if self.box.touching_X(0):
            self.direction=1
    
    def draw(self):
        self.draw_Entity(self.box)

#print(Tools.Messaging.recv_Message.__doc__)

myGame(600,600,"Gaming Time")