# Driver Class Heirarchy #

The driver class is a heirarchy.    These are the "tank drivers".  Changing
drivers will change the way the tank behaves.

## Driver.java ##
Driver.java is a base class.  It supports the following methods:

   * DoMove: this performs any corrections, changes, updates to the move.
   * HitByBullet:  performs any driver actions needed when the bot is hit by a bullet
   * HitWall: performs any driver actions needed when the bot hits a wall.

## DriverFactroy.java ##

This class creates an instance of the required driver, based on the genen, and
returns it to the calling routine. 

This code uses the first value in the first key of the gene.  These numbers are raw, no documentation is provided.

## Subclassed Drivers ##

   * **NonDriver.java** just sits there, does nothing.
   * **ContinuousDriver,java** constanly has somewhere to go, Turns and moves at the same time.
   * **MoveOrTurnDriver.java** Is either moving or turning, but not both.
   * **DuckAndCoverDriver.java** When hit will attempt to turn purpendicular to the bullet and move a random direction along that line.

## DriverUtils.java##
This file will contain common routines shared among drivers.
