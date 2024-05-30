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
    "hex": {
        "scenario_args": [
            (1,),
            (-1,),
            (10,),
            (-10,),
            (-9_223_372_036_854_775_808,),
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
        "scenario_args": [
            (1,),
            (20,),
            (100,),
            (500,),
            (5000,),
        ]
    },
    "zip": {
        "scenario_args": [
            (1, 1),
            (20, 20),
            (100, 100),
            (500, 300),
            (300, 150),
        ]
    },
}
