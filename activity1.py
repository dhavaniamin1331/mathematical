# Program to find if a number is Armstrong number 

# Take input from the user number = int(input("Input your number: "))
number = int(input("Input yout number: "))

# Calculate number of digits 
digits = len(str(number))

# Initialize result varible
resultNumber = 0

# find the sum of a^digits of each digit 
temp = number 
while temp > 0:
    digit = temp % 10 
    resultNumber += digit  ** digits
    temp //= 10

# display the result 
if number == resultNumber:
    print(number,"is a Armstrong number")
else:
     print(number, "is not an Armstrong number")
     