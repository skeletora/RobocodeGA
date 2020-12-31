package generic.gunner;

import generic.parser.*;

import robocode.*;
import robocode.util.*;

public class Gunner {
    double firePower;
    AdvancedRobot bot;
    Parser parser;

    public Gunner(Parser p, AdvancedRobot bot) {
        this.bot = bot;
        this.parser = p;
    }

    void WasScanned(ScannedRobotEvent e);
    void WasHitByBullet(HitByBulletEvent e); 
    void NewTarget();  // radar control spots a target, send to gunner.
    void DoGun(); // called every loop.
    void SetFirepower(double power)
}

