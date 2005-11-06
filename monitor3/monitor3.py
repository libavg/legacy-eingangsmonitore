#!/usr/bin/python
# -*- coding: utf-8 -*-

#TODO: Bessere Icons, korrekt eingefärbt

import sys, os, math
sys.path.append('/usr/local/lib/python2.4/site-packages/libavg')
import avg
from datetime import date

sys.path.append('../')
import anim

class Ad:
    def __init__(self, name, index, start_date, end_date, init_func):
        self.name = name
        self.index = index
        self.start_date = start_date
        self.end_date = end_date
        self.init_func = init_func

class starsoda_ad:
    def __init__(self):
        self.__curFrame=0
        self.__stern = Player.getElementByID("starsoda_stern")
        self.__flasche = Player.getElementByID("starsoda_flasche")
        self.__starsoda = Player.getElementByID("starsoda_starsoda")
        self.__taste = Player.getElementByID("starsoda_taste_of_time")
        anim.LinearAnim(self.__flasche, "x", 6600, -240, 765)
        Player.setTimeout(1200, lambda: setattr(self.__stern, "opacity", 0))
        Player.setTimeout(1900, lambda: setattr(self.__stern, "opacity", 1))
        Player.setTimeout(4700, lambda: setattr(self.__starsoda, "opacity", 1))
        Player.setTimeout(4700, 
                lambda: anim.LinearAnim(self.__starsoda, "x", 
                        5700, 351.0, 671.0))
        Player.setTimeout(5000, lambda: setattr(self.__taste, "opacity", 1))
        Player.setTimeout(5000, 
                lambda: anim.LinearAnim(self.__taste, "x", 
                        1700, 196, 316))
        Player.setTimeout(6300, lambda: anim.fadeOut(self.__taste, 400))
        Player.setTimeout(6350, lambda: anim.fadeOut(self.__starsoda, 400))
        Player.setTimeout(6700, self.__stop)
    def __stop(self):
        anim.fadeOut(Player.getElementByID("werbung"), 200) 
        Player.setTimeout(2000, init_werbung)

class cwars_ad:
    def __start_logo(self): 
        Player.getElementByID("c-wars").opacity = 1
        anim.fadeOut(Player.getElementByID("c-wars"), 3000)
        anim.LinearAnim(Player.getElementByID("c-wars"), "x", 5000, 66, 40) 
    def __start_words1(self): 
        anim.LinearAnim(Player.getElementByID("moon"), "opacity", 1000, 0.0, 1.0)
        anim.LinearAnim(Player.getElementByID("where_past"), 
                "opacity", 2000, 1.0, 0.0)
    def __start_words2(self):
        anim.LinearAnim(Player.getElementByID("meets_future"), 
                "opacity", 2000, 1.0, 0.0)
    def __start_url(self): 
        Player.getElementByID("www_c-wars_com").opacity = 1
        anim.fadeOut(Player.getElementByID("www_c-wars_com"), 1500)
    def __stop(self): 
        Player.getElementByID("trailer").opacity=0.0
        Player.getElementByID("trailer").stop()
        Player.getElementByID("moon").opacity = 1
        anim.fadeOut(Player.getElementByID("moon"), 500)
        Player.setTimeout(2000, init_werbung)
    def __init__(self):
        node = Player.getElementByID("trailer")
#        node.seekToFrame(0)
        node.play()
        node.opacity=1
        Player.setTimeout(2000, self.__start_logo)
        Player.setTimeout(3000, self.__start_words1)
        Player.setTimeout(4500, self.__start_words2)
        Player.setTimeout(6000, self.__start_url)
        Player.setTimeout(8500, self.__stop)
        

#def init_puppets_text()
#{
#  animateFloatAttr("puppets_text"+curTextIndex, "y", 109, 0, 1800);
#  animateFloatAttr("puppets_text"+curTextIndex, "opacity", 1, 0, 1500);
#}

