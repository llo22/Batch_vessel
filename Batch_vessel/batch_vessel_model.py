import numpy as np 
import Data as d 
from scipy.integrate import solve_ivp
from functions import modelODE, stop_condition
import matplotlib.pyplot as plt 

stop_condition.terminal = True
global x_opening

# Inizialization of the array to save all the values 
z_sol = np.zeros([(d.n_integral*d.n_steps)])
t_sol = np.linspace(0,d.tau,(d.n_integral*d.n_steps))

# Initial conditions
X0 = [d.h0]
x_opening = (1,) 

# Solve ODE
time_range = np.linspace(0,d.tau,(d.n_integral*d.n_steps))
sol = solve_ivp(modelODE,(0,d.tau),X0,t_eval=time_range ,events=stop_condition, args=x_opening)

t_until_stop = sol.t
z = sol.y[0,:]

# To complete integration until the required tau 
for i in range(0,np.size(z)):
    z_sol[i] = z[i]
    
for i in range(0,np.size(t_until_stop)):
    t_sol[i] = t_until_stop[i]
        
t_opt = sol.t_events[0][0]
