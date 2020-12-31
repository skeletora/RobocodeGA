package generic.driver;

import generic.parser.*;

import robocode.*;
import robocode.util.*;

public class DriverFactory {

    public static Driver MakeDriver(Parser parser, AdvancedRobot bot) {
        Driver d;

        int driverType  = parser.MethodID(0);
        switch(driverType) {
           case 3:
                d = new ContinuousDriver(parser, bot); 
                break;
           case 2:
                d = new MoveOrTurnDriver(parser, bot); 
                break;
           case 1:
                d = new DuckAndCoverDriver(parser, bot); 
                break;
           default:
                d = new NonDriver(parser, bot); 
                break;
        }
        return d;
    }
}

