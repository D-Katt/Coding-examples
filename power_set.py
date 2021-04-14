# Given an integer array nums that may contain duplicates, return all possible subsets (the power set).
# The solution set must not contain duplicate subsets. Return the solution in any order.

# Example 1:
# Input: nums = [1,2,2]
# Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

# Example 2:
# Input: nums = [0]
# Output: [[],[0]]

# Constraints:
# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10


def combinations(cur_seq, prev_combinations: set):
    """Function returns subsequences of elements in cur_seq
    from 1 element to len(cur_seq) elements and updated set
    of all seen combinations of numbers.
    """
    result = []
    for i in range(1, len(cur_seq) + 1):
        cur_combination = cur_seq[0:i]
        key = tuple(cur_combination)
        if key not in prev_combinations:
            result.append(cur_combination)
            prev_combinations.add(key)
    return result, prev_combinations


def power_set(seq: list):
    """Function returns all possible combinations of numbers
    in seq without duplicates.
    """
    # Sort the original sequence in an ascending order
    seq = sorted(seq)
    # List to add combinations
    result = [[]]
    # Set to keep track of already added combinations
    seen_combinations = set()
    # Call combinations() function for all sub-sequences,
    # starting from 1st, 2nd ... n-th element of seq.
    for i in range(len(seq)):
        cur_result, seen_combinations = combinations(seq[i:], seen_combinations)
        result.extend(cur_result)
    return result


nums = [-8, -6, -8, 0, 1, 1, 2, 3, 3, 4]

print(power_set(nums))
