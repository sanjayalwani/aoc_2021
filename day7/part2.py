import argparse

parser = argparse.ArgumentParser("Given an input file, prints the solution")

parser.add_argument('file_name', type=str, help='Input file name')

def main():
    args = parser.parse_args()

    f = open(args.file_name, "r")

    hpos = [int(x) for x in f.readline().split(',')]

    mean = int(sum(hpos)/len(hpos))
    median = hpos[int(len(hpos)/2)]
    learnrate = 1

    endlearning = False

    def calcCost(positions, dest):
        cost = 0
        for pos in positions:
            dist = abs(pos - dest)
            poscost = dist * (dist + 1) / 2
            cost += poscost
        return cost

    epoch = 1
    meancost = calcCost(hpos, mean)
    while (not endlearning):
        shiftup = mean + 1
        shiftdown = mean - 1
        upcost = calcCost(hpos, shiftup)
        dncost = calcCost(hpos, shiftdown)
        if (upcost < meancost):
            meancost = upcost
            mean = shiftup
        elif (dncost < meancost):
            meancost = dncost
            mean = shiftdown
        else:
            endlearning = True
        epoch += 1
    print('best cost is:', meancost)
    print('mean is:', mean)
    print('epoch', epoch)
if __name__ == "__main__":
    main()
