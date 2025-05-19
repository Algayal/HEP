from array import array

import pythia8
import ROOT

N_EVENTS = 100000


def trigger(tree, pythia):
    """Function sets up root output file and applies the trigger HLT_DoubleIsoMu20_eta2p1"""
    # Particle branches
    p1_pt = array("f", [0.0])
    p2_pt = array("f", [0.0])
    p1_eta = array("f", [0.0])
    p2_eta = array("f", [0.0])
    p1_phi = array("f", [0.0])
    p2_phi = array("f", [0.0])

    tree.Branch("p1_pt", p1_pt, "p1_pt/F")
    tree.Branch("p2_pt", p2_pt, "p2_pt/F")
    tree.Branch("p1_eta", p1_eta, "p1_eta/F")
    tree.Branch("p2_eta", p2_eta, "p2_eta/F")
    tree.Branch("p1_phi", p1_phi, "p1_phi/F")
    tree.Branch("p2_phi", p2_phi, "p2_phi/F")

    pion_pt = ROOT.std.vector("float")()
    pion_eta = ROOT.std.vector("float")()
    pion_phi = ROOT.std.vector("float")()

    tree.Branch("pion_pt", pion_pt)
    tree.Branch("pion_eta", pion_eta)
    tree.Branch("pion_phi", pion_phi)

    passed = 0
    # Event loop
    for i in range(N_EVENTS):
        if not pythia.next():
            continue

        muons = []
        pion_pt.clear()
        pion_eta.clear()
        pion_phi.clear()

        for p in pythia.event:
            if not p.isFinal():
                continue
            if abs(p.id()) == 13:
                muons.append(p)
            elif abs(p.id()) == 211:  # Charged pion
                pion_pt.push_back(p.pT())
                pion_eta.push_back(p.eta())
                pion_phi.push_back(p.phi())

        if len(muons) < 2:
            continue

        # Sort muons by descending pT
        muons.sort(key=lambda p: p.pT(), reverse=True)

        # Trigger condition
        if (
            muons[0].pT() > 20
            and abs(muons[0].eta()) < 2.1
            and muons[1].pT() > 20
            and abs(muons[1].eta()) < 2.1
        ):
            p1_pt[0] = muons[0].pT()
            p1_eta[0] = muons[0].eta()
            p1_phi[0] = muons[0].phi()
            p2_pt[0] = muons[1].pT()
            p2_eta[0] = muons[1].eta()
            p2_phi[0] = muons[1].phi()

            tree.Fill()
            passed += 1

    return passed


#################### Signal Simulation ###################
pythia_signal = pythia8.Pythia()
# Proton-proton collision at 13.6 TeV
pythia_signal.readString("Beams:idA = 2212")
pythia_signal.readString("Beams:idB = 2212")
pythia_signal.readString("Beams:eCM = 13600.")
# Z/gamma* production, then turn off all Z decays and  allow only Z → μμ
pythia_signal.readString("WeakSingleBoson:ffbar2gmZ = on")
pythia_signal.readString("23:onMode = off")
pythia_signal.readString("23:onIfAny = 13")
pythia_signal.init()

fout1 = ROOT.TFile("signal.root", "RECREATE")
tree1 = ROOT.TTree("Events", "Z→μμ events")
signal_passed = trigger(tree1, pythia_signal)
tree1.Write()
fout1.Close()
pythia_signal.stat()

#################### Background Simulation ##################
pythia_background = pythia8.Pythia()
pythia_background.readString("Beams:idA = 2212")
pythia_background.readString("Beams:idB = 2212")
pythia_background.readString("Beams:eCM = 13600")
pythia_background.readString("Top:gg2ttbar = on")
pythia_background.readString("Top:qqbar2ttbar = on")
pythia_background.readString("6:m0 = 172.5")
pythia_background.init()

fout2 = ROOT.TFile("background.root", "RECREATE")
tree2 = ROOT.TTree("Events", "tt̄ → μμ background events")
background_passed = trigger(tree2, pythia_background)
tree2.Write()
fout2.Close()
pythia_background.stat()

print(
    f"Trigger efficiency (signal): {signal_passed} / {N_EVENTS} = {signal_passed / N_EVENTS:.2%}"
)
print(
    f"Trigger efficiency (background): {background_passed} / {N_EVENTS} = {background_passed / N_EVENTS:.2%}"
)
