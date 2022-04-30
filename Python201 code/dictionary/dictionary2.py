import json
data = json.load(open("data.json"))

def translate(word):
    return data [word]

word = input("Enter a word please: ")
print(translate(word))