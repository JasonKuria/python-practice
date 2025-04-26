# recursive function to find the sum of digits in a number
def fun(n):
    if n == 0:
        return 0  # base case
    # Recursive case:
    # Add the last digit (n % 10) to the result of fun(n // 10)
    # (which removes the last digit and continues)
    return (n % 10) + fun(n // 10)

n = 12345
#function call
print(fun(n))