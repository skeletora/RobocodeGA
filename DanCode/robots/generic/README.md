# The Generic Robot 

This is a simple generic bot that executes the gene.    This robot relies on a java property (ROBOT_GENE) for its configuration.

Java properties appear to be the java equivelent to command line arguments.

Change the code in this directory to modify the robot.  The supplied makefile will put a  copy of the "executable" in the robots directory.

## driver

This dirctory contains the heirarchy for the driver.  

## parser

A simple parser.  Probably not needed, but I was learning java.  This definately can be improved.

## gunner

This directory contains code for the gunner.  It is currently in development.

### GenericBot.java

This code is the main code for the generic bot.  It currently creates an instance of a parser and a driver.  In the future a gunner and a radar operator will most likely be added.
