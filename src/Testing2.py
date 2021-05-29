from GameTools.Templates import ProjectTemplates
import GameTools, time,pygame
from GameTools import Templates, Entity,Tools
from GameTools.Tools import Math
from GameTools.Templates import FullTemplate

game = FullTemplate.createGame(600,600,"My Game",frameRate=60)
box = Entity.Entity(Math.plane(0,0,200,200))

@FullTemplate.start(game)
def start():
    GameTools.Tools.Messaging.send_Message("Default Message",None,TestKwarg='coolTest')

@FullTemplate.events(game)
def events(dt):
    pass

@FullTemplate.update(game)
def update(dt):
    box.move(Math.point(50*dt,0))
    if box.plane.x+box.plane.w-10>=game.width:
        box.plane.x=0

@FullTemplate.draw(game)
def draw():
    pygame.draw.rect(game.window,(0,0,0),box.plane.export())

game.start_GameLoop()