
use("../common.js");


function init_video() 
{
  var node = AVGPlayer.getElementByID("rotation");
  node.play();
}

var curLine = 1;

function move_welcome()
{
  var node = AVGPlayer.getElementByID("begruessungstext"+curLine);
  node.x-=5;
  if (node.x < -300) {
    node.x = 700;
    curLine++;
    if (curLine > 3) {
      curLine = 1;
    }
  }
}

var curFrame;
var intervalID;

function move_starsoda()
{
  curFrame++;
  
  var flasche = AVGPlayer.getElementByID("starsoda_flasche");
  flasche.x +=10;
  var stern = AVGPlayer.getElementByID("starsoda_stern");
  var starsoda = AVGPlayer.getElementByID("starsoda_starsoda");
  var taste = AVGPlayer.getElementByID("starsoda_taste_of_time");
  switch(curFrame) {
    case 18: 
      stern.opacity=0;
      break;
    case 28:
      stern.opacity=1;
      break;
    case 70:
      starsoda.opacity=1;
      break;
    case 75:
      taste.opacity=1;
      break;
    case 95:
      starsoda.opacity=0;
      taste.opacity=0;
      break;
    case 100:
      flasche.x = -230;
      AVGPlayer.getElementByID("topscreen").opacity=0.0; 
      AVGPlayer.clearInterval(intervalID);
      AVGPlayer.setTimeout(2000, "init_werbung();");
      break;
  }
  if (curFrame > 70) {
    starsoda.x+=4;
  }
  if (curFrame > 75) {
    taste.x+=6;
  }
}

function init_starsoda()
{
  curFrame=0;
  intervalID=AVGPlayer.setInterval(10,"move_starsoda();");
  AVGPlayer.getElementByID("starsoda_starsoda").x=351;
  AVGPlayer.getElementByID("starsoda_taste_of_time").x=196;
}

var curTextIndex;
/*
function init_puppets_text()
{
  animateFloatAttr("puppets_text"+curTextIndex, "y", 109, 0, 1800);
  animateFloatAttr("puppets_text"+curTextIndex, "opacity", 1, 0, 1500);
}

function move_puppets()
{
  curFrame++;
  var puppets = AVGPlayer.getElementByID("puppets");
  var puppets_logo = AVGPlayer.getElementByID("puppets_logo");
  var curText;
  var lastText;
  switch(curFrame) {
    case 20:
      puppets.opacity=1;
      break;
    case 60:
      puppets_logo.opacity=1;
      break;
    case 90:
      curText = AVGPlayer.getElementByID("puppets_text1");
      curTextIndex=1;
      init_puppets_text();
      break;
    case 120:
    case 150:
    case 180:
    case 210:
    case 240:
    case 270:
    case 300:
      lastText = AVGPlayer.getElementByID("puppets_text"+curTextIndex);
      curTextIndex++;
      curText = AVGPlayer.getElementByID("puppets_text"+curTextIndex);
      init_puppets_text();
      break;
    case 370:
      puppets_logo.opacity=0;
      break;
    case 380:
    case 385:
      puppets.opacity=0;
      break;
    case 382:
    case 387:
      puppets.opacity=1;
      break;
    case 410:  
      AVGPlayer.getElementByID("topscreen").opacity=0.0; 
      AVGPlayer.clearInterval(intervalID);
      AVGPlayer.setTimeout(2000, "init_werbung();");
      break;
  }
  if (curFrame > 20 && curFrame <= 60) {
     puppets.x += 3; 
     var jumpPos=(curFrame-21)%13;
     if (jumpPos > 6) {
         jumpPos = 12-jumpPos;
     }
     var jumpHeight=60;
     var y=5;
     switch(jumpPos) {
         case 0: 
           puppets.x-=3;
           break;
         case 1:
           y-=jumpHeight/8;
           puppets.x-=3;
           break;
         case 2:
           y-=jumpHeight/4;
           break;
         case 3:
           y-=jumpHeight/2;
           break;
         case 4:
           y-=3*jumpHeight/4;
           break;
         case 5:
           y-=7*jumpHeight/8;
           break;
         case 6:
           y-=jumpHeight;
           break;
     }
     puppets.y = y;
  }
}

function init_puppets()
{
  curFrame=0;
  intervalID=AVGPlayer.setInterval(10,"move_puppets();");
  AVGPlayer.getElementByID("topscreen").opacity=1; 
  AVGPlayer.getElementByID("werbung_switch").activechild=1;
  AVGPlayer.getElementByID("puppets").opacity=0;
  AVGPlayer.getElementByID("puppets").x=360;
  AVGPlayer.getElementByID("puppets_logo").opacity=0;
  AVGPlayer.getElementByID("puppets_text1").opacity=0;
  AVGPlayer.getElementByID("puppets_text2").opacity=0;
  AVGPlayer.getElementByID("puppets_text3").opacity=0;
  AVGPlayer.getElementByID("puppets_text4").opacity=0;
  AVGPlayer.getElementByID("puppets_text5").opacity=0;
  AVGPlayer.getElementByID("puppets_text6").opacity=0;
  AVGPlayer.getElementByID("puppets_text7").opacity=0;
  AVGPlayer.getElementByID("puppets_text8").opacity=0;
}
*/

function godzilla_appears() {
    var godzilla=AVGPlayer.getElementByID("godzilla");
    godzilla.opacity=1;
    animateFloatAttr("godzilla_group", "y", 200, 4, 600); 
}

