import argparse

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

    risklev = 0
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
                risklev += 1 + cell
    print(risklev)
if __name__ == "__main__":
    main()
