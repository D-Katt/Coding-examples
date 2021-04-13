# There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].
# You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station
# to its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.
# Given two integer arrays gas and cost, return the starting gas station's index
# if you can travel around the circuit once in the clockwise direction, otherwise return -1.
# If there exists a solution, it is guaranteed to be unique

# Example 1:
# Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
# Output: 3
# Explanation:
# Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
# Travel to station 4. Your tank = 4 - 1 + 5 = 8
# Travel to station 0. Your tank = 8 - 2 + 1 = 7
# Travel to station 1. Your tank = 7 - 3 + 2 = 6
# Travel to station 2. Your tank = 6 - 4 + 3 = 5
# Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
# Therefore, return 3 as the starting index.

# Example 2:
# Input: gas = [2,3,4], cost = [3,4,3]
# Output: -1
# Explanation:
# You can't start at station 0 or 1, as there is not enough gas to travel to the next station.
# Let's start at station 2 and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
# Travel to station 0. Your tank = 4 - 3 + 2 = 3
# Travel to station 1. Your tank = 3 - 3 + 3 = 3
# You cannot travel back to station 2, as it requires 4 unit of gas but you only have 3.
# Therefore, you can't travel around the circuit once no matter where you start.

# Constraints:
# gas.length == n
# cost.length == n
# 1 <= n <= 104
# 0 <= gas[i], cost[i] <= 104

gas = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]


def find_starting_station(gas: list, cost: list):
    """Function returns starting station index for a circular route.
    If there is no such station, returns -1.
    """
    n_stations = len(gas)
    # Indexes of stations in correct order
    sequence = [i for i in range(n_stations)]
    # Iterate over all possible starting points
    for ind in range(n_stations):
        # Reset gas tank
        tank = 0
        negative_gas = False
        # Create a list of station indexes starting from current index
        # and ending with the same index
        cur_sequence = sequence[ind:]
        if ind == 0:  # If we started at 0, add 0 at the end
            cur_sequence += [sequence[0]]
        elif ind < n_stations - 1:  # If we started somewhere in between
            cur_sequence += sequence[:ind+1]
        else:  # If we started at the last index, add the whole original sequence
            cur_sequence += sequence
        # Iterate over the circle sequence
        for station in cur_sequence:
            tank += gas[station]
            tank -= cost[station]
            # Check gas level
            if tank < 0:
                negative_gas = True
                break
        # If we managed to complete the circle, return starting index
        if not negative_gas:
            return ind
    # Case where no starting point allows to complete the route
    return -1


print(find_starting_station(gas, cost))
