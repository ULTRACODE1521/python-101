"""a=1     #float  

print(a)
print(int(a))"""


"""first = '100'
second = '150'
print(first + second)"""

#write a program to ask users to enter how many hours he/she worked. then multiply it by $12, then print the result

workhours = int(input("Enter the amount of hours you worked: ")) 
moneyperhour = int(input("Enter the amount of money you earn per hour: "))
money= workhours * moneyperhour
print("This is the money you earned from your work: $",money)