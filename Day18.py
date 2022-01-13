def main():
    lines = []
    with open('day18.txt') as f:
        lines = f.readlines()

    for i in range(0, len(lines)):
        lines[i] = lines[i].strip()

    grid = []
    for line in lines:
        row = []
        for char in line:
            row.append(char)
        grid.append(row)


    numRows = len(grid)
    numCols = len(grid[0])
    numIterations = 100
    for iteration in range(numIterations):
        newGrid = [["." for x in range(numCols)] for y in range(numRows)]
        for row in range(numRows):
            for col in range(numCols):
                numNeighbors = 0

                if row > 0:
                    if grid[row - 1][col] == "#":
                        numNeighbors += 1
                if col > 0:
                    if grid[row][col - 1] == "#":
                        numNeighbors += 1
                if row < numRows - 1:
                    if grid[row + 1][col] == "#":
                        numNeighbors += 1
                if col < numCols - 1:
                    if grid[row][col + 1] == "#":
                        numNeighbors += 1
                if row > 0 and col > 0:
                    if grid[row - 1][col - 1] == "#":
                        numNeighbors += 1
                if row > 0 and col < numCols - 1:
                    if grid[row - 1][col + 1] == "#":
                        numNeighbors += 1
                if row < numRows - 1 and col > 0:
                    if grid[row + 1][col - 1] == "#":
                        numNeighbors += 1
                if row < numRows - 1 and col < numCols - 1:
                    if grid[row + 1][col + 1] == "#":
                        numNeighbors += 1

                if grid[row][col] == "#":
                    if numNeighbors == 2 or numNeighbors == 3:
                        newGrid[row][col] = "#"
                else:
                    if numNeighbors == 3:
                        newGrid[row][col] = "#"

        newGrid[0][0] = "#"
        newGrid[0][numCols - 1] = "#"
        newGrid[numRows - 1][0] = "#"
        newGrid[numRows - 1][numCols - 1] = "#"
        grid = newGrid



    numOn = 0
    for row in range(numRows):
        for col in range(numCols):
            if grid[row][col] == "#":
                numOn += 1
    print(numOn)




if __name__ == "__main__":
    main()