import pickle
fp = open("picklefile.txt", "wb")
sn = ["Dhoni","virat","Dhawan"]
pickle.dump(sn,fp)
fp.close()
