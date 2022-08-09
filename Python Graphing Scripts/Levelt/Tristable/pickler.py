import pickle
from numpy import *



noiselessSS = loadtxt('noiselessSSwide.dat', unpack=True)
noiseSS = loadtxt('noiseSSwide.dat', unpack=True)

pickleFile = open("SS.pickle", "wb")
pickle.dump([noiselessSS, noiseSS], pickleFile)
pickleFile.close()
