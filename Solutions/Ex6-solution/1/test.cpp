#include "Random.h"
#include "Plot.h"
#include <iostream>

int main(){

    Random* gaus_tree = new Random();
    gaus_tree->random_gaus();
              
    Plot* hist = new Plot();
    hist->hist_plot(); 
    return 0;
}