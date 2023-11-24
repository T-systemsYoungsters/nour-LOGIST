import math
import block_library

class Badblock(block_library.Block):
    def __init__(self, filename:str ,width:int ,height:int):
        super().__init__(filename ,width ,height)
        # The "center" the sprite will orbit
        self.center_x:int = 0
        self.center_y:int = 0
 
        # Current angle in radians
        self.angle:int = 0
 
        # How far away from the center to orbit, in pixels
        self.radius:int = 0
 
        # How fast to orbit, in radians per frame
        self.speed:float = 0.05


    def update(self):
        """ Update the ston's position. """
        # Calculate a new x, y
        self.rect.x = self.radius * math.sin(self.angle) + self.center_x
        self.rect.y = self.radius * math.cos(self.angle) + self.center_y
 
        # Increase the angle in prep for the next round.
        self.angle += self.speed
 

