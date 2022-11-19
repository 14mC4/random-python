#File: counter.py
# Charles Goodling Assignment 3

# created a counter function.
def counter():

    # outputing a string asking a question then declaring the input as "sentence"
    sentence = input("Enter a sentence to be deciphered: ")

    # breaking up the "sentence" variable into separate strings.
    # for example If the user enters "The Dog" then it will split into ["The","Dog"]
    words = sentence.split()

    # Below is breaking down the length of each word in the variable "words" which is where we split the sentence.
    characters_per_word = {w:len(w) for w in words}

    # Declaring the amount of words in the sentence.
    AmountWords= len(words)

    #outputing You entered + user input
    print("You entered: ", sentence,)

    #outputing a string + AmountWord
    print("The number of words in the sentence are", AmountWords)

    #outputing the breakdown
    print("Here is the breakdown of each word into amount of characters: ", characters_per_word)

counter()
