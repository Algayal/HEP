import numpy as np
import ROOT

masses = np.loadtxt("higgs_output.txt")

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

# Plot
canvas = ROOT.TCanvas("c1", "Higgs Mass Distribution", 800, 600)
hist.Draw()
bwFit.Draw("same")
canvas.SaveAs("higgs_mass_distribution.png")
