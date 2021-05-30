import GameTools.Timing as timing
import pygame
from . import ProjectTemplates
pygame.init()

class game(ProjectTemplates.Pygame):
    '''
    Simply contains game properties for an async project
    '''
    def __init__(self,w,h,title, frameRate = 60, fillColor = (255,255,255)):
        self.width = w
        self.height = h
        #print(self.width,self.height)
        self.currentWidth = self.width
        self.currentHeight = self.height
        self.title = title
        self.window = pygame.display.set_mode((self.width,self.height),pygame.RESIZABLE)
        pygame.display.set_caption(title)
        self.clock = pygame.time.Clock()
        self.frameRate = frameRate
        self.fillColor = fillColor
        self.running = True

        self.events = self.placeHolder
        self.update = self.placeHolder
        self.draw = self.placeHolder
        self.start = self.placeHolder
    
    # def start_GameLoop(self):
    #     '''
    #     a method that handles the startup sequence of the gameloop.
    #     this specifically works with pygame rendering.
  	# 	'''
    #     self.start()
    #     while self.running:
    #         self.clock.tick(self.frameRate)
    #         timing.DeltaTime.calculate_DeltaTime()
    #         if pygame.event.get(eventtype=pygame.QUIT):
    #             self.running=False
    #             continue
    #         self.events(timing.DeltaTime.deltaTime)
    #         self.update(timing.DeltaTime.deltaTime)
    #         self.window.fill(self.fillColor)
    #         self.draw()
    #         pygame.display.update()
    #     pygame.quit()
    
    def placeHolder(self,dt=0):
        pass


def createGame(w,h,title, frameRate = 60, fillColor = (255,255,255)):
    return game(w,h,title, frameRate=frameRate , fillColor=fillColor)


def events(gameProps):
    def inner(func):
        gameProps.events = func
        return func
    return inner

def draw(gameProps):
    def inner(func):
        gameProps.draw = func
        return func
    return inner

def update(gameProps):
    def inner(func):
        gameProps.update = func
        return func
    return inner

def start(gameProps):
    def inner(func):
        gameProps.start = func
        return func
    return inner