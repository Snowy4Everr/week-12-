# Objective:
# Students will use logical (and, or, not) and chained comparison operators in Python to build compound conditions.

# Key Notes:

# and → Both conditions must be True

# or → At least one condition must be True

# not → Inverts True/False

# You can chain comparisons: 1 < x < 5

# Examples:
x = 10
print(x > 5 and x < 15)   # True
print(x < 5 or x == 10)   # True
print(not(x == 10))       # False
print(1 < x < 20)         # True


# Practice Problems:

# Write an expression that checks if a number is between 50 and 100 (inclusive).
number = 60
print(number >= 50 and number <= 100)
# Write an expression that checks if a number is NOT equal to 0 and greater than 10.
num = 15
print(not(num == 0) and num > 10)
# Use chained comparison to check if 3 < 4 < 5.
print(3 < 4 < 5)
# Challenge: Create a password rule using logical operators:

password = input("what is your password?")
if len(password) >= 8 and any(char.isdigit() for char in password):
    print("Password is valid.")

else:
    print("Password is invalid" \
    "It must be at least 8 characters long and contain at least one digit.")