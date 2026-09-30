import math

def task1():
    #Task 1

    # Initialize pi and ask the user for the radius
    pi = 3.14159
    radius = float(input("Enter the radius of your sphere: "))

    # Ask user to choose between surface area and volume
    print("To calculate surface area, enter 1")
    print("To calculate volume, enter 2")

    # Take user input to decide calculation
    quantity = input("What do you want to calculate: ")

    # Make sure user cannot enter a number other than 1 or 2
    while (quantity != '1') and (quantity != '2'):
        quantity = input("Error: Invalid input. Please enter 1 to calculate surface area or 2 to calculate volume: ")

    # If user chooses 1, calculate and print surface area
    if quantity == '1':
        surface_area = 4 * pi * radius * radius
        print("The sphere surface area is: ", surface_area)

    # Otherwise if user chooses 2, calculate and print volume
    elif quantity == '2':
        volume = (4 * pi * radius * radius * radius)/3
        print("The sphere volume is: ", volume)

def task2():
    # Task 2

    # Ask the user to input a number
    number = float(input("Please enter a number: "))

    # Check if negative, zero, or positive and print result
    if number < 0:
        print("Your number is negative!")
    elif number == 0:
        print("Your number is zero!")
    elif number > 0:
        print("Your number is positive!")

def task3():
    # Iterate between 0 and 100
    for i in range(101):
        # Print if divisible by 4
        if (i % 4) == 0:
            print(i, end=" ")

def task4():
    # Continuously sum integers until the user enters 'q' to quit
    sum = 0
    sumInput = input("Enter an integer (or 'q' to quit): ")
    
    while sumInput != 'q':
        sum = sum + int(sumInput)
        sumInput = input("Enter an integer (or 'q' to quit): ")
        
    print("Your sum is", sum)

def task5():
    # Approximate Euler's number (e) using a Taylor series
    euler = 0
    index = input("How many terms would you like to sum? ")
    
    for i in range(int(index)):
        euler = euler + (1 / math.factorial(i))
        
    print("Your number is:", euler)

def task8():
    # Truncate a number to a specific number of decimal places without rounding
    number = float(input("Enter a number to truncate: "))
    digits = int(input("Enter a number of decimals to truncate to: "))
    
    # Shift decimal point right, chop off fractional part, then shift back left
    factor = 10 ** digits
    truncated = (int(number * factor)) / factor
    
    print("Your number truncated is:", truncated)

def get_grade_range(score):
    # Determine and print the letter grade based on the final percentage
    if score >= 85:
        grade = 'A'
    elif score >= 70:
        grade = 'B'
    elif score >= 60:
        grade = 'C'
    elif score >= 50:
        grade = 'D'
    else:
        print('This grade is in the Fail range.')
        return 

    print(f"This grade is in the {grade} range. The instructor will decide if it is {grade}+, {grade}, or {grade}-.")

def task9():
    # Calculate a weighted final grade from various assignment and exam scores
    ice = float(input("Enter total ICE score (out of 500): "))
    exam1 = float(input("Enter Exam 1 score (out of 60): "))
    exam2 = float(input("Enter Exam 2 score (out of 60): "))
    final_exam = float(input("Enter Final Exam score (out of 100): "))
    quiz = float(input("Enter Orientation Quiz score (out of 40): "))
    labs = float(input("Enter total Labs score (out of 900): "))
    hw = float(input("Enter total Homework score (out of 400): "))

    # Calculate points earned based on syllabus weights
    points_earned = (
        (ice / 500) * 14
        + (exam1 / 60) * 10
        + (exam2 / 60) * 10
        + (final_exam / 100) * 20
        + (quiz / 40) * 1
        + (labs / 900) * 25
        + (hw / 400) * 10
    )
    
    # Scale the 90 available points up to a standard 100% scale
    final_percentage = (points_earned / 90) * 100

    print(f"\nFinal Percentage Score: {final_percentage:.2f}%")
    get_grade_range(final_percentage)

task1()
task2()
task3()
task4()
task5()
task8()
task9()