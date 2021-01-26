# Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.

# Example 1:
# Input: [[1, 1], [2, 2], [3, 3]]
# Output: 3

# Example 2:
# Input: [[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]
# Output: 4

# We need to check linear regression slope and intercept and vertical lines
# starting from each pair of points.

coordinates = [[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]

max_points = 0

# Iterate through coordinates in three nested loops.
for i in range(len(coordinates)):

    # First two points are used to benchmark slope and intercept for next points.
    x1, y1 = coordinates[i]
    for j in range(i + 1, len(coordinates)):
        x2, y2 = coordinates[j]

        # Vertical line
        if x1 == x2:
            vert_line_points = 2
            slope = None
            intercept = None

        # Regression line
        else:
            vert_line_points = 1
            # First two points are always on a same line.
            regr_line_points = 2
            slope = (y2 - y1) / (x2 - x1)
            intercept = y1 - slope * x1

        # For each next point calculate slope and intercept and compare with the benchmark.
        for z in range(j + 1, len(coordinates)):
            next_x, next_y = coordinates[z]
            if next_x == x1:
                vert_line_points += 1
            else:
                next_slope = (next_y - y1) / (next_x - x1)
                next_intercept = next_y - next_slope * next_x
                if next_slope == slope and next_intercept == intercept:
                    regr_line_points += 1

        # Update maximum value.
        if vert_line_points > max_points:
            max_points = vert_line_points
        if regr_line_points > max_points:
            max_points = regr_line_points

print(max_points)
