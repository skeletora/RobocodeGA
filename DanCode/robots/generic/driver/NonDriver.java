package generic.driver;

import generic.parser.*;

import robocode.*;
import robocode.util.*;

public class NonDriver extends Driver {
    
    public NonDriver(Parser parser, AdvancedRobot bot) {
        super(parser,bot);
        System.out.println("You just hired a non-driver");
    }

    public void DoMove() {
       System.out.println("I am just too scared to do anyting");
    }
}

