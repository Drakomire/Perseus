"""
Download constants and open files
This should be rerun when init() is run to refresh the data
"""


import json
import os
from .nicknames import *

#Constants
STAT_KEYWORDS = {
  "durability": "hp",
  "cannon" : "fp",
  "antiaircraft" : "aa",
  "torpedo" : "trp",
  "air" : "avi",
  "reload" : "rld",
  "dodge" : "eva",
  "hit" : "acc"
}