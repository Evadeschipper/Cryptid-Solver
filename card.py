
from mapElements import E1, E2, E3, E4, E5, E6

mapInstructions = ({"position_y": "top", "position_x": "left", "element": E3, "reversed": False},
       {"position_y": "top", "position_x": "right", "element": E4, "reversed": True},
       {"position_y": "middle", "position_x": "left", "element": E1, "reversed": True},
       {"position_y": "middle", "position_x": "right", "element": E2, "reversed": False},
       {"position_y": "bottom", "position_x": "left", "element": E5, "reversed": True},
       {"position_y": "bottom", "position_x": "right", "element": E6, "reversed": True})

structures = ({"colour": "blue", "type": "standing stone", "x": 8, "y": 0},
              {"colour": "blue", "type": "abandoned shack", "x": 6, "y": 3},
              {"colour": "white", "type": "standing stone", "x": 7, "y": 5.5},
              {"colour": "white", "type": "abandoned shack", "x": 9, "y": 7.5},
              {"colour": "green", "type": "standing stone", "x": 11, "y": 1.5},
              {"colour": "green", "type": "abandoned shack", "x": 6, "y": 2})

hints = {"3": {"alpha": 2, "beta": 79, "eta": 28, "?": 37},
         "4": {"alpha": 84, "beta": 1, "gamma": 6, "eta": 67, "?": 14},
         "5": {"alpha": 66, "beta": 71, "gamma": 68, "delta": 73, "eta": 29, "?": 6}}