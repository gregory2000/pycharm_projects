from BNfinder.BDE import BDE
from BNfinder.data import dataset

score=eval("BDE")(data_factor=1.0, chi_alpha=0.9999, sloops=False)
print score

def learn_structure(sample_data,dataset_name):
   d = dataset(dataset_name).fromNewFile(open(sample_data))
   score2,g,subpars = d.learn(score=score,data_factor=1.0)
   d.write_bif(g,dataset_name+".bif")
   d.write_cpd(g,file(dataset_name+"_cpd.txt","w"))
   return score2,g,subpars




