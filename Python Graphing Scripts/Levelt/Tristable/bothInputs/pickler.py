import pickle
from numpy import *



noiselessSS = loadtxt('noiselessSSwideLong.dat', unpack=True)
noiseSS = loadtxt('noiseSSwideB.dat', unpack=True)

pickleFile = open("SSLong.pickle", "wb")
pickle.dump([noiselessSS, noiseSS], pickleFile)
pickleFile.close()
