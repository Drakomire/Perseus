"""
Import requirements
"""

from download import init as initPerseusAPI
#This function downloads all the API data
# initPerseusAPI()
from src.ships.ship import Ship

#Temporary Testing Data
s = Ship("Percy",nicknames=True)
print(s.name)
print(s.skills)
