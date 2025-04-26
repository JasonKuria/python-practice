#calculating facotrials using recursion
def recur_factorial(n):
    #form a base case whre if n=1 , return 1
   if n == 1:
       return n
   else:
       # Recursive case: n times factorial of (n-1)
       return n*recur_factorial(n-1)
# Initialize the number whose factorial we want to find
num = 7

# check if the number is negative
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
   # Check if the number is 0
elif num == 0:
   print("The factorial of 0 is 1")
else:
    # If the number is positive, calculate and print its factorial
   print("The factorial of", num, "is", recur_factorial(num))