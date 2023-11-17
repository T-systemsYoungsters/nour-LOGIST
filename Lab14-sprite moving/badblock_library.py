import math
import block_library

class Badblock(block_library.Block):
    def __init__(self, filename,width,height):
        super().__init__(filename,width,height)
        # The "center" the sprite will orbit
        self.center_x = 0
        self.center_y = 0
 
        # Current angle in radians
        self.angle = 0
 
        # How far away from the center to orbit, in pixels
        self.radius = 0
 
        # How fast to orbit, in radians per frame
        self.speed = 0.05


    def update(self):
        """ Update the ball's position. """
        # Calculate a new x, y
        self.rect.x = self.radius * math.sin(self.angle) + self.center_x
        self.rect.y = self.radius * math.cos(self.angle) + self.center_y
 
        # Increase the angle in prep for the next round.
        self.angle += self.speed
 