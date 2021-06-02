from .__init__ import *

def getNickname(arg):
    #if answer is a nickname, replace answer with ship it is referencing.
    if arg.lower() in nicknames:
        arg = nicknames[arg.lower()];

    return arg;
