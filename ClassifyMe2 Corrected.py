# Write a function named determineStatus() that prompts the user for how many
# credits they have earned and uses a decision structure (if, else, etc.) to
# determine the class standing of the student. The function should display the
# standing to the student (90 points).

def determineStatus():
    userInput = eval(input("How many credit hours do you have? "))
    hours = userInput
    F=30
    J=60
    S=90
    Max=200
    if hours <= Max:
      if hours < 0 :
        print("You can't have negative credit hours")
      if 0 <= hours < F:
        print("You are classified as a Freshman")
      if hours >= F and hours < J:
        print("You are classified as a Sophmore")
      if hours >= J and hours < S:
        print("You are classified as a Junior")
      if hours >= S and hours < Max:
        print("You are classified as a Senior")
      if hours >= 200:
        print("With",hours," hours you are either an Alumni, 2nd Degree seeking student or lying about your hours.")
    
# Write a main() function that calls the determineStatus() function (5 points).


def main():
  determineStatus() # Call to determineStatus() function
  
    
main()# Call to main function
