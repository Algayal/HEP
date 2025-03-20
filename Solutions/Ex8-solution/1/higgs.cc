#include "Pythia8/Pythia.h"
using namespace Pythia8;

int main() {
    Pythia pythia;

    pythia.readString("Higgs:useBSM = off"); // Ensure SM Higgs is used

    pythia.init();

    // Get the Higgs total decay width
    double higgsWidth = pythia.particleData.mWidth(25); // PDG ID 25 is the Higgs boson

    std::cout << "Higgs width (Γ_H) for m_H = 125 GeV: " << higgsWidth << " GeV" << std::endl;

    return 0;
}
