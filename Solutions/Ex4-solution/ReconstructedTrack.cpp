#include "ReconstructedTrack.h"

#include <cmath>

ReconstructedTrack::ReconstructedTrack() {}
ReconstructedTrack::~ReconstructedTrack() {}


double ReconstructedTrack::x() const {return trans_x; };
double ReconstructedTrack::y() const {return trans_y; };

double ReconstructedTrack::pseudo() const {
    double phi = atan(trans_y/trans_x);
    return -log(tan(phi/2));
}

void ReconstructedTrack::setXY(double x, double y) {
    trans_x = x;
    trans_y = y;
}

