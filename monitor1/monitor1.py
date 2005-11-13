#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys, os, math, random
sys.path.append('/usr/local/lib/python2.4/site-packages/libavg')
import avg
from datetime import datetime, timedelta

sys.path.append('../')
import anim

curLine = 19

def newWelcome():
    global curLine
    node = Player.getElementByID("begruessungstext"+str(curLine))
    curLine += 1
    if curLine > Player.getElementByID("begruessungstext").getNumChildren():
        curLine = 1
    if curLine == 7 or curLine == 14:
        anim.LinearAnim(node, "x", 10000, -150, 800, newWelcome)
    else:
        anim.LinearAnim(node, "x", 11500, 800, -300, newWelcome)
        

def moveWelcome():
    global curLine
    node = Player.getElementByID("begruessungstext"+str(curLine))
    if curLine == 7 or curLine == 14:
        # Das sind die Zeilen, die nach rechts laufen.
        node.x += 90.0/framerate
        if node.x > 800:
            node.x = -150
            curLine += 1
        if curLine > Player.getElementByID("begruessungstext").getNumChildren():
            curLine = 1
    else:
        node.x -= 90.0/framerate
        if node.x < -300:
            node.x = 800
            curLine += 1
        if curLine > Player.getElementByID("begruessungstext").getNumChildren():
            curLine = 1

def normalize(v):
    v = v - int(v)
    if v < 0:
        v = v + 1
    return v

def calcMoonAge(year, mon, day):
    # calculate the Julian date at 12h UT
    YY = year - int((12-mon)/10)
    MM = mon+9 
    if MM >= 12:
        MM = MM - 12
    K1 = int(365.25*(YY+4712))
    K2 = int(30.6*MM+0.5)
    K3 = int(int((YY/100)+49)*0.75)-38
    
    JD = K1+K2+day+59          # for dates in Julian calendar
    if JD > 2299160:
        JD = JD - K3         # for Gregorian calendar
    # calculate moon's age in days
    IP = normalize((JD-2451550.1)/29.530588853)
    return int(IP*29.53)
    
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
    Player.getElementByID("secs_bis_start").text = secs+"S"+ms+"MS"

    timeVelocity += random.random()-0.5
    if timeVelocity > 2:
        timeVelocity -= 0.1
    elif timeVelocity < -2:
        timeVelocity += 0.1
    if timeVelocity > 5:
        timeVelocity -= 0.2
    elif timeVelocity < -5:
        timeVelocity += 0.2
    if random.random() > 0.9995:
        timeVelocity = random.random()*100-50 
    liftoffTime += timedelta(0,timeVelocity/framerate)

moonAge = -1

def calcMoon():
    global moonAge
    now = datetime.now().date()
    newMoonAge = calcMoonAge(now.year, now.month, now.day)
    if newMoonAge != moonAge:
        moonAge = newMoonAge
        moonNode = Player.getElementByID("mond")
        for i in range(0,moonNode.getNumChildren()):
            moonNode.getChild(i).opacity = 0
            moonNode.getChild(i).angle = 0
        if moonAge < 15:
            moonNode.getChild(moonAge).opacity = 1
        else:
            curNode = moonNode.getChild(29-moonAge)
            curNode.opacity = 1
            curNode.angle = 3.1415

def onframe():
#    moveWelcome()
    calcTime()
    calcMoon()

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
Player.setTimeout(10, newWelcome)
Player.getElementByID("bkgndvideo").opacity = 0.4
Player.getElementByID("bkgndvideo").play()
framerate = Player.getVideoRefreshRate()
if framerate < 60:
    framerate = 60
framerate = 30 
Player.play(30, 1)
