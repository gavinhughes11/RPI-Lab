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