'''
    This class is for adding "gravity" to the game which will drop the 
    gems and rocks
'''
from game.shared.point import Point

class Gravity:
    
    def __init__(self, fall_speed = 1):
        self.fall_speed = Point(0, fall_speed)
        
        
    def drop_down(self, item):
        '''
            drops the item down as if it is falling
            
            Args: 
            item is the rock or gem that is falling
        '''
        # self.fall_speed.scale()
        item.set_velocity(self.fall_speed)
        
        