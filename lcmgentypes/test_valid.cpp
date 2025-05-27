#include <iostream>
#include "example_valid_t.hpp"

int main() {
    lcmgentypes::example_valid_t msg;
    msg.timestamp = 123456789;
    msg.name = "Hello Test";
    msg.enabled = 1;
    msg.num_ranges = 2;
    msg.ranges = {100, 200};
    msg.position[0] = 1.0;
    msg.position[1] = 2.0;
    msg.position[2] = 3.0;
    msg.orientation[0] = 0.1;
    msg.orientation[1] = 0.2;
    msg.orientation[2] = 0.3;
    msg.orientation[3] = 0.4;

    std::cout << "Type: " << msg.getTypeName() << std::endl;
    std::cout << "Name: " << msg.name << std::endl;
    std::cout << "Timestamp: " << msg.timestamp << std::endl;

    return 0;
}