function godzilla_shoots() {
    var eyes=AVGPlayer.getElementByID("eyes");
    eyes.opacity=1;
    var rays=AVGPlayer.getElementByID("rays");
    rays.opacity=1;
    rays.angle=10;
    rays.pivotx=378;
    animateFloatAttr("rays", "angle", 10, 0, 300);
}

function show_title() {
    var title=AVGPlayer.getElementByID("title");
    title.opacity=1;
}

function show_date() {
    var title=AVGPlayer.getElementByID("title");
    title.opacity=0;
    var date=AVGPlayer.getElementByID("date");
    date.opacity=1;
}

function fadeout() {
    animateFloatAttr("city", "opacity", 1, 0, 300); 
    animateFloatAttr("godzilla", "opacity", 1, 0, 300); 
    animateFloatAttr("eyes", "opacity", 1, 0, 300); 
    animateFloatAttr("rays", "opacity", 1, 0, 300); 
    animateFloatAttr("date", "opacity", 1, 0, 1500); 
}

function init_mingle() {
    print("init_mingle");
    AVGPlayer.getElementByID("werbung_switch").activechild=1;
    animateFloatAttr("city", "opacity", 0, 1, 400);
    animateFloatAttr("city", "x", 0, -250, 5000);
    var godzilla_group=AVGPlayer.getElementByID("godzilla_group");
    godzilla_group.y=200;
    AVGPlayer.setTimeout(1000, "godzilla_appears()");
    AVGPlayer.setTimeout(2500, "godzilla_shoots()");
    AVGPlayer.setTimeout(3200, "show_title()");
    AVGPlayer.setTimeout(5000, "show_date()");
    AVGPlayer.setTimeout(5500, "fadeout()");
    AVGPlayer.setTimeout(8500, "init_werbung();");
    AVGPlayer.getElementByID("godzilla").opacity=0;
    AVGPlayer.getElementByID("eyes").opacity=0;
    AVGPlayer.getElementByID("rays").opacity=0;
    AVGPlayer.getElementByID("title").opacity=0;
    AVGPlayer.getElementByID("date").opacity=0;
    AVGPlayer.getElementByID("topscreen").opacity=1.0; 
}

function stop_phneutral()
{
    animateFloatAttr("ph_neutral_logo", "opacity", 1, 0, 500);       
    AVGPlayer.setTimeout(2000, "init_werbung();");
}

function init_phneutral()
{
  curFrame=0;
  animateFloatAttr("ph_neutral_logo", "opacity", 0, 1, 500);       
  AVGPlayer.getElementByID("ph_neutral_logo").play();
  AVGPlayer.setTimeout(10000, "stop_phneutral()");
//  intervalID=AVGPlayer.setInterval(10,"move_starsoda();");
}

function gmove(id,speed)
{
    var node = AVGPlayer.getElementByID(id);
    node.opacity=1;
	node.x = node.x+speed;
	if (node.x > 
        AVGPlayer.getElementByID("gimp_main").width) 
	{
		node.x = -300;
	}
	if (node.x < -300) 
	{
		node.x = 
            AVGPlayer.getElementByID("gimp_main").width;
	}
}

function stopGimpAnimation()
{
    AVGPlayer.setTimeout(2000, "init_werbung();");
    AVGPlayer.getElementByID("topscreen").opacity = 0.0;
    AVGPlayer.clearInterval(intervalID);
}

function startGimpAnimation()
{
	intervalID= AVGPlayer.setInterval(27,"gmove('gimp_title',9);");
    AVGPlayer.setTimeout(8500, "stopGimpAnimation()");
}

var curWerbung=0;

var adSchedule=[{name:"phneutral", index: 3,
                 startDate:new Date(2004,4,16), endDate:new Date(2004,4,23), 
                 func:"init_phneutral()"},
                {name:"starsoda", index:0, 
                 startDate:new Date(2002,4,16), endDate:new Date(2014,4,23), 
                 func:"init_starsoda()"},
                {name:"meet and mingle", index:1,
                 startDate:new Date(2004,2,1), endDate:new Date(2004,3,1), 
                 func:"init_mingle()"},
                {name:"puppetmastaz", index:2,
                 startDate:new Date(2004,2,1), endDate:new Date(2004,3,1), 
                 func:"init_puppets()"},
                {name:"gimp", index:4,
                 startDate:new Date(2004,2,1), endDate:new Date(2014,3,1), 
                 func:"startGimpAnimation()"}];

var curAds;

function init_werbung()
{
  curWerbung++;
  curWerbung %= curAds.length;
  AVGPlayer.getElementByID("topscreen").opacity=1; 
  AVGPlayer.getElementByID("werbung_switch").activechild=
        curAds[curWerbung].index;
  eval(curAds[curWerbung].func);
}

function init_cur_ads()
{
    print("Configured ads: ");
    curAds = new Array();
    for (var i in adSchedule) {
        var curAd = adSchedule[i];
//        print("startDate: " + curAd.startDate);
//        print("endDate: " + curAd.endDate);
        if (curAd.startDate == null ||
            (curAd.startDate <= new Date() && 
             curAd.endDate >= new Date())) {
            curAds.push(curAd);
            print("  "+curAd.name);
        }
    }
}
var Log = new Logger;
Log.setCategories(Log.LOG_PROFILE | 
                  Log.LOG_WARNING | 
                  Log.LOG_CONFIG); 

AVGPlayer.loadFile("monitor1.avg");

init_cur_ads();
AVGPlayer.setTimeout(10,"init_video();");
AVGPlayer.setInterval(10,"move_welcome();");
AVGPlayer.setTimeout(100, "init_werbung();");
AVGPlayer.play(15);
