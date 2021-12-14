"""Advent of code: https://adventofcode.com/2021/day/3
Day 3 Puzzle 2
You should verify the life support rating, which can be determined by multiplying
the oxygen generator rating by the CO2 scrubber rating.
Both the oxygen generator rating and the CO2 scrubber rating are values
that can be found in the diagnostic report by filtering out values until only one remains.
Start with the full list of binary numbers from your diagnostic report
and consider just the first bit of those numbers. Then:
- Keep only numbers selected by the bit criteria for the type of rating value
  for which you are searching. Discard numbers which do not match the bit criteria.
- If you only have one number left, stop; this is the rating value for which you are searching.
- Otherwise, repeat the process, considering the next bit to the right.
The bit criteria depends on which type of rating value you want to find:
- To find oxygen generator rating, determine the most common value (0 or 1) in the current bit position,
  and keep only numbers with that bit in that position. If 0 and 1 are equally common,
  keep values with a 1 in the position being considered.
- To find CO2 scrubber rating, determine the least common value (0 or 1) in the current bit position,
  and keep only numbers with that bit in that position. If 0 and 1 are equally common,
  keep values with a 0 in the position being considered.
Use the binary numbers in your diagnostic report  to calculate the oxygen generator rating
and CO2 scrubber rating, then multiply them together. (Be sure to represent your answer in decimal, not binary.)
"""

file_path = 'day_3_data.txt'

# Read all binary numbers as a list.
with open(file_path, 'r') as file_handler:
    data = file_handler.readlines()

oxygen_list = data.copy()
co2_list = data.copy()


def select_number(sequence: list, most_freq: bool = True) -> str:
    """Function selects one number from a sequence of binary numbers
    based on most frequent or least frequent numbers in each index position.
    :param sequence: List of binary numbers
    :param most_freq: Selection criteria (if True - select the most frequent,
    if False - select the least frequent value)
    :return: String containing selected number
    """
    n_chars = len(sequence[0].strip())

    for i in range(n_chars):
        # Count zeroes and ones in the current index position.
        counter = [0, 0]
        for num in sequence:
            counter[int(num[i])] += 1

        # Find the most frequent value
        if counter[0] == counter[1]:
            freq_criteria = '1'
        else:
            freq_criteria = '0' if counter[0] > counter[1] else '1'

        # Update the list.
        if most_freq:
            sequence = list(filter(lambda x: x[i] == freq_criteria, sequence))
        else:
            sequence = list(filter(lambda x: x[i] != freq_criteria, sequence))

        if len(sequence) == 1:
            break

    return sequence[0]


oxygev_value = select_number(oxygen_list)
co2_value = select_number(co2_list, most_freq=False)

# Convert to integers and multiply.
oxygev_value = int(oxygev_value, 2)
co2_value = int(co2_value, 2)

mtpl = oxygev_value * co2_value
print(mtpl)
