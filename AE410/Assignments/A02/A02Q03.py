import numpy as np
from matplotlib import pyplot as plt

step      = 0.001
factor    = np.pi/180.0
deviation = 10

N       =     5
r_0     = 10000
theta   =    30
# gamma_M = theta # Pure pursuit guidance
gamma_M = theta + deviation # Deviated pursuit guidance
gamma_T =   120

X_M  =   0
Y_M  =   0
X_T0 = r_0*np.cos(gamma_M*factor)
Y_T0 = r_0*np.sin(gamma_M*factor)
v_M  = 500
# v_T  = 300 # Q4a
# v_T  = 250 # Q4b
v_T  = 300 # Q4c1
vX_T = v_T*np.cos(gamma_T*factor)
vY_T = v_T*np.sin(gamma_T*factor)

def targetLocation(time):
  return [X_T0 + vX_T*t for t in np.arange(0, time, step)], [Y_T0 + vY_T*t for t in np.arange(0, time, step)]

def missileLocation(time):
  global gamma_M, theta
  missileLocX = [X_M]
  missileLocY = [Y_M]
  LatAcc      = []
  D_T         = [X_T0, Y_T0]
  D_M         = [X_M,  Y_M]
  V_M         = [v_M*np.cos(gamma_M*factor), v_M*np.sin(gamma_M*factor)]
  
  for t in np.arange(0, time, step):
    D_T      = [X_T0 + vX_T*t, Y_T0 + vY_T*t]
    rVec     = [D_T[0]-D_M[0], D_T[1]-D_M[1]]
    rLen     = np.linalg.norm(rVec)
    theta    = np.arctan2(D_T[1]-D_M[1], D_T[0]-D_M[0])/factor
    
    # gamma_M = theta # Pure pursuit guidance
    gamma_M = theta + deviation # Deviated pursuit guidance
    V_M     = [v_M*np.cos(gamma_M*factor), v_M*np.sin(gamma_M*factor)]
    D_M[0] += V_M[0]*step
    D_M[1] += V_M[1]*step
    
    missileLocX.append(D_M[0])
    missileLocY.append(D_M[1])
    LatAcc.append(v_M*v_T*np.sin(gamma_T-theta)/rLen)
  return missileLocX, missileLocY, LatAcc

'''
time = 27
missileX, targetX = [X_M+1, X_M], [X_T0, X_T0]
while abs(missileX[-1] - targetX[-1]) > abs(missileX[-2] - targetX[-2]):
  missileX, missileY, LatAcc = missileLocation(time)
  targetX,  targetY  = targetLocation(time)
  time += step
print(time-step)
'''

# time = 31.25 # Q4a
# time = 28.01 # Q4b
time = 33 # Q4c1
# time = 33.26 # Q4c2
# time = 36.25 # Q4c3
missileX, missileY, LatAcc = missileLocation(time)
targetX,  targetY  = targetLocation(time)

plt.plot(missileX, missileY); plt.plot(targetX,  targetY); plt.show()
plt.plot(np.arange(0, time, step), LatAcc); plt.show()