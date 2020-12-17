**** driver.py ****

The main executable.  This generates 37 different genes and runs them in parallel.  The results are printed.  This will probably be replaced.

**** RunRobocode.py ****
This is the script to run the code in parallel.  It takes an array of "genes" and retuns a corresponding array of results.

**** battle.battle ****
This file contains the configuration for a battle.  It seems that he wants the extension .battle.  Why fight it.

**** configuration.py ****

The file configuration.py has paths and other relavant information for running the code in parallel.


* ROBOHOME is the directory to where the base robocode is installed.
   This will probably not change.

* USER the locataion in the user directory that is the root of the project.

* ROBOT_PATH is the location of the robots directory.
   This is a local copy because I don't want users to write to the system wide
   robot directory and there does not appear to be an option to 
   look into two directoryes

* cmd1 and cmd2 are the command to run the code.
   These probabl should not change.

* PROCS is the number of processors to use.  
    This will probably not change.

