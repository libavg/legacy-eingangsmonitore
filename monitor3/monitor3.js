
use("../common.js");

var timeCount = 0;

function move_graphs()
{
    timeCount++;
    var node1 = AVGPlayer.getElementByID("athmo_data_1");
    var node2 = AVGPlayer.getElementByID("athmo_data_2");
        node1.x--;
        if (node1.x == -400) {
            node1.x = 400;
        }
        node2.x--;
        if (node2.x == -400) {
            node2.x = 400;
        }
    
    if (timeCount % 2 == 0) {
        node1 = AVGPlayer.getElementByID("lf_data_1");
        node2 = AVGPlayer.getElementByID("lf_data_2");
        node1.x--;
        if (node1.x == -400) {
            node1.x = 400;
        }
        node2.x--;
        if (node2.x == -400) {
            node2.x = 400;
        }
    }
}

var Log = new Logger;
Log.setCategories(Log.LOG_PROFILE | 
                  Log.LOG_WARNING | 
                  Log.LOG_CONFIG); 

var ok = AVGPlayer.loadFile("monitor3.avg");
if (!ok) {
    print ("js: AVGPlayer.loadFile returned false");
}

AVGPlayer.setInterval(10, "move_graphs();");
AVGPlayer.play(25);
print("end");
