
from card import mapInstructions, structures
from mapCreate import mapCreate
import numpy

def surroundingTiles(x, y, distance):

    alltiles = []

    xs = numpy.arange(x-distance, x+distance+1, 1)
    ys = numpy.concatenate([numpy.arange(0.5*distance, distance+0.5, 0.5), numpy.arange(0.5*distance, distance, 0.5)[::-1]])

    # calculate coordinates for the surrounding tiles.
    for i, xvalue in enumerate(xs):
        for yvalue in numpy.arange(y-ys[i], y+ys[i]+0.5, 1):
            alltiles.append({"x": xvalue, "y": yvalue})

    # Then filter out the tiles that have 
    # * an x-coordinate outside of range [0, 11] OR
    # * an y-coordinate out of range [0, 8.5]

    tiles = []

    for tile in alltiles:
        if tile['x'] >= 0 and tile['x'] <= 11 and tile['y'] >= 0 and tile['y'] <= 8.5:
            tiles.append(tile)

    return tiles

def distance(Map, distance, what):

    # First find the tiles that satisfy the condition. (e.g. tiles with a blue structure on it). 

    temptiles = []

    if what in ["forest", "desert", "swamp", "mountain", "water"]:
        for tile in Map:
            if tile["terrain"] == what:
                temptiles.append(tile)
    elif what == "bear":
        for tile in Map:
            if tile["bear"] == True:
                temptiles.append(tile)
    elif what == "cougar":
        for tile in Map:
            if tile["cougar"] == True:
                temptiles.append(tile)
    elif what == "animal":
        for tile in Map:
            if tile["bear"] == True or tile["cougar"] == True:
                temptiles.append(tile)
    elif what in ["blue", "white", "green"]:
        for tile in Map:
            if tile["structure"]["colour"] == what:
                temptiles.append(tile)
    elif what in ["standing stone", "abandoned shack"]:
        for tile in Map:
            if tile["structure"]["type"] == what:
                temptiles.append(tile)

    # Then from those tiles, determine which tiles are within the required distance. 

    affectedTiles = []

    for tile in temptiles:
        affectedTiles.extend(surroundingTiles(tile["x"], tile["y"], distance))

    # Mark those tiles in the map as satisfying the hint. 

    for tile in Map:
        for affectedTile in affectedTiles:
            if tile["x"] == affectedTile["x"] and tile["y"] == affectedTile["y"]:
                tile[str(distance)+what] = True
    
    for tile in Map:
        if tile.get(str(distance)+what) == None:
            tile[str(distance)+what] = False

    return Map

"""
Possible hints:
- On one of two types of terrain: Can already very easily be checked.
    * forest or desert / forest or water / forest or swamp / forest or mountain /
      desert or water / desert or swamp / desert or mountain / water or swamp /
      water or mountain / swamp or mountain
- Within one space of a terrain type or animal territory: needs to be checked. 
    * forest / desert / swamp / mountain / water / animal
- Within two spaces of animal territory or a type of structure:
    * standing stone / abandoned shack / cougar / bear
- Within three spaces of a colour of structure:
    * blue structure / white structure / green structure

"""

def mapAnalyze(mapInstructions, structures):

    Map = mapCreate(mapInstructions, structures)

    terrainhints = (("forest", "desert"), ("forest", "water"), ("forest", "swamp"),
                    ("forest", "mountain"), ("desert", "water"), ("desert", "swamp"),
                    ("desert", "mountain"), ("water", "swamp"), ("water", "mountain"),
                    ("swamp", "mountain"))

    distancehints = ((1, "forest"), (1, "desert"), (1, "swamp"), (1, "mountain"),
                     (1, "water"), (1, "animal"), (2, "standing stone"), (2, "abandoned shack"),
                     (2, "cougar"), (2, "bear"), (3, "blue"), (3, "white"), (3, "green"))

    for hint in terrainhints:
        for tile in Map:
            if tile["terrain"] == hint[0] or tile["terrain"] == hint[1]:
                tile[hint[0]+"/"+hint[1]] = True
            else:
                tile[hint[0]+"/"+hint[1]] = False

    for hint in distancehints:
        Map = distance(Map, hint[0], hint[1])

    return Map

hints = ('forest/desert', 'forest/water', 'forest/swamp', 'forest/mountain', 'desert/water', 
         'desert/swamp', 'desert/mountain', 'water/swamp', 'water/mountain', 'swamp/mountain', 
         '1forest', '1desert', '1swamp', '1mountain', '1water', '1animal', 
         '2standing stone', '2abandoned shack', '2cougar', '2bear', '3blue', '3white', '3green')

if __name__ == "__main__":

    Map = mapAnalyze(mapInstructions, structures)
    print(Map)
