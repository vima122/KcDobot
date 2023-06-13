from library import *
connect()
home()
h = 25
for i in range(3):
    moveJ(205,-102,-112,0)
    suction(True)
    moveL(183,-195,-20,0)
    railMove(500)
    moveJ(160,-131,-111+(h*i),0)
    suction(False)
    moveL(183,-195,-20,0)
    railMove(100)