#include "ReconstructedTrack.h"
#include "Simulation.h"
#include <iostream>

using namespace std;

int main () {

    double input_x = 123.4;
    double input_y = 56.7;
    double particle = 2345;
    double parent = 6677;
    
    /*
    // test for the ReconstructedTrack class
    ReconstructedTrack track;
    track.setXY(input_x, input_y);

    // Output some results from the object
    cout << "Reconstructed track input "
        << input_x << " "
        << input_y << endl;
    cout << "Reconstructed track pseudorapidity,x,y " 
        << track.pseudo() << " "
        << track.x() << " "
        << track.y() << endl;
    */

    // Class with inheritance
    Simulation sim;

    // Inherited member functions
    sim.setXY(input_x, input_y);
    cout << "The transverse momentum in the x-direction: " << sim.x() << endl;
    cout << "The transverse momentum in the y-direction: " << sim.y() << endl;
    cout << "Pseudorapidity: " <<  sim.pseudo() << endl;
    
    // Non-inherited member functions    
    sim.set_id(particle, parent);
    cout << "Particle id: " << sim.get_particle_id() << endl;
    cout << "Parent partile id: "<<sim.get_parent_partile_id() << endl;

    return 0;
}