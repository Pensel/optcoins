import pickle

hashrate = input("Bitte gib hier deine Hashrate in Megahashes ein und bestätige mit Enter! \n")
hashrate *= 1000

print(hashrate)

pickle.dump(hashrate, "config.cfg")