from . import basics
import GameTools.Tools as Tools
import pygame

class rectangle(basics.Entity):
    def __init__(self, plane,color):
        super().__init__(plane)
        self.color = color
        self.cached_info=[100,100,0]

    def draw(self,game):
        scaleFactor=self.cached_info
        if [game.currentWidth,game.currentHeight] != self.cached_info[0::1]:
            scaleFactor = [
                game.currentWidth,
                game.currentHeight,
                ((game.currentWidth**2)+(game.currentHeight**2))**0.5
            ]
            self.cached_info = scaleFactor
        plane = self.plane.export()
        plane = [
            plane[0]*scaleFactor[2],
            plane[1]*scaleFactor[2],
            plane[2]*scaleFactor[2],
            plane[3]*scaleFactor[2],
        ]
        #self.currentPlane = Tools.Math.Basics.plane(*plane)
        pygame.draw.rect(game.window,self.color,plane)