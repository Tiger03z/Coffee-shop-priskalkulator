#Kilde: The Coffee Shop Price Calculator - www.101computing.net/the-coffee-shop-price-calculator

"variabler"


price = 0
kaffer = []
recit = []
sm = 0


 

# funksjoner som printer ut al informasjon som skal sendes i begynelsen
def welcome():
   print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
   print("+                                 +")
   print("+         The Coffee Shop         +")
   print("+             Welcome             +")
   print("+                                 +")
   print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
   print("")
def coffeeMeny ():
   print("We serve the following coffees:")
   print("----------------------------")
   print(" > Espresso      £2.50")
   print(" > Americano     £3.00")
   print(" > Latte         £2.50")
   print(" > Cappuccino    £3.00")
   print(" > Macchiato     £2.50")
   print(" > Mocha         £3.50")
   print(" > Flat White    £2.50")
   print("----------------------------")
def coffeeSize():
   print("We have the following sizes:")
   print(" > Medium      + £0.00")
   print(" > Large       + £0.50")
   print(" > XL          + £1.00")
   print("----------------------------")
def coffeTaste():
   print("We have the following add-ons:")
   print("----------------------------")
   print(" > Vanilla     + £1.00")
   print(" > Milk        + £0.50")
   print(" > Suger       + £0.50")
   print(" > Nothing     + £0.00")
   print("----------------------------")
#####
#andre funsjoner for at kode skal funke
# funksjon som lager tomme ordbøker som kan brukes senere i coden
def kopperAdd ():
   #en løkke for å repitere det så så mange ganger sil svaret brukeren gir
   for x in range(antallKoper):
      kaffer.append({f"{x}smak": "", "size": "", "tilbehør": ""})
      recit.append({f"{x}smak": "", "size": "", "tilbehør": ""})
#denne funkjonen endrer prisene inpå "price" og inpå "recit"
def prisOmSmak():
   global price
   global kaffe
   if kaffe == "Espresso":
      price += 2.50
      recit[sm][f"{sm}smak"] = 2.50
   elif kaffe == "Americano":
      price += 3.00
      recit[sm][f"{sm}smak"] = 3.00
   elif kaffe == "Latte":
      price += 2.50
      recit[sm][f"{sm}smak"] = 2.50
   elif kaffe == "Cappuccino":
      price += 3.00
      recit[sm][f"{sm}smak"] = 3.00
   elif kaffe == "Macchiato":
      price += 2.50
      recit[sm][f"{sm}smak"] = 2.50
   elif kaffe == "Mocha":
      price += 3.50
      recit[sm][f"{sm}smak"] = 3.50
   elif kaffe == "Flat White":
      price += 2.50
      recit[sm][f"{sm}smak"] = 2.50
   else:
      print("Invalid coffee selection.")
      kaffe = str(input("What coffee do you want? ")).title()
      prisOmSmak()
### same funksjon som endrer prisene inpå "price" og inpå "recit"
def prisOmStørelse():
   global price
   global size
   if size == "Small":
      price += 0
      recit[sm]["size"] = 0
   elif size == "Medium":
      price += 0.50
      recit[sm]["size"] = 0.50
   elif size == "Large":
      price += 1.00
      recit[sm]["size"] = 1.00
   else:
      print("Invalid size selection.")
      size = str(input("What size do you want? ")).title()
      prisOmStørelse()
### same funksjon som endrer prisene inpå "price" og inpå "recit"
def prisOmTilbehør():
   global price
   global tilbehør
   if tilbehør == "Vanilla":
      price += 1.00
      recit[sm]["tilbehør"] = 1.00
   elif tilbehør == "Milk":
      price += 0.50
      recit[sm]["tilbehør"] = 0.50
   elif tilbehør == "Suger":
      price += 0.50
      recit[sm]["tilbehør"] = 0.50
   elif tilbehør == "Nothing":
      price += 0.00
      recit[sm]["tilbehør"] = 0.00
   else:
      print("Invalid add-on selection.")
      tilbehør = str(input("What add-on do you want? ")).title()
      prisOmTilbehør()
########
#coden som skjøres begyner her

welcome()

antallKoper = int(input("How manny cups do you want? "))
kopperAdd()

coffeeMeny()
while antallKoper > 0 :
   kaffe = str(input("What coffee do you want? ")).title()
   prisOmSmak()
   antallKoper -= 1
   kaffer[sm][f"{sm}smak"] = kaffe
   kaffer[sm]["size"] = size
   sm += 1
print(kaffer)
print(recit)



#Complete the code here...
print("----------------------------")
print("Total Cost: £" + str(price))




#not using prob
"""coffee = input("What type of coffee would you like? ").title()
if coffee=="Espresso":
   price = price + 2.50
elif coffee=="Americano":
   price = price + 3
elif coffee=="Latte":
   price = price + 2.50
"""