package generic.driver;

import generic.parser.*;

import robocode.*;
import robocode.util.*;

public class DriverUtils {

    public static double Between(double min, double max) {

       double delta = max - min;
       double sign = 1;
       if (Math.random() < 0.5) {
           sign = -1;
       }

       return sign * (Math.random()* delta + min);
    }
}
