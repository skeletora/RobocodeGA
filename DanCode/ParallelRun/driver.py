#!/usr/bin/python3

from RunRobocode import *

def BuildBot(a,b,c,d,e):
        bot =  str(a) + ","  + str(b) +","+ str(c) +"," +  \
               str(d) + "," + str(e) + ":0,0,0,0"
        return bot;

generation = [];

mode = 0;
minMove = 20;
delta = 20;
angle = 0;

i = 0;
while (mode < 2) :
    minMove = 20;
    while minMove <=200:
       bot =BuildBot(mode, minMove, minMove+delta, angle ,100);
       generation.append(bot);
       minMove += 10;
       i += 1
    mode += 1;

results = RunGeneration(generation);

for res in results:
   print(res);
