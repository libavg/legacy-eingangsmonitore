useModule("player");
var AVGPlayer = new Player;

function floatAnimationStep(nodeName, attrName, startValue, endValue, duration, curTime)
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

function animateFloatAttr(nodeName, attrName, startValue, endValue, duration)
{
    var code = "floatAnimationStep(\""+nodeName+"\", \""+attrName+"\", "
                +startValue+", "+endValue+", "+duration+", "+30+");";
    eval(code);
}

function stoerung()
{
    animateFloatAttr("stoerung_horiz", "y", 600, -70, 4000);
}

function stoerung_vert()
{
    var node = AVGPlayer.getElementByID("stoerung_vert");
    node.y += 80;
    if (node.y > 600) {
        node.y = 10;
    }
    animateFloatAttr("stoerung_vert", "x", 770, -100, 1000);
}

var wellenInt = 0;
var wellenCount;

function getCurWelle()
{
    var w=wellenCount%12;
    if (w<6) {
        return w;
    } else {
        return 11-w;
    }
}

function welle()
{
    var curWelle = getCurWelle();
    var node = AVGPlayer.getElementByID("welle"+curWelle);
    node.opacity=0.0;
    wellenCount++;
    curWelle = getCurWelle();
    node = AVGPlayer.getElementByID("welle"+curWelle);
    node.opacity=0.4;
}

function startStoerung()
{
    if (wellenInt == 0) {
        wellenCount=0;
        moveStoerung();
        wellenInt=AVGPlayer.setInterval(10,"welle();");
    }
}

function moveStoerung()
{
print("move");
    var event=AVGPlayer.getCurEvent();
    var y=event.yPosition;
    y=(y-6)-(y-6)%10+4;
    var node=AVGPlayer.getElementByID("distortion");
    node.y = y;
}

function endStoerung()
{
    AVGPlayer.clearInterval(wellenInt);
    var node=AVGPlayer.getElementByID("welle"+getCurWelle());
    node.opacity=0.0;
    wellenInt = 0;
}

function quit()
{
    AVGPlayer.stop();
}

