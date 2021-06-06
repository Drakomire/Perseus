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
api.initiate()

g = api.Gear(1822)
url = g.icon
image = Image.open(io.BytesIO(requests.get(url).content))
image.show()
