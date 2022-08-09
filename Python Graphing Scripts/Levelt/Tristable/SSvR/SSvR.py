from numpy import *
import matplotlib.pyplot as plt
import numpy as np
import pickle

pickleFile = open("/Users/christopherhughes/Documents/GitHub/bifurcationRivalry/Python Graphing Scripts/Levelt/Tristable/SS.pickle", "rb")
SS = pickle.load(pickleFile)
Time, n1, n2, nf, RL1,HL1,RR2,HR2,RF,HF,RB1,HB1,RB2,HB2,RBF,HBF,RA1,RA2,RAF,IVL,IVR,IVF,ANGLEVAL = SS[0]


inputL = arange(0.4,0.6, 0.005)
dominance = []
transitions = 0
last = 'right'

for i in range(1, len(ANGLEVAL)):
    if (RL1[i] > RR2[i] and RL1[i] > RF[i]) and (last == 'right' or last == 'fuse'):
        last = 'left'
        transitions = transitions + 1
    if (RF[i] > RR2[i] and RF[i] > RL1[i]) and (last == 'left' or last == 'right'):
        last = 'fuse'
        transitions = transitions + 1
    if (RR2[i] > RF[i] and RR2[i] > RL1[i]) and (last == 'left' or last == 'fuse'):
        last = 'right'
        transitions = transitions + 1
    if i%200000 == 0:
        dominance.append(transitions/100)
        transitions = 0

plt.scatter(inputL, dominance)
plt.show()
