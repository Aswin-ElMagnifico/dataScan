import pickle
import re
file = open("dataset_2.dat", "rb")

firm = input("enter firm number: ")


try:

    while True:
        obj = pickle.load(file)
        if re.match(obj.fei_id, firm, re.IGNORECASE):
            obj.display()

except EOFError:
    pass