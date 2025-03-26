import ROOT

# Create ROOT histograms
h_pt = ROOT.TH1F("h_pt", "Muon p_{T};p_{T} [GeV];Counts", 100, 0, 8)
h_eta = ROOT.TH1F("h_eta", "Muon Pseudorapidity #eta;#eta;Counts", 100, -5, 5)

# Open the muons.txt file
with open("muons.txt") as f:
    for line in f:
        pt_str, eta_str = line.strip().split()
        pt = float(pt_str)
        eta = float(eta_str)
        h_pt.Fill(pt)
        h_eta.Fill(eta)

# Draw histograms
c1 = ROOT.TCanvas("c1", "Muon Distributions", 1200, 600)
c1.Divide(2, 1)

c1.cd(1)
h_pt.Draw()

c1.cd(2)
h_eta.Draw()

c1.SaveAs("muon_distributions.png")
