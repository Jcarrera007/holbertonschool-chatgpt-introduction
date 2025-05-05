#!/usr/bin/python3
import sys

def factorial(n):
    if n == 0:
        return 1
    elif n < 0:
        raise ValueError("Factorial is undefined for negative numbers.")
    else:
        return n * factorial(n - 1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <non-negative integer>")
        sys.exit(1)
    
    try:
        num = int(sys.argv[1])
        result = factorial(num)
        print(result)
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)
    except RecursionError:
        print("Error: Number too large.")
        sys.exit(1)

