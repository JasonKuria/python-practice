# Python program to find the factorial of a number

# Initialize whatever number whose factorial should be found
num = 7
factorial = 1
# Check if the number is negative
if num < 0:
    # Facorial does not exist for negativ numbers,
   print("Sorry, factorial does not exist for negative numbers")
    # Check if the number is 0
elif num == 0:
    # The factorial of 0 is 1 by definition
   print("The factorial of 0 is 1")
else:
    # Calculate the factorial for positive numbers
   for i in range(1,num + 1):
       # Multiply factorial by each numbe from 1 to num
       factorial = factorial*i
       # Print the final result
   print("The factorial of",num,"is",factorial)