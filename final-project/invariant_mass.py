import matplotlib.pyplot as plt
import numpy as np
import uproot

#################### 2b ############################


def invariant_mass(pt1, eta1, phi1, pt2, eta2, phi2):
    return np.sqrt(2 * pt1 * pt2 * (np.cosh(eta1 - eta2) - np.cos(phi1 - phi2)))


# Load signal from pure_muon.root
sig_tree = uproot.open("pure_muon.root")["Events"]
pt1_s = sig_tree["mu1_pt"].array()
eta1_s = sig_tree["mu1_eta"].array()
phi1_s = sig_tree["mu1_phi"].array()
pt2_s = sig_tree["mu2_pt"].array()
eta2_s = sig_tree["mu2_eta"].array()
phi2_s = sig_tree["mu2_phi"].array()


# Normalize signal events to expected real event rate:
# Each simulated event is weighted by (σ × L / N_gen) so that the histogram represents
# the expected number of events in fb per bin under 100 fb⁻¹ of integrated luminosity
LUMINOSITY = 100  # fb^-1, based on Run 3
SIGMA_SIGNAL = 62000  # fb (DY-like Z' signal)
SIGMA_BACKGROUND = 924000  # fb (ttbar background)
N_GEN_SIGNAL = 100000
N_GEN_BACKGROUND = 100000
BINS = np.linspace(60, 120, 60)  # bin edges

m_signal = invariant_mass(pt1_s, eta1_s, phi1_s, pt2_s, eta2_s, phi2_s)
w_signal = SIGMA_SIGNAL * LUMINOSITY / N_GEN_SIGNAL
weights_signal = np.full_like(m_signal, w_signal)

# Load background
bg_tree = uproot.open("background.root")["Events"]
pt1_b = bg_tree["p1_pt"].array()
eta1_b = bg_tree["p1_eta"].array()
phi1_b = bg_tree["p1_phi"].array()
pt2_b = bg_tree["p2_pt"].array()
eta2_b = bg_tree["p2_eta"].array()
phi2_b = bg_tree["p2_phi"].array()

m_background = invariant_mass(pt1_b, eta1_b, phi1_b, pt2_b, eta2_b, phi2_b)
w_background = SIGMA_BACKGROUND * LUMINOSITY / N_GEN_BACKGROUND
weights_background = np.full_like(m_background, w_background)

# Fill Histograms
hist_sig, _ = np.histogram(m_signal, bins=BINS, weights=weights_signal)
hist_bg, _ = np.histogram(m_background, bins=BINS, weights=weights_background)
hist_tot = hist_sig + hist_bg
bin_centers = 0.5 * (BINS[:-1] + BINS[1:])


# Plot
plt.figure(figsize=(10, 6))
plt.hist(
    BINS[:-1],
    bins=BINS,
    weights=hist_bg,
    alpha=0.4,
    label="Background",
    color="red",
    histtype="stepfilled",
)
plt.hist(
    BINS[:-1],
    bins=BINS,
    weights=hist_sig,
    alpha=0.7,
    label="Signal",
    color="blue",
    histtype="stepfilled",
)
plt.step(
    BINS[:-1],
    hist_tot,
    where="mid",
    label="Signal + Background",
    color="black",
    linewidth=1.2,
)

plt.xlabel(r"Invariant Mass $M_{\mu\mu}$ [GeV]")
plt.ylabel("Events / bin (fb)")
plt.title(f"Invariant Mass Distribution (L = {LUMINOSITY} fb⁻¹)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("Invariant_mass.png")

#################### 2c ############################
# The following fits can be plotted if one wishes

from scipy.integrate import quad
from scipy.optimize import curve_fit


# Fit Model: Gaussian (signal) + 2nd order polynomial (background)
def fit_function(x, A, mu, sigma, a0, a1, a2):
    gaussian = A * np.exp(-((x - mu) ** 2) / (2 * sigma**2))
    background = a0 + a1 * x + a2 * x**2
    return gaussian + background


# Fit
p0 = [max(hist_tot), 91.2, 2.5, 1, 0, 0]  # initial guesses
popt, pcov = curve_fit(fit_function, bin_centers, hist_tot, p0=p0)


# Background-only Function
def background_only(x):
    a0, a1, a2 = popt[3:]
    return a0 + a1 * x + a2 * x**2


# Signal-only Function
def signal_only(x):
    return fit_function(x, *popt) - background_only(x)


# Integration range
mass_window = (80, 100)

# Integrate signal and background
N_S, _ = quad(signal_only, *mass_window)
N_B, _ = quad(background_only, *mass_window)

significance = N_S / np.sqrt(N_B)
required_lumi = ((5 / significance) ** 2) * LUMINOSITY

print(f"Fit signal peak: mu = {popt[1]:.2f} GeV, sigma = {popt[2]:.2f} GeV")
print(f"Mass window: {mass_window[0]}–{mass_window[1]} GeV")
print(f"Estimated Signal (NS): {N_S:.1f} fb")
print(f"Estimated Background (NB): {N_B:.1f} fb")
print(f"Statistical Significance: {significance:.2f}σ")
print(f"Required luminosity for 5σ: {required_lumi:.1f} fb⁻¹")
years_needed = required_lumi / 50  # Assuming 50 fb^-1/year
print(f"Estimated time at CMS: {years_needed:.2f} years")
