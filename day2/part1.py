import argparse

parser = argparse.ArgumentParser("Given an input file, prints the solution")

parser.add_argument('file_name', type=str, help='Input file name')

def main():
    args = parser.parse_args()

    f = open(args.file_name, "r")

    coords = [0,0]

    for line in f:
        movement_tuple = line.split();
        bearing = movement_tuple[0];
        distance = int(movement_tuple[1]);

        if (bearing == "forward"):
            coords[0] += distance
        else:
            if (bearing == "down"):
                coords[1] += distance
            else:
                coords[1] -= distance

    print(coords[0]*coords[1])

if __name__ == "__main__":
    main()
