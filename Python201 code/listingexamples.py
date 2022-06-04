fruits =  ['pineapple', 'watermelon', 'strawberry']
colors = ['red','black','green','blue','yellow','gray','turquoise']

print(fruits[1])
print(fruits[-1])
print(colors[2:5])
print(colors)

fruits.append('kiwi')
colors.insert(0, 'orange')
colors.remove('yellow')
colors.pop(3)

print(fruits)
print(colors)

del fruits[3]
del colors

print(fruits)

