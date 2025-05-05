#!/usr/bin/python3
import sys

# Iterate directly over arguments instead of using indices
for arg in sys.argv[1:]:  # sys.argv[0] is the script name, skip it if not needed
    print(arg)
