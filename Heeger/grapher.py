from numpy import *
import matplotlib.pyplot as plt





Time,RL1,HL1,RR2,HR2,RF,HF,RB1,HB1,RB2,HB2,RBF,HBF,RA1,RA2,RAF,IVL,IVR,IVF,ANGLEVAL = loadtxt('slow.dat', unpack=True)




states =[]
times = []
durations = []
lastState = 'Left'
lastTime = 0
for i in range(len(Time)):
    if RB1[i] >= RBF[i] and RB1[i] >= RB2[i]:
        if lastState != 'Left':
            states.append(lastState)
            times.append(lastTime)
            durations.append(Time[i]-lastTime)
            lastTime = Time[i]
            lastState = 'Left'
    if RB2[i] >= RBF[i] and RB2[i] >= RB1[i]:
        if lastState != 'Right':
            states.append(lastState)
            times.append(lastTime)
            durations.append(Time[i]-lastTime)
            lastTime = Time[i]
            lastState = 'Right'
    if RBF[i] >= RB1[i] and RBF[i] >= RB2[i]:
        if lastState != 'Fusion':
            states.append(lastState)
            times.append(lastTime)
            durations.append(Time[i]-lastTime)
            lastTime = Time[i]
            lastState = 'Fusion'
states.append(lastState)
times.append(lastTime)
durations.append(Time[i]-lastTime)

RB1Duration=[]
RB1Starts=[]
RB2Duration=[]
RB2Starts=[]
RBFDuration=[]
RBFStarts=[]
for i in range(len(states)):
    if states[i]=='Left':
        RB1Duration.append(durations[i])
        RB1Starts.append(times[i])
    if states[i]=='Right':
        RB2Duration.append(durations[i])
        RB2Starts.append(times[i])
    if states[i]=='Fusion':
        RBFDuration.append(durations[i])
        RBFStarts.append(times[i])



plt.subplot(2,1,1)
plt.title('States over time')
plt.ylabel('State')

plt.barh(y='Left', left=RB1Starts, width=RB1Duration, color='red')
plt.barh(y='Right', left=RB2Starts, width=RB2Duration, color='blue')
plt.barh(y='Fusion', left=RBFStarts, width=RBFDuration, color='green')

plt.subplot(2,1,2)
plt.xlabel('Time (ms)')
plt.ylabel('Angle(degrees)')
plt.plot(Time, ANGLEVAL)

plt.show()
