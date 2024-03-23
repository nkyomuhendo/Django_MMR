# generate a function to return random numbers between a start value and end value
# from random import *
import random

from .models import Exercise


# def mentalMath(user_choice=category, table_of_choice=table, requestedSampleSize=no_of_samples, testValue_lower=low_test_mark, testValue_upper=upper_test_mark):

def create_exercises_from_product(product, user):
    # Unpack product attributes
    category = product.category
    table = product.table
    no_of_samples = product.no_of_samples
    low_test_mark = product.low_test_mark
    upper_test_mark = product.upper_test_mark


    user_choice = category
    table_of_choice = table
    requestedSampleSize = no_of_samples
    testValue_lower = low_test_mark
    testValue_upper = upper_test_mark

    testableRange = getTestableRange(testValue_lower, testValue_upper)

    q = getListOfTestableNumbers(requestedSampleSize, testableRange)

    random.shuffle(q)

    print("category: ", user_choice,  "of type: ", type(user_choice),  " and length: ", len(str(user_choice)))
    print()
    print("category Name: ", category.name,  "of type: ", type(category.name), "and length: ", len(str(category.name)))


    # for i in range(0, len(q)):
    #     x = table_of_choice
    #     y = q[i]
    #     exercises_data = []
    #     # z = x * y
    #     # print(f'{i + 1}.  {x} X {y} = {z}')
    #     if user_choice == "multiply":
    #         z = multi_func(x, y)
            
    #         {
    #             "item_No": i + 1,
    #             "x_val": x,  # Adjust as needed
    #             "y_val": y,  # Adjust as needed
    #             "z_val": z,  # Adjust as needed
    #             "o_val": '___',  # Adjust as needed
    #             "p_val": False,  # Default value
    #             "q_val": category.name  # Using category name as an example
    #         }.append(exercises_data)
    #     # for idx in range(no_of_samples)
    
    #         print(f'{i + 1}.  {x} X {y} = {z}')
    #     elif user_choice == "add":
    #         z = add_func(x, y)
            
    #         {
    #             "item_No": i + 1,
    #             "x_val": x,  # Adjust as needed
    #             "y_val": y,  # Adjust as needed
    #             "z_val": z,  # Adjust as needed
    #             "o_val": '___',  # Adjust as needed
    #             "p_val": False,  # Default value
    #             "q_val": category.name  # Using category name as an example
    #         }.append(exercises_data)
            
    #         print(f'{i + 1}.  {x} + {y} = {z}')
    #     else:
    #         print("Sorry you entered a wrong choice!")
    
    exercises_data = [
        ({
            "item_No": i + 1,
            "x_val": table_of_choice,  # Adjust as needed
            "y_val": q[i],  # Adjust as needed
            "z_val": ((table_of_choice + q[i]) if category.name == "Addition" else (table_of_choice * q[i])),  # Adjust as needed
            "o_val": '___',  # Adjust as needed
            "p_val": False,  # Default value
            "q_val": '___'  # Using category name as an example
        } ) for i in range(len(q))
    ]

    print()
    print(exercises_data)

    exercises_to_create = []
    for data in exercises_data:
        exercise = Exercise(
            product=product,
            **data
        )
        exercises_to_create.append(exercise)

    Exercise.objects.bulk_create(exercises_to_create)


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
        return random.sample(testableRange, k=(len(testableRange)))
    elif (requestedSampleSize > len(testableRange)):
        # return (testableRange)*(requestedSampleSize//len(testableRange)) + ((requestedSampleSize)%len(testableRange))*someFunc(shuffles_returns_onetestableRange))
        return (testableRange)*(requestedSampleSize//len(testableRange)) + getRandomTestElements(((requestedSampleSize)%len(testableRange)), testableRange)
    else:
        print("Very small test number set selected")
        return getRandomTestElements(requestedSampleSize, testableRange)


# getRandomTestElements(((requestedSampleSize)%len(testableRange)), testableRange)

def getRandomTestElements(a, b):
    print("Value of b before shuffle: \n", b)
    k = b.copy()
    random.shuffle(k)
    print("Value of b after shuffle: \n", b)
    print("Value of k after shuffle: \n", k)
    j = k.copy()
    myRandomTestElements = []
    if ( a < len(b)):
        for i in range(0, a):
            myRandomTestElements.append(j.pop())
        return myRandomTestElements
    elif (a > len(b)):
        for i in range(0, len(b)):
            myRandomTestElements.append(j.pop())
        return myRandomTestElements
    else:
        pass



master_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100] 

# table_list_l1 = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# User choice selection for either addition or subtraction numbers
# user_choice = input("Hello, Eli and Grace Pearl... What would you like to practice today? 'multiply' or 'add'?")

# table_of_choice = int(input("Please enter your preferred practice table: "))

print()
print("Please enter the number of questions or samples to test: ")
# requestedSampleSize = 20  # This is the number of questions to try
# requestedSampleSize = int(input(": "))

# tableOfChoice_unBlended = 5 # This is the single table of 5 on one side of the computation eg level1

# Need to create a func that returns a list of test table numbers when given a lower and upper marks
print("Please enter the lower and upper test mark numbers to constitute a test range:")
# testableRange = (2, 12) # Where 2 is lower table map and 12 is top map inclusive. [2,3,4,...12]
# testValue_lower = int(input("Lower Value: "))
# testValue_upper =  int(input("Upper Value: "))


# testableRange = getTestableRange(testValue_lower, testValue_upper)
# print(testableRange)

# create a list of testable numbers.. i.e. those on the right side of the equation.

# listOfTestableNumbers = slice_of_masterList(from_posn2tosay12_as_a_listlist) + list_from_a_func(which_randomly_picks_a_sample_from(requestedSampleSize-testablerange)ensuring_its not repeating some numers more than accepatble frequency given the sample size)


# print()
# q = getListOfTestableNumbers(requestedSampleSize, testableRange)
# print("List Of Testable Numbers: ")
# print(q)

# random.shuffle(q)

# print("Q list after shuffle: ", q)

# Set the desired table to practice with



# for i in range(0, len(q)):
#     x = table_of_choice
#     y = q[i]

#     # z = x * y
#     # print(f'{i + 1}.  {x} X {y} = {z}')
#     if user_choice == "multiply":
#         z = multi_func(x, y)
#         print(f'{i + 1}.  {x} X {y} = {z}')
#     elif user_choice == "add":
#         z = add_func(x, y)
#         print(f'{i + 1}.  {x} + {y} = {z}')
#     else:
#         print("Sorry you entered a wrong choice!")

# print(getTestableRange(2, 5))

# p = 21 // 2
# r = 21 % 2

# print(f'P = {p}, R = {r}')
