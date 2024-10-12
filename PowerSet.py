#Name: Irhan Iftikar
#Date: October 2024
#Description: Code that finds the Power Set of a set of numbers entered by the user
#Source: Code modified and adapted from https://stackoverflow.com/questions/1482308/how-to-get-all-subsets-of-a-set-powerset

#Function that creates a set based on the user's input of numbers
def user_input():
    list_input = input("Enter numbers to create a set, separated by commas: ")
    #Splits values by commas, removes duplicates from set, converts string values to integers
    user_list = [int(x) for x in list(dict.fromkeys(list_input.split(',')))]
    return user_list

#Function that prints the Power Set of the original set
def powerset(user_list):
    powerset = []
    for i in range(1 << len(user_list)):
        powerset.append([user_list[j] for j in range(len(user_list)) if (i & (1 << j))])
    #Sorts Power Set by increasing length
    powerset.sort(key=len)
    print("Powerset: ")
    for value in powerset:
        print(value)

#Main function that executes other functions
def main():
    user_list = user_input()
    powerset(user_list)

while True:
    try:
        main()
    except ValueError: 
        print("You incorrectly entered the numbers.")