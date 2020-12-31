package generic.driver;

import generic.parser.*;

import robocode.*;
import robocode.util.*;

public class MoveOrTurnDriver extends Driver {
    int MIN_DISTANCE = 20;
    int MAX_DISTANCE = 200;
    int MIN_ANGLE = 20;
    int MAX_ANGLE = 160;
    double movePct = .7;

    public MoveOrTurnDriver(Parser parser, AdvancedRobot bot) {
        super(parser,bot);

        System.out.println("Hiring a move or turn driver");

        MIN_DISTANCE = parser.Argument(0,1);
        MAX_DISTANCE = parser.Argument(0,2);
        MIN_ANGLE = parser.Argument(0,3);
        MAX_ANGLE = parser.Argument(0,4);

        movePct = parser.Argument(0,5)/100.0;
    }

    public double NewDistance() {
        return DriverUtils.Between(MIN_DISTANCE, MAX_DISTANCE);
    }

    public double NewAngle() {
        return DriverUtils.Between(MIN_ANGLE, MAX_ANGLE);
    }

    public void DoMove() {
        double dist=0, ang=0;

        dist = Math.abs(bot.getDistanceRemaining());
        ang = Math.abs(bot.getTurnRemaining());

        if (dist == 0 && ang == 0) {
           if (Math.random() < movePct) {
               distance = NewDistance();
               bot.setAhead(distance);
           } else {
               angle = NewAngle();
               bot.setTurnRight(angle);
           }
        }
    }
}
