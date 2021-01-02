package generic;

//import java.io.File;
//import java.util.Scanner;
//import java.io.FileNotFoundException;

import generic.parser.Parser;
import generic.driver.*;
import generic.gunner.*;

import robocode.*;
import java.awt.Color;

/*
 * GenericBot - a robot by (GenericBotMaker)
 */
public class GenericBot extends AdvancedRobot {
    private Parser parser;
    private Driver driver;
    private Gunner gunner;

    public void run() {
       
       // out.println("Running the generic bot");
       // java makes suck.
       parser = new Parser();
       driver = DriverFactory.MakeDriver(parser,this);
       gunner = GunnerFactory.MakeGunner(parser,this);
       
       // Color args are color of: body,gun,radar
       setColors(Color.blue,Color.blue,Color.red); 
	
       while(true) {
           driver.DoMove();
           gunner.DoGun();
           execute();
       }
    }

    public void onScannedRobot(ScannedRobotEvent e) {
        gunner.WasScanned(e);
    }

    public void onHitByBullet(HitByBulletEvent e) {
        driver.HitByBullet(e);
        gunner.WasHitByBullet(e);
    }
	       
    public void onHitWall(HitWallEvent e) {
        driver.HitWall(e);
    }	
}
