import numpy as np 
import Model_ as M 
import Data as d
import batch_vessel_model as BM 
import torch as T 

# Reshaping and turning tensors into arrays 

x_model = T.reshape(M.Z_tens,(d.n_steps*d.n_integral,d.n_runs))
x_m = x_model.detach().numpy()

t_model = T.reshape(M.Time_tens,(d.n_steps*d.n_integral,d.n_runs))
t_m = t_model.detach().numpy()

opening_sequence_array = T.reshape(M.OP_tens,(d.n_steps*d.n_integral,d.n_runs))
opening_sequence_array = opening_sequence_array.detach().numpy()


R = np.empty([M.n_runs,1])

for r in range(0,M.n_runs):
    if x_m[-1,r] > 0: 
        R[r,0] = M.t_span+1
    else:
        result_time_index = np.where(x_m[:,r] == 0)[0]
        R[r,0] = t_m[result_time_index[0],r]
    
minimum_time_index = min(range(len(R)), key=R.__getitem__)
print('Minimum time required:  %f seconds' %R[minimum_time_index,0])
print('Optimal time: %f seconds' %BM.t_opt)
print('Best run: %f' %minimum_time_index)

opening_sequence = M.OP_tens[:,0,minimum_time_index]
opening_sequence = opening_sequence.detach().numpy()

print('Best first guess:', opening_sequence)