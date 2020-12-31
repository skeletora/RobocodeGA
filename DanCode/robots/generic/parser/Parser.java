package generic.parser;

//import java.io.File;
//import java.util.Scanner;
//import java.io.FileNotFoundException

public class Parser {

    int config[][];
    String gene;

    public Parser() {
        int i;

        String data = System.getProperty("ROBOT_GENE");
        gene = data;
        String[] cmds = data.split(":");

        config = new int[cmds.length][];

        for(i=0; i < cmds.length; i++) {
            config[i] = ParseCommand(cmds[i]);
        }
    }

    public String GetGene() {
       return gene;
    }

    int[] ParseCommand(String cmd) {

        int i;

        String[] bits;
        bits = cmd.split(",");

        int[] rv = new int[bits.length];

        for(i = 0; i < bits.length; i++) {
            rv[i] =   Integer.parseInt(bits[i]);
        }

        return rv;
    }

    public int ArgCount(int actionClass) {
        if (actionClass >= 0 && actionClass < config.length) {
            return config[actionClass].length;
        }
        return -1;
    }

    public int MethodID (int actionClass) {
        if (actionClass >= 0 && actionClass < config.length) {
            return config[actionClass][0];
        }
        return -1;
    }

    public int Argument(int actionClass, int methodIndex) {
        if (actionClass >= 0 && actionClass < config.length) {
            if (methodIndex >= 0 && methodIndex < config[actionClass].length){
                 return config[actionClass][methodIndex];
            }
        }
        return -1;
    }
}
