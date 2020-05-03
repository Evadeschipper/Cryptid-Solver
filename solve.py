
from card import mapInstructions, structures
from mapAnalyze import mapAnalyze, hints
from collections import defaultdict, namedtuple

def testCombination(combination, Map):

    nTiles = 0
    Tiles = []

    for tile in Map:
        meetsConditions = []

        for hint in combination:
            meetsConditions.append(tile[hint])
        
        if all(meetsConditions):
            nTiles += 1
            Tiles.append({'x': tile['x'], 'y': tile['y']})

    return nTiles, Tiles

def possibleCombinations(knownhints, nTeams):

    possibleCombinations = {}
    tempCombinations = {}

    # make a combination of hints. 
    # Check for that combination how many hexagons on the map are possible. 
    # If this is not 1, continue. 
    # If this is 1, add the combination to a list of possible combinations. 

    for hint in hints:

        if (nTeams - len(knownhints) > 1):
            for hint2 in hints:

                if (nTeams - len(knownhints) > 2):
                    for hint3 in hints:

                        if (nTeams - len(knownhints) > 3):
                            for hint4 in hints:

                                combi = knownhints + [hint, hint2, hint3, hint4]
                                nTileOptions, Tiles = testCombination(combi, Map)
                                if nTileOptions == 1:
                                    tempCombinations[tuple(sorted(combi))] = Tiles[0]
                        else:
                            combi = knownhints + [hint, hint2, hint3]
                            nTileOptions, Tiles = testCombination(combi, Map)
                            if nTileOptions == 1:
                                tempCombinations[tuple(sorted(combi))] = Tiles[0]
                else:
                    combi = knownhints + [hint, hint2]
                    nTileOptions, Tiles = testCombination(combi, Map)
                    if nTileOptions == 1:
                        tempCombinations[tuple(sorted(combi))] = Tiles[0]
        else:
            combi = knownhints + [hint]
            nTileOptions, Tiles = testCombination(combi, Map)
            if nTileOptions == 1:
                tempCombinations[tuple(sorted(combi))] = Tiles[0]

    # Only keep distinct combinations. 
    uniqueCombinations = list(map(sorted, tempCombinations))
    uniqueCombinations = [list(item) for item in set(tuple(row) for row in uniqueCombinations)]

    for combi in uniqueCombinations:
        possibleCombinations[tuple(combi)] = tempCombinations[tuple(combi)]

    return possibleCombinations

def hexProbs(possibleCombinations):

    counts = defaultdict(int)
    Tile = namedtuple('Tile', ['x', 'y'])

    for coordinate in possibleCombinations.values():
        counts[Tile(coordinate['x'], coordinate['y'])] += 1

    probs = {}
    nCombi = len(possibleCombinations)

    for key in counts:
        probs[key] = counts[key] / nCombi

    probs = {k: v for k, v in sorted(probs.items(), key=lambda item: item[1])}
    return probs

if __name__ == "__main__":

    Map = mapAnalyze(mapInstructions, structures)

    # nTeams = 3
    # knownhints = ['water/mountain']
   
    nTeams = 4
    knownhints = ['1animal', 'desert/swamp', '3blue', '1desert']

    leftCombinations = possibleCombinations(['3blue', '1desert'], nTeams)
    test = hexProbs(leftCombinations)
    print(test)

