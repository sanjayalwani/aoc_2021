import argparse

parser = argparse.ArgumentParser("Given a file with newline separated integers returns number of strictly increasing adjacent depths")

parser.add_argument('file_name', type=str, help='Depths input file name')

def main():
    args = parser.parse_args()

    f = open(args.file_name, "r")

    coords = [0,0]
    aim = 0;
    for line in f:
        movement_tuple = line.split();
        bearing = movement_tuple[0];
        distance = int(movement_tuple[1]);

        if (bearing == "forward"):
            coords[0] += distance
            coords[1] += aim*distance
        else:
            if (bearing == "down"):
                aim += distance
            else:
                aim -= distance

    print(coords[0]*coords[1])

if __name__ == "__main__":
    main()
