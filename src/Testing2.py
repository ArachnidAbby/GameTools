'''
Testing a new project template!
This is called the "FullTemplate" (I know, bad name)
Essentially removes the need for your project to be class based.
I kind of like this template more?
'''

from GameTools.Templates import ProjectTemplates
import GameTools, time, pygame
from GameTools import Templates, Entity, Tools
from GameTools.Tools import Math
from GameTools.Templates import FullTemplate

game = FullTemplate.createGame(6,"My Game",frameRate=60)
box = Entity.shapes.rectangle(Math.plane(0,0,0.2,0.2),(0,0,0))#position and size are a percentage of the screensize!

@FullTemplate.start(game)
def start():
    GameTools.Tools.Messaging.send_Message("Default Message",None,TestKwarg='coolTest')

@FullTemplate.events(game)
def events(dt):
    pass

@FullTemplate.update(game)
def update(dt):
    box.move(Math.point(0.2*dt,0))
    #print(box.plane.x+box.plane.w)
    if box.plane.x+box.plane.w>=1:
        box.plane.x=0

@FullTemplate.draw(game)
def draw():
    game.draw_Entity(box)

game.start_GameLoop()