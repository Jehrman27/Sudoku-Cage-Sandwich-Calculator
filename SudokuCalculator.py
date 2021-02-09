# Sudoku Killer/Sandwich Calculator

#   This program will calculate all possible combinations that a pool of digits add or multiply to a given number

import itertools                            # Import library needed for calculating all combinations
import math                                 # Import library for calculating product of all elements in an iterable

totalNum = ""                               # The number to sum/multiple to
totalPrompt = False                         # Track if user was prompted to enter the total, yet
poolList = [1, 2, 3, 4, 5, 6, 7, 8, 9]      # The pool of numbers to sum/multiply
excludePrompt = False                       # Track if user was prompted to exclude, yet
excludeConf = ""                            # Yes/no if numbers should be excluded from pool
excludeTemp = ""                            # Temporary storage of numbers to exclude
excludelist = ""                            # The numbers we want to exclude from the pool
multList = ""                               # The list of combinations that multiply to numFinal
operConf = ""                               # Choice of operation to complete at end of program
operPrompt = False                             # Track if user entered valiid operation

# This function adds up all combinations of digits in pool and prints all that add to total
def summate(total, pool): 

    sumsList = [""]                         # The list of combinations that sum to numFinal

    sums = itertools.chain(itertools.combinations(pool, r=n) for n in range(1,len(pool)+1))

    for it in  sums:
        for s in it:
            #print ( f"sum{s} = {s if isinstance(s,int) else sum(s)}")
            if sum(s) == total:
                sumsList.append(s)
                
    print(sumsList) 

# This function multiplies all combinations of digits in pool and prints all that multiply to total
def multimate(total, pool): 

    multiList = [""]                            # The list of combinations that multiply to numFinal

    products = itertools.chain(itertools.combinations(pool, r=n) for n in range(1,len(pool)+1))

    for it in  products:
        for s in it:
            if math.prod(s) == total:
                multiList.append(s)
                
    print(multiList)

# Ask user for the final number to sum/mult to and check if its a valid entry
while totalNum.isnumeric() == False or totalNum == 0:
    
    if totalPrompt == False: # The first prompt
        
        totalNum = input("Please enter the non-negative whole number you want to sum/multiply to: ")

        totalPrompt = True

    else: # Subsequent prompts

        totalNum = input("Invalid entry. Please enter a non-negative whole number: ")

        totalPrompt = True

totalNum = int(totalNum) # Typecast the total to an integer for comparing later


while excludePrompt == False:
    
    print("The current pool:", poolList) # Display the current pool before each prompt

    excludeTemp = input("Enter a digit to exclude from the pool (enter 0 to continue): ")

    if excludeTemp.isnumeric() == True: # Test if the input is a positive whole number

        if excludeTemp == "0": # If input is 0, exit loops and continue with program

            excludePrompt = True
            excludeConf = "no"
        
        elif int(excludeTemp) in poolList: # If the input is in the current pool list, remove it

            excludeTemp = int(excludeTemp)
            poolList.remove(excludeTemp)

        elif int(excludeTemp) not in poolList: # If input isn't found in the pool, prompt again

            print("Entry not found in the pool.")                    

    else: print("Invalid entry.")

while operPrompt == False:
    operConf = input("Please enter what operation you would like to use (Sum, Multiply, Both): ")

    if operConf.lower() == "sum":

        summate(totalNum, poolList)
        operPrompt = True
        
    elif operConf.lower() == "multiply":

        multimate(totalNum, poolList)
        operPrompt = True
        
    elif operConf.lower() == "both":

        summate(totalNum, poolList)
        multimate(totalNum, poolList)
        operPrompt = True
