#!/bin/python3
import subprocess
from multiprocessing import Lock, Process, Queue, current_process
import time
import queue 
import os

from configuration import *

def RunBot(cmd,bot, fileName):
    res = []
    cmd = cmd + [fileName];
    subprocess.run(cmd, stdout=subprocess.DEVNULL);
    o = open(fileName)
    for line in o:
       if line.find("GenericBot.GenericBot*") != -1:
            stats = line.split()
            res.append(bot);
            res.append(stats[0]);
            res.append(stats[2]);
            res.append(stats[3]);
    o.close();
    os.remove(fileName);

    return res;

def BuildLine(bot):
    line = "-DROBOT_GENE="+bot;
    cmd = cmd1 + [line] + cmd2;
    return cmd;

def DoRun(bot, myid):
    fileName = "result"+str(myid);
    cmd = BuildLine(bot);
    res = RunBot(cmd,bot, fileName);
    return res;

# stolen from on line
def DoJob(work, answers):
    while True:
        try:
            task = work.get_nowait()
            (theid,bot) = task.split("+");
            res = DoRun(bot, theid);
            res.append(theid);
            answers.put([theid,res])
        except queue.Empty:
            break

def RunGeneration(generation):

    work = Queue()
    answers = Queue()
    processes = []
    results = []

    i = 0;
    for bot in generation:
           work.put(str(i)+"+"+bot)
           results.append('');
           i += 1;

    for w in range(PROCS):
        p = Process(target=DoJob, args=(work, answers))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    while not answers.empty():
        res = answers.get()
        results[int(res[0])] = res[1];

    return results 
