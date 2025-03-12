## Installing and Running FeynHiggs

### First Run
```sh
wget http://wwwth.mpp.mpg.de/members/heinemey/feynhiggs/newversion/FeynHiggs-2.19.0.tar.gz --no-check-certificate
tar xfvz FeynHiggs-2.19.0.tar.gz
cd FeynHiggs-2.19.0
sed -i '/CFLAGS-/ s/-Wall/-Wall -fPIE/' configure
./configure
make
cd example
gfortran demo.cc -I../build -L../build/ -lFH -lstdc++ -o demo.exe
```

### Modifying `demo.cc`
Modify the `demo.cc` file by adding the function `myWidth`.

### Comparing Widths with PyROOT
Using the same data file produced in Part 1 and the PyROOT script `compare-width.py`, plot the desired graphs.
