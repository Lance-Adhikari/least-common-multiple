def gcd(a, b):
    # Repeat until the second number becomes zero.
    while b != 0:
        remainder = a % b

        # Replacing (a, b) with (b, remainder) preserves their GCD.
        a = b
        b = remainder

    # The last nonzero value is the GCD for positive inputs.
    return a


def lcm(a, b):
    small_number = min(a, b)
    bigger_number = max(a, b)
    # Use LCM(a, b) = a * b / GCD(a, b), dividing before multiplying.
    answer = (small_number // gcd(a, b)) * bigger_number
    return answer


# Read two positive integers.
a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))

print("LCM =", lcm(a, b))
