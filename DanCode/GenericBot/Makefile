.PHONY: clean

# needs to be set to your robot directory
ROBOTS = /home/dbennett/robots

JCC = /usr/bin/javac
ROBOCODE_HOME = /usr/local/robocode/current
ROBOT_PATH = ${ROBOCODE_HOME}/libs/robocode.jar

CLASS_PATH = /usr/lib/jvm/java-1.8.0-openjdk-1.8.0.252.b09-0.fc30.x86_64/jre/lib/rt.jar

FINAL_PATH = ${CLASS_PATH}:${ROBOT_PATH}
JARGS = -encoding UTF-8 

GenericBot.class: GenericBot.java
	echo ${FINAL_PATH}
	${JCC} ${JARGS}  -classpath ${FINAL_PATH}  GenericBot.java
	cp GenericBot.class ${ROBOTS}/GenericBot

clean:
	rm -f GenericBot.class
