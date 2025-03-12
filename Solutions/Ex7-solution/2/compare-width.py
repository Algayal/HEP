import numpy as np
import ROOT

# Read data from files
hdecay_masses, hdecay_widths = [], []
feynhiggs_masses, feynhiggs_widths = [], []

with open("width-hdecay.txt", "r") as h:
    for line in h:
        values = line.strip().split()
        hdecay_masses.append(values[0])
        hdecay_widths.append(values[1])

with open("width-feynhiggs.txt", "r") as f:
    for line in f:
        values = line.strip().split()
        feynhiggs_masses.append(values[0])
        feynhiggs_widths.append(values[1])

hdecay_masses_array = np.array(hdecay_masses, dtype=np.float64)
hdecay_widths_array = np.array(hdecay_widths, dtype=np.float64)

feynhiggs_masses_array = np.array(feynhiggs_masses, dtype=np.float64)
feynhiggs_widths_array = np.array(feynhiggs_widths, dtype=np.float64)

# Ratio
ratios = [
    fh / hd if hd != 0 else 0
    for fh, hd in zip(feynhiggs_widths_array, hdecay_widths_array)
]
ratios_array = np.array(ratios, dtype=np.float64)

# Create TGraphs
graph_hdecay = ROOT.TGraph(
    len(hdecay_masses_array), hdecay_masses_array, hdecay_widths_array
)
graph_feynhiggs = ROOT.TGraph(
    len(feynhiggs_masses_array), feynhiggs_masses_array, feynhiggs_widths_array
)
graph_ratios = ROOT.TGraph(
    len(feynhiggs_masses_array), feynhiggs_masses_array, ratios_array
)

# Set graph styles
graph_hdecay.SetLineColor(ROOT.kRed)
graph_hdecay.SetLineWidth(2)
graph_hdecay.SetTitle("HDECAY Widths;Mass (GeV);Width (GeV)")

graph_feynhiggs.SetLineColor(ROOT.kBlue)
graph_feynhiggs.SetLineWidth(2)
graph_feynhiggs.SetTitle("FeynHiggs Widths;Mass (GeV);Width (GeV)")


graph_ratios.SetLineWidth(2)
graph_ratios.SetTitle("Width Ratio ;Mass (GeV); FeyHiggs / Hdecay")

# Create canvas with two subpads
canvas = ROOT.TCanvas("canvas", "Width Comparison", 1200, 500)
canvas.Divide(2, 2)

canvas.cd(1)
graph_hdecay.Draw("AL")

canvas.cd(2)
graph_feynhiggs.Draw("AL")

canvas.cd(3)
graph_ratios.Draw("AL")

# Show the plot
canvas.Draw()
canvas.SaveAs("plots.png")
ROOT.gApplication.Run()
