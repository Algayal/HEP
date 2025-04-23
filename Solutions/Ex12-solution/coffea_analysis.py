import os

import matplotlib.pyplot as plt
from coffea.nanoevents import NanoAODSchema, NanoEventsFactory

script_dir = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(script_dir, "DYJetsToLL.root")

events = NanoEventsFactory.from_root(
    filename,
    schemaclass=NanoAODSchema,
).events()

# Apply HLT_IsoMu24 trigger
events = events[events.HLT.IsoMu24]

# Extract pileup information
nPU = events.PV.npvs.compute()

# Plot the pileup distribution
plt.hist(nPU, bins=100, range=(0, 100), histtype="step", linewidth=2)
plt.xlabel("PV_npvs")
plt.ylabel("Events")
plt.title("Pileup Distribution (HLT_IsoMu24)")
plt.grid(True)
output_path = os.path.join(script_dir, "pileup_coffea.png")
plt.savefig(output_path)
plt.show()
