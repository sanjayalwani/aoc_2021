import argparse
from collections import deque

parser = argparse.ArgumentParser("Given an input file, prints the solution")

parser.add_argument('file_name', type=str, help='Input file name')
parser.add_argument('days', type=int, help='Number of days')

def main():
    args = parser.parse_args()

    growthrate = 7
    f = open(args.file_name, "r")
    initial = [int(x) for x in f.readline().split(',')]

    days = args.days
    buckets = deque([0 for x in range(9)])

    for time in initial:
        buckets[time] += 1

    for i in range(days):
        newfish = buckets[0]
        buckets.rotate(-1)
        buckets[6] += newfish


    print('Final count at day', days, 'is', sum(buckets))
if __name__ == "__main__":
    main()
