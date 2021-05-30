from . import basics
import GameTools.Tools as Tools
import pygame

global cached_info
cached_info = {"scaleFactor":[-1,-1,-1,]}

class rectangle(basics.Entity):
    def __init__(self, plane,color):
        super().__init__(plane)
        self.color = color
        #self.cached_info=[100,100,0]

    def draw(self,game):
        '''
        properly scales and moved the shape to fit with screensize
        ... oh yeah... and it also draws the shape
        '''
        global cached_info
        scaleFactor=cached_info["scaleFactor"]
        if [game.currentWidth,game.currentHeight] != cached_info["scaleFactor"][0::1]:
            scaleFactor = [
                game.currentWidth,
                game.currentHeight,
                ((game.currentWidth**2)+(game.currentHeight**2))**0.5,
            ]
            cached_info["scaleFactor"] = scaleFactor
        plane = self.plane.export()
        plane = [
            plane[0]*scaleFactor[0],
            plane[1]*scaleFactor[1],
            plane[2]*scaleFactor[2],
            plane[3]*scaleFactor[2],
        ]
        #self.currentPlane = Tools.Math.Basics.plane(*plane)
        pygame.draw.rect(game.window,self.color,plane)

    def touching_X(self,X):
        '''
        converts to pixel coordinates and tests if it has collided on the X
        '''
        global cached_info
        added = self.plane.w*cached_info["scaleFactor"][2]
        eX = self.plane.x*cached_info["scaleFactor"][0]
        if eX+added>=X*cached_info["scaleFactor"][0]:
            return True
        if eX>=X*cached_info["scaleFactor"][0]:
            return True
        return False
    
    def touching_Y(self,Y,game):
        '''
        converts to pixel coordinates and tests if it has collided on the X
        '''
        added = self.plane.h*cached_info["scaleFactor"][2]
        eY = self.plane.y*cached_info["scaleFactor"][0]
        if eY+added>=Y*cached_info["scaleFactor"][0]:
            return True
        if eY>=Y*cached_info["scaleFactor"][0]:
            return True
        return False