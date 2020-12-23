package GenericBot;
import java.io.File;
import java.util.Scanner;
import java.io.FileNotFoundException;
import robocode.*;
import java.awt.Color;

/*
 * GenericBot - a robot by (GenericBot)
 */
public class GenericBot extends AdvancedRobot
{
    double MIN_DISTANCE = 20;
    double MAX_DISTANCE = 200;
    double MIN_ANGLE = 20;
    double MAX_ANGLE = 160;
    int moveType = 0;
    double movePct = .7;

    double distance=0;;
    double angle=0;

    Parser parser;
/*
    void ReadParams() {

        String data;

        // experiment with getting properties.
        String[] cmds = data.split(":");
        String[] move = cmds[0].split(",");

        switch(move[0]) {
           case "0":
              moveType = 1; 
              break;
           case "1":
              moveType = 0;
             
        }

        MIN_DISTANCE = Double.parseDouble(move[1]);
        MAX_DISTANCE = Double.parseDouble(move[2]);
        MIN_ANGLE = Double.parseDouble(move[3]);
        MAX_ANGLE = Double.parseDouble(move[4]);

        if (moveType == 1) {
              movePct = Double.parseDouble(move[5]);
        }
    }
*/
    double Between(double min, double max) {
        
       double delta = max - min;
       double sign = 1;
       if (Math.random() < 0.5) {
           sign = -1;
       }
		 
       return sign * (Math.random()* delta + min);
    }

    double NewDistance() {
        return Between(MIN_DISTANCE, MAX_DISTANCE);
    }	

    double NewAngle() {
        return Between(MIN_ANGLE, MAX_ANGLE);
    }

    // turn and move at the same time.
    void ContinuousTurnAndMove() {
	double dist=0, ang=0;

	dist = getDistanceRemaining();
	ang = getTurnRemaining();

	if (Math.abs(dist) <= 0) {
	    distance = NewDistance();
  	    setAhead(distance);
	} 
	if (Math.abs(ang) <=  0 ) {
            angle = NewAngle();
	    setTurnRight(angle);
	}

        execute();
    }
              
    void MoveOrTurn() {
	double dist=0, ang=0;

	dist = Math.abs(getDistanceRemaining());
	ang = Math.abs(getTurnRemaining());

        if (dist == 0 && ang == 0) {
           if (Math.random() < movePct) {
	       distance = NewDistance();
  	       setAhead(distance);
           } else {
               angle = NewAngle();
	       setTurnRight(angle);
           }
        }
        execute();
    }

    void DoMove() {
       switch (moveType) {
          case 0:
              ContinuousTurnAndMove();
              break;
          case 1:
              MoveOrTurn();
              break;
          default:
       }
    }

    public void run() {
        // body,gun,radar
       setColors(Color.blue,Color.blue,Color.red); 
	
       //ReadParams();
       while(true) {
           DoMove();

       }
    }

    public void onScannedRobot(ScannedRobotEvent e) {
	fire(1);
    }

    public void onHitByBullet(HitByBulletEvent e) {
	back(10);
    }
	       
    public void onHitWall(HitWallEvent e) {
        double distance = getDistanceRemaining();
        setBack(distance * 10);
    }	
}

enum  ActionT {
    MOVEMENT (0),
    TARGET (1),
    BULLET (2);

    int index;

    ActionT(int index) {
        this.index = index;
    }

    double index() { return index;}
}


class Parser {

    double config[][];

    Parser() {
        int i;

        String data = System.getProperty("ROBOT_GENE");
        System.out.println("Gene" + data);

        String[] cmds = data.split(":");

	config = new double[cmds.length][];

	for(i=0; i < cmds.length; i++) {
	    config[i] = ParseCommand(cmds[i]);
	}
    }

    double[] ParseCommand(String cmd) {

	int i;

        String[] bits;
	bits = cmd.split(",");

	double[] rv = new double[bits.length];

	for(i = 0; i < bits.length; i++) {
            rv[i] =   Double.parseDouble(bits[i]);
	}

	return rv;
    }

    public double MethodID (ActionT actionClass) {
	if (actionClass.index >= 0 && actionClass.index < config.length) {
            return config[actionClass.index][0]; 
	} 
	return -1;
    }

    public double Argument(ActionT actionClass, int methodIndex) {
	if (actionClass.index >= 0 && actionClass.index < config.length) {
            if (methodIndex >= 0 && methodIndex < config[actionClass.index].length){
		 return config[actionClass.index][methodIndex];
	    }
	}
	return -1;
    }
}

