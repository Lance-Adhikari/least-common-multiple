def lcm_simple(a, b):
    # The LCM cannot be smaller than either positive input.
    number = max(a, b)

    while True:
        # The first number divisible by both inputs is their LCM.
        if number % a == 0 and number % b == 0:
            return number
        else:
            number += 1


# Read two positive integers.
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

print("Answer: " + str(lcm_simple(a, b)))
