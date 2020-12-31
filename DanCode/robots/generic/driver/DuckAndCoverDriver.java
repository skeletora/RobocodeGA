
package generic.driver;

import generic.parser.*;

import robocode.*;
import robocode.util.*;

public class DuckAndCoverDriver extends Driver {
    int MIN_DISTANCE = 20;
    int MAX_DISTANCE = 200;
    int ROTATE_DIR = 0;

    int turning = 0;
    int turn = 1;


    public DuckAndCoverDriver(Parser parser, AdvancedRobot bot) {
        super(parser,bot);

        System.out.println("Hiring a Duck and Cover  driver");

        MIN_DISTANCE = parser.Argument(0,1);
        MAX_DISTANCE = parser.Argument(0,2);
        ROTATE_DIR = parser.Argument(0,3);
    }

    public double NewDistance() {
        return DriverUtils.Between(MIN_DISTANCE, MAX_DISTANCE);
    }

    public void DoMove() {
        double dist=0, ang=0;

        ang = bot.getTurnRemaining();
        if (ang == 0 && turning ==1) {
            bot.setAhead(distance);
            turning = 0;
        }
    }

    public void HitByBullet(HitByBulletEvent e) {
        // what angle was the bullet comming from
        double bulletHeading = e.getHeadingRadians();
        System.out.println("I was hit by a bullet heading " 
                                           + bulletHeading*RtoD);

        double myAngle = bot.getHeadingRadians();

        // what angle do I want to go?
        double angle = (bulletHeading+turn*Math.PI/2.0)%(PI2);
        turn *= -1;

        System.out.println("My Angle is  " + myAngle*RtoD);
        System.out.println("Setting my angle to  " + angle*RtoD);

         double left, right;

         if (myAngle > angle) {
            left = PI2-myAngle + angle; 
            right = myAngle -angle ;
         }  else {
            left = angle - myAngle;
            right = (myAngle + PI2-angle);
         }

         if(left > right) { 
             bot.setTurnRightRadians(right);
             System.out.println("Turning right by  " + (right)*RtoD);
         } else {
             bot.setTurnLeftRadians(left);
             System.out.println("Turning left by  " + (left)*RtoD);
         }

         turning = 1;

         distance = NewDistance();
    }

}
