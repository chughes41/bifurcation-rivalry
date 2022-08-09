import pickle
from numpy import *
import matplotlib.pyplot as plt
import matplotlib


twoParam = loadtxt('PlotsFinal/2Param.dat', unpack=True)
twoParamSecond = loadtxt('PlotsFinal/2ParamCurve.dat', unpack=True)
twoParamThird = loadtxt('PlotsFinal/2Param3rd.dat', unpack=True)
twoParamFourth = loadtxt('PlotsFinal/2Param4th.dat', unpack=True)
twoParamFifth = loadtxt('PlotsFinal/2Param5th.dat', unpack=True)
twoParamSixth = loadtxt('PlotsFinal/2Param6th.dat', unpack=True)
twoParamSeventh = loadtxt('PlotsFinal/2Param7th.dat', unpack=True)
twoParamEighth = loadtxt('PlotsFinal/2Param8th.dat', unpack=True)
twoParamNinth = loadtxt('PlotsFinal/2Param9th.dat', unpack=True)
plt.scatter(twoParamThird[1], twoParamThird[0])
plt.scatter(twoParamFourth[0], twoParamFourth[1])
plt.scatter(twoParamEighth[0], twoParamEighth[1])
#plt.scatter(twoParamSixth[0], twoParamSixth[1])
#plt.scatter(twoParamSeventh[0], twoParamSeventh[1])
plt.scatter(twoParamNinth[0], twoParamNinth[1])
plt.xlim(0,3.5)
plt.ylim(0,1)
plt.xlabel("wa")
plt.ylabel("wo")
plt.show()
