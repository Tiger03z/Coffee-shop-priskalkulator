
from re import match


kaffer = [
    {"0": "latte", "size": "Xl", "tillhør": "IT"},
    {"1": "cappuccino", "size": "Medium", "tillhør": "Design"},
    {"2": "espresso", "size": "Large", "tillhør": "soker"},
    {"3": "americano", "size": "Small", "tillhør": "melk"}
]
tall = 4
tallomtekst = str(tall)
kaffer.append({tall+"smak": "", "size": "", "tillbehør": ""})

kaffer[0]["0"] = "bigtalk"
kaffer[4][tallomtekst+"smak"] = "cahhe"
print(kaffer)



kaffe = str(input("What coffee do you want? ")).title()
def checknumber(x):
    match kaffe:
        case "Espresso":
            print("It's Espresso")
        case "Americano":
            print("It's Americano")
        case _:
            print("It's neither Espresso nor Americano")
    
checknumber("Espresso")
checknumber("Americano")