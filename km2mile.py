# File: km2mile.py
# Charles Goodling Assignment 2

def km2mile():
    X = eval(input("Enter the amount of Kilometers to be converted : "))
    Converter = 0.62
    Miles = X * Converter
    print(X,"kilometers would be equal to",end=" ")
    print(Miles,"miles.")

km2mile()
