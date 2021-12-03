import argparse

parser = argparse.ArgumentParser("Given an input file, prints the solution")

parser.add_argument('file_name', type=str, help='Input file name')

def main():
    args = parser.parse_args()

    f = open(args.file_name, "r")

    count = 0

    firstline = f.readline()
    one_counts = [int(x) for x in firstline[:-1]]
    print('one_counts', one_counts)
    n = len(one_counts)
    for line in f:
        i = 0
        for char in line[:-1]:
            if(int(char)): one_counts[i] += 1
            i += 1
        count += 1
    print('one_counts', one_counts)
    gamma_bits = [1 if one_counts[i] > count/2 else 0 for i in range(n)]
    print('gamma_bits', gamma_bits)
    gamma = 0;
    for i in range(n):
        gamma += gamma_bits[i]*2**(n-i-1)

    maxint = 2**n - 1
    epsilon = maxint - gamma
    print('gamma', gamma)
    print('epsilon', epsilon)
    print('sol', gamma*epsilon)

if __name__ == "__main__":
    main()
