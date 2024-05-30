conf = {
    "abs": {
        "scenario_args": [
            (1,),
            (-1,),
            (10,),
            (-10,),
            (-9_223_372_036_854_775_808,),
        ]
    },
    "hex": {
        "scenario_args": [
            (1,),
            (-1,),
            (10,),
            (-10,),
            (-9_223_372_036_854_775_808,),
        ]
    },
    "sum": {
        # Takes size of the list that will be generated with range
        "scenario_args": [
            (1,),
            (20,),
            (100,),
            (500,),
            (5000,),
        ]
    },
    "map": {
        # Takes size of the list that will be generated with range
        "scenario_args": [
            (1,),
            (20,),
            (100,),
            (500,),
            (5000,),
        ]
    },
    "filter": {
        # Takes size of the list that will be generated with range
        "scenario_args": [
            (1,),
            (20,),
            (100,),
            (500,),
            (5000,),
        ]
    },
    "zip": {
        # Takes size of the list that will be generated with range
        "scenario_args": [
            (1, 1),
            (20, 20),
            (100, 100),
            (500, 300),
            (300, 150),
        ]
    },
    "enumerate": {
        # Takes size of the list that will be generated with range
        "scenario_args": [
            (1,),
            (20,),
            (100,),
            (500,),
            (300,),
        ]
    },
    "any": {
        # Takes size of the list that will be generated with range
        "scenario_args": [
            (1,),
            (20,),
            (100,),
            (500,),
            (300,),
        ]
    },
    "all": {
        # Takes size of the list that will be generated with range
        "scenario_args": [
            (1,),
            (20,),
            (100,),
            (500,),
            (300,),
        ]
    },
}
