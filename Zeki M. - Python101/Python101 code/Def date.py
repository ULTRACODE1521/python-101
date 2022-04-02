#Write a program to convert a date in form "mm/dd/yyyy" to month, day , and year

def main():
    #input the date
    dateStr= input("Enter a date (mm/dd/yyyy):")

    #split into components
    monthStr, dayStr, yearStr=dateStr.split("/")

    #convert monthStr to the month nametuple
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    monthStr=months[int(monthStr)-1]

    #output result in month, day, year format
    print("The converted date is:",monthStr, dayStr+",", yearStr)

main()
