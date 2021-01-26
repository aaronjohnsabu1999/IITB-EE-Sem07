import numpy as np
from matplotlib import pyplot as plt
N       =   5
v_M     = 400
v_T     = 200
step    =   0.01
gamma_M = np.pi/3.0
gamma_T = np.pi/2.0

def targetLocation(time):
  return [10000 for t in np.arange(0,time,step)], [200*t for t in np.arange(0,time,step)]

def missileLocation(time):
  global v_T, v_M, gamma_T, gamma_M, N, step
  if time < 3:
    return [200*t for t in np.arange(0,time,step)], [200*np.sqrt(3)*t for t in np.arange(0,time,step)], []
  missileLocX = [200*t for t in np.arange(0,3,step)]
  missileLocY = [200*np.sqrt(3)*t for t in np.arange(0,3,step)]
  missileLoc  = [[200*t, 200*np.sqrt(3)*t] for t in np.arange(0,3,step)]
  LatAcc      = []
  D_T1        = [10000, 200*(3-step)]
  D_M         =  missileLoc[-1]
  V_M         = [v_M*np.cos(gamma_M), v_M*np.sin(gamma_M)]
  for t in np.arange(3, time, step):
    D_T1     = [10000, 200*(t-step)]
    rVec     = [D_T1[0]-D_M[0],D_T1[1]-D_M[1]]
    rLen     = np.linalg.norm(rVec)
    Theta    = np.arctan((D_T1[1]-D_M[1])/(D_T1[0]-D_M[0]))
    ThetaDer = (v_T*np.sin(gamma_T-Theta) - v_M*np.sin(gamma_M-Theta)) / rLen
    gammaDer =   N*ThetaDer
    A_M      = [-gammaDer*V_M[1], gammaDer*V_M[0]]    
    gamma_M  = gamma_M + gammaDer*step
    V_M = [v_M*np.cos(gamma_M), v_M*np.sin(gamma_M)]
    D_M[0]  += V_M[0]*step
    D_M[1]  += V_M[1]*step
    if D_M[0] > 10000:
      break
    missileLocX.append(D_M[0])
    missileLocY.append(D_M[1])
    LatAcc.append(np.linalg.norm(A_M))
  return missileLocX, missileLocY, LatAcc

missileX, missileY, LatAcc = missileLocation(30.2)
targetX, targetY           = targetLocation(30.2)
plt.plot(missileX, missileY); plt.plot(targetX,  targetY); plt.show()
plt.plot(LatAcc); plt.show()