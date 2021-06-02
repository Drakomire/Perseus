"""
File Downloads
"""
import requests
import json
import io
import os

dir = os.path.dirname(__file__)

#REMINDER TO ADD WHITELIST/BLACKLIST FOR DOWNLOADS

def init():
    #Get the ship database
    j = requests.get('https://raw.githubusercontent.com/Drakomire/perseus-data/master/dist/ships/ships.json').content
    skills = json.loads(j)
    f = open(os.path.join(dir,"ships/data/ships.json"), "w")
    f.write(json.dumps(skills))
    f.close()
    del f

    #Get the ship type database
    j = requests.get('https://raw.githubusercontent.com/Drakomire/perseus-data/master/dist/ships/types.json').content
    types = json.loads(j)
    f = open(os.path.join(dir,"ships/data/types.json"), "w")
    f.write(json.dumps(types))
    f.close()
    del f

    #Get the ship retrofit database
    content = requests.get('https://raw.githubusercontent.com/Drakomire/perseus-data/master/dist/ships/retrofit.json').content
    f = open(os.path.join(dir,"ships/data/retrofit.json"), "w")
    f.write(content.decode('utf-8'))
    f.close()
    del f


    #Get the ship skill database
    j = requests.get('https://raw.githubusercontent.com/Drakomire/perseus-data/master/dist/ships/skills.json').content
    skills = json.loads(j)
    f = open(os.path.join(dir,"ships/data/skills.json"), "w")
    f.write(json.dumps(skills))
    f.close()
    del f

    #Get the ship nickname database
    ## TODO: Change github host location
    content = requests.get('https://raw.githubusercontent.com/Drakomire/perseus-data/master/dist/ships/nicknames.json').content
    f = open(os.path.join(dir,"ships/data/nicknames.json"), "w")
    f.write(content.decode('utf-8'))
    f.close()
    del f

    #Get the ship lookup table
    content = requests.get('https://raw.githubusercontent.com/Drakomire/perseus-data/master/dist/ships/lookup_table.json').content
    f = open(os.path.join(dir,"ships/data/lookup_table.json"), "w")
    f.write(content.decode('utf-8'))
    f.close()
    del f

    print("Repo up to date!")
