package generic.gunner;

import generic.parser.*;

import robocode.*;
import robocode.util.*;

public class GunnerFactory {

    public static Gunner MakeGunner(Parser parser, AdvancedRobot bot) {
        Gunner g;

        int gunnerType  = parser.MethodID(1);
        switch(gunnerType) {
           case 1:
                g = new RandomGunner(parser, bot); 
                break;
           case 0:
           default:
                g = new NonGunner(parser, bot); 
                break;
        }
        return g;
    }
}

