#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys, os, math
sys.path.append('/usr/local/lib/python2.4/site-packages/libavg')
import avg
from datetime import date

sys.path.append('../')
import anim

FRAMERATE = 60 
curLine = 1

def move_welcome():
    global curLine
    node = Player.getElementByID("begruessungstext"+str(curLine))
    node.x -= 90.0/FRAMERATE
    if node.x < -300:
        node.x = 800
        curLine += 1
    if curLine > 6:
        curLine = 1

Player = avg.Player()
Log = avg.Logger.get()
bDebug = not(os.getenv('CLEUSE_DEPLOY'))
if (bDebug):
    Player.setResolution(0, 0, 0, 0) 
else:
    Player.setResolution(1, 0, 0, 0)
    Player.showCursor(0)
    Log.setDestination("/var/log/cleuse.log")
Log.setCategories(Log.APP |
                  Log.WARNING | 
                  Log.PROFILE |
#                 Log.PROFILE_LATEFRAMES |
                  Log.CONFIG 
#                 Log.MEMORY  |
#                 Log.BLTS    |
#                  Log.EVENTS
                  )

Player.loadFile("monitor1.avg")
anim.init(Player)
Player.setInterval(10, move_welcome)
Player.play(FRAMERATE)

