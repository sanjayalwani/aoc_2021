#include <fstream>
#include <iostream>

int main() {
    std::ifstream myFile("input.txt");

    std::string line1;
    int coords[2] = {0, 0};
    while (std::getline(myFile, line1)) {
        size_t pos = line1.find(' ');
        std::string dir = line1.substr(0,pos);
        std::string units_str = line1.substr(pos + 1, line1.length() - pos - 1);
        int units = std::stoi(units_str);
        if (dir == "forward") coords[0] += units;
        else if (dir == "down") coords[1] += units;
        else coords[1] -= units;
    }
    std::cout << "Forward movement: " << coords[0];
    std::cout << "\nDepth: " << coords[1];
    std::cout << "\nSolution: " << coords[0]*coords[1] << std::endl;
    return 0;
}
