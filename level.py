from tile import Tile
import pygame


class Level():
    """
    Class containing the information of a level.

    A level will contain a 2D list of tiles and the all the information of
    each tile in the list.

    Attributes
    ----------

    Methods
    ----------
    __init__():
        Tile initialization

    read_level():
        Populates list with numbers representing a level

    read_tiles():
        Reads tiles into a 2D list

    load_level_surface():
        Loads tiles onto the level surface

    draw_level_surface():
        Draws the level surface on the window

    """

    def __init__(self, filename):
        """
        Initialization of all variables related to a level.

        Parameters
        ----------
        filename - reference to the level file

        Raises
        ----------
        None

        Authors
        ----------
        Jon O'Brien
        """

        self.tile_size = 64
        self.x = 0
        self.y = 0
        self.tiles, self.w, self.h = self.read_tiles(filename)
        self.level_surface = pygame.Surface((self.w, self.h))
        self.load_level_surface()

    def read_level(self, filename):
        """
        Reads a level file and creates a level initialized with
        the values in 'filename'.

        Parameters
        ----------
        filename - name of level file

        Raises
        ----------
        None

        Returns
        ----------
        level_data - list of level data read from 'csv' file

        Authors
        ----------
        Jon O'Brien
        """

        level_data = []

        level_file = open(filename, "r")

        for line in level_file:
            level_data.append(line.strip("\n").split(","))

        return level_data

    def read_tiles(self, filename):
        """
        Initialization of all variables and Sprite.

        Parameters
        ----------
        filename - name of level file

        Raises
        ----------
        None

        Returns
        ----------
        tiles - list of tiles in a level
        w - width of a level
        h - height of a level

        Authors
        ----------
        Jon O'Brien
        """

        tiles = []
        level = self.read_level(filename)

        x = 0
        y = 0

        # the for loop will extend when we get all the tiles in.

        for row in level:
            x = 0
            for tile in row:
                if tile == 'value of tile':
                    tiles.append(Tile('image file', x *
                                      self.tile_size, y * self.tile_size, None))
                elif tile == 'another value':
                    tiles.append(Tile('image file', x *
                                      self.tile_size, y * self.tile_size, None))
                x += 1
            y += 1

        w = x * self.tile_size
        h = y * self.tile_size

        return tiles, w, h

    def load_level_surface(self):
        """
        Draw level tiles onto the level surface.

        Parameters
        ----------

        Raises
        ----------
        None

        Authors
        ----------
        Jon O'Brien
        """

        for tile in self.tiles:
            tile.draw_tile(self.level_surface)

    def draw_level_surface(self, surface):
        """
        Draw level surface onto the game window

        Parameters
        ----------

        Raises
        ----------
        None

        Authors
        ----------
        Jon O'Brien
        """
        surface.blit(self.level_surface, (0, 0))
