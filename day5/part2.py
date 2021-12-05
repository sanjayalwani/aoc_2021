import argparse

parser = argparse.ArgumentParser("Given an input file, prints the solution")

parser.add_argument('file_name', type=str, help='Input file name')

def main():
    args = parser.parse_args()

    f = open(args.file_name, "r")
    maxcoords = [0, 0]
    linesegments = []
    for line in f:
        orig, dest = line.split(' -> ')
        orig = [int(x) for x in orig.split(',')]
        dest = [int(y) for y in dest.split(',')]
        if (orig[0] > maxcoords[0]): maxcoords[0] = orig[0]
        if (orig[1] > maxcoords[1]): maxcoords[1] = orig[1]
        if (dest[0] > maxcoords[0]): maxcoords[0] = dest[0]
        if (dest[1] > maxcoords[1]): maxcoords[1] = dest[1]
        linesegments.append((orig, dest))

    grid = [[0 for x in range(maxcoords[0]+1)] for y in range(maxcoords[1]+1)]
    print('grid from 0,0 to ', maxcoords)

    for lineseg in linesegments:
        orig, dest = lineseg
        if(orig[0] == dest[0]):
            # x coord is same
            x = orig[0]
            ymin = min(orig[1], dest[1])
            ymax = max(orig[1], dest[1]) + 1
            for y in range(ymin, ymax):
                grid[y][x] += 1
        elif(orig[1]==dest[1]):
            # y coord same
            y = orig[1]
            xmin = min(orig[0], dest[0])
            xmax = max(orig[0], dest[0]) + 1
            for x in range(xmin, xmax):
                grid[y][x] += 1
        else:
            # diagonal
            x, y = orig
            xd, yd = dest
            diff = abs(xd - x) + 1
            delx = 1 if xd > x else -1
            dely = 1 if yd > y else -1
            for numberofiterations in range(diff):
                grid[y][x] += 1
                y += dely
                x += delx

    for line in grid:
        print(line)
    count = 0
    for row in grid:
        for cell in row:
            if cell > 1: count += 1

    print(count)
if __name__ == "__main__":
    main()
