import numpy as np
from matplotlib import pyplot as plt

step   = 0.01
time   = 100
factor = np.pi/180.0

def targetLocation(t):
  return (3000*np.cos(30*factor)+400*t*np.cos(170*factor), 3000*np.sin(30*factor)+400*t*np.sin(170*factor))

def missileLocation(t):
  return (500*t*np.cos(45*factor), 500*t*np.sin(45*factor))

missileX, missileY = [], []
targetX,  targetY  = [], []
VTheta,   VR       = [], []
oldMissileLoc      = missileLocation(0)
oldTargetLoc       = targetLocation(0)
oldR               = np.linalg.norm([oldMissileLoc[0]-oldTargetLoc[0],oldMissileLoc[1]-oldTargetLoc[1]])
oldTheta           = np.arctan2(oldMissileLoc[1]-oldTargetLoc[1],oldMissileLoc[0]-oldTargetLoc[0])
for t in np.arange(0, time, step):
  missileLoc = missileLocation(t)
  targetLoc  = targetLocation(t)
  r          = np.linalg.norm([missileLoc[0]-targetLoc[0],missileLoc[1]-targetLoc[1]])
  theta      = np.arctan2(missileLoc[1]-targetLoc[1],missileLoc[0]-targetLoc[0])

  Vr     = (r-oldR)/step
  Vtheta = r*(theta-oldTheta)/step
  VR.append(Vr)
  VTheta.append(Vtheta)
  
  oldMissileLoc = missileLoc
  oldTargetLoc  = targetLoc
  oldR          = r
  oldTheta      = theta

plt.plot(VR[1:]); plt.show()
plt.plot(VTheta[1:]); plt.show()
plt.plot(VTheta[1:], VR[1:]); plt.show()