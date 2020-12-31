package generic.gunner;

import generic.parser.*;

import robocode.*;
import robocode.util.*;

public class GunFactory {

    public static Gunner MakeGunner(Parser parser, AdvancedRobot bot) {
        Gunner g;

        int gunnerType  = parser.MethodID(0);
        switch(gunnerType) {
           default:
                g = new NonGunner(parser, bot); 
                break;
        }
        return g;
    }
}

