from .__init__ import *

class Gear:
    def __init__(self,id,level=10):
        self.id = str(id)
        self.gear = gear[self.id]
        self.level = level

    @property
    def icon(self):
        return self.gear["image"]
