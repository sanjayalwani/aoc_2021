import argparse
from collections import deque
parser = argparse.ArgumentParser("Given an input file, prints the solution")

parser.add_argument('file_name', type=str, help='Input file name')

def main():
    args = parser.parse_args()

    f = open(args.file_name, "r")

    matrix = []

    for line in f:
        matrix.append([int(num) for num in line.strip()])

    def getval(i,j):
        if i < 0 or i >= len(matrix): return None
        if j < 0 or j >= len(matrix[0]): return None

        return matrix[i][j]

    lowpoints = []
    for i, row in enumerate(matrix):
        for j, cell in enumerate(row):
            nbr = [getval(i-1,j), getval(i+1, j), getval(i,j-1), getval(i,j+1)]
            nbr = [(None if x == None else int(x)) for x in nbr]
            low = True
            for nb in nbr:
                if nb == None:
                    continue
                elif nb <= cell:
                    low = False
                    break
            if low == True:
                lowpoints.append((i, j))

    def getnbrs(i,j):
        nbr = [(i-1,j), (i+1, j), (i,j-1), (i,j+1)]
        return nbr
    # Basins of cardinality = lowpoints
    basinsscore = []
    for point in lowpoints:
        basum = 1
        seenlist = [point]
        searchq = deque()
        searchq.append(point)
        while len(searchq):
            curr = searchq.popleft()
            nbrs = getnbrs(*curr)
            for nbr in nbrs:
                if nbr in seenlist: continue
                val = getval(*nbr)
                if val == None: continue
                if val < 9:
                    basum += 1
                    searchq.append(nbr)
                    seenlist.append(nbr)
        basinsscore.append(basum)

    tops = sorted(basinsscore, reverse=True)
    print(tops)
    print(tops[0]*tops[1]*tops[2])

if __name__ == "__main__":
    main()
