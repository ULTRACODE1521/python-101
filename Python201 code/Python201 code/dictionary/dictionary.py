import json
from difflib import get_close_matches
data = json.load(open("data.json"))

def translate(w):
    w=w.lower()
    if w in data :
        return data[w]
    
    elif len(get_close_matches(w,data.keys())) >0:
        yn = input("Did you mean %s instead? Enter y if yes or n for no: " %get_close_matches(w,data.keys()) [0])
        if yn == 'y':
            return data [get_close_matches(w,data.keys()) [0]]
        elif yn=='n':
            return 'The word does not exist, Please check your word.'
        else:
            return 'I do not understand that word.'
    else:
        return "The word does not exist, Please check your word."

word = input("Enter a word please: ")
print(translate(word))