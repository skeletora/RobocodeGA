package generic.gunner;

import generic.parser.*;

import robocode.*;
import robocode.util.*;

public class NonGunner extends Gunner {

    NonGunner(Parser p, AdvancedRobot bot ) {
       super(p,bot);
       System.out.println("A non gunner was created");
    }
}

