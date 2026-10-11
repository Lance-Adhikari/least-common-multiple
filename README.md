# Least Common Multiple

Two Python approaches to finding the least common multiple (LCM) of two positive integers. The LCM is the smallest positive number divisible by both inputs. For example, **lcm(6, 8) = 24**.

## Solutions

- [LCM_Easy.py](LCM_Easy.py): Starts at the larger input and checks each number until it finds one divisible by both.
- [LCM_Efficient.py](LCM_Efficient.py): Finds the GCD using the Euclidean algorithm, then calculates the LCM using `a * b / gcd(a, b)`. Integer division happens before multiplication.

Both scripts prompt for two positive integers and print their LCM.
