In the future this repo is going to host Perseus. My auto-updating Azur Lane API. Perseus is going to use the game's source code to update immediately after an update.

### Source files
[Source Repo](https://github.com/Drakomire/perseus-data) <br>
Shoutout to @octo-kumo for making the repo I forked 

### Documentation
It doesn't work yet so don't even try
<br>
but if you really want to...
<br>
1. Download the folder
2. `import perseus.Ship` (you'll have to rename it ig)

### Functions
`s = Ship("Name as string")
s = ship(ID number)
`
<br>
Optional arguments:
<br>
level - int <br>
affinity - int <br>
retrofit - bool <br>
nicknames - bool (Whether ship nicknames are used in the contructor. False by default.)

<br>
`
s.stat - returns stats at level 120 retroit
s.id - ship's id number
s._retrofit - returns if ship has a retrofit (Not really intended to be used by the user yet. Maybe I should change this one a bit)
`
