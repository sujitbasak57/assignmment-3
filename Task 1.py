def factorial(n):
    """Calculates the factorial of a given number using recursion."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Test the function with a sample number
if __name__ == "__main__":
    num = 5  # Change this number to test with different inputs
    result = factorial(num)
    print(f"The factorial of {num} is: {result}")
