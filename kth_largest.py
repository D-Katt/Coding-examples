# Given an integer array nums and an integer k, return the kth largest element in the array.
# Note that it is the kth largest element in the sorted order, not the kth distinct element.

# Example 1:
# Input: nums = [3,2,1,5,6,4], k = 2
# Output: 5

# Example 2:
# Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
# Output: 4

# Constraints:
# 1 <= k <= nums.length <= 104
# -104 <= nums[i] <= 104

from collections import Counter


def kth_largest(arr: list, k: int):
    """Function returns k-th largest element of the array arr.
    """
    # Do not search if k is larger than total number of elements
    if k > len(arr):
        raise IndexError
    # Count all numbers
    nums = Counter(arr)
    # Go from the largest to smaller ones
    for key in sorted(nums, reverse=True):
        if nums[key] >= k:
            return key
        else:
            k -= nums[key]


nums = [3, 2, 1, 5, 6, 4]
k = 2
print(kth_largest(nums, k))

nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
k = 4
print(kth_largest(nums, k))
