'''
    This class is to simplify the creation of artifacts in the game
'''
import random

from game.shared.point import Point
from game.shared.color import Color

from game.casting.artifact import Artifact

class AddArtifact:
    
    def __init__(self, cast, messages, font_size = 15, cols = 60, rows = 40, cell_size = 15):
        self._cast = cast
        self._messages = messages
        self._FONT_SIZE = font_size
        self._COLS = cols
        self._ROWS = rows
        self._CELL_SIZE = cell_size
    
    def add(self, from_top = True):
        if random.randint(0, 1):
            text = chr(42)
            message = 'gem'
        else: 
            text = chr(111)
            message = 'rock'

        x = random.randint(1, self._COLS - 1)
        # y = random.randint(1, self._ROWS - 1)
        
        if from_top:
            y = 1
        else:
            y = random.randint(1, self._ROWS * .8)
            
        position = Point(x, y)
        position = position.scale(self._CELL_SIZE)

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = Color(r, g, b)
        
        artifact = Artifact()
        artifact.set_text(text)
        artifact.set_font_size(self._FONT_SIZE)
        artifact.set_color(color)
        artifact.set_position(position)
        artifact.set_message(message)
        self._cast.add_actor("artifacts", artifact)