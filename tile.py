import pygame


class Tile(pygame.sprite.Sprite):
    """
    Represents a Tile within a Level.

    Tile contains attributes to determine what the tile is, where its located,
    the image for the tile being used, the physics type of the tile.

    Attributes
    ----------

    Methods
    ----------
    __init__():
        Tile initialization

    draw_tile():
        Draw tile to level surface

    """

    def __init__(self, image, x, y, physics):
        """
        Initialization of all variables and Sprite of a tile.

        Parameters
        ----------
        image - name of tile image
        x - horizontal location
        y - vertical location
        physics - physics type of tile

        Raises
        ----------
        None

        Authors
        ----------
        Jon O'Brien
        """

        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(image)
        self.physics = physics
        self.x = x
        self.y = y

    def draw_tile(self, level_surface):
        """
        Function to draw a tile on the level surface

        Parameters
        ----------
        level_surface - draws tile onto the level surface at location x, y

        Raises
        ----------
        None

        Authors
        ----------
        Jon O'Brien
        """

        level_surface.blit(self.image, (self.x, self.y))