#def move_puppets()
#{
#  curFrame++;
#  var puppets = Player.getElementByID("puppets");
#  var puppets_logo = Player.getElementByID("puppets_logo");
#  var curText;
#  var lastText;
#  switch(curFrame) {
#    case 20:
#      puppets.opacity=1;
#      break;
#    case 60:
#      puppets_logo.opacity=1;
#      break;
#    case 90:
#      curText = Player.getElementByID("puppets_text1");
#      curTextIndex=1;
#      init_puppets_text();
#      break;
#    case 120:
#    case 150:
#    case 180:
#    case 210:
#    case 240:
#    case 270:
#    case 300:
#      lastText = Player.getElementByID("puppets_text"+curTextIndex);
#      curTextIndex++;
#      curText = Player.getElementByID("puppets_text"+curTextIndex);
#      init_puppets_text();
#      break;
#    case 370:
#      puppets_logo.opacity=0;
#      break;
#    case 380:
#    case 385:
#      puppets.opacity=0;
#      break;
#    case 382:
#    case 387:
#      puppets.opacity=1;
#      break;
#    case 410:  
#      Player.getElementByID("werbung").opacity=0.0; 
#      Player.clearInterval(intervalID);
#      Player.setTimeout(2000, "init_werbung();");
#      break;
#  }
#  if (curFrame > 20 && curFrame <= 60) {
#     puppets.x += 3; 
#     var jumpPos=(curFrame-21)%13;
#     if (jumpPos > 6) {
#         jumpPos = 12-jumpPos;
#     }
#     var jumpHeight=60;
#     var y=5;
#     switch(jumpPos) {
#         case 0: 
#           puppets.x-=3;
#           break;
#         case 1:
#           y-=jumpHeight/8;
#           puppets.x-=3;
#           break;
#         case 2:
#           y-=jumpHeight/4;
#           break;
#         case 3:
#           y-=jumpHeight/2;
#           break;
#         case 4:
#           y-=3*jumpHeight/4;
#           break;
#         case 5:
#           y-=7*jumpHeight/8;
#           break;
#         case 6:
#           y-=jumpHeight;
#           break;
#     }
#     puppets.y = y;
#  }
#}

#def init_puppets()
#{
#  curFrame=0;
#  intervalID=Player.setInterval(10,"move_puppets();");
#  Player.getElementByID("werbung").opacity=1; 
#  Player.getElementByID("werbung_switch").activechild=1;
#  Player.getElementByID("puppets").opacity=0;
#  Player.getElementByID("puppets").x=360;
#  Player.getElementByID("puppets_logo").opacity=0;
#  Player.getElementByID("puppets_text1").opacity=0;
#  Player.getElementByID("puppets_text2").opacity=0;
#  Player.getElementByID("puppets_text3").opacity=0;
#  Player.getElementByID("puppets_text4").opacity=0;
#  Player.getElementByID("puppets_text5").opacity=0;
#  Player.getElementByID("puppets_text6").opacity=0;
#  Player.getElementByID("puppets_text7").opacity=0;
#  Player.getElementByID("puppets_text8").opacity=0;
#}

#def godzilla_appears() {
#    var godzilla=Player.getElementByID("godzilla");
#    godzilla.opacity=1;
#    animateFloatAttr("godzilla_group", "y", 200, 4, 600); 
#}

#def godzilla_shoots() {
#    var eyes=Player.getElementByID("eyes");
#    eyes.opacity=1;
#    var rays=Player.getElementByID("rays");
#    rays.opacity=1;
#    rays.angle=10;
#    rays.pivotx=378;
#    animateFloatAttr("rays", "angle", 10, 0, 300);
#}

#def show_title() {
#    var title=Player.getElementByID("title");
#    title.opacity=1;
#}

#def show_date() {
#    var title=Player.getElementByID("title");
#    title.opacity=0;
#    var date=Player.getElementByID("date");
#    date.opacity=1;
#}

#def fadeout() {
#    animateFloatAttr("city", "opacity", 1, 0, 300); 
#    animateFloatAttr("godzilla", "opacity", 1, 0, 300); 
#    animateFloatAttr("eyes", "opacity", 1, 0, 300); 
#    animateFloatAttr("rays", "opacity", 1, 0, 300); 
#    animateFloatAttr("date", "opacity", 1, 0, 1500); 
#}

