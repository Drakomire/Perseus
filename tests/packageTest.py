import sys
import os
import time
from PIL import Image
import requests
import io

sys.path.append('../src')

#Import the module
from perseus import Perseus

api = Perseus()

# g = api.Gear(52)
# url = g.icon
# image = Image.open(io.BytesIO(requests.get(url).content))
# image.show()

s = api.Ship("Percy",nicknames=True,affinity=95,oathed=False,level=44,limit_break=1)
print(s.stats)

# url = s.skins[0]["thumbnail"]
# image = Image.open(io.BytesIO(requests.get(url).content))
# image.show()


# ships = api.getAllShips()
# for ship in ships:
#     print(ship.name)

# gears = api.getAllGear()
# for gear in gears:
#     print(gear.name,":\t",gear.rarity)