from . import basics
import GameTools.Tools as Tools
import pygame

global cached_info
cached_info = [-1,-1,-1]

class rectangle(basics.Entity):
    def __init__(self, plane,color):
        super().__init__(plane)
        self.color = color
        #self.cached_info=[100,100,0]

    def draw(self,game):
        global cached_info
        scaleFactor=cached_info
        if [game.currentWidth,game.currentHeight] != cached_info[0::1]:
            scaleFactor = [
                game.currentWidth,
                game.currentHeight,
                ((game.currentWidth**2)+(game.currentHeight**2))**0.5
            ]
            cached_info = scaleFactor
        plane = self.plane.export()
        plane = [
            plane[0]*scaleFactor[0],
            plane[1]*scaleFactor[1],
            plane[2]*scaleFactor[2],
            plane[3]*scaleFactor[2],
        ]
        #self.currentPlane = Tools.Math.Basics.plane(*plane)
        pygame.draw.rect(game.window,self.color,plane)