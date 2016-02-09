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
'''
[
  {
    "faceId": "0134d17b-d7e1-41e9-9819-7c5a37795297",
    "faceRectangle": {
      "width": 166,
      "height": 166,
      "left": 187,
      "top": 145
    },
    "faceLandmarks": {
      "pupilLeft": {
        "x": 240.3,
        "y": 180.5
      },
      "pupilRight": {
        "x": 308.3,
        "y": 193.9
      },
      "noseTip": {
        "x": 289.2,
        "y": 233.5
      },
      "mouthLeft": {
        "x": 229.5,
        "y": 263
      },
      "mouthRight": {
        "x": 282.5,
        "y": 274.5
      },
      "eyebrowLeftOuter": {
        "x": 206.9,
        "y": 157.8
      },
      "eyebrowLeftInner": {
        "x": 279,
        "y": 170.8
      },
      "eyeLeftOuter": {
        "x": 225.8,
        "y": 173.1
      },
      "eyeLeftTop": {
        "x": 240.2,
        "y": 175.8
      },
      "eyeLeftBottom": {
        "x": 238.3,
        "y": 182.5
      },
      "eyeLeftInner": {
        "x": 253,
        "y": 181
      },
      "eyebrowRightInner": {
        "x": 299.9,
        "y": 175.4
      },
      "eyebrowRightOuter": {
        "x": 328.8,
        "y": 179.8
      },
      "eyeRightInner": {
        "x": 297.6,
        "y": 188
      },
      "eyeRightTop": {
        "x": 308.7,
        "y": 189.9
      },
      "eyeRightBottom": {
        "x": 305.2,
        "y": 196
      },
      "eyeRightOuter": {
        "x": 315.6,
        "y": 195
      },
      "noseRootLeft": {
        "x": 270.8,
        "y": 184.5
      },
      "noseRootRight": {
        "x": 294,
        "y": 188.2
      },
      "noseLeftAlarTop": {
        "x": 267.3,
        "y": 217.7
      },
      "noseRightAlarTop": {
        "x": 297,
        "y": 222.4
      },
      "noseLeftAlarOutTip": {
        "x": 255.1,
        "y": 228.2
      },
      "noseRightAlarOutTip": {
        "x": 299.3,
        "y": 234
      },
      "upperLipTop": {
        "x": 272.9,
        "y": 261.4
      },
      "upperLipBottom": {
        "x": 270.8,
        "y": 267.2
      },
      "underLipTop": {
        "x": 267.5,
        "y": 269.9
      },
      "underLipBottom": {
        "x": 264.4,
        "y": 279.5
      }
    },
    "faceAttributes": {
      "age": 29.7,
      "gender": "male",
      "headPose": {
        "roll": 8.1,
        "yaw": 31.9,
        "pitch": 0
      },
      "smile": 0.001,
      "facialHair": {
        "moustache": 0,
        "beard": 0.5,
        "sideburns": 0
      }
    }
  }
]
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

mEyeDistance = 0
fEyeDistance = 0
avgEyeDistance = 0

mEyeYLoc = 0
fEyeYLoc = 0
avgEyeYLoc = 0

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




        eyeDistance = data["faceLandmarks"]["eyeRightInner"]["x"] - data["faceLandmarks"]["eyeLeftInner"]["x"] 
        eyeDistance = eyeDistance/ data["faceRectangle"]["width"]
        if(male):
            mEyeDistance+=eyeDistance
        else:
            fEyeDistance+=eyeDistance
        avgEyeDistance += eyeDistance

        '''
          "faceRectangle": {
      "width": 166,
      "height": 166,
      "left": 187,
      "top": 145
    },'''

        eyeYLoc = data["faceLandmarks"]["eyeRightTop"]["y"] - data["faceRectangle"]["top"]
        eyeYLoc = eyeYLoc/ data["faceRectangle"]["height"]
        if(male):
            mEyeYLoc+=eyeYLoc
        else:
            fEyeYLoc+=eyeYLoc
        avgEyeYLoc += eyeYLoc

        #fAge += data["faceAttributes"]["age"]
        rolls +=data["faceAttributes"]["headPose"]["roll"]
        pitches += data["faceAttributes"]["headPose"]["pitch"]
        yaws += data["faceAttributes"]["headPose"]["yaw"]


        if(i == 1350):
            break;
        #print(i)
        w.close()
        i+=1
        n+=1
    except Exception as e:
        i+=1
        print("[Errno {0}] {1}".format(e.errno, e.strerror))
        errors+=1
print( "M:" + str(males/n))
print("F:" + str(females/n))
print("MOUST:" + str(moustaches/males))
print("BEARD:" + str(beards/males))
print("SMILES(M):" + str(mSmiles) + " SMILES(F):" + str(fSmiles) + " TOTAL SMILES:" + str(fSmiles + mSmiles))
print("AVG AGE(M):" + str(mAge/males) + " AVG AGE(F):" + str(fAge/females) + " AVG AGE:" + str( ((mAge + fAge)/n) ))
print("AVG EYE DIST(M):" + str(mEyeDistance/males) + " AVG EYE DIST(F):" + str(fEyeDistance/females) + " AVG EYE DIST:" + str(avgEyeDistance/n) )
print("AVG EYE Y Location(M):" + str(mEyeYLoc/males) + " AVG EYE Y Location(F):" + str(fEyeYLoc/females) + " AVG EYE Y Location:" + str(avgEyeYLoc/n) )
print("ROLL:" + str(rolls/n) + "\nYaw:" + str(yaws/n) + "\nPITCH:" + str(pitches/n)) 
print(str(errors) + " Errors")



y1 = [males, mSmiles, mAge/males, mEyeDistance/males * 100, mEyeYLoc/males * 100]
y2 = [females, fSmiles, fAge/females, fEyeDistance/females * 100, fEyeYLoc/females * 100]

N = len(y1)
ind = np.arange(N)    # the x locations for the groups
width = 0.2       # the width of the bars: can also be len(x) sequence

#ind is the x coordinates of the left sides of the bars
#second is a list containing all values of bars
#third is the width of each bar
#And the 4th is color
plt.bar(ind, y1 , width, color=[.949, .055, .055])
plt.bar(ind + .2, y2 , width, color=[.11, .224, .643])

#label of y axis

#plt.ylabel('# of Arrests')

#title of graph
plt.title('Mugshot Stats')

#distance between markers of x-axis
#second argument are x labels for each marker
plt.xticks(ind + .2, ["Population","Smiles","Avg Age","Avg Eye Dist (%)", "Avg Eye Y (%)"])



plt.show()