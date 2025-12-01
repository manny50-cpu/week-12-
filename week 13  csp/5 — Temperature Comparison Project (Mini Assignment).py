# Objective:
# Apply comparison and logical operators to a real-world problem.

# Scenario:
# Write a program that:

# Asks the user for today’s temperature. 
temperature = float(input("What is the weather like?"))

# Prints whether it’s cold, warm, or hot using comparison operators.
if temperature>= 80 and temperature <=100:
    print("Its hot outside ")
elif temperature>=50 and temperature<=79:
     print("Its warm outside")
elif temperature <=-10 or temperature>=110:
     print("Extreme temperature warning")
else:
     print("its cold outside")

     
        
    

# If the temperature is out of range (below -10 or above 110), display “Extreme temperature warning!”

# Starter Code:

