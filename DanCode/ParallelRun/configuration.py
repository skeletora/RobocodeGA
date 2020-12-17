# directory where the robocode executable is held
ROBOHOME = "/usr/local/robocode/current"

USER = "/home/dbennett/"

# path to local copy of the robots
ROBOT_PATH = USER + "RobocodeGA/DanCode/robots"

# Parts of command to execute robocode with
cmd1 = ["java", "-Xmx512M"];

path = "-DROBOTPATH=" + ROBOT_PATH;
cmd1.append(path);

cmd2 = ["-cp", ROBOHOME+"/libs/robocode.jar", "robocode.Robocode", "-battle", "./battle.battle", "-nodisplay", "-nosound", "-results"]

# number of processes to run
PROCS = 10
