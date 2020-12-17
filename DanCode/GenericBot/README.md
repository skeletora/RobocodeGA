# GenericBot #

This code implements a generic robot in robocode.
This is the code you should change to change the generic bot.

This code is very much a work in progress.  It will be changing.

## Communicating the Configuration ##
The configuration is communcated via java properties.  In this case the property "ROBOT_GENE" is parsed for configuration information.

**Semi outdated note information**

This can, and probably will change.

The input format is:
key : key : key

For move
move-mode,min-distance, max-distance, min-angle,max-angle, percent chance to move

Move Mode is 0 for move and turn
             1 for move or turn

Chance to move is only used in mode 1.
