void randomnumbers(){

// Opening a root file using TFile class, which returns a pointer 
    TFile *file = TFile::Open("file.root", "RECREATE");
    file->cd();

// Creating a pointer to a Tree object linking a branch to a variable 
    TTree *mytree = new TTree("mytree", "Storing data");
    Float_t number;
    mytree->Branch("number", &number, "number/F");

// Using TRandom class as a random number generator    
    TRandom3 randGen(0); 
    for (int i = 0; i<1000; ++i){
        number = randGen.Gaus(0,1);
        mytree->Fill();
    }

// Writing into the tree and closing the file 
    mytree->Write();
    file->Close();
}