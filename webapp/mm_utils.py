# generate a function to return random numbers between a start value and end value
# from random import *
import random


def add_func(a, b):
    return a + b

def multi_func(a, b):
    return a * b


def getTestableRange(a, b):
    x = a
    y = b + 1
    return master_list[x:y]


def getListOfTestableNumbers(a, b):
    requestedSampleSize = a
    testableRange = b
    if (requestedSampleSize == len(testableRange)): #Needs further review
        return random.shuffle(testableRange)
    elif (requestedSampleSize > len(testableRange)):
        # return (testableRange)*(requestedSampleSize//len(testableRange)) + ((requestedSampleSize)%len(testableRange))*someFunc(shuffles_returns_onetestableRange))
        return (testableRange)*(requestedSampleSize//len(testableRange)) + getRandomTestElements(((requestedSampleSize)%len(testableRange)), testableRange)
    else:
        print("Very small test number set selected")


# getRandomTestElements(((requestedSampleSize)%len(testableRange)), testableRange)

def getRandomTestElements(a, b):
    print("Value of b before shuffle: \n", b)
    k = b
    random.shuffle(k)
    print("Value of b after shuffle: \n", b)
    print("Value of k after shuffle: \n", k)
    j = k
    myRandomTestElements = []
    for i in range(0, a):
        myRandomTestElements.append(j.pop())
    return myRandomTestElements


master_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100] 

# table_list_l1 = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# User choice selection for euther addition or subtraction numbers
user_choice = input("Hello, Eli and Grace Pearl... What would you like to practice today? 'multiply' or 'add'?")

print()
print("Please enter the number of questions or samples to test: ")
# requestedSampleSize = 20  # This is the number of questions to try
requestedSampleSize = int(input(": "))

# tableOfChoice_unBlended = 5 # This is the single table of 5 on one side of the computation eg level1

# Need to create a func that returns a list of test table numbers when given a lower and upper marks
print("Please enter the lower and upper test mark numbers to constitute a test range:")
# testableRange = (2, 12) # Where 2 is lower table map and 12 is top map inclusive. [2,3,4,...12]
testValue_lower = int(input("Lower Value: "))
testValue_upper =  int(input("Upper Value: "))
testableRange = getTestableRange(testValue_lower, testValue_upper)
print(testableRange)

# create a list of testable numbers.. i.e. those on the right side of the equation.

# listOfTestableNumbers = slice_of_masterList(from_posn2tosay12_as_a_listlist) + list_from_a_func(which_randomly_picks_a_sample_from(requestedSampleSize-testablerange)ensuring_its not repeating some numers more than accepatble frequency given the sample size)

print()
q = getListOfTestableNumbers(requestedSampleSize, testableRange)
print("List Of Testable Numbers: ")
print(q)

random.shuffle(q)

print("Q list after shuffle: ", q)

for i in range(len(q)):
    x = 5
    y = q[i]

    # z = x * y
    # print(f'{i + 1}.  {x} X {y} = {z}')
    if user_choice == "multiply":
        z = multi_func(x, y)
        print(f'{i + 1}.  {x} X {y} = {z}')
    elif user_choice == "add":
        z = add_func(x, y)
        print(f'{i + 1}.  {x} + {y} = {z}')
    else:
        print("Sorry you entered a wrong choice!")

# print(getTestableRange(2, 5))

# p = 21 // 2
# r = 21 % 2

# print(f'P = {p}, R = {r}')
