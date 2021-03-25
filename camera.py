import pygame

vec = pygame.math.Vector2  #vec 2 class from pygame.math
from abc import ABC        #Abstract base class 


class Camera:

    def __init__(self, player):
        self.player = player   #Reference player
        self.offset = vec(0,0) #Offset values to set the camera
        self.offset_float = vec(0,0) 
        self.DISPLAY_width, self.DISPLAY_height = 100,100 # Height and Width displa [Numbers to be TBD] 
        self.CONST = vec(0,0)  #TBD


    def setmethod(self,method):
        self.method = method

    def scroll(self):
        self.method.scroll()


    def __init__(self, camera,player):
        self.camera = camera
        self.player = player

class CamScroll(ABC):
    def __init__(self, camera,player):
        self.camera = camera
        self.player = player

    @abstractmethod
    def scroll(self):
        pass


class Follow(CamScroll):
    def __init__(self, camera, player):
        CamScroll.__init__(self, camera, player)

    def scroll(self):
        self.camera.offset_float.x += (self.player.rect.x - self.camera.offset_float.x + self.camera.CONST.x)
        self.camera.offset_float.y += (self.player.rect.y - self.camera.offset_float.y + self.camera.CONST.y)
        self.camera.offset.x, self.camera.offset.y = int(self.camera.offset_float.x), int(self.camera.offset_float.y)

