#include "MET.h"
#include <cmath>
#include <iostream> 

MET::MET() {}

MET::~MET() {}

float MET::phi() {
    float cos_angle;
    float dot_product = x[0] * y[0] + x[1] * y[1] + x[2] * y[2];
    float magnitude_x = std::sqrt(x[0] * x[0] + x[1] * x[1] + x[2] * x[2]);
    float magnitude_y = std::sqrt(y[0] * y[0] + y[1] * y[1] + y[2] * y[2]);
    cos_angle = dot_product / (magnitude_x * magnitude_y);
    return std::acos(cos_angle)*180/M_PI;

}

void MET::printphi() {
    std::cout << "The angle between the vectors: " << phi() << "°" << std::endl;
}

void MET::printx() {
    std::cout << "x-component of the transverse momentum: ";
    std::cout << "(" << x[0] <<"," << x[1] << "," << x[2] << ")" << std::endl;
}

void MET::printy() {
    std::cout << "y-component of the transverse momentum: ";
    std::cout << "(" << y[0] <<"," << y[1] << "," << y[2] << ")" << std::endl;

}
