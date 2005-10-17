#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys, os, math, random
sys.path.append('/usr/local/lib/python2.4/site-packages/libavg')
import avg
from datetime import datetime, timedelta

sys.path.append('../')
import anim

FRAMERATE = 60 
curLine = 1

def moveWelcome():
    global curLine
    node = Player.getElementByID("begruessungstext"+str(curLine))
    node.x -= 90.0/FRAMERATE
    if node.x < -300:
        node.x = 800
        curLine += 1
    if curLine > 6:
        curLine = 1

liftoffTime = datetime(2023,5,23)
timeVelocity = 0
lastMins = "" 

def calcTime():
    global liftoffTime, timeVelocity, lastMins
    now = datetime.now()
    dateString = "stationsceit:  "+now.date().isoformat()
    Player.getElementByID("stationsdatum").text = dateString
    timeString = now.time().isoformat()[0:8]
    Player.getElementByID("stationszeit").text = timeString
    timeToStart = liftoffTime-now
    # This isn't really correct, but who's going to notice...
    mins = "%(#)02d" % {'#': long((timeToStart.seconds%3600)/60)}
    if mins != lastMins:
        years = "%(#)02d" % {'#': long(timeToStart.days/365)}
        months = "%(#)02d" % {'#': long((timeToStart.days%365)/30)}
        days = "%(#)02d" % {'#': long(timeToStart.days%30)}
        hours = "%(#)02d" % {'#': long(timeToStart.seconds/3600)}
        startString = "P"+years+"Y"+months+"M"+days+"DT"+hours+"H"+mins+"M"
        Player.getElementByID("zeit_bis_start").text = startString
        lastMins = mins
    secs = "%(#)02d" % {'#': long(timeToStart.seconds%60)}
    ms = "%(#)03d" % {'#': long(timeToStart.microseconds/1000)}
    Player.getElementByID("secs_bis_start").text = secs+"S" #+ms+"MS"

    timeVelocity += random.random()-0.5
    if timeVelocity > 2:
        timeVelocity -= 0.1
    elif timeVelocity < -2:
        timeVelocity += 0.1
    if timeVelocity > 5:
        timeVelocity -= 0.2
    elif timeVelocity < -5:
        timeVelocity += 0.2
    if random.random() > 0.9998:
        timeVelocity = random.random()*100-50 
    liftoffTime += timedelta(0,timeVelocity/FRAMERATE)

def onframe():
    moveWelcome()
    calcTime()

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
Player.setInterval(10, onframe)
Player.play(FRAMERATE)

