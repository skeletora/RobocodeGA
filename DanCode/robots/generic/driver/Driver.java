package generic.driver;

import generic.parser.*;

import robocode.*;
import robocode.util.*;

public class Driver {
    AdvancedRobot bot;
    Parser parser;

    double PI2 = Math.PI*2.0;
    double PI = Math.PI;
    double RtoD = 180.0/Math.PI;

    double distance=0;
    double angle = 0;

    public Driver(Parser p, AdvancedRobot bot) {
        this.bot = bot;
        this.parser = p;
    }

    public void DoMove() {}
    public void HitByBullet(HitByBulletEvent e) {}

    public void HitWall(HitWallEvent e) { 
       System.out.println("I hit a wall") ;
       distance = this.bot.getDistanceRemaining();
       this.bot.setAhead(-distance);
    }
}

