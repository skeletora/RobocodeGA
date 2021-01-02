package generic.gunner;

import generic.parser.*;

import robocode.*;
import robocode.util.*;

import robocode.Rules;

public class Gunner {
    double firePower;
    AdvancedRobot bot;
    Parser parser;

    double BULLET_MAX;
    double BULLET_MIN;

    public Gunner(Parser p, AdvancedRobot bot) {
        this.bot = bot;
        BULLET_MAX = Rules.MAX_BULLET_POWER;
        BULLET_MIN = Rules.MIN_BULLET_POWER;

        this.parser = p;
    }

    public void WasScanned(ScannedRobotEvent e) {} ;

    public void WasHitByBullet(HitByBulletEvent e) {} ; 

    public void DoGun() {} ; 

    // these three allow others to control the gunner.
    public void SetFirepower(double power) {
        firePower = power;
    }

    // radar control spots a target, send to gunner.
    public void NewAngle() {} ;  
    // radar control says to fire now.
    public void Fire() {};
}

