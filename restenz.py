def ecor1(seq, enzima): 
    sitiocorte = seq.find(enzima)
    frag1 = seq[:sitiocorte + len(enzima)]
    frag2 = seq[sitiocorte + len(enzima):]
    return([[frag1, len(frag1)], [frag2, len(frag2)]])