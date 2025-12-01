# Objective:
# Apply comparison and logical operators to a real-world problem.

# Scenario:
# Write a program that:

# Asks the user for today’s temperature.

# Prints whether it’s cold, warm, or hot using comparison operators.

# If the temperature is out of range (below -10 or above 110), display “Extreme temperature warning!”

# Starter Code:
temp = int(input("What is today's temperature?"))
if temp >= 80 and temp <= 100:
    print("It is very hot outside, please dress appropriately.")
elif temp > 110 or temp < -10:
    print("Extreme temperature warning! It is advised to not go outside until further notice, as the temperature is dangerous.")
elif temp >= 0 and temp <= 32:
    print("It is very cold outside. Depending on the lower temperature, you may need to dress warmer.")
elif temp >= 50 and temp <= 79:
    print("It is warm out. Depending on if it is warmer than 60, be advised to wear lighter clothes.")
    
