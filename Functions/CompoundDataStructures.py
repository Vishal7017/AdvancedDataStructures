elements = {"hydrogen" : {"number": 1, "weight": 1.00094, "symbol": "H"},
            "helium" : {"number": 2, "weight": 4.002602, "symbol" : "He"}}


helium = elements["helium"]
hydrogen_weight = elements["hydrogen"]["weight"]

oxygen = {"number": 8, "weight":15.999, "symbol": "O"}
elements["oxygen"] = oxygen

print('elements = ', elements)