from numpy import *
import matplotlib.pyplot as plt





Time, n1, n2, n3, RL1,HL1,RR2,HR2,RF,HF,RB1,HB1,RB2,HB2,RBF,HBF,RA1,RA2,RAF,IVL,IVR,IVF,ANGLEVAL = loadtxt('50_0_10000.dat', unpack=True)

states =[]
biStates=[]
angles = []
durations = []
lastState = ''
tristable = False
lastAngle = 0
for i in range(50,len(ANGLEVAL)):
    if RB1[i] >= RBF[i] and RB1[i] >= RB2[i]:
        if lastState != 'Left':
            states.append(lastState)
            angles.append(lastAngle)
            durations.append(ANGLEVAL[i]-lastAngle)
            lastAngle = ANGLEVAL[i]
            lastState = 'Left'
    if RB2[i] >= RBF[i] and RB2[i] >= RB1[i]:
        if lastState != 'Right':
            states.append(lastState)
            angles.append(lastAngle)
            durations.append(ANGLEVAL[i]-lastAngle)
            lastAngle = ANGLEVAL[i]
            lastState = 'Right'
    if RBF[i] >= RB1[i] and RBF[i] >= RB2[i]:
        if lastState != 'Fusion':
            states.append(lastState)
            angles.append(lastAngle)
            durations.append(ANGLEVAL[i]-lastAngle)
            lastAngle = ANGLEVAL[i]
            lastState = 'Fusion'
            tristable = True
    if not tristable:
        biStates.append(1)
    else:
        biStates.append(0)


states.append(lastState)
angles.append(lastAngle)
durations.append(ANGLEVAL[i]-lastAngle)

RB1Duration=[]
RB1Starts=[]
RB2Duration=[]
RB2Starts=[]
RBFDuration=[]
RBFStarts=[]

for i in range(len(states)):
    if states[i]=='Left':
        RB1Duration.append(durations[i])
        RB1Starts.append(angles[i])
    if states[i]=='Right':
        RB2Duration.append(durations[i])
        RB2Starts.append(angles[i])
    if states[i]=='Fusion':
        RBFDuration.append(durations[i])
        RBFStarts.append(angles[i])


TimeR, n1, n2, n3, RL1,HL1,RR2,HR2,RF,HF,RB1,HB1,RB2,HB2,RBF,HBF,RA1,RA2,RAF,IVL,IVR,IVF,ANGLEVALR = loadtxt('0_50_10000.dat', unpack=True)


statesR =[]
biStatesR=[]
anglesR = []
durationsR = []
lastStateR = 'Fusion'
tristableR = True
lastAngleR = 0
for i in range(50,len(ANGLEVALR)):
    if RB1[i] >= RBF[i] and RB1[i] >= RB2[i]:
        if lastStateR != 'Left':
            statesR.append(lastStateR)
            anglesR.append(lastAngleR)
            durationsR.append(ANGLEVALR[i]-lastAngleR)
            lastAngleR = ANGLEVALR[i]
            lastStateR = 'Left'
            tristableR = False
    if RB2[i] >= RBF[i] and RB2[i] >= RB1[i]:
        if lastStateR != 'Right':
            statesR.append(lastStateR)
            anglesR.append(lastAngleR)
            durationsR.append(ANGLEVALR[i]-lastAngleR)
            lastAngleR = ANGLEVALR[i]
            lastStateR = 'Right'
            tristableR = False
    if RBF[i] >= RB1[i] and RBF[i] >= RB2[i]:
        if lastStateR != 'Fusion':
            statesR.append(lastStateR)
            anglesR.append(lastAngleR)
            durationsR.append(ANGLEVALR[i]-lastAngleR)
            lastAngleR = ANGLEVALR[i]
            lastStateR = 'Fusion'
    if not tristableR:
        biStatesR.append(1.03)
    else:
        biStatesR.append(0.03)


statesR.append(lastStateR)
anglesR.append(lastAngleR)
durationsR.append(ANGLEVALR[i]-lastAngleR)

RB1DurationR=[]
RB1StartsR=[]
RB2DurationR=[]
RB2StartsR=[]
RBFDurationR=[]
RBFStartsR=[]
for i in range(len(statesR)):
    if statesR[i]=='Left':
        RB1DurationR.append(durationsR[i])
        RB1StartsR.append(anglesR[i])
    if statesR[i]=='Right':
        RB2DurationR.append(durationsR[i])
        RB2StartsR.append(anglesR[i])
    if statesR[i]=='Fusion':
        RBFDurationR.append(durationsR[i])
        RBFStartsR.append(anglesR[i])




plt.subplot(3,1,3)
plt.xlabel('Angle(degrees)')
plt.ylabel('State')
plt.xlim([0, 50])
plt.plot(ANGLEVAL[50:], biStates, linestyle='-', color = 'blue')
plt.plot(ANGLEVALR[50:],biStatesR, linestyle='-', color = 'red')


plt.subplot(3,1,1)
plt.xlim([0, 50])
plt.title('States over time (2.5 S)')
plt.ylabel('State')

plt.barh(y='Left', left=RB1Starts, width=RB1Duration, color='red')
plt.barh(y='Right', left=RB2Starts, width=RB2Duration, color='blue')
plt.barh(y='Fusion', left=RBFStarts, width=RBFDuration, color='green')


plt.subplot(3,1,2)
plt.xlim([0, 50])
plt.ylabel('State')

plt.barh(y='Left', left=RB1StartsR, width=RB1DurationR, color='red')
plt.barh(y='Right', left=RB2StartsR, width=RB2DurationR, color='blue')
plt.barh(y='Fusion', left=RBFStartsR, width=RBFDurationR, color='green')


plt.show()
