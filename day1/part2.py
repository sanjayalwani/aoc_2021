import argparse

parser = argparse.ArgumentParser("Given a file with newline separated integers returns number of strictly increasing adjacent depth 3-windows")

parser.add_argument('file_name', type=str, help='Depths input file name')

def main():
    args = parser.parse_args()

    f = open(args.file_name, "r")

    k_window_size = 3;
    # Initialization
    window = [0] * k_window_size

    for i in range(k_window_size):
        window[i] = int(f.readline())

    count = 0;
    iterations = 0;
    # Maintenance
    for entry in f:
        value = int(entry)

        # We roll the window around with mod arithmetic to avoid excess swaps
        if (value > window[iterations % 3]): count += 1
        window[iterations % 3] = value;

        iterations += 1

    print(count);

if __name__ == "__main__":
    main()
