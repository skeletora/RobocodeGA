
package generic.gunner;

import generic.parser.*;

import robocode.*;
import robocode.util.*;

public class NonGunner extends Gunner {

    NonGunner(Parser p, AdvanceRobot bot ) {
       super(p,bot);
       System.out.println("A non gunner was created");
    }

    void WasScanned(ScannedRobotEvent e);
    void WasHitByBullet(HitByBulletEvent e); 
    void NewTarget();  // radar control spots a target, send to gunner.
    void DoGun(); // called every loop.
    void SetFirepower(double power)
}

