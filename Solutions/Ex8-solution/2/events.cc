#include "Pythia8/Pythia.h"
#include <fstream>
#include <iostream>


using namespace Pythia8;

int main() {
    Pythia pythia;
    pythia.readString("Beams:eCM = 13000.");  // LHC energy
    pythia.readString("Higgs:useBSM = off"); 
    pythia.readString("PDF:pSet = 8"); // Option 8 = CTEQ6L1
    pythia.readString("HiggsSM:all = on");
    pythia.init();

    // Open output text file
    std::ofstream outFile("higgs_output.txt");
    if (!outFile) {
        std::cerr << "Error opening file for writing!" << std::endl;
        return 1;
    }

    // Event loop
    int nEvents = 1000;
    for (int i = 0; i < nEvents; i++) {
        if (!pythia.next()) continue;

 
        for (int j = 0; j < pythia.event.size(); j++) {
            if (pythia.event[j].id() == 25) { // Higgs boson PDG ID = 25
                outFile << pythia.event[j].m() << std::endl;
                break;
            }
        }
    }

    // Close the file
    outFile.close();
    std::cout << "Higgs boson masses saved to higgs_output.txt" << std::endl;

    return 0;
}
