# Charles Goodling
# PowerCalc.py
# 04-16-17
# Assignment 7

# This program will ask a user for two inputs. First input will be the base number then the second
# will be the exponent or power the user would like the calculator to solve. This calculator works
# for negatives and positive bases and powers.
# For Example, User inputs 2 for Base and 2 for Power. The calculator outputs 4.

# I tried to make sure I covered all posible inputs and answers. I like to code and it makes things
# more challenging to do more than requested. So I apologize if I went above the requirements.



# Below we are creating the recursive statement to do the math for us. We are calling Base and Power
# from the main function where the user Inputs the numbers.

def pow(base, power):
    
    # Below the function will check if the base is greater then -1 due to having both positive and negative
    # numbers.
    
    if base > -1:

        # Below the function is checking the powers whether 0 or 1+.
        # Any positive number to the 0 power will be 1.
        if power == 0:
            return 1
        
        #  Below is checking to see if the power is negative and then conducting math to give us
        # proper math input because powers can definitely be negative.
        if power < -1:
            return 1 / pow(base, -power)

        # If a power is 1 then the output will be the base. 2^1 would be 2.
        elif power == 1:
            return base
        # Now if the power is positive and above 1 then we will conduct the math giving up our output.
        else :
            return base * pow(base, power - 1)

    # I feel like I could have posibbly made the code shorter but I felt this section was necessary for
    # Negative bases. If a base is negative then the power output for 0 would be -1 rather than 1.
    if base <= -1:
        if power == 0:
            return -1

    # Works the same way as previous but it is meant for negative powers hence the -1. Though a negative
    # base to a negative exponent does not give the same base it will give a decimal.
        if power <= -1:
            return -1 / pow(base, -power)
        elif power == 1:
            return base
        else :
            return base * pow(base, power - 1)

# Test the input given. Will not accept decimals nor letters.
def determineBase():
        while True:
            try:
                base = int(input ('Please Enter A Base: '))
            except ValueError:
                print("Please use numbers only. No letters nor decimals.")
                continue
            else:
                return base
# Same as above just to test the Power given.
def determinePower():

        while True:
            try:
                power = int(input ('Please Enter A Power: '))
            except ValueError:
                print("Please use numbers only. No letters nor decimals.")
                continue
            else:
                return power


def main():

    #Declares base as the above function.
    base = determineBase()
    #Declares the power as the above function.
    power = determinePower()
    # Runs the above function calling base and power
    pow(base, power)
    # prints both inputs and the answer.
    print("The answer to",base,"to the power of", power,"is", pow(base,power),".")
main()
