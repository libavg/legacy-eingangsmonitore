#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys, os, math
sys.path.append('/usr/local/lib/python2.4/site-packages/libavg')
import avg
from datetime import date

sys.path.append('../')
import anim

FRAMERATE = 15
timeCount = 0

def move_graphs():
    global timeCount
    timeCount += 1
    node1 = Player.getElementByID("athmo_data_1")
    node2 = Player.getElementByID("athmo_data_2")
    node1.x -= 1
    if node1.x == -400:
        node1.x = 400
    node2.x -= 1
    if node2.x == -400:
        node2.x = 400
    
    if timeCount % 2 == 0:
        node1 = Player.getElementByID("lf_data_1")
        node2 = Player.getElementByID("lf_data_2")
        node1.x -= 1
        if node1.x == -400:
            node1.x = 400
        node2.x -= 1
        if node2.x == -400:
            node2.x = 400

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
                  Log.CONFIG |
#                 Log.MEMORY  |
#                 Log.BLTS    |
                  Log.EVENTS)

Player.loadFile("monitor3.avg")
anim.init(Player)
Player.setInterval(10, move_graphs)
Player.play(FRAMERATE)

