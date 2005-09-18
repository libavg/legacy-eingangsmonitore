#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys, os, math, subprocess
sys.path.append('/usr/local/lib/python2.4/site-packages/libavg')
import avg

sys.path.append('../')
import anim

FRAMERATE = 75 

timeCount = 0

def move_graphs():
    global timeCount
    timeCount += 1
    node1 = Player.getElementByID("ceit_graph1")
    node2 = Player.getElementByID("ceit_graph2")
    node1.x -= 1
    if node1.x == -500:
        node1.x = 500
    node2.x -= 1
    if node2.x == -500:
        node2.x = 500
        
curMessage=0
messages=["es ist mal wieder ceit cu fegen", 
          "cugang combiosc inactiv",
          "c_wercraftfluctuation",
	      "magnetic_es feld activ",
	      "nerdc_leuder activ. bitte beachten sie die sicherheitshinweise." ]
curLine=0

def move_message():
    global messageInterval
    node = Player.getElementByID("hinweis"+str(curLine))
    node.x-= 150/FRAMERATE
    if node.x < -300:
        Player.clearInterval(messageInterval)
        node.x = 800

def new_message():
    global curLine
    global curMessage
    global messageInterval
    curLine += 2
    if curLine == 4:
        curLine = 1
    elif curLine == 5:
        curLine = 2 
    curMessage += 1
    if curMessage == 5:
        curMessage = 0
    Player.getElementByID("hinweis_icon"+str(curLine)).activechild = curMessage
    Player.getElementByID("hinweis_text"+str(curLine)).text = messages[curMessage]
    messageInterval = Player.setInterval(10, move_message)

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
Player.setInterval(10, move_graphs)
Player.setInterval(10000, new_message)
Player.play(FRAMERATE)

