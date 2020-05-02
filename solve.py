
from card import mapInstructions, structures
from mapAnalyze import mapAnalyze, hints

def testCombination(combination, Map):

    nTiles = 0

    for tile in Map:
        meetsConditions = []

        for hint in combination:
            meetsConditions.append(tile[hint])
        
        if all(meetsConditions):
            nTiles += 1

    return nTiles

def possibleCombinations(knownhints, nTeams):

    possibleCombinations = []

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
                                nTileOptions = testCombination(combi, Map)
                                if nTileOptions == 1:
                                    possibleCombinations.append(combi)
                        else:
                            combi = knownhints + [hint, hint2, hint3]
                            nTileOptions = testCombination(combi, Map)
                            if nTileOptions == 1:
                                possibleCombinations.append(combi)
                else:
                    combi = knownhints + [hint, hint2]
                    nTileOptions = testCombination(combi, Map)
                    if nTileOptions == 1:
                        possibleCombinations.append(combi)
        else:
            combi = knownhints + [hint]
            nTileOptions = testCombination(combi, Map)
            if nTileOptions == 1:
                possibleCombinations.append(combi)

    # Only keep distinct combinations. 
    possibleCombinations = list(map(sorted, possibleCombinations))
    possibleCombinations = [list(item) for item in set(tuple(row) for row in possibleCombinations)]

    return possibleCombinations

if __name__ == "__main__":

    Map = mapAnalyze(mapInstructions, structures)

    nTeams = 3
    knownhints = ['water/mountain']

    test = possibleCombinations(knownhints, nTeams)
    print(test)

