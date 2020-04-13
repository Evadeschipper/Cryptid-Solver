
import numpy

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

# Write distance function

def surroundingTiles(x, y, distance):

    alltiles = []

    xs = numpy.arange(x-distance, x+distance+1, 1)
    ys = numpy.concatenate([numpy.arange(0.5*distance, distance+0.5, 0.5), numpy.arange(0.5*distance, distance, 0.5)[::-1]])

    print(xs)
    print(ys)

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
    # Then from those tiles, determine which tiles are within the required distance. (surroundingTiles())
     # Mark those tiles in the map as satisfying the hint. 

    distance = 1

    return distance

if __name__ == "__main__":

    print(surroundingTiles(5, 5, 2))
