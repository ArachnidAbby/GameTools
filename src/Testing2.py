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

game = FullTemplate.createGame(720,512,"My Game",frameRate=-1)
box = Entity.shapes.rectangle(Math.plane(0,0,Math.calculate_Coords(206,game),Math.calculate_Coords(206,game)),(0,0,0))#position and size are a percentage of the screensize!
game.direction = 1
font = pygame.font.Font('freesansbold.ttf', 32)
game.text= font.render('30', True, (0,255,0), (0,0,255))

@FullTemplate.start(game)
def start():
    GameTools.Tools.Messaging.send_Message("Default Message",None,TestKwarg='coolTest')

@FullTemplate.events(game)
def events(dt):
    for event in pygame.event.get():
        pass

@FullTemplate.update(game)
def update(dt):
    game.text = font.render(str(int(1/dt)), True, (0,255,0), (0,0,255))
    box.move(Math.point(0.2*dt*game.direction,0))
    if box.touching_X(1):
        game.direction=-1
    if box.touching_X(0):
        game.direction=1

@FullTemplate.draw(game)
def draw():
    game.draw_Entity(box)
    game.window.blit(game.text,[0,0])

game.start_GameLoop()