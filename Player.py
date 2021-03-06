from Ship import *
from Laser import *
from timeit import default_timer as timer

class Player(Ship):
    def __init__(self, x, y, img, health=100):
        super().__init__(x, y, health)
        self.ship_img = img[0]
        self.laser_img = img[1]
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.max_health = health   
        self.cool_down_timer = 0
        self.lasers = []

    def move_lasers(self):
        for laser in self.lasers:
            laser.y -= laser.velocity

    def fire(self):
        self.cool_down_timer = timer()
        self.lasers.append(Laser(self.x, self.y, self.laser_img, 10))

    def can_fire(self):
        end = timer()
        if (end - self.cool_down_timer < 0.5):
            return False
        else:
            return True

