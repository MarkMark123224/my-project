#include "Bike.h"

Bike::Bike(const string &modelName, double price)
    : model(modelName), pricePerHour(price) {}

string Bike::getModel() const {
    return model;
}

double Bike::getPricePerHour() const {
    return pricePerHour;
}
