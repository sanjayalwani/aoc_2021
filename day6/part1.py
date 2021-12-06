import argparse

parser = argparse.ArgumentParser("Given an input file, prints the solution")

parser.add_argument('file_name', type=str, help='Input file name')
parser.add_argument('days', type=int, help='Number of days')

def main():
    args = parser.parse_args()

    growthrate = 7
    f = open(args.file_name, "r")
    initial = [int(x) for x in f.readline().split(',')]

    days = args.days
    for i in range(days):
        newfish = []
        for idx in range(len(initial)):
            tmr = initial[idx]
            if tmr == 0: newfish.append(8)
            initial[idx] -= 1
            if initial[idx] < 0: initial[idx] = 6
        initial.extend(newfish)


    print('Final count at day', days, 'is', len(initial))
if __name__ == "__main__":
    main()
