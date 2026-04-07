#ifndef BIKE_H
#define BIKE_H

#include <string>
using namespace std;

class Bike {
private:
    string model;
    double pricePerHour;

public:
    Bike(const string &modelName, double price);

    string getModel() const;
    double getPricePerHour() const;
};

#endif
