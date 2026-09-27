#Kilde: The Coffee Shop Price Calculator - www.101computing.net/the-coffee-shop-price-calculator

"variabler"
import re


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
#####
#andre funsjoner for at kode skal funke
def kopperAdd ():
   #en løkke for å lage tomme ordbøker som kan brukes senere i coden
   for x in range(antallKoper):
      kaffer.append({f"{x}smak": "", "size": "", "tilbehør": ""})
      recit.append({f"{x}smak": "", "size": "", "tilbehør": ""})
def prisOmSmak():
   #denne funkjonen endrer prisene inpå "price" og inpå "recit"
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
########
#coden begyner her

welcome()

antallKoper = int(input("How manny cups do you want? "))
kopperAdd()

print(kaffer)
print(recit)
coffeeMeny()




while antallKoper > 0 :
   kaffe = str(input("What coffee do you want? ")).title()
   prisOmSmak()
   size = str(input("What size do you want? ")).title()
   prisOmStørelse()
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