package generic;

//import java.io.File;
//import java.util.Scanner;
//import java.io.FileNotFoundException;

import generic.parser.Parser;
import generic.driver.*;
//import generic.gunner.*;

import robocode.*;
import java.awt.Color;

/*
 * GenericBot - a robot by (GenericBotMaker)
 */
public class GenericBot extends AdvancedRobot
{
    private Parser parser;
    private Driver driver;

    public void run() {
       
       out.println("Running the generic bot");
       //  java makes suck.
       parser = new Parser();

       driver = DriverFactory.MakeDriver(parser,this);
       
       // Color args are color of: body,gun,radar
       setColors(Color.blue,Color.blue,Color.red); 
	
       while(true) {
           driver.DoMove();
           execute();
       }
    }

    public void onScannedRobot(ScannedRobotEvent e) {
	fire(1);
    }

    public void onHitByBullet(HitByBulletEvent e) {
        driver.HitByBullet(e);
    }
	       
    public void onHitWall(HitWallEvent e) {
        driver.HitWall(e);
    }	
}
