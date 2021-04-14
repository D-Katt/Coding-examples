# Given a string s containing only digits, return all possible valid IP addresses
# that can be obtained from s. You can return them in any order.
# A valid IP address consists of exactly four integers, each integer is between 0 and 255,
# separated by single dots and cannot have leading zeros.
# For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses
# and "0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses.


# Example 1:
# Input: s = "25525511135"
# Output: ["255.255.11.135","255.255.111.35"]

# Example 2:
# Input: s = "0000"
# Output: ["0.0.0.0"]

# Example 3:
# Input: s = "1111"
# Output: ["1.1.1.1"]

# Example 4:
# Input: s = "010010"
# Output: ["0.10.0.10","0.100.1.0"]

# Example 5:
# Input: s = "101023"
# Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]

# Constraints:
# 0 <= s.length <= 3000
# s consists of digits only.


def check_number(number: str):
    """Function check a segment of IP address.
    """
    # Leading zeros
    if number[0] == '0' and len(number) > 1:
        return False
    # Correct range
    num = int(number)
    if 0 <= num <= 255:
        return True
    # Incorrect range
    else:
        return False


def ip_addresses(inp_nums: str) -> list:
    """Function generates IP addresses from a given string
    that contains digits. If no address could be generated,
    returns and empty list.
    :argument inp_nums: String of digits
    :return List of strings with all possible IP addresses
    """

    # List to add valid IPs
    ips = []

    def dfs(remaining_s: str, prev_nums: list) -> tuple:
        """Function generates IP addresses from remaining part of the string.
        :argument remaining_s: End of string without the starting segment already used
        :argument prev_nums: List with all valid IPs from the beginning of the original string
        :returns A tuple with a boolean value and a list of valid IP strings
        """
        # If there are no more characters remaining in the string,
        # it means all previous characters were used in valid numbers.
        if len(remaining_s) == 0:
            return True, prev_nums
        # Numbers (1-3 digits long) starting from the beginning of the remaining string
        for i in range(1, 4):
            sub_s = remaining_s[:i]
            # If the number is valid, call this function
            # with the remaining part of the string and update current IP
            if check_number(sub_s):
                result, valid_ips = dfs(remaining_s[i:], prev_nums + [sub_s])
                # Check that we did not exceed 4 numbers and reached the end of original string
                if len(valid_ips) == 4 and result:
                    # Point of success
                    ips.append('.'.join(valid_ips))
                    return True, prev_nums
        # Impossible to create IP address
        return False, []

    _, _ = dfs(inp_nums, [])
    return ips


for s in ['25525511135', '0000', '1111', '010010', '101023']:
    print('-' * 50)
    print('Input:', s)
    print('Output:', ip_addresses(s))
