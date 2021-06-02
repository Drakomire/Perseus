"""
Import requirements
"""

from .download import init as initPerseusAPI
#This function downloads all the API data
initPerseusAPI()
from .ships.ship import Ship
