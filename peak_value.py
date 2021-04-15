# A peak element is an element that is strictly greater than its neighbors.
# Given an integer array nums, find a peak element, and return its index.
# If the array contains multiple peaks, return the index to any of the peaks.
# You may imagine that nums[-1] = nums[n] = -∞.

# Example 1:
# Input: nums = [1,2,3,1]
# Output: 2
# Explanation: 3 is a peak element and your function should return the index number 2.

# Example 2:
# Input: nums = [1,2,1,3,5,6,4]
# Output: 5
# Explanation: Your function can return either index number 1 where the peak element is 2,
# or index number 5 where the peak element is 6.

# Constraints:
# 1 <= nums.length <= 1000
# -231 <= nums[i] <= 231 - 1
# nums[i] != nums[i + 1] for all valid i.

# Follow up: Could you implement a solution with logarithmic complexity?

from sys import maxsize


def find_peak(arr: list, start_idx: int, end_idx: int, right_bound: int, both_neighbors=True):
    """Function returns an index of the element,
    which is greater than both its neighbours.
    Otherwise returns -1.
    :argument arr: original array of integers
    :argument start_idx: starting index for the current segment
    :argument end_idx: ending index for the current segment
    :argument right_bound: last index of the original array
    :argument both_neighbors: Boolean argument to include or not include peaks
    at the ends of array, which have only one neighbor
    :return Integer index of the first found peak value or -1
    """

    # If we are searching for peaks including border elements
    if not both_neighbors:
        arr = [-maxsize] + arr + [-maxsize]  # Append -∞ at both ends
        end_idx += 2  # Increase ending index and right bound
        right_bound += 2

    # List containing 1 element (current peak value)
    index = [-1]

    def peak_index(start_idx: int, end_idx: int):
        """Function recursively searches for peak value using middle position
        between two indexes.
        """
        # Middle position in the current segment
        middle = (start_idx + end_idx) // 2
        # Check that current middle position is not the 1st or last in the original arr
        if middle == 0 or middle == right_bound:
            return
        # Peak value (any peak, not the largest one)
        if arr[middle] > arr[middle - 1] and arr[middle] > arr[middle + 1]:
            index[0] = middle
            return
        # If peak is still not found, call this function for two segments
        if index[0] == -1 and (middle - start_idx) > 1:
            peak_index(start_idx, middle)
        if index[0] == -1 and (end_idx - middle) > 1:
            peak_index(middle, end_idx)

    peak_index(start_idx, end_idx)

    # Correct the index if we previously appended -∞ to the original arr
    if not both_neighbors and index[0] != -1:
        index[0] -= 1

    return index[0]


for nums in [[1, 2, 3, 1], [1, 2, 1, 3, 5, 6, 4], [1, 2, 3, 4, 5, 6], [2, 2, 2], [8, 5, 3]]:
    print('-' * 40)
    print(nums)
    n_elements = len(nums)

    index = find_peak(nums, start_idx=0, end_idx=n_elements - 1, right_bound=n_elements)
    print('Peak index (strictly two neighbors):', index)

    index = find_peak(nums, start_idx=0, end_idx=n_elements - 1, right_bound=n_elements, both_neighbors=False)
    print('Peak index (two neighbors or one for border elements):', index)
