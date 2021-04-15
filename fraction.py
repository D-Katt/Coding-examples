# Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.
# If the fractional part is repeating, enclose the repeating part in parentheses.
# If multiple answers are possible, return any of them.
# It is guaranteed that the length of the answer string is less than 104 for all the given inputs.

# Example 1:
# Input: numerator = 1, denominator = 2
# Output: "0.5"

# Example 2:
# Input: numerator = 2, denominator = 1
# Output: "2"

# Example 3:
# Input: numerator = 2, denominator = 3
# Output: "0.(6)"

# Example 4:
# Input: numerator = 4, denominator = 333
# Output: "0.(012)"

# Example 5:
# Input: numerator = 1, denominator = 5
# Output: "0.2"

# Constraints:
# -231 <= numerator, denominator <= 231 - 1
# denominator != 0


def fraction(n: int, m: int):
    """Function divides n by m and returns a string
    with the resulting fraction enclosing
    repeating part in parentheses.
    """
    fr = str(n / m)
    integer, decimal = fr.split('.')
    # Check for repeating digits
    repeating = ''
    seen = set()
    # Iterate over decimal part
    for num in decimal:
        # Add new numbers to set and pattern string
        if num not in seen:
            repeating += num
            seen.add(num)
        # If we see the same number, check the pattern
        else:
            # If we can reconstruct decimal string by repeating this pattern,
            # update decimal string and break the cycle
            len_repeating = len(repeating)
            n_repeats = len(decimal) // len_repeating
            if n_repeats * repeating == decimal[:n_repeats * len_repeating]:
                decimal = f'({repeating})'
                break
    # Join two parts of the fraction
    if decimal != '0':
        return integer + '.' + decimal
    else:
        return integer


for n, m in ((1, 2), (2, 1), (2, 3), (4, 333), (1, 5)):
    print(n, '/', m, '=', fraction(n, m))
