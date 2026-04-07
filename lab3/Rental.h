#ifndef RENTAL_H
#define RENTAL_H

#include "Bike.h"
#include <vector>

class Rental {
private:
    vector<Bike> bikes;
    vector<int> hours;

public:
    void addRental(const Bike &bike, int hourCount);
    double totalPrice() const;
    void printReport() const;
};

#endif
