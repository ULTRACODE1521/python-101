from tkinter import Tk, simpledialog, messagebox
def read_from_file():
    with open("capitals_data.txt") as file:
        for line in file:
            line=line.rstrip("\n") #this will add a new line after each city
            country,city = line.split("/")

def write_to_file(country_name, city_name):
    with open ("capitals_data.txt", "a") as file:
        file.write("\n" + country_name+ "/" + city_name)
print ("Ask me the Capital cities of the world")
root=Tk()
root.withdraw()
the_world={}
read_from_file