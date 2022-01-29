#each item in the list is a list
# grid 4 rows + 3 columns
number_grid = [
    [1, 2, 3], # row 0
    [4, 5, 6], # row 1
    [7, 8, 9], # row 2
    [0]]      # row 3

print(number_grid[0][0])

#nested forloop
number_grid = [
    [1, 2, 3], # row 0
    [4, 5, 6], # row 1
    [7, 8, 9], # row 2
    [0]]      # row 3

for row in number_grid:
    for col in row:
        print(col)
