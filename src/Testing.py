from GameTools.Templates import ProjectTemplates
import GameTools, time,pygame
from GameTools import Templates, Entity,Tools
from GameTools.Tools import Math
from GameTools.Templates import ProjectTemplates

class myGame(ProjectTemplates.Pygame):
    def start(self):
        self.box = Entity.shapes.rectangle(Math.plane(0,0,0.2,0.2),(0,0,0))
        GameTools.Tools.Messaging.send_Message("Default Message",None,TestKwarg='coolTest')
    def update(self, dt):
        self.box.move(Math.point(0.2*dt,0))
        if self.box.plane.x+self.box.plane.w>1:
            self.box.plane.x=0
    
    def draw(self):
        self.draw_Entity(self.box)

#print(Tools.Messaging.recv_Message.__doc__)

myGame(6,"Gaming Time")