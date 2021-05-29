from GameTools.Templates import ProjectTemplates
import GameTools, time,pygame
from GameTools import Templates, Entity,Tools
from GameTools.Tools import Math
from GameTools.Templates import ProjectTemplates

class myGame(ProjectTemplates.Pygame):
    def start(self):
        self.box = Entity.Entity(Math.plane(0,0,200,200))
        GameTools.Tools.Messaging.send_Message("Default Message",None,TestKwarg='coolTest')
    def update(self, dt):
        self.box.move(Math.point(50*dt,0))
        if self.box.plane.x+self.box.plane.w-10>=self.width:
            self.box.plane.x=0
    
    def draw(self):
        pygame.draw.rect(self.window,(0,0,0),self.box.plane.export())

#print(Tools.Messaging.recv_Message.__doc__)

myGame(600,600,"Gaming Time")