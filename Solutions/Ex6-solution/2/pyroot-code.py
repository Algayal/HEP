from array import array

import ROOT

"""
It is uneccessary to used OOP for this script, although it can be done, 
since import ROOT takes care of all headers, object instantiations, pointers etc ... 
"""

# Open .root file
file = ROOT.TFile("file.root", "RECREATE")
file.cd()

# Create a Tree and branch
tree = ROOT.TTree("tree", "storing data")
number = array("f", [0])
tree.Branch("number", number, "number/F")

# Generate gaussian distribution and save it into .root file
gen = ROOT.TRandom3(0)
for i in range(0, 1000):
    number[0] = gen.Gaus(0, 1)
    tree.Fill()

tree.Write()
file.Close()

# Open the root file and read the tree
fIN = ROOT.TFile.Open("file.root")
readtree = fIN.Get("tree")

# Create histogram
hist = ROOT.TH1F("hist", "Random Number Distribution", 100, -4, 4)
hist.SetFillColor(5)
hist.SetLineColor(1)
hist.SetLineWidth(3)
hist.GetXaxis().SetTitle("Random numbers")
hist.GetYaxis().SetTitle("Counts")

# Fit the histogram using root defined gaussian
readtree.Project("hist", "number")
hist.Fit("gaus")


# Keep the canvas open
ROOT.gApplication.Run()
