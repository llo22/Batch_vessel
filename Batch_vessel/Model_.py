import Data as d
import batch_vessel_model as BM
import numpy as np 
import math 
from scipy.integrate import solve_ivp 
import torch as T
import random
from functions import modelODE, stop_condition

# Input 

n_runs = d.n_runs
n_steps = d.n_steps
n_integral = d.n_integral

t_span = BM.t_opt*3
t_step =  t_span/n_steps
t = np.linspace(0,t_span,n_steps)

# Inizialitation
Z = np.zeros([n_steps, n_integral])
Time = np.empty([n_steps,n_integral])
Opening_values = np.zeros([n_steps,n_integral])
X0 = [d.h0]
i = 0

# Generating empty tensors 
tensor = T.ones(())
Z_tens = tensor.new_empty((n_steps,n_integral,n_runs))
OP_tens = tensor.new_empty((n_steps,n_integral,n_runs))
Time_tens = tensor.new_empty((n_steps,n_integral,n_runs))


for r in range(0,n_runs): 
    t_until_stop = 0
    for i_step in range(0,n_steps):
        
        z_sol = np.zeros([1,n_integral])
        t_sol = np.linspace(t_step*i_step,t_step*(1+i_step),n_integral)
        
        
        # Valve opening
        x = random.randint(0,10)
        x_opening = (x/10,)
        
        # Integration 
        stop_condition.terminal = True
        
        t_in = t_step*i_step
        t_out = t_step*(1+i_step)
        time = np.linspace(t_in,t_out,n_integral)
        
        sol = solve_ivp(modelODE, (t_in,t_out), X0, t_eval=time, events=stop_condition, args=x_opening)
        
        t = sol.t
        z = sol.y[0,:]
        
        if np.size(t_sol)<n_integral: 
            if t_until_stop != 0:
                continue
            t_until_stop = sol.t_events
            t_until_stop = np.array(t_until_stop)

        for i in range(0,np.size(z)):
            z_sol[0,i] = z[i]

        for i in range(0,np.size(t)):
            t_sol[i] = t[i]
            
        x_array = np.ones(n_integral)*x_opening
        
        # Saving Data 
        Z[i_step,:] = z_sol
        Time[i_step,:] = t_sol
        Opening_values[i_step,:] = x_array
        
        
        # Update values
        X0 = [z_sol[0,-1]]
        
        if i_step == (n_steps-1): 
            X0 = [d.h0]

    if z[-1] > 0: 
        Time += 1 

    # Storing data for each run
    Z_t = T.from_numpy(Z)
    Z_tens[:,:,r] = Z_t
    
    OP_t = T.from_numpy(Opening_values)
    OP_tens[:,:,r] = OP_t
    
    Time_t = T.from_numpy(Time)
    Time_tens[:,:,r] = Time_t
    
    

