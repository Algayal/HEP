#include "Pythia8/Pythia.h"
#include <fstream>
#include <iostream>


using namespace Pythia8;

int main() {
    Pythia pythia;
    pythia.readString("Beams:eCM = 13000.");  // LHC energy
    pythia.readString("Higgs:useBSM = off");   
    pythia.readString("PDF:pSet = LHAPDF6:cteq6l1"); // Use CTEQ6L1 PDFs, not working, had problems
    // with installation 
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
                std::cout << "Higgs mass: " << pythia.event[j].m() << std::endl; //to check
                outFile << pythia.event[j].m() << std::endl;
            }
        }
    }

    // Close the file
    outFile.close();
    std::cout << "Higgs boson masses saved to higgs_output.txt" << std::endl;

    return 0;
}
