import argparse

parser = argparse.ArgumentParser("Given an input file, prints the solution")

parser.add_argument('file_name', type=str, help='Input file name')

def main():
    args = parser.parse_args()

    f = open(args.file_name, "r")

    count = 0

    for line in f:
        fourdig = line.split('|')[1].strip().split(' ')
        for dig in fourdig:
            if len(dig) in [2,3,4,7]: count += 1

    print(count)
if __name__ == "__main__":
    main()
