count = 0
with open("muons.txt") as f:
    for line in f:
        pt_str, eta_str = line.strip().split()
        pt = float(pt_str)
        eta = float(eta_str)
        if pt > 5 and abs(eta) < 2.5:
            count += 1
prob = (count / 50000) * 100  # 50000 is the total number of events generated
print(f"The probability of detecting a muon with pₜ < 5 GeV and |η| < 2.5 is: {prob} %")
