## Installing and Running HDECAY

### Step 1: Install and Build HDECAY
```sh
wget http://tiger.web.psi.ch/hdecay/hdecay.tar.gz
tar xfvz hdecay.tar.gz
make
```

### Step 2: Set Higgs Mass Parameters
Edit the input file `hdecay.in` and set the Higgs mass parameters:
```
MABEG   = 125.0
MAEND   = 125.0
```
Run HDECAY:
```sh
./run
```
Check the output file `br.sm2` to confirm that the mass is correctly set and the width is `0.4077E-02`.

### Step 3: Generate Data for Plotting
Modify the input file `hdecay.in` again to compute widths for different masses:
```
MABEG    = 80.0   # starting mass
MAEND    = 140.0  # ending mass
NMA      = 61     # number of points
```
This runs calculations for different masses and stores results in `br.sm2`. The mass range can be adjusted as needed. The upper limit is set to 140 GeV to improve clarity around 125 GeV, since the width increases rapidly beyond 140 GeV.

### Step 4: Extract Data for Plotting
Extract the mass and width columns into `width_data.txt`:
```sh
grep -v '#' br.sm2 | awk '{print $1, $7}' > width_data.txt
```

### Step 5: Plot the Results
Use a simple PyROOT script (`plot_width.py`) to visualize the results. The output plot is saved as `higgs_width_plot.png`.

### Step 6: Clean Up
```sh
make clean
```

### Edited and Added Files
- **Edited:** `hdecay.in` (input file), `br.sm2` (output file)
- **Added:** `plot_width.py` (Python script), `higgs_width_plot.png` (output plot)
