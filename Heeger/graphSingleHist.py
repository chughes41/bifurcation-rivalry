from numpy import *
import matplotlib.pyplot as plt
import statistics





Time, n1, n2, n3, RL1,HL1,RR2,HR2,RF,HF,RB1,HB1,RB2,HB2,RBF,HBF,RA1,RA2,RAF,IVL,IVR,IVF,ANGLEVAL = loadtxt('histogramTest10.dat', unpack=True)

states =[]
biStates=[]
Times = []
durations = []
lastState = ''
tristable = False
lastTime = 0
for i in range(50,len(Time)):
    if RB1[i] >= RBF[i] and RB1[i] >= RB2[i]:
        if lastState != 'Left':
            states.append(lastState)
            Times.append(lastTime)
            durations.append(Time[i]-lastTime)
            lastTime = Time[i]
            lastState = 'Left'
    if RB2[i] >= RBF[i] and RB2[i] >= RB1[i]:
        if lastState != 'Right':
            states.append(lastState)
            Times.append(lastTime)
            durations.append(Time[i]-lastTime)
            lastTime = Time[i]
            lastState = 'Right'
    if RBF[i] >= RB1[i] and RBF[i] >= RB2[i]:
        if lastState != 'Fusion':
            states.append(lastState)
            Times.append(lastTime)
            durations.append(Time[i]-lastTime)
            lastTime = Time[i]
            lastState = 'Fusion'
            tristable = True
    if not tristable:
        biStates.append(1)
    else:
        biStates.append(0)


states.append(lastState)
Times.append(lastTime)
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
        RB1Starts.append(Times[i])
    if states[i]=='Right':
        RB2Duration.append(durations[i])
        RB2Starts.append(Times[i])
    if states[i]=='Fusion':
        RBFDuration.append(durations[i])
        RBFStarts.append(Times[i])

lengths = []
lastTime = 0
lastState = 'test'
for i in range(len(Times)):
    if((Times[i]-lastTime)>400):
        if(states[i]==lastState and lastState != 'test'):
            curTime = lengths.pop()
            lengths.append((Times[i]-lastTime + curTime)/1000)
        else:
            lengths.append((Times[i]-lastTime)/1000)
        lastState = states[i]
        lastTime = Times[i]

# Creating histogram
binwidth = 0.1
fig, ax = plt.subplots(figsize =(10, 7))
ax.hist(lengths, bins=arange(min(lengths), max(lengths) + binwidth, binwidth))

print(statistics.mean(lengths),statistics.stdev(lengths))

# Show plot
plt.show()
