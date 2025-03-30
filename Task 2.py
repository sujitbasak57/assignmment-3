import math

def calculate_math_operations():
    try:
        # Taking user input
        num = float(input("Enter a number: "))

        # Calculating using math module
        sqrt_value = math.sqrt(num)
        log_value = math.log(num)  # Natural logarithm (base e)
        sine_value = math.sin(num)  # Sine of the number (in radians)

        # Displaying results
        print(f"Square root of {num}: {sqrt_value}")
        print(f"Natural logarithm of {num}: {log_value}")
        print(f"Sine of {num} (in radians): {sine_value}")

    except ValueError:
        print("Error: Please enter a valid positive number.")

# Run the function
if __name__ == "__main__":
    calculate_math_operations()
