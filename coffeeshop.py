#Kilde: The Coffee Shop Price Calculator - www.101computing.net/the-coffee-shop-price-calculator

"variabler"
price = 0
kaffer = []
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
def kopperAdd ():
   for x in range(antallKoper):
      kaffer.append({f"{x}smak": "", "size": "", "tillbehør": ""})
########



welcome()

antallKoper = int(input("How manny cups do you want? "))
kopperAdd()

print(kaffer)

coffeeMeny()




while antallKoper > 0 :
   kaffe = str(input("What coffee do you want? "))
   antallKoper -= 1
   kaffer[sm][f"{sm}smak"] = kaffe
   sm += 1
print(kaffer)


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