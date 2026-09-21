#Kilde: The Coffee Shop Price Calculator - www.101computing.net/the-coffee-shop-price-calculator
#Printer ut al informasjon som skal sendes i begynelsen
print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
print("+                               +")
print("+         The Coffee Shop       +")
print("+              Welcome          +")
print("+                               +")
print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
print("")
print("We serve the following coffees:")
print(" > Espresso      £2.50")
print(" > Americano     £3.00")
print(" > Latte         £2.50")
print(" > Cappuccino    £3.00")
print(" > Macchiato     £2.50")
print(" > Mocha         £3.50")
print(" > Flat White    £2.50")
print("----------------------------")

price = 0
coffee = input("What type of coffee would you like? ").title()
if coffee=="Espresso":
   price = price + 2.50
elif coffee=="Americano":
   price = price + 3
elif coffee=="Latte":
   price = price + 2.50

#Complete the code here...
print("----------------------------")
print("Total Cost: £" + str(price))