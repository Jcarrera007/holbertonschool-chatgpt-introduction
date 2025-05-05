#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1  # Correction: decrement n to avoid infinite loop
    return result

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <integer>")
        sys.exit(1)

    try:
        num = int(sys.argv[1])
        if num < 0:
            raise ValueError("Negative numbers don't have factorials.")
    except ValueError as ve:
        print(f"Error: {ve}")
        sys.exit(1)

    f = factorial(num)
    print(f)
