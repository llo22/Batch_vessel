import matplotlib.pyplot as plt
import Result_min_time as Res
import batch_vessel_model as BM 
import Model_ as M 
import new_results as nr
import Optimization_constrNMPY as opt

fig = plt.figure(1)
ax1 = fig.add_subplot(111)
color = 'tab:blue'
ax1.set_xlabel('t (s)')
ax1.set_ylabel('Liquid Level (m)', color=color)
ax1.plot(Res.t_m[:,Res.minimum_time_index],Res.x_m[:,Res.minimum_time_index], color=color)

plt.figure(2)
plt.plot(Res.t_m[:,Res.minimum_time_index],Res.x_m[:,Res.minimum_time_index], color='tab:blue')

ax2 = ax1.twinx()
color = 'tab:orange'
ax2.set_ylabel('%', color=color)
ax2.set_ylim([0,1.1])
ax2.step(Res.t_m[:,Res.minimum_time_index],Res.opening_sequence_array[:,Res.minimum_time_index], color=color)
ax2.set_title('Valve Opening')
fig.tight_layout()

plt.figure(2)
plt.plot(BM.t_sol,BM.z_sol.T, color='tab:red')
plt.xlabel('t (s)')
plt.ylabel('Liquid Level (m)')
plt.title('Liquid Profile')

fig = plt.figure(3)
ax1 = fig.add_subplot(111)
ax1.plot(nr.Time,nr.Z, color='tab:green')
ax1.set_xlabel('t (s)')
ax1.set_ylabel('Liquid Level (m)')
plt.plot(BM.t_sol,BM.z_sol.T, color='tab:red')
ax1.set_title('Liquid Profile')

# ax2 = ax1.twinx()
# color = 'tab:green'
# ax2.set_ylabel('%', color=color)
# ax2.step(nr.Time,opt.valve_best_opening, color=color)
# ax2.set_title('Valve Opening')
# fig.tight_layout()
