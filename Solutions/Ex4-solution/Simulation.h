#ifndef SIMULATION_H
#define SIMULATION_H

#pragma once

#include "ReconstructedTrack.h"


class Simulation : public ReconstructedTrack
{
public:
    Simulation();
    ~Simulation();

    //Getters 
    double get_particle_id() const;
    double get_parent_partile_id() const;

    //Setter
    void set_id(double particle, double parent);

private:
    double particle_id;
    double parent_partile_id;
};

#endif