#ifndef RECONSTRUCTEDTRACK_H
#define RECONSTRUCTEDTRACK_H

#pragma once

class ReconstructedTrack
{
public:
    ReconstructedTrack();
    ~ReconstructedTrack();
    
    //Getters
    double x() const;
    double y() const;
    double pseudo() const;

    //Setters
    void setXY(double x, double y);

private:
    double trans_x;
    double trans_y;
 
};

#endif