import argparse

parser = argparse.ArgumentParser("Given a file with newline separated integers returns number of strictly increasing adjacent depths")

parser.add_argument('file_name', type=str, help='Depths input file name')

def main() -> None:
    args = parser.parse_args()

    f = open(args.file_name, "r")

    prev: int = int(f.readline())
    count: int = 0;

    for entry in f:
        value: int = int(entry)
        if (value > prev): count += 1
        prev = value

    print(count);

if __name__ == "__main__":
    main()
