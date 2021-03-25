import pygame
from player import Player

class Physics():

    """
    Represents the physics that are attributed to each tile on screen
    
    Contains a max speed, horizontal, and vertical acceleration allowed for an object affected by physics
    (e.g. enemies and the player) based on which tile type they are currently in contact with

    Attributes
    ----------
    maxSpeed - dictates the maximum speed the object can achieve in the tile
    xAccel - dictates the change in the object's horizontal speed in the tile
    yAccel - dictates the change in the object's vertical speed in the tile


    Methods
    ----------
    __init__():
        Program initialisation.
    
    affect_player():
        Applies physics to the player object to adjust velocity and movement on screen

    affect_enemies():
        Applies physics to all enemy objects on screen to adjust their velocity and movement on screen
    """

    def __init__(self, maxSpeed, xAccel, yAccel):

        """
        Initialization of all variables

        Parameters
        ----------
        maxSpeed - the maximum speed for the object in the tile being utilized
        xAccel - the horizontal acceleration for the object in the tile being utilized
        yAccel - the vertical acceleration for the object in the tile being utilized

        Raises
        ----------
        None

        Authors
        ----------
        Branden Wheeler
        """ 
        self.maxSpeed = maxSpeed
        self.xAccel = xAccel
        self.yAccel = yAccel


    def affect_things(self, player):
        """
        Adjusts the properties of the player object based on the current physics to affect
        their movement on screen through their change in position (velocity) and change in 
        velocity (acceleration)

        Parameters
        ----------
        player - the player object that needs to have its properties adjusted by physics

        Raises
        ----------
        None

        Authors
        ----------
        Branden Wheeler
        """

        if(self.maxSpeed > abs(player.xVel) > 0):
            player.xVel += self.xAccel

        if (player.jumping or player.falling):
            player.yVel -= self.yAccel



    def affect_enemies(self, enemies):
        """
        Adjusts the properties of a list of enemy objects based on their current physics to affect
        their movement on screen through their change in position (velocity) and change in 
        velocity (acceleration)

        Parameters
        ----------
        enemies - the list of enemy objects currently on screen

        Raises
        ----------
        None

        Authors
        ----------
        Branden Wheeler
        """ 

