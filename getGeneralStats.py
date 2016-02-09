import json
import os.path
import numpy as np
import matplotlib.pyplot as plt
'''
"faceAttributes": {"gender": "female", 
"facialHair": {"sideburns": 0.0, "beard": 0.0, "moustache": 0.0}, 
"smile": 0.005, "age": 42.4, 
"headPose": {"roll": 8.2, "yaw": -0.5, "pitch": 0.0}}}'
'''
i = 10
females = 0

males = 0
sideburns = 0
beards = 0
moustaches = 0

mSmiles = 0
fSmiles = 0

mAge = 0
fAge = 0

rolls = 0
yaws = 0
pitches = 0



errors=0
n=0

male = False



while os.path.isfile(str(i) + ".json"): 
    w = open(str(i) + ".json","r")
    data = w.readline()
    try:
        data = json.loads(str(data))
        if(len(data) == 0):
            i+=1
            continue
        data = data[0]
        if( data["faceAttributes"]["gender"] == "male" ):
            male = True
            males +=1
        else:
            male = False
            females +=1

        if( data["faceAttributes"]["facialHair"]["beard"] > .5 ):
            beards +=1

        if( data["faceAttributes"]["facialHair"]["moustache"] > .5 ):
            moustaches +=1

        if( "smile" in data["faceAttributes"] and data["faceAttributes"]["smile"] > .2 ):
            if(male):
                mSmiles +=1
            else:
                fSmiles +=1

        if(male):
            mAge += data["faceAttributes"]["age"]
        else:
            fAge += data["faceAttributes"]["age"]
            
        #print(i)
        w.close()
        i+=1
        n+=1
    except Exception as e:
        i+=1
        #print("Error")
        errors+=1
print( "M:" + str(males/n))
print("F:" + str(females/n))
print("MOUST:" + str(moustaches/males))
print("BEARD:" + str(beards/males))
print("SMILES(M):" + str(mSmiles/males) + " SMILES(F):" + str(fSmiles/females))
print("AVG AGE(M):" + str(mAge/males) + "AVG AGE(F):" + str(fAge/females) + "AVG AGE:" + str( ((mAge + fAge)/n) ))
print(str(errors) + " Errors")

print(i)



y1 = [males,mSmiles,mAge/males]
y2 = [females,fSmiles,fAge/females]

N = len(y1)
ind = np.arange(N)    # the x locations for the groups
width = 0.2       # the width of the bars: can also be len(x) sequence

#ind is the x coordinates of the left sides of the bars
#second is a list containing all values of bars
#third is the width of each bar
#And the 4th is color
plt.bar(ind, y1 , width, color='r')
plt.bar(ind + .2, y2 , width, color='b')

#label of y axis

#plt.ylabel('# of Arrests')

#title of graph
plt.title('MugShot Stats')

#distance between markers of x-axis
#second argument are x labels for each marker
plt.xticks(ind + .2, ["Population","Smiles","Average Age"])

plt.show()