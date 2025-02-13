#include "Simulation.h"

Simulation::Simulation(){}

Simulation::~Simulation(){}

double Simulation::get_particle_id() const {return particle_id; }

double Simulation::get_parent_partile_id() const {return parent_partile_id; }

void Simulation::set_id(double particle, double parent) {
    particle_id = particle;
    parent_partile_id = parent;
}
