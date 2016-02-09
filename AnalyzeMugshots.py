import http.client, urllib.request, urllib.parse, urllib.error, base64, json, csv, time

headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': 'b6240136ea434fde8136bd256cc88906',
}

params = urllib.parse.urlencode({
    # Request parameters
    'returnFaceId': 'true',
    'returnFaceLandmarks': 'true',
    'returnFaceAttributes': 'age,gender,headPose,smile,facialHair',
})

body = {
    # Request parameters
    'url': 'http://previews.123rf.com/images/warrengoldswain/warrengoldswain1107/warrengoldswain110700246/9967759-Old-man-detailed-portrait-lots-of-wrinkles-Stock-Photo.jpg',
}
jsonDicts = []
f = open("data.txt","r")
i = 0
start = time.time() #Starting up timer
for line in f:
    i+=1 #Using numbers as json file names
    try:
        conn = http.client.HTTPSConnection('api.projectoxford.ai') #Establishing connection
        body['url'] = line #Changing url to current one in file
        conn.request("POST", "/face/v1.0/detect?%s" % params, str(body), headers) #Send request
        response = conn.getresponse() #get response in bytes
        data = response.read() #read in response to data
        #print(data) #prints the bytes data
        print(i)
        data = data.decode("utf-8") #converts bytes to string
        f = open(str(i) + '.json', 'w')
        #print >> f, 'Filename:', filename  # or f.write('...\n')
        f.write(str(data)) #writes string to file
        f.close() #closes file

        d = json.loads(str(data))
        jsonDicts.append(d)
       
        conn.close()

        if(i % 20 == 0):
            end = time.time()
            while((end - start) < 65):
                end = time.time()
            start = time.time()
        if(i == 1350):
            break
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))

w = csv.writer(open("output.csv", "w"))
for d in jsonDicts:
    for key, val in d.items():
        w.writerow([key, val])

####################################