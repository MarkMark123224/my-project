#include "Rental.h"
#include <iostream>
using namespace std;

void Rental::addRental(const Bike &bike, int hourCount) {
    bikes.push_back(bike);
    hours.push_back(hourCount);
}

double Rental::totalPrice() const {
    double sum = 0;
    for (size_t i = 0; i < bikes.size(); i++) {
        sum += bikes[i].getPricePerHour() * hours[i];
    }
    return sum;
}

void Rental::printReport() const {
    cout << "Прокат велосипедів:\n";

    for (size_t i = 0; i < bikes.size(); i++) {
        cout << "- " << bikes[i].getModel()
             << ", годин: " << hours[i]
             << ", ціна/год: " << bikes[i].getPricePerHour()
             << ", сума: "
             << bikes[i].getPricePerHour() * hours[i]
             << "\n";
    }

    cout << "Загальна вартість: " << totalPrice() << "\n";
}
