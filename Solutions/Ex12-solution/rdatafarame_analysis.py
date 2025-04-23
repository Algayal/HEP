import os

import matplotlib.pyplot as plt
import ROOT

ROOT.ROOT.EnableImplicitMT()
script_dir = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(script_dir, "DYJetsToLL.root")

df = ROOT.RDataFrame("Events", filename)

# Filter events that passed the trigger HLT_IsoMu24
rdf_triggered = df.Filter("HLT_IsoMu24", "Trigger: HLT_IsoMu24")

# Create histogram of PV_npvs (pileup)
histo = rdf_triggered.Histo1D(
    ("pileup", "Pileup Distribution;PV_npvs;Events", 100, 0, 100), "PV_npvs"
)

c = ROOT.TCanvas()
histo.Draw()
output_path = os.path.join(script_dir, "pileup_rdataframe_root.png")
c.SaveAs(output_path)
