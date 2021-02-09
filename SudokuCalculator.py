# Sudoku Killer/Sandwich Calculator

#   This program will accept a final number and a pool of numbers and
# calculate all of the possible ways that the pool of numbers will
# sum and multiply to the final number.

from itertools import combinations

totalNum = ""                               # The number to sum/multiple to
totalPrompt = False                         # Track if user was prompted to enter the total, yet
poolList = [1, 2, 3, 4, 5, 6, 7, 8, 9]      # The pool of numbers to sum/multiply
excludePrompt = False                       # Track if user was prompted to exclude, yet
excludeConf = ""                            # Yes/no if numbers should be excluded from pool
excludeTemp = ""                            # Temporary storage of numbers to exclude
excludelist = ""                            # The numbers we want to exclude from the pool
sumsList = ""                               # The list of combinations that sum to numFinal
multList = ""                               # The list of combinations that multiply to numFinal

# Ask user for the final number to sum/mult to and check if its a valid entry
while totalNum.isnumeric() == False or totalNum == 0:
    
    if totalPrompt == False:
        
        totalNum = input("Please enter the non-negative whole number you want to sum/multiply to: ")

        totalPrompt = True

    else:

        totalNum = input("Invalid entry. Please enter a non-negative whole number: ")

        totalPrompt = True

print (type(totalNum))

print("The default pool of digits contains the whole numbers 1 through 9.")

# Confirm if user wants to exclude any digits in the default pool.
excludeConf = input("Would you like to exclude any of these digits? (yes/no): ")

while excludePrompt == False:
    
    if excludeConf == "yes":
        
        # ask what digits to exclude
        while excludeConf == "yes":

            print("The current pool:", poolList)

            excludeTemp = input("Enter a digit to exclude from the pool (enter 0 if done): ")

            if excludeTemp.isnumeric() == True:

                if excludeTemp == "0":

                    # If the user entered a 0, exit while loops
                    excludePrompt = True
                    excludeConf = "no"
                
                elif int(excludeTemp) in poolList:

                    print("temp in pool list.")
                    excludeTemp = int(excludeTemp)
                    poolList.remove(excludeTemp)

                elif int(excludeTemp) not in poolList:

                    print("Entry not found in the pool.")                    

            else: print("Invalid entry.")
            
        # excludePrompt = True
        
    elif excludeConf != "no":
        
        excludeConf = input("Invalid entry. Please enter yes or no: ")

    else: excludePrompt = True




    













