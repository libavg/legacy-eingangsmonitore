print("----Logger setup----");
var Log = new Logger;
Log.setCategories(Log.LOG_PROFILE | 
                  Log.LOG_WARNING | 
                  Log.LOG_CONFIG  |
                  Log.LOG_EVENTS);

print ("----player test----");
useModule("player");
var AVGPlayer = new Player;

function floatAnimationStep(nodeName, attrName, startValue, endValue,
        duration, curTime)
{
    var node = AVGPlayer.getElementByID(nodeName);
    if (curTime < duration) {
        var curValue = startValue+(endValue-startValue)*curTime/duration;
        eval("node."+attrName+"="+curValue);
        var code = "floatAnimationStep(\""+nodeName+"\", \""+attrName+"\", "
                +startValue+", "+endValue+", "+duration+", "+(curTime+30)+");";
        AVGPlayer.setTimeout(30, code);
    } else {
        eval("node."+attrName+"="+endValue);
    }
}

function animateAttr(nodeName, attrName, startValue, endValue, duration)
{
    var code = "floatAnimationStep(\""+nodeName+"\", \""+attrName+"\", "
                +startValue+", "+endValue+", "+duration+", "+30+");";
    AVGPlayer.setTimeout(30, code);
}

function init() {
    var node = AVGPlayer.getElementByID("trailer");
    node.play();
//    node.seekToFrame(100);
    animateAttr("trailer", "angle", -3.1415/2, 0, 2500);
    AVGPlayer.getElementByID("trailer").opacity=1;

}

function start_logo() {
    animateAttr("c-wars", "opacity", 1.0, 0.0, 3000);
    animateAttr("c-wars", "x", 66, 40, 5000); 
}

function start_words1() {
    animateAttr("moon", "opacity", 0.0, 1.0, 1000);
    animateAttr("where_past", "opacity", 1.0, 0.0, 2000);
}

function start_words2() {
    animateAttr("meets_future", "opacity", 1.0, 0.0, 2000);
}

function start_url() {
    animateAttr("www_c-wars_com", "opacity", 1.0, 0.0, 1500);
}

function fadeout() {
//    AVGPlayer.getElementByID("trailer").stop();
    AVGPlayer.getElementByID("trailer").opacity=0.0;
    animateAttr("moon", "opacity", 1.0, 0.0, 500);
}

function start_animation() {
    AVGPlayer.showCursor(false);
    AVGPlayer.setTimeout(10, "init();");
    AVGPlayer.setTimeout(2000, "start_logo();");
    AVGPlayer.setTimeout(3000, "start_words1();");
    AVGPlayer.setTimeout(4500, "start_words2();");
    AVGPlayer.setTimeout(6000, "start_url();");
    AVGPlayer.setTimeout(8500, "fadeout();");
}

AVGPlayer.loadFile("trailer.avg");
AVGPlayer.setTimeout(10, "start_animation();");
AVGPlayer.setInterval(12000, "start_animation();");
AVGPlayer.play(25);
print("end");
