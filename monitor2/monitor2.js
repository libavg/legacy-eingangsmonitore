
use("../common.js");

var timeCount = 0;

function move_graphs()
{
    timeCount++;
    var node1 = AVGPlayer.getElementByID("ceit_graph1");
    var node2 = AVGPlayer.getElementByID("ceit_graph2");
    node1.x--;
    if (node1.x == -500) {
        node1.x = 500;
    }
    node2.x--;
    if (node2.x == -500) {
        node2.x = 500;
    }
}

var curMessage=0;
var messages=["es ist mal wieder ceit cu fegen", 
              "cugang combiosc inactiv",
              "c_wercraftfluctuation",
	      "magnetic_es feld activ",
	      "nerdc_leuder activ. bitte beachten sie die sicherheitshinweise." ];

var curLine=0;
var messageInterval;

function move_message()
{
  var node = AVGPlayer.getElementByID("hinweis"+curLine);
  node.x-=10;
  if (node.x < -300) {
    AVGPlayer.clearInterval(messageInterval);
    node.x = 800;
  }
}

function new_message()
{
  curLine+=2;
  if (curLine == 4) {
    curLine = 1;
  } else if (curLine == 5) {
    curLine = 0;
  }

  curMessage++;
  if (curMessage == 5) {
    curMessage = 0;
  }
  AVGPlayer.getElementByID("hinweis_icon"+curLine).activechild = curMessage;
  AVGPlayer.getElementByID("hinweis_text"+curLine).text = messages[curMessage];
  messageInterval = AVGPlayer.setInterval(10, "move_message()");
}

var Log = new Logger;
Log.setCategories(Log.LOG_PROFILE | 
                  Log.LOG_WARNING | 
                  Log.LOG_CONFIG); 

AVGPlayer.loadFile("monitor2.avg");

AVGPlayer.setInterval(10, "move_graphs();");
//AVGPlayer.setInterval(5000, "new_message();");
AVGPlayer.play(25);
print("end");
