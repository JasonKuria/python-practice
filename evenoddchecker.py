
# Ask the user to enter a number then change to integer
num = int(input("Enter a number: "))

# Check if the number is divisible by 2
if (num % 2) == 0:
# If divisible, print that the number is Even
   print("{0} is Even".format(num))
else:
    # If not divisible, print that the number is Odd
   print("{0} is Odd".format(num))