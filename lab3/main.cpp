#include "Bike.h"
#include "Rental.h"
#include <iostream>

using namespace std;

int main() {
    Rental rental;

    rental.addRental(Bike("Giant", 50), 2);
    rental.addRental(Bike("Trek", 70), 3);

    rental.printReport();

    return 0;
}
