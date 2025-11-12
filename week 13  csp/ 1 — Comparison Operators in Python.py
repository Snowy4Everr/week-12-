# Objective:
# Students will learn how to compare values using Python’s comparison operators and interpret Boolean results.

# Topics Covered:
# ==, !=, >, <, >=, <=

# Key Notes:

# Comparison operators compare two values and return either True or False.

# Remember: = is assignment, while == is comparison.

a = 3
b = 4
print(a) #output of 3
print(b) #output of 4

print(a == b)   # False #checks for equality
print(a != b)   # True #checks if it is not equal
print(a > b)    # False #checks for greater than
print(a < b)    # True #checks for less than
print(a >= b)   # False #checks for greater than or equal to
print(a <= b)   # True #checks for less than or equal to


#predict the output of the following comparisons:
10 > 5 #output True
7 == 2 * 3 + 1 #output True
8 != 8 #output False
4 <= 2 + 2 #output True

# Write 3 examples that result in True and 3 that result in False.
2 >= 2 #output True
1 > 9 #output False
4 + 4 == 8 #output True
2 * 5 == 11 #output False
3 < 6 #output True
9 <= 1 #output False
# Create a simple grade-checking condition:

# practice problem :
# where a student must check if their score is greater than or equal to 60 to pass a test.# The password must be at least 8 characters long and contain at least one digit.password = "mypassword1"
# # the password must be at least 8 characters long
#and contain at least one digit.password = "mypassword1"

#asking student score
score = int(input("What is your score?"))
## & is an "and" operator

#if the score is between 90 - 100, you got an A
if score >= 90 and score <=100:
    print("You got an A!")
#if the score is between 80 - 89, you got a B
elif score >=80 and score <=89:
    print("You got a B.")
#if the score is between 70 - 79, you got a C
elif score >=70 and score <=79:
    print("You got a C.")
#if the score is betwen 61 - 69, you got a D
elif score >=60 and score <=69:
    print("You got a D.")
else:
    print("You failed, come for ACLAB.")
if score >= 60:
    print("You passed the test.")
else:
    print("You didn't pass the test.")

#ask for a password
password = input("what is your password?")
if len(password) >= 8 and any(char.isdigit() for char in password):
    print("Password is valid.")

else:
    print("Password is invalid" \
    "It must be at least 8 characters long and contain at least one digit.")