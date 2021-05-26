import datetime, time
global deltaTime, currentTime
deltaTime = 0
currentTime = time.time()

def calculate_DeltaTime():
    global deltaTime, currentTime
    #print(currentTime, deltaTime)
    c = time.time()
    deltaTime = c-currentTime
    currentTime = c