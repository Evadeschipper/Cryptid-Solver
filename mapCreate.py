
from card import mapInstructions, structures

def mapCreate(mapInstructions, structures):

    Map = []
    recode_X = {0:5, 1:4, 2:3, 3:2, 4:1, 5:0}
    recode_Y = {0:2.5, 0.5:2, 1:1.5, 1.5:1, 2:0.5, 2.5:0}

    for instruction in mapInstructions:

        Element = instruction['element']
        
        # Reverse the mapElement. 
        if instruction['reversed'] == True:

            for tile in Element:
                tile['x'] = recode_X[tile['x']]
                tile['y'] = recode_Y[tile['y']]
        
        # Add 6 to x values for mapElements for which position_x = right.
        if instruction['position_x'] == "right":

            for tile in Element:
                tile['x'] += 6

        # Add 3 to y values for mapElements for which position_y = middle.
        if instruction['position_y'] == "middle":

            for tile in Element:
                tile['y'] += 3
        
        # Add 6 to y values for mapElements for which position_y = bottom.
        elif instruction['position_y'] == "bottom":

            for tile in Element:
                tile['y'] += 6

        # Add the tiles to the map.
        for tile in Element:
            Map.append(tile)

    # Add the structures to the map. 
    for building in structures:
        for tile in Map:

            if (tile['x'] == building['x'] and tile['y'] == building['y']):
                tile['structure']['present'] = True
                tile['structure']['colour'] = building['colour']
                tile['structure']['type'] = building['type'] 

    return Map

if __name__ == "__main__":

    Map = mapCreate(mapInstructions, structures)