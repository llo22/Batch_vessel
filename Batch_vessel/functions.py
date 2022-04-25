import Data as d
import math 
import numpy as np 
from scipy.integrate import solve_ivp

def modelODE(t,z,x_opening):
    dzdt = -x_opening*d.A_ratio*math.sqrt(2*d.g*abs(z))
    dz = dzdt
    return dz

def modelODE_(t,z,x_op):
    dzdt = -(x_op/10)*d.A_ratio*math.sqrt(2*d.g*abs(z))
    dz = dzdt
    return dz


def stop_condition(t,z,x_opening): 
    return z[0]

def callbackF(x_opt,N_it,n_steps,t_step,n_integral,X0): 
    print('N_it:', N_it)
    print('x_opt:', x_opt)
    N_it +=1

def obj(x_opt,n_steps,t_step,n_integral,X0,N_it,x_op): 
    t_until_stop = 0
    integration_initial_values = np.zeros([n_steps,2])
    integration_initial_values[0,:] = X0

    
    for i_step in range(0,n_steps):
   
        # Valve opening 
        x_op = (x_opt[i_step],)
        
        # Integration 
        stop_condition.terminal = True
        
        X0_new = integration_initial_values[i_step,:]
        t_in = t_step*i_step
        t_out = t_step*(1+i_step)
        time = np.linspace(t_in,t_out,n_integral)
       
        sol = solve_ivp(modelODE_ , (t_in,t_out),X0_new ,t_eval=time, events=stop_condition,args=x_op)
        
        t_sol = sol.t
        z_sol = sol.y[0,:]
 

        if np.size(t_sol)<n_integral: 
            if t_until_stop != 0:
                continue
            t_until_stop = sol.t_events
            t_until_stop = np.array(t_until_stop)
        
        # Update values
        if i_step < n_steps-1:
            integration_initial_values[i_step+1,:] = [z_sol[-1]]
        else:
            break
        
    #Objective function to minimize time of emptying 
    return t_until_stop