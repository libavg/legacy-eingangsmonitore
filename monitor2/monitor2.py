#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys, os, math
sys.path.append('/usr/local/lib/python2.4/site-packages/libavg')
import avg

sys.path.append('../')
import anim

Player = avg.Player()
Log = avg.Logger.get()
bDebug = not(os.getenv('CLEUSE_DEPLOY'))
if (bDebug):
    Player.setResolution(0, 0, 0, 0) 
else:
    Player.setResolution(1, 0, 0, 0)
    Player.showCursor(0)
    Log.setDestination("//log/cleuse.log")
Log.setCategories(Log.APP |
                  Log.WARNING | 
                  Log.PROFILE |
#                 Log.PROFILE_LATEFRAMES |
                  Log.CONFIG |
#                 Log.MEMORY  |
#                 Log.BLTS    |
                  Log.EVENTS)

Player.loadFile("monitor2.avg")
anim.init(Player)
framerate = Player.getVideoRefreshRate()
if framerate < 60:
    framerate = 60
Player.play(framerate, 1)

