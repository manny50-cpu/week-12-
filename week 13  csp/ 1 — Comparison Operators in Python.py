# Objective:
# Students will learn how to compare values using Python’s comparison operators and interpret Boolean results.

# Topics Covered:
# ==, !=, >, <, >=, <=

# Key Notes:

# Comparison operators compare two values and return either True or False.

# Remember: = is assignment, while == is comparison.

a = 3
b = 4

print(a)
print(b)
print(a==5) #output is going to be false

print(a == b)   # False
print(a != b)   # True
print(a > b)    # False
print(a < b)    # True
print(a >= b)   # False
print(a <= b)   # True


#predict the output of the following comparisons:
10 > 5 #true
7 == 2 * 3 + 1 #true
8 != 8 #false
4 <= 2 + 2 #true

# Write 3 examples that result in True and 3 that result in False.
print(7<2) #false
print(5==4) #false
print(5!=4) #true
print(7+5 == 12) # true
print(5 == 5) #true
print(2<= 1) #false

# Create a simple grade-checking condition:

# practice problem :
# where a student must check if their score is greater than or equal to 60 to pass a test.# The password must be at least 8 characters long and contain at least one digit.password = "mypassword1"

score= int(input("What is your score?"))
if score>= 60:
    print("You passed the test")
else:
    print("You didnt pass")
password= input("What is your password?")
print(password)

grade= int(input("What is your percentage?"))

if grade>=90 & grade<=100:
    print("you got an A")
elif grade>=80 & grade<=89:
    print("You got a B")
elif grade>=70 & grade<=79:
    print("you got a c")
elif grade>=60 & grade<=69:
    print("You got a D")
else: 
    print("you got an F, come for aclab")