First Install and compile according to the instructions given in readme.txt file in lecture 10 example.
Difference is that we are using B4/B4a simulation (not B2/B2a), which is a simple Sampling Calorimeter setup.
To learn about the geometry of the detector, it can be found at: https://geant4-userdoc.web.cern.ch/Doxygen/examples_doc/html/basic_2B4_2B4a_2src_2DetectorConstruction_8cc_source.html
"// Geometry parameters
  G4int nofLayers = 10;
  G4double absoThickness = 10. * mm;
  G4double gapThickness = 5. * mm;
  G4double calorSizeXY = 10. * cm;
    // Get materials
  auto defaultMaterial = G4Material::GetMaterial("Galactic");
  auto absorberMaterial = G4Material::GetMaterial("G4_Pb");
  auto gapMaterial = G4Material::GetMaterial("liquidArgon");"

Then edit the vis.mac file.
I ran into problems with installing DAWN, so I made the following edits to vis.mac:
1. Uncomment /vis/viewer/flush; this will create an image of the detector simulation in the current folder 
2. Uncomment the lines based on the particle you wish to simulate  
/gun/particle e-
#/gun/particle proton
#/gun/particle alpha
/gun/energy 10 GeV
/run/beamOn 1

Now to change the absorber material, we change the source code "geant4/share/Geant4/examples/basic/B4/B4a/src/B4DetectorConstruction.cc".
Specifically lines to:
 69.  nistManager->FindOrBuildMaterial("G4_WATER");
103.   auto absorberMaterial = G4Material::GetMaterial("G4_WATER");
then rebuild everything in another file and proceed as before.
