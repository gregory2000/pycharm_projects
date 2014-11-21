__author__ = 'g42gregory'
import numpy as np
import scipy.io as sio

contents = sio.loadmat('dataset4.mat')

w_gen_feas = contents['w_gen_feas']
w_init = contents['w_init']
pos_examples_nobias = contents['pos_examples_nobias']
neg_examples_nobias = contents['neg_examples_nobias']

np.savetxt('dataset4_w_gen_feas.txt', w_gen_feas)
np.savetxt('dataset4_w_init.txt', w_init)
np.savetxt('dataset4_pos_examples_nobias.txt', pos_examples_nobias)
np.savetxt('dataset4_neg_examples_nobias.txt', neg_examples_nobias)

print w_gen_feas
print w_init
print pos_examples_nobias
print neg_examples_nobias
