.PHONY: clean
.SUFFIXES: .java .class
.java.class:
	${JC} ${JFLAGS} $*.java

JC = /usr/bin/javac

ROBOCODE_HOME = /usr/local/robocode/current
ROBOT_PATH = ${ROBOCODE_HOME}/libs/robocode.jar

CLASS_PATH = /usr/lib/jvm/java-1.8.0-openjdk-1.8.0.252.b09-0.fc30.x86_64/jre/lib/rt.jar

FINAL_PATH = ${CLASS_PATH}:${ROBOT_PATH}

JFLAGS = -encoding UTF-8  -classpath ${FINAL_PATH} -Xlint:deprecation 

DRIVER_CLASSES = driver/DriverFactory.java driver/Driver.java driver/NonDriver.java driver/ContinuousDriver.java driver/DriverUtils.java driver/MoveOrTurnDriver.java driver/DuckAndCoverDriver.java

CLASSES = GenericBot.java  parser/Parser.java ${DRIVER_CLASSES}

default: ${classes}
	${JC} ${JFLAGS} ${CLASSES} 

clean:
	rm -f *.class
	rm -f driver/*.class
	rm -f parser/*.class
