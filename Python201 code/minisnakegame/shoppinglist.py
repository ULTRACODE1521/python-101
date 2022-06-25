print("Welcome to Shopping List!")
numItems = input("How many items do you want? ")
myTup = ()
myList = []

for x in range(int(numItems)):
    itemName = input("Enter item name: ")
    itemPrice = input("Enter item price: ")
    myTup = (itemPrice, itemName)
    myList.append(myTup)

myList.sort()

for x in range(len(myList)): print(myList[x][1] + " = " + myList[x][0])