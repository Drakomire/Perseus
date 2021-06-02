import json
import os
from .nicknames import *
from .stats import *
from .retrofit import *
from .skills import *
from .__init__ import *

class Ship:
    def __init__(self,ship,level=120,limit_break=3,affinity=100,oathed=False,retrofit=True,nicknames=False):
        if (type(ship) == int):
            self.id = str(ship)

        else:
            #Nicknames
            if (nicknames):
                ship = getNickname(ship).lower()
            else:
                ship = ship.lower()

            if (ship in lookup_table):
                self.id = str(lookup_table[ship])
                self.ship = ships[self.id]
            else:
                raise ValueError('Ship name is not valid')

        try:
            self.ship = ships[self.id]
            self.level = level
            self.limit_break = limit_break
            self.affinity = affinity
            self.oathed = oathed

            #Turn retrofit to false by defualt if the ship does not have one
            if (retrofit == True):
                retrofit = "retrofit" in self.ship

            self._retrofit = retrofit

        except KeyError:
            raise ValueError('Ship ID is not valid')

    @property
    def name(self):
        return self.ship["name"]["en"]

    @property
    def stats(self):
        return Stats.getStats(self)

    @stats.setter
    def stats(self, val):
        self._stats = val

    @property
    def limit_break(self):
        return self._limit_break-1

    @limit_break.setter
    def limit_break(self, val):
        self._limit_break = val+1

    @property
    def retrofit(self):
        if "retrofit" in self.ship:
            return self.ship["retrofit"]
        else:
            return None

    def getRetrofitStats(self):
        return Retrofit.getRetrofitStats(self.ship)

    def getRetrofitShipID(self):
        return Retrofit.getRetrofitShipID(self)

    @property
    def hull_type(self):
        return types[str(self.hull_id)]["en"]

    @property
    def hull_id(self):
        return self.ship["type"]

    @property
    def armor_type(self):
        return ARMOR_TYPE[self.ship["armor"]]

    @property
    def armor_id(self):
        return self.ship["armor"]

    @property
    def skills(self):
        return Skill.getSkills(self)

    def __str__(self):
        return str(self.id)
#
# s = Ship("Hyuuga",retrofit=False)
# print(s.id)
# print(s.getRetrofitShipID())
# print(s.stats)
