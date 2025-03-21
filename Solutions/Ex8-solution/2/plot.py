import os

import numpy as np
import ROOT

current_dir = os.getcwd()
txt_path = os.path.join(
    current_dir, "2/higgs_output.txt"
)  # incase of error change the path

masses = np.loadtxt(txt_path)

root_file = ROOT.TFile("higgs_output.root", "RECREATE")
hist = ROOT.TH1F("hMass", "Higgs Mass Distribution; Mass (GeV); Events", 50, 120, 130)


# Fill histogram
for mass in masses:
    hist.Fill(mass)

bwFit = ROOT.TF1("bwFit", "[0]*TMath::BreitWigner(x, [1], [2])", 120, 130)
bwFit.SetParameters(100, 125, 2.5)  # Initial guesses: norm, mean, width
hist.Fit(bwFit, "R")

# Extract width
width = bwFit.GetParameter(2)
print(f"Extracted Higgs Breit-Wigner Width: {width:.4f} GeV")
hist.Write()
root_file.Close()
ROOT.gApplication.Run()
