import math 

# Tank data 
g = 9.81                                        #m/s
r_vessel = 0.1                                  #m
r_foro = 0.002                                  #m
A_foro = math.pi*math.pow(r_foro,2)             #m2
A_base = math.pi*math.pow(r_vessel,2)           #m2
L = 0.8                                         #m
tau = 1000                                      #s

A_ratio = A_foro/A_base     
h0 = 0.5                                        #m
v0 = 0.00000001                                          #m/s

#  Model Data
n_runs = 10
n_steps = 5
n_integral = 5