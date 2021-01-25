package generic.driver;

import generic.parser.*;

import robocode.*;
import robocode.util.*;

public class ContinuousDriver extends Driver {
    int MIN_DISTANCE = 20;
    int MAX_DISTANCE = 200;
    int MIN_ANGLE = 20;
    int MAX_ANGLE = 160;

    public ContinuousDriver(Parser parser, AdvancedRobot bot) {
        super(parser, bot);

        System.out.println("Hiring a continuous driver");

        //The way this works for X,Y is:
        //X indicates the colon segment
        //  ex) movement - 0: ??? - 1: ??? - 2:...
        //Y indicates the index within that colon
        //  ex) 1 (0),0 (1),30 (2):3 (0), 10 (1):...
        MIN_DISTANCE = parser.Argument(0,1);
        MAX_DISTANCE = parser.Argument(0,2);
        MIN_ANGLE = parser.Argument(0,3);
        MAX_ANGLE = parser.Argument(0,4);
    }

    public double NewDistance() {
        return DriverUtils.Between(MIN_DISTANCE, MAX_DISTANCE);
    }

    public double NewAngle() {
        return DriverUtils.Between(MIN_ANGLE, MAX_ANGLE);
    }

    public void DoMove() {
        double dist=0, ang=0;

        dist = bot.getDistanceRemaining();
        ang = bot.getTurnRemaining();

        if (Math.abs(dist) <= 0) {
            distance = NewDistance();
            bot.setAhead(distance);
        }
        if (Math.abs(ang) <=  0 ) {
            angle = NewAngle();
            bot.setTurnRight(angle);
        }
    }
}
