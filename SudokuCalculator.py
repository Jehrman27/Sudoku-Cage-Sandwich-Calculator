# Sudoku Killer/Sandwich Calculator

#   This program will calculate all possible combinations that a pool of digits add or multiply to a given number

import itertools                            # Import library needed for calculating all combinations

totalNum = ""                               # The number to sum/multiple to
totalPrompt = False                         # Track if user was prompted to enter the total, yet
poolList = [1, 2, 3, 4, 5, 6, 7, 8, 9]      # The pool of numbers to sum/multiply
excludePrompt = False                       # Track if user was prompted to exclude, yet
excludeConf = ""                            # Yes/no if numbers should be excluded from pool
excludeTemp = ""                            # Temporary storage of numbers to exclude
excludelist = ""                            # The numbers we want to exclude from the pool
multList = ""                               # The list of combinations that multiply to numFinal
operConf = ""                               # Choice of operation to complete at end of program


def summate(total, pool):

    sumsList = [""]                             # The list of combinations that sum to numFinal

    sums = itertools.chain(itertools.combinations(pool, r=n) for n in range(1,len(pool)+1))

    for it in  sums:
        for s in it:
            #print ( f"sum{s} = {s if isinstance(s,int) else sum(s)}")
            if sum(s) == total:
                sumsList.append(s)
                
    print(sumsList)


# Ask user for the final number to sum/mult to and check if its a valid entry
while totalNum.isnumeric() == False or totalNum == 0:
    
    if totalPrompt == False: # The first prompt
        
        totalNum = input("Please enter the non-negative whole number you want to sum/multiply to: ")

        totalPrompt = True

    else: # Subsequent prompts

        totalNum = input("Invalid entry. Please enter a non-negative whole number: ")

        totalPrompt = True

totalNum = int(totalNum) # Typecast the total to an integer for comparing later

print("The default pool of digits contains the whole numbers 1 through 9.")

# Confirm if user wants to exclude any digits in the default pool
excludeConf = input("Would you like to exclude any of these digits? (yes/no): ")

while excludePrompt == False:
    
    if excludeConf == "yes":
        
        while excludeConf == "yes": # If user wants to exclude digits, prompt which

            print("The current pool:", poolList) # Display the current pool before each prompt

            excludeTemp = input("Enter a digit to exclude from the pool (enter 0 if done): ")

            if excludeTemp.isnumeric() == True: # Test if the input is a positive whole number

                if excludeTemp == "0": # If input is 0, exit loops and continue with program

                    excludePrompt = True
                    excludeConf = "no"
                
                elif int(excludeTemp) in poolList: # If the input is in the current pool list, remove it

                    print("temp in pool list.")
                    excludeTemp = int(excludeTemp)
                    poolList.remove(excludeTemp)

                elif int(excludeTemp) not in poolList: # If input isn't found in the pool, prompt again

                    print("Entry not found in the pool.")                    

            else: print("Invalid entry.")
        
    elif excludeConf != "no": # If input is neither "yes" or "not", give an error and prompt again
        
        excludeConf = input("Invalid entry. Please enter yes or no: ")

    else: excludePrompt = True


operConf = input("Please enter what operation you would like to use (Sum, Multiply, Both): ")

if operConf.lower() == "sum": summate(totalNum, poolList)
