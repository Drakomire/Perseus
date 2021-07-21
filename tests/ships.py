import sys

sys.path.append('../src')
from perseus import Perseus, Lang

from pprint import pprint

api = Perseus(url="http://perseusapi.duckdns.org:5000")

import time

# for s in api.getAllShips():
#     slots = s.slot_ids
#     slots_flattened = [slot for all_in_slot in slots for slot in all_in_slot]
#     if 12 in slots_flattened:
#         print(s.name)

s = api.Ship("Saratoga")
print(s.slot_names)
print(s.armor_id)
print(s.armor_type)