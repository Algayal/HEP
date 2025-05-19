from math import atan, exp, log, pi, sqrt, tan
from random import gauss

import numpy as np
import uproot

# We want to know if any charged pions are too close to a muon (i.e. within a small angular distance).
# If so, the muon might be part of a jet → not a clean signal muon → reject.
# We then store the events that pass the selection into another root file, pure_muon.root

# Load signal.root file
file = uproot.open("signal.root")
tree = file["Events"]

# creating data arrays
mu1_pt = tree["p1_pt"].array()
mu2_pt = tree["p2_pt"].array()
mu1_eta = tree["p1_eta"].array()
mu2_eta = tree["p2_eta"].array()
mu1_phi = tree["p1_phi"].array()
mu2_phi = tree["p2_phi"].array()

pion_pt = tree["pion_pt"].array()
pion_eta = tree["pion_eta"].array()
pion_phi = tree["pion_phi"].array()


# Smearing Functions
def smear_pt(pt):
    """1% smearing"""
    return pt * gauss(1.0, 0.01)


# Angle smearing: η → θ converted → smeared → back to η
def smear_angle(angle):
    """2 mrad smearing"""
    return angle + gauss(0.0, 0.002)


def eta_to_theta(eta):
    return 2 * atan(exp(-eta))


def theta_to_eta(theta):
    return -log(tan(theta / 2))


def deltaR(eta1, phi1, eta2, phi2):
    """ΔR = sqrt(η^2 + φ^2) tells how close two particles are in angle. Will be used to check if
    particles are "isolated" or part of a jet."""
    dphi = phi1 - phi2
    # apply periodic boundary conditions
    if dphi > pi:
        dphi -= 2 * pi
    if dphi < -pi:
        dphi += 2 * pi
    deta = eta1 - eta2
    return sqrt(deta**2 + dphi**2)


sel_pt1 = []
sel_eta1 = []
sel_phi1 = []
sel_pt2 = []
sel_eta2 = []
sel_phi2 = []

# event loop
n_total = len(mu1_pt)  # or = len(mu2_pt)
n_passed = 0

for i in range(n_total):
    # 1. Smear muons
    pt1 = smear_pt(mu1_pt[i])
    pt2 = smear_pt(mu2_pt[i])

    theta1 = eta_to_theta(mu1_eta[i])
    theta2 = eta_to_theta(mu2_eta[i])

    theta1 = smear_angle(theta1)
    theta2 = smear_angle(theta2)

    eta1 = theta_to_eta(theta1)
    eta2 = theta_to_eta(theta2)

    phi1 = smear_angle(mu1_phi[i])
    phi2 = smear_angle(mu2_phi[i])

    # 2. Apply pT selection
    if pt1 < 30 or pt2 < 30:
        continue

    # 3. Track isolation
    iso1 = 0.0
    iso2 = 0.0

    for j in range(len(pion_pt[i])):
        dr1 = deltaR(eta1, phi1, pion_eta[i][j], pion_phi[i][j])
        dr2 = deltaR(eta2, phi2, pion_eta[i][j], pion_phi[i][j])
        if dr1 < 0.3:
            iso1 += pion_pt[i][j]
        if dr2 < 0.3:
            iso2 += pion_pt[i][j]

    if iso1 < 1.5 and iso2 < 1.5:
        sel_pt1.append(pt1)
        sel_eta1.append(eta1)
        sel_phi1.append(phi1)
        sel_pt2.append(pt2)
        sel_eta2.append(eta2)
        sel_phi2.append(phi2)
        n_passed += 1

with uproot.recreate("pure_muon.root") as fout:
    fout["Events"] = {
        "mu1_pt": np.array(sel_pt1),
        "mu1_eta": np.array(sel_eta1),
        "mu1_phi": np.array(sel_phi1),
        "mu2_pt": np.array(sel_pt2),
        "mu2_eta": np.array(sel_eta2),
        "mu2_phi": np.array(sel_phi2),
    }

print(f"Total events analyzed: {n_total}, events passing: {n_passed}")
