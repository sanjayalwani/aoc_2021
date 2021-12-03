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
    linesarr = [firstline]
    linesbackup = [firstline]
    for line in f:
        i = 0
        linesarr.append(line)
        linesbackup.append(line)
        for char in line[:-1]:
            if(int(char)): one_counts[i] += 1
            i += 1
        count += 1
    print('one_counts', one_counts)
    gamma_bits = [1 if one_counts[i] >= count/2 else 0 for i in range(n)]
    print('gamma_bits', gamma_bits)

    mcb = gamma_bits[0]
    pos = 0
    while (len(linesarr) > 1):
        removals = []
        nbc = 0
        for i in range(len(linesarr)):
            if (linesarr[i][pos] != str(mcb)): removals.append(i)
            else:
                if (int(linesarr[i][(pos + 1) % (n - 1)])): nbc += 1
        pos = pos + 1 % n
        print('number to remove out of', len(linesarr), ' is ', len(removals))
        for i in reversed(removals):
            del linesarr[i]
        print('oxygen pos', pos)

        if (nbc>=len(linesarr)/2):
            mcb = 1
        else:
            mcb = 0
        print('next mcb is' , mcb , 'with nbc', nbc)
    oxgen = linesarr[0]

    lcb = 1 - gamma_bits[0]
    pos = 0
    while (len(linesbackup) > 1):
        removals = []
        nbc = 0
        for i in range(len(linesbackup)):
            if (linesbackup[i][pos] != str(lcb)): removals.append(i)
            else:
                if (int(linesbackup[i][(pos + 1) % (n-1)])): nbc += 1
        pos = pos + 1 % n
        for i in reversed(removals):
            del linesbackup[i]

        if (nbc>=len(linesbackup)/2):
            lcb = 0
        else:
            lcb = 1
    cogen = linesbackup[0]
    print('oxygen', oxgen)
    print('cogen', cogen)
    ox = 0
    co = 0
    for i in range(n):
        ox += int(oxgen[i])*2**(n-i-1)
        co += int(cogen[i])*2**(n-i-1)

    print('ox,co', ox, co)
    print('sol', ox*co)
if __name__ == "__main__":
    main()
