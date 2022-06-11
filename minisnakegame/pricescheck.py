"""x = round (5.74567854,3)
print(x)"""

"""for x in "Toronto":
    if x== "n":
        break
    print(x)"""
    
# create a list of object(pen,pencil,bottle)
# use a for loop to access those objects and when it gets to pencil, break

"""list = ["book","water bottle", "boots"]"""

"""for x in list:
    if x== "water bottle":
        break
    print(x)"""
    
prices = [3.44, 9.99, 2.50, 20.00]
total=0
for price in prices:
    print ("item costs $", price)
    total = total+price
print ("shopping total", round(total, 2))