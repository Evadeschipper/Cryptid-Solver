
from card import mapInstructions, structures
from mapAnalyze import mapAnalyze, hints

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
                                    tempCombinations[tuple(sorted(combi))] = Tiles
                        else:
                            combi = knownhints + [hint, hint2, hint3]
                            nTileOptions, Tiles = testCombination(combi, Map)
                            if nTileOptions == 1:
                                tempCombinations[tuple(sorted(combi))] = Tiles
                else:
                    combi = knownhints + [hint, hint2]
                    nTileOptions, Tiles = testCombination(combi, Map)
                    if nTileOptions == 1:
                        tempCombinations[tuple(sorted(combi))] = Tiles
        else:
            combi = knownhints + [hint]
            nTileOptions, Tiles = testCombination(combi, Map)
            if nTileOptions == 1:
                tempCombinations[tuple(sorted(combi))] = Tiles

    # Only keep distinct combinations. 
    uniqueCombinations = list(map(sorted, tempCombinations))
    uniqueCombinations = [list(item) for item in set(tuple(row) for row in uniqueCombinations)]

    for combi in uniqueCombinations:
        possibleCombinations[tuple(combi)] = tempCombinations[tuple(combi)]

    return possibleCombinations

if __name__ == "__main__":

    Map = mapAnalyze(mapInstructions, structures)

    nTeams = 3
    knownhints = ['water/mountain']

    test = possibleCombinations(knownhints, nTeams)
    print(test)