#def init_mingle() {
#    print("init_mingle");
#    Player.getElementByID("werbung_switch").activechild=1;
#    animateFloatAttr("city", "opacity", 0, 1, 400);
#    animateFloatAttr("city", "x", 0, -250, 5000);
#    var godzilla_group=Player.getElementByID("godzilla_group");
#    godzilla_group.y=200;
#    Player.setTimeout(1000, "godzilla_appears()");
#    Player.setTimeout(2500, "godzilla_shoots()");
#    Player.setTimeout(3200, "show_title()");
#    Player.setTimeout(5000, "show_date()");
#    Player.setTimeout(5500, "fadeout()");
#    Player.setTimeout(8500, "init_werbung();");
#    Player.getElementByID("godzilla").opacity=0;
#    Player.getElementByID("eyes").opacity=0;
#    Player.getElementByID("rays").opacity=0;
#    Player.getElementByID("title").opacity=0;
#    Player.getElementByID("date").opacity=0;
#    Player.getElementByID("werbung").opacity=1.0; 
#}

#def stop_phneutral()
#{
#    animateFloatAttr("ph_neutral_logo", "opacity", 1, 0, 500);       
#    Player.setTimeout(2000, "init_werbung();");
#}

#def init_phneutral()
#{
#  curFrame=0;
#  animateFloatAttr("ph_neutral_logo", "opacity", 0, 1, 500);       
#  Player.getElementByID("ph_neutral_logo").play();
#  Player.setTimeout(10000, "stop_phneutral()");
#//  intervalID=Player.setInterval(10,"move_starsoda();");
#}

#def gmove(id,speed):
#    node = Player.getElementByID(id)
#    node.opacity=1
#    node.x += speed
#    if node.x > Player.getElementByID("gimp_main").width:
#        node.x = -300
#    if node.x < -300:
#        node.x = Player.getElementByID("gimp_main").width

#def stopGimpAnimation():
#    global intervalID
#    Player.setTimeout(2000, init_werbung)
#    Player.getElementByID("werbung").opacity = 0.0
#    Player.clearInterval(intervalID)

#def startGimpAnimation():
#    global intervalID
#    intervalID= Player.setInterval(27, lambda: gmove('gimp_title',9))
#    Player.setTimeout(8500, stopGimpAnimation)

adSchedule= [
#              Ad("phneutral", 3, date(2004,4,16), date(2004,4,23), init_phneutral),
              Ad("starsoda", 0, date(2002,4,16), date(2014,4,23), starsoda_ad)
#              Ad("meet and mingle", 1, date(2004,2,1), date(2004,3,1), init_mingle),
#              Ad("puppetmastaz", 2, date(2004,2,1), date(2004,3,1), init_puppets),
#              Ad("gimp", 4, date(2004,2,1), date(2014,10,1), startGimpAnimation)
#              Ad("c-wars", 5, date(2004,2,1), date(2014,10,1), cwars_ad)
            ]

curWerbung = 0

def init_werbung():
    global curWerbung
    global curAds
    curWerbung += 1
    curWerbung %= len(curAds)
    Player.getElementByID("werbung").opacity=1
    Player.getElementByID("werbung_switch").activechild = curAds[curWerbung].index
    curAds[curWerbung].init_func()

def init_cur_ads():
    global curAds
    print("Configured ads: ")
    curAds = []
    for curAd in adSchedule:
        print("startDate: " + str(curAd.start_date))
        print("endDate: " + str(curAd.end_date))
        if curAd.start_date <= date.today() and curAd.end_date >= date.today():
            curAds.append(curAd)
            print("  "+curAd.name)


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

Player.loadFile("monitor3.avg")
init_cur_ads()
anim.init(Player)
Player.setTimeout(100, init_werbung)
framerate = Player.getVideoRefreshRate()
if framerate < 60:
    framerate = 60
Player.play(framerate, 1)

