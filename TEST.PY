
kaffer = [
    {"0": "latte", "size": "Xl", "tillhør": "IT"},
    {"1": "cappuccino", "size": "Medium", "tillhør": "Design"},
    {"2": "espresso", "size": "Large", "tillhør": "Økonomi"},
    {"3": "americano", "size": "Small", "tillhør": "Markedsføring"}
]
tall = 4
tallomtekst = str(tall)
kaffer.append({"4smak": "", "size": "", "tillbehør": ""})

kaffer[0]["0"] = "bigtalk"
kaffer[4][tallomtekst+"smak"] = "cahhe"
print(kaffer)

