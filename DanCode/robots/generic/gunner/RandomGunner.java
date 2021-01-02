package generic.gunner;

import generic.parser.*;

import robocode.*;
import robocode.util.*;

public class RandomGunner extends Gunner {

    //   paramterers
    //   First minimum energy: this is the minimum energy the robot must
    //       maintain when firing.  
    //
    int MIN_ENERGY  = 50; 

    public RandomGunner(Parser p, AdvancedRobot bot) {
        super(p,bot);
        System.out.println("A random gunner has arrived");
        MIN_ENERGY = parser.Argument(1,1);
    }

    @Override
    public void DoGun(){
        double power;

        double angle = bot.getGunTurnRemainingRadians();

        // if the gun is not turning, turn it.
        if (angle == 0) {
            angle = Math.random()*Math.PI;
            double dir = Math.random();
            if (dir < 0.5) {
               angle *= -1;
            }
            bot.setTurnGunRight(angle);
        }

        // if the gun is cool, fire it.
        if (bot.getGunHeat() == 0 ) {
            power = Math.random()*(BULLET_MAX-BULLET_MIN) + BULLET_MIN;
            // only fire if our energy is above the set min.
            if (bot.getEnergy() -power > MIN_ENERGY) {
                bot.fireBullet(power);
            }
        }
    }
}

