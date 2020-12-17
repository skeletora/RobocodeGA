# My contribution to the project #



This branch contains the following directories

**robots**
This is a copy of the robots for robocode.

I decided on a per-user directory so that the users are not modifying the global copy.  

It appears that the robot needs to be placed in a subdirectory by the robot name.  More work on this may need to be done.

When new class of robot is placed in this directory, the robots.database needs to be rebuilt.  Robocode will do this but it may impact a parallel run.  This does not need to be done when a new instance of an existing robot is plalce.  (IE not after a new build, just after a completely new robot is added)


**ParallelRun**

This directory cotains the code to run robocode in parallel. 

Among other things, this sets the java property ROBOT_GENE when calling each individual robot.    Communication of the results is done via an output file from robocode.  These files are removed once they are read.

**GenericBot**

This is a simple generic bot that executes the gene.    This robot relies on a java property (ROBOT_GENE) for its configuration.

Java properties appear to be the java equivelent to command line arguments.

Change the code in this directory to modify the robot.  The supplied makefile will put a  copy of the "executable" in the robots directory.

