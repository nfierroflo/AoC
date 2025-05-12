import os

def count_xmas_in_grid(grid, word="XMAS"):
    rows = len(grid)
    cols = len(grid[0])
    word_len = len(word)
    count = 0
    # Directions: (dx, dy)
    directions = [
        (0, 1),   # right
        (0, -1),  # left
        (1, 0),   # down
        (-1, 0),  # up
        (1, 1),   # down-right
        (1, -1),  # down-left
        (-1, 1),  # up-right
        (-1, -1), # up-left
    ]
    for i in range(rows):
        for j in range(cols):
            for dx, dy in directions:
                found = True
                for k in range(word_len):
                    ni = i + dx * k
                    nj = j + dy * k
                    if not (0 <= ni < rows and 0 <= nj < cols):
                        found = False
                        break
                    if grid[ni][nj] != word[k]:
                        found = False
                        break
                if found:
                    count += 1
    return count

def count_x_mas(grid):
    rows = len(grid)
    cols = len(grid[0])
    count = 0
    patterns = [("MAS", "MAS"), ("MAS", "SAM"), ("SAM", "MAS"), ("SAM", "SAM")]
    for i in range(1, rows-1):
        for j in range(1, cols-1):
            if grid[i][j] != 'A':
                continue
            # Diagonals
            diag1 = grid[i-1][j-1] + grid[i][j] + grid[i+1][j+1]
            diag2 = grid[i-1][j+1] + grid[i][j] + grid[i+1][j-1]
            for p1, p2 in patterns:
                if diag1 == p1 and diag2 == p2:
                    count += 1
    return count

def text2grid(text):
    with open(text, 'r') as file:
        return [line.strip() for line in file if line.strip()]

if __name__ == "__main__":
    
    current_dir = os.path.dirname(os.path.abspath(__file__))
    input_file = os.path.join(current_dir, "input.txt")

    grid = text2grid(input_file)

    print(f"Part 1: {count_xmas_in_grid(grid)}")
    print(f"Part 2: {count_x_mas(grid)}")
