"""In a magic square, each row, each column, and both diagonals add up to the same number.
A partially filled magic square is shown below. Write a program to check through all the
possibilities to fill in the magic square.
5 _ _
_ 6 2
3 8 _"""

# Known numbers in the grid
used = {5, 6, 2, 3, 8}
for a in range(1, 11):
    if a in used:
        continue
    for b in range(1, 11):
        if b in used or b == a:
            continue
        for c in range(1, 11):
            if c in used or c == a or c == b:
                continue
            for d in range(1, 11):
                if d in used or d == a or d == b or d == c:
                    continue

                # Build grid
                grid = [
                    [5, a, b],
                    [c, 6, 2],
                    [3, 8, d]
                ]
                S = sum(grid[0])
                if sum(grid[1]) != S or sum(grid[2]) != S:
                    continue
                if (grid[0][0] + grid[1][0] + grid[2][0] != S or
                    grid[0][1] + grid[1][1] + grid[2][1] != S or
                    grid[0][2] + grid[1][2] + grid[2][2] != S):
                    continue
                if (grid[0][0] + grid[1][1] + grid[2][2] != S or
                    grid[0][2] + grid[1][1] + grid[2][0] != S):
                    continue
                for row in grid:
                    print(row)
                print("Magic sum:", S)
                exit()