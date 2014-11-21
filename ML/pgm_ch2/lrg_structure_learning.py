import pandas as pd
import numpy as np
from random import randint, sample

def rand_index(dframe, n_samples = 100):
   rindex = np.array(sample(xrange(len(dframe)), n_samples if n_samples <= len(dframe) else len(dframe)))
   result = [{i:j.values()[0] for i, j in dframe.iloc[[k]].to_dict().items()} for k in rindex]
   print result

if __name__ == "__main__":
   df = pd.read_csv('alarm.csv')
   rand_index(df, n_samples=1)

