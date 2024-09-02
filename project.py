#import needed library
import pandas as pd
import numpy as np
import sys


df = pd.read_csv("EDIA.csv")


def main():
    if greeting(input("Welcome to EDIAv2. It is only designed for Emegency Professionals. If you are a professional write yes to contninue and if not, write no to exit: ")):
        prefereddisease = disease()
        print(drugdose(prefereddisease))
    else:
        sys.exit("Thank you for your honesty!")


def greeting(greetanswer):
    greetanswer = greetanswer.lower()
    if greetanswer == 'yes':
        return True
    else:
        return False


def disease():
    print ("Available Disease in this version include:")
    for disease in list(set(df["Disease"])):
        print (disease)
    return input("Please Select your disease: ")


def drugdose(selecteddisease):
    print ("Available drugs for your disease:")
    with open('EDIA.txt') as f:
        files = f.readlines()
        for object in files:
            object = object.split(",")
            if object[0] == selecteddisease:
                print (object[1])
    selecteddrug = input("Please enter drug name: ").lower()
    for object in files:
        object = object.split(",")
        if object[0] == selecteddisease and object[1] == selecteddrug:
            return f"{object[2]}"


if __name__ == '__main__':
    main()
