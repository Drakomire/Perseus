import sys

sys.path.append('../src')
from perseus import Perseus, Lang, Pos
from perseus._ships.skill import Skill

from pprint import pprint

api = Perseus(url="http://localhost:5000")
# api = Perseus(url="http://perseusapi.duckdns.org:5000")
# nautalis and ingraham

# g = api.Gear("Prototype BF-109G", level=10)
g = api.Gear("F7F Tigercat", level=13)


x_join = " x "

s = f"""
Stats: {g.stat_boosts}
Level: {g.level}
Plane Health: {g.hp}
RoF: {g.reload}
Speed: {g.speed}
Dodge Limit: {g.dodge_limit}
Crash Damage: {g.crash_damage}
Ordnance: {''.join([
    f'''
    Name: {arm.name}
    Damage: {x_join.join([str(v) for v in arm.damage])} ({arm.damage[0]*arm.damage[1]})
    '''
    for arm in g.armament
])}
"""

print(s)