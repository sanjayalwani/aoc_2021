import argparse

parser = argparse.ArgumentParser("Given an input file, prints the solution")

parser.add_argument('file_name', type=str, help='Input file name')

def main():
    args = parser.parse_args()

    f = open(args.file_name, "r")


    inputs = [int(x) for x in f.readline().split(',')]
    boards = []


    def make_row(board_string):
        return [int(x) for x in board_string.split()]
    while (f.readline()):
        bingoboard = []
        abort = False
        for i in range(5):
            tmp = f.readline()
            if (tmp == '\n'): abort = true
            bingoboard.append(make_row(tmp))
        if (abort): break
        boards.append(bingoboard)

    print('Boards initialized: ', len(boards))

    # for boolean board
    def isBingo(board):
        bingo = False
        for row in board:
            bingorow = True
            for cell in row:
                if not cell: bingorow = False
            if bingorow: return True
        for col in range(5):
            bingocol = True
            for row in board:
                if not row[col]: bingocol = False
            if bingocol: return True

    markers = []
    for b in range(len(boards)):
        markers.append([[False for x in range(5)] for y in range(5)])

    bingo = False
    winnerboard = None
    winnermarker = None
    winneraction = None
    for action in inputs:
        for board_index, board in enumerate(boards):
            for i, row in enumerate(board):
                for j, cell in enumerate(row):
                    if cell == action: markers[board_index][i][j] = True
                    # That's a lot of nested loops :#
            if isBingo(markers[board_index]):
                bingo = True
                print('board', board_index, ' wins')
                for row in board: print(row)
                for row in markers[board_index]: print(row)
                winnerboard = board
                winnermarker = markers[board_index]
                winneraction = action
                break

        if bingo: break

    unmarksum = 0
    for i in range(5):
        for j in range(5):
            if not winnermarker[i][j]: unmarksum += winnerboard[i][j]

    print('unmarked ', unmarksum)
    print('winning number', winneraction)
    print('sol', unmarksum*winneraction)

if __name__ == "__main__":
    main()
