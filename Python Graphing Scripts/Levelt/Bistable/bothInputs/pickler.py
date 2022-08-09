import pickle
from numpy import *



noiselessSS = loadtxt('noiselessSSwideB.dat', unpack=True)
noiseSS = loadtxt('noiseSSwideB.dat', unpack=True)

pickleFile = open("SSB.pickle", "wb")
pickle.dump([noiselessSS, noiseSS], pickleFile)
pickleFile.close()
