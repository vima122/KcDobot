import DobotDllType as dType
CON_STR = {
    dType.DobotConnect.DobotConnect_NoError:  "Dobot Connected",
    dType.DobotConnect.DobotConnect_NotFound: "Dobot Not Found",
    dType.DobotConnect.DobotConnect_Occupied: "Dobot Occupied"}

def connect():
    global api
    api = dType.load()
    state = dType.ConnectDobot(api, "", 115200)[0]
    dType.SetDeviceWithL(api, True)
    dType.SetQueuedCmdClear(api)
    dType.SetQueuedCmdStartExec(api)
    return CON_STR[state]
    
def disconnect():
    dType.DisconnectDobot(api)
    
def moveJ(x,y,z,r):
    dType.SetPTPCmd(api, 1, x, y, z, r, 1)
def moveL(x,y,z,r):
    dType.SetPTPCmd(api, 2, x, y, z, r, 1)
def jump(x,y,z,r):
    dType.SetPTPCmd(api, 0, x, y, z, r, 1)
def jumpHeight(n):
    dType.SetPTPJumpParams(api, n, 100, isQueued=0)
def suction(b):
    if b == True:
        b = 1
    elif b == False:
        b = 0
    dType.SetEndEffectorSuctionCup(api, 1,  b, 1)
def gripper(b):
    if b == True:
        dType.SetEndEffectorGripper(api, 1,  1, 1)
    elif b == False:
        dType.SetEndEffectorGripper(api, 0,  0, 1)
def laser(b):
    if b == True:
        b = 1
    elif b == False:
        b = 0
    dType.SetEndEffectorLaser(api, b,  b, isQueued=0)
def sleep(ms):
    dType.dSleep(ms)
def convMove(s):
    dType.SetEMotor(api, 0, 1, s, 1)
def convDist(s,d):
    dType.SetEMotorS(api, 0, 1, s, d, 1)
def getColor():
    dType.SetColorSensor(api, 1, 2, version=2)
    color = dType.GetColorSensor(api)
    if color == [1,0,0]:
        return "red"
    elif color == [0,1,0]:
        return "blue"
    elif color == [0,0,1]:
        return "green"
def getSensor():
    dType.SetInfraredSensor(api,  1, 4, version=2)
    if dType.GetInfraredSensor(api, 4) == 1:
        return True
    else:
        return False
def railMove(c):
    current_pose = dType.GetPose(api)
    dType.SetPTPWithLCmd(api, 1, current_pose[0], current_pose[1], current_pose[2], current_pose[3], c, 1)
def getRailMove():
    return dType.GetPoseL(api)
    
def home():
    dType.SetHOMECmd(api, 1, 1)
def getPose():
    return dType.GetPose(api)