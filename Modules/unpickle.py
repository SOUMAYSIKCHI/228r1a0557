import pickle
fp = open("picklefile.txt", "rb")
unpick = pickle.load(fp)
print(unpick)
