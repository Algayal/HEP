void plotfit(){

// Open root file and read the branch. 
// Incase the file contains more than one branch, we need to be more careful
    TFile *fIN = TFile::Open("file.root");
    TTree *readtree = (TTree*)fIN->Get("mytree");

// Create a histogram and Fill it using TTree::Draw()
    TH1F *hist = new TH1F("hist", "Random Number Distribution", 100, -4, 4);
    hist->SetFillColor(5);
    hist->SetLineColor(1);
    hist->SetLineWidth(3);
    hist->GetXaxis()->SetTitle("Random numbers");
    hist->GetYaxis()->SetTitle("Counts");

// Fitting the histogram using root defined gaussian      
    readtree->Draw("number >> hist");
    hist->Fit("gaus");
    
}