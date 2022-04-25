import constrNMPy as cNM 
import Data as d 
import batch_vessel_model as BM 
import numpy as np 
import Result_min_time as Res
from functions import obj,callbackF

# Input 
n_steps = d.n_steps
n_integral = d.n_integral
t_span = BM.t_opt*3
t_step =  t_span/n_steps
X0 = [d.h0]
OP_0 = Res.opening_sequence*10
N_it = 1
x_op = (0,) 

LB = np.zeros(n_steps)
UB = np.ones(n_steps)*10

res = cNM.constrNM(obj,OP_0,LB,UB, args=(n_steps,t_step,n_integral,X0,N_it,x_op), maxiter = 1000, callback=callbackF)

valve_best_opening = list(res.values())
print('valve_best_opening:', valve_best_opening[4]/10)
valve_best_opening = np.asarray(valve_best_opening[4])