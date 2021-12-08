import argparse

parser = argparse.ArgumentParser("Given an input file, prints the solution")

parser.add_argument('file_name', type=str, help='Input file name')

def main():
    args = parser.parse_args()

    f = open(args.file_name, "r")

    count = 0
    sumans = 0
    for line in f:
        digboard = [None for x in range(7)]
        signals = line.split('|')[0].strip().split(' ')
        fourdig = line.split('|')[1].strip().split(' ')
        digits = {"sixes": [], "fives": []}
        for dig in signals:
            if len(dig) == 3: digits["seven"] = dig
            if len(dig) == 2: digits["one"] = dig
            if len(dig) == 6: digits["sixes"].append(dig)
            if len(dig) == 5: digits["fives"].append(dig)

        top = next(iter(set(digits["seven"]) - set(digits["one"])))
        topright = None
        six = ""
        for cand in digits["sixes"]:
            mask = set(digits["one"]) - set(cand)
            if len(mask) == 1:
                six = cand
                topright = next(iter(mask))

        five = ""
        for cand in digits["fives"]:
            if not topright in cand:
                five = cand
        bottomleft = next(iter(set(six) - set(five)))

        nine = ""
        zero = ""
        for cand in digits["sixes"]:
            if cand != six:
                if bottomleft in cand:
                    zero = cand
                else:
                    nine = cand
        two = ""
        three = ""
        for cand in digits["fives"]:
            if cand != five:
                if bottomleft in cand:
                    two = cand
                else:
                    three = cand

        def strcmp(s1, s2):
            return ''.join(sorted(s1)) == ''.join(sorted(s2))
        ans = ""
        for dig in fourdig:
            if len(dig) == 7:
                ans += str(8)
            elif len(dig) == 3:
                ans += str(7)
            elif len(dig) == 4:
                ans += str(4)
            elif len(dig) == 2:
                ans += str(1)
            elif len(dig) == 5:
                if strcmp(dig, five): ans += '5'
                elif strcmp(dig, two): ans += '2'
                else: ans += '3'
            else:
                if strcmp(dig, six): ans += '6'
                elif strcmp(dig, nine): ans += '9'
                else: ans += '0'

        sumans += int(ans)
    print(sumans)
if __name__ == "__main__":
    main()
