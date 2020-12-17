# GenericBot #

This code implements a generic robot in robocode.
This is the code you should change to change the generic bot.

This code is very much a work in progress.  It will be changing.

## Communicating the Configuration ##
The configuration is communcated via java properties.  In this case the property "ROBOT_GENE" is parsed for configuration information.

This property is set in the command line when the java program is invoked.  See the code in ParallelRun.

## Building the robot ##

The makefile in this directory should build the robot and upon successful build, place a copy in the robots directory.

```bash
make
```

### Semi outdated note information ###

This can, and probably will change.

The input format is:
key : key : key

For move
move-mode,min-distance, max-distance, min-angle,max-angle, percent chance to move

Move Mode is 0 for move and turn
             1 for move or turn

Chance to move is only used in mode 1.

## TODO ##
  * Build wall avoidance code.
  * Build the methods for the specified behaviors
  * Clean the code up quite a bit.
