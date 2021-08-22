import sys

sys.path.append('../src')
from perseus import Perseus, Lang, Pos
from perseus._ships.skill import Skill

from pprint import pprint

api = Perseus(url="http://localhost:5000")
# api = Perseus(url="http://perseusapi.duckdns.org:5000")
# nautalis and ingraham

g = api.Gear("Prototype BF-109G", level=10)

# print(g.stat_boosts)
# print(g.reload)
# print(g.spread)
# print(g.firing_angle)

# print(g.range)


# print(f"damage: {g.ingame_damage}")
# print(g.volley)
# print(g.volley_time)
# print(g.coefficient)
# print(g.armor_mods)

ordinance = g.ordinance

for arm in ordinance:
    print(arm.name)

print(g.speed)
print(g.dodge_limit)
print(g.crash_damage)