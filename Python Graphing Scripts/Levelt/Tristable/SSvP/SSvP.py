from numpy import *
import matplotlib.pyplot as plt
import pickle


pickleFile = open("/Users/christopherhughes/Documents/GitHub/bifurcationRivalry/Python Graphing Scripts/Levelt/Tristable/SS.pickle", "rb")
SS = pickle.load(pickleFile)
Time, n1, n2, nf, RL1,HL1,RR2,HR2,RF,HF,RB1,HB1,RB2,HB2,RBF,HBF,RA1,RA2,RAF,IVL,IVR,IVF,ANGLEVAL = SS[0]

inputL = arange(0.4,0.6, 0.005)
predominance = []

numL = 0
numR = 0
for i in range(1, len(ANGLEVAL)):
    if RL1[i] >= RR2[i]:
        numL = numL + 1
    elif RR2[i] > RL1[i]:
        numR = numR + 1
    if i%200000 == 0:
        predominance.append(numL/(numR+numL))
        numL = 0
        numR = 0

plt.scatter(inputL, predominance)
plt.show()
