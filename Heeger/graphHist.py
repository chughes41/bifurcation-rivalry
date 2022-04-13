from numpy import *
import matplotlib.pyplot as plt





Time,RL1,HL1,RR2,HR2,RF,HF,RB1,HB1,RB2,HB2,RBF,HBF,RA1,RA2,RAF,IVL,IVR,IVF,ANGLEVAL = loadtxt('50_0_10000.dat', unpack=True)

binWidth = (len(Time)-1)/10
statesLeft = 0
statesRight = 0
statesTristable=0
stateCount=0
states = []
for i in range(len(Time)):
    if RB1[i] >= RBF[i] and RB1[i] >= RB2[i]:
        statesLeft += 1
    if RB2[i] >= RBF[i] and RB2[i] >= RB1[i]:
        statesRight += 1
    if RBF[i] >= RB1[i] and RBF[i] >= RB2[i]:
        statesTristable += 1
    stateCount +=1
    print
    if stateCount % binWidth == 0:
        stateCount = 0
        propRiv = (statesLeft+statesRight)/binWidth
        statesLeft = 0
        statesRight = 0
        statesTristable=0
        states.append(propRiv)


TimeR,RL1,HL1,RR2,HR2,RF,HF,RB1,HB1,RB2,HB2,RBF,HBF,RA1,RA2,RAF,IVL,IVR,IVF,ANGLEVALR = loadtxt('0_50_10000.dat', unpack=True)

statesLeft = 0
statesRight = 0
statesTristable=0
stateCount=0

statesR = []
for i in range(len(TimeR)):
    if RB1[i] >= RBF[i] and RB1[i] >= RB2[i]:
        statesLeft += 1
    if RB2[i] >= RBF[i] and RB2[i] >= RB1[i]:
        statesRight += 1
    if RBF[i] >= RB1[i] and RBF[i] >= RB2[i]:
        statesTristable += 1
    stateCount +=1
    if stateCount % binWidth   == 0:
        stateCount = 0
        propRiv = (statesLeft+statesRight)/binWidth
        statesLeft = 0
        statesRight = 0
        statesTristable=0
        statesR.append(propRiv)




Angles = [0,5,10,15,20,25,30,35,40,45]
AnglesR = [45,40,35,30,25,20,15,10,5,0]

plt.subplot(1,1,1)
plt.xlabel('Angle(degrees)')
plt.ylabel('State')
plt.title('Slow Rotation')
plt.plot(Angles, statesR, linestyle='-', color = 'red', marker = '.')
plt.plot(AnglesR,states, linestyle='-', marker = '.')


plt.show()
