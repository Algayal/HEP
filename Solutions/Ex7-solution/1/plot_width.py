import numpy as np
import ROOT

# Read data from file
mass, width = [], []
with open("width-hdecay.txt", "r") as f:
    for line in f:
        values = line.strip().split()
        if len(values) == 2:  # Ensure only two columns
            try:
                mass.append(float(values[0]))
                width.append(float(values[1]))
            except ValueError:
                continue  # Skip lines that aren't numeric

mass_array = np.array(mass, dtype=np.float64)
width_array = np.array(width, dtype=np.float64)

# Create a TGraph
graph = ROOT.TGraph(len(mass_array), mass_array, width_array)
graph.SetTitle("Higgs Width vs Mass;Mass (GeV);Width (GeV)")
graph.SetMarkerStyle(20)
graph.SetMarkerSize(0.5)
graph.SetLineWidth(1)

# Create a canvas and plot
c1 = ROOT.TCanvas("c1", "Higgs Width Plot", 800, 600)
graph.Draw("APL")


c1.Draw()
c1.SaveAs("higgs_width_plot.png")
ROOT.gApplication.Run()
