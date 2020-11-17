import pickle
import re

file = open("imports.dat", "rb")
months = {'january': '01', 'feburary': '02', 'march': '03', 'april': '04', 'may': '05', 'june': '06', 'july': '07',
              'august': '08', 'september': '09', 'october': '10', 'november': '11', 'december': '12'}

choice = int(input("1. Firm name \t 2. Month  ?: "))
try:
    if (choice == 1):
        Fname = input("Enter Firm name: ")

        while True:
            obj = pickle.load(file)

            if re.search(Fname, obj.fname, re.IGNORECASE):
                print(obj.fname)
                print(obj.iname)
                print(obj.iref)
                print(obj.date + "\n\n")

    if (choice == 2):
        month = input("enter month: ").lower()
        year = input("enter year: ")

        while True:
            obj = pickle.load(file)
            format_date = months[month] + '/[0-3][1-9]/' + year
            date = obj.date.split()
            dt = date[3]
            if re.search(format_date, dt, re.IGNORECASE):
                print(obj.fname)
                print(obj.iname)
                print(obj.iref)
                print(obj.date + "\n\n")


except:
    pass




