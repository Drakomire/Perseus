In the future this repo is going to host Perseus. My auto-updating Azur Lane API. Perseus is going to use the game's source code to update immediately after an update.

### Using my ship nickname handler (Python Only)
I recommend using code to make the file auto update. Simply use something like this.
Its possible the repo owner may change in the future so watch out for that.


    content = requests.get('https://raw.githubusercontent.com/Drakomire/Perseus/main/data/nicknames.py').content
    f = open("nicknames.py", "w")
    f.write(content.decode('utf-8'))
    f.close()


In the file you want to use nicknames in:

    import nicknames
     
    #Get a nickname automatically. Input can be any case, Output is correct capitalization.
    ship_name = nicknames.getNickname(ship_name)
    
    #Get the entire nickname list if you want to
    list = nicknames.nicknames

