import random
n= random.randint(0,100)
guesses = 0
while True:
    guesses = guesses + 1
    print("I am thinking of a number(1,100), can you guess it?")
    g= int(input())
    if g==n:
        break
    elif g < n :
        print ("too low")
    elif g > n :
        print ("too high")
    #tell users if the number they entered is too high or too low
    else:
        print("Wrong")
        
print("Correct, you took", guesses,"guesses")
#tell correct, you took 00 guesses