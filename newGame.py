import os
myMap = """
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
X              X               X
X              X               X
X              X               X
X    XXXXX     X     XXXXX     X
X    X   X     X     X / X     X
X    X   X           X   X     X
X    X   X     X     X   X     X
X    XX XX     X     XX XX     X
X              X               X
X              X               X
X              X               X
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
"""

myMap2 = """
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
X                              X
X                              X
X                              X
X                              X
X                       @      X
X                              X
X                              X
X                              X
X                              X
X                              X
X                              X
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
"""
myMap3 = """
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
X                             /X
X                              X
X                              X
X                              X
X                       @      X
X                              X
X                              X
X                              X
X                              X
X                              X
X                              X
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
"""
myMap4 = """
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
X     X     X   X      X    X  X
X     X     X   X      X    X  X
X     X     XX XX      XX  XX  X
X                              X
X     X     XXXXXXX            X
X     X     X     X            X
X     X     X     X            X
X     X     X     X            X
XXX XXX     XXX XXX     XXX  XXX
X   X+X                 X      X
X     X                 X      X
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
"""
myMap5 = """
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
X     X     X   X      X    X  X
X     X     X   X      X    X  X
X     X     XX XX      XX  XX  X
X                              X
X     X     XXXXXXX            X
X     X     X     X            X
X     X     X     X            X
X     X     X     X            X
XXX XXX     XXX XXX     XXX  XXX
X   X X                 X      X
X     X                 X      X
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
"""

rowLength = 33
class GameState:
    locX = 7
    locY = 5
    Map = myMap
    
def loc2Map(myState) :
	mapLocation = myState.locY*rowLength + myState.locX
	return mapLocation

def stewart(myState):
    print ("Hello there traveler!")
    input ("answer: ")
    print ("Can you go get my sack that I left in the town?")
    respond = input ("y/n: ")
    if "y" in respond:
        input ("Ok, hurry back.")
        myState.Map = myMap3
        
    else:
        input ("If you ever feel like helping me out come on back.")     
def nextLevel(myState):
        global myMap
        global myMap2
        global myMap3
        global myMap4
        global myMap5
        if myState.Map == myMap:
            nextMap = myMap2
            myState.locX = 1
            myState.locY = 1
        if myState.Map == myMap2:
            nextMap = myMap3
        if myState.Map == myMap3:
            nextMap = myMap4
        if myState.Map == myMap4:
            nextMap = myMap5
        myState.Map = nextMap
        return myState

def move(direction, myState): 
    loc = loc2Map(myState)
    
    if "w" in direction:
        if myState.Map[loc - rowLength + 1] == "@":
                stewart(myState)
        elif myState.Map[loc - rowLength + 1] == "/":
                nextLevel(myState)
        elif myState.Map[loc - rowLength + 1] != "X":
                myState.locY -= 1

    elif "s" in direction:
        if myState.Map[loc + rowLength + 1] == "@":
                stewart(myState)
        elif myState.Map[loc + rowLength + 1] == "/":
                nextLevel(myState)
        elif myState.Map[loc + rowLength + 1] != "X":
                myState.locY += 1

                
    elif "a" in direction:
        if myState.Map[loc] == "@":
                stewart(myState)
        elif myState.Map[loc] == "/":
                nextLevel(myState)
        elif myState.Map[loc] != "X":
                myState.locX -= 1

            
    elif "d" in direction:
        if myState.Map[loc + 2] == "@":
                stewart(myState)
        elif myState.Map[loc + 2] == "/":
                nextLevel(myState)
        elif myState.Map[loc + 2] != "X": # +2 to balance the bounds out
                myState.locX += 1
    return myState
        
def drawMap(myState):
    mapLocation = loc2Map(myState)
    currentMap = myState.Map[:(mapLocation+1)] + "O" + myState.Map[(mapLocation+2):] # +2 kills the space
    # +1 is required due to the newline in the beginning
    print(currentMap)

def playGame():
    myState = GameState()
    playing = True

    while playing:
        os.system("cls")
        drawMap(myState)
        cmd = input("Direction (w,a,s,d or q): ")
    
        if "w" in cmd or "a" in cmd or "s" in cmd or "d" in cmd:
            move(cmd, myState)
        elif "q" in cmd:
            playing = False

    print("Goodbye!")

playGame()
