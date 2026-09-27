#Kilde: The Coffee Shop Price Calculator - www.101computing.net/the-coffee-shop-price-calculator

#variabler
price = 0
kaffer = []
recit = []
##sm er for å ha en teller jeg kan bruke over hele programmet
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
   print("----------------------------")
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
   print("----------------------------")
   print("We have the following sizes:")
   print(" > Medium      + £0.00")
   print(" > Large       + £0.50")
   print(" > XL          + £1.00")
   print("----------------------------")
def coffeeTaste():
   print("----------------------------")
   print("We have the following add-ons:")
   print("----------------------------")
   print(" > Vanilla     + £1.00")
   print(" > Milk        + £0.50")
   print(" > Sugar       + £0.50")
   print(" > Nothing     + £0.00")
   print("----------------------------")
#printer ut reciten i en løkke for å repitere det så mange ganger som brukeren har bestilt kopper
def recitPrint():
   global sm
   print("----------------------------")
   print("Here is your receipt:       ")
   for x in range(antallKoper):
      #windows
      #print(f"{kaffer[sm][f"{sm}smak"]} £{recit[sm][f"{sm}smak"]}    {kaffer[sm]["size"]} £{recit[sm]["size"]}    {kaffer[sm]["tilbehør"]} £{recit[sm]["tilbehør"]}")
      print(f"{kaffer[sm][f'{sm}smak']} £{recit[sm][f'{sm}smak']}    {kaffer[sm]['size']} £{recit[sm]['size']}    {kaffer[sm]['tilbehør']} £{recit[sm]['tilbehør']}")
      sm += 1
#####
#andre funsjoner for at kode skal funke
# funksjon som lager tomme ordbøker som kan brukes senere i coden
def kopperAdd ():
   #en løkke for å repitere det så så mange ganger sil svaret brukeren gir
   for x in range(antallKoper):
      kaffer.append({f"{x}smak": "smak", "size": "size", "tilbehør": "tilbehør"})
      recit.append({f"{x}smak": "2.50", "size": "1.00", "tilbehør": "0.50"})
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
   if size == "Medium":
      price += 0
      recit[sm]["size"] = 0.00
   elif size == "Large":
      price += 0.50
      recit[sm]["size"] = 0.50
   elif size == "Xl":
      price += 1.00
      recit[sm]["size"] = 1.00
   else:
      print("Invalid size selection.")
      size = str(input(f"What size do you want for your {kaffer[sm][f'{sm}smak']}? ")).title()
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
   elif tilbehør == "Sugar":
      price += 0.50
      recit[sm]["tilbehør"] = 0.50
   elif tilbehør == "Nothing":
      price += 0.00
      recit[sm]["tilbehør"] = 0.00
   else:
      print("Invalid add-on selection.")
      #windows
      #tilbehør = str(input(f"What addon do you want for your {kaffer[sm]["size"]} {kaffer[sm][f'{sm}smak']}? ")).title()
      tilbehør = str(input(f"What addon do you want for your {kaffer[sm]['size']} {kaffer[sm][f'{sm}smak']}? ")).title()
      prisOmTilbehør()
########
#coden som skjøres begyner her

welcome()

antallKoper = int(input("How manny cups do you want? "))

kopperAdd()
#lagre nummeret for senere bruk
tall = antallKoper

coffeeMeny()
while antallKoper > 0 :
   kaffe = str(input("What coffee do you want? ")).title()
   prisOmSmak()
   antallKoper -= 1
   kaffer[sm][f"{sm}smak"] = kaffe
   sm += 1

#barrefor å resette til defult
antallKoper = tall
sm = 0
coffeeSize()
while antallKoper > 0 :
   size = str(input(f"What size do you want for your {kaffer[sm][f'{sm}smak']}? ")).title()
   prisOmStørelse()
   antallKoper -= 1
   kaffer[sm]["size"] = size
   sm += 1

#barrefor å resette til defult
antallKoper = tall
sm = 0

coffeeTaste()
while antallKoper > 0 :
   #windows
   #tilbehør = str(input(f"What addon do you want for your {kaffer[sm]["size"]} {kaffer[sm][f"{sm}smak"]}? ")).title()
   tilbehør = input(f"What addon do you want for your {kaffer[sm]['size']} {kaffer[sm][f'{sm}smak']}? ").title()
   prisOmTilbehør()
   antallKoper -= 1
   kaffer[sm]["tilbehør"] = tilbehør
   sm += 1

antallKoper = tall
sm = 0
recitPrint()


print("----------------------------")
print("Your Total Cost is: £" + str(price))