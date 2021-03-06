#!/bin/bash
#ssh localhost
python3 inputter.py	#takes maps.json as input
hdfs namenode -format
start-dfs.sh
start-yarn.sh
#jps to verify there are 6 processes
hdfs dfs -mkdir /user/
hdfs dfs -mkdir /user/hadoop/
hdfs dfs -mkdir /user/hadoop/input
# ./Images contains all images
hdfs dfs -put Images/*.png /user/hadoop/input
#input.txt is generated by inputter.py
hdfs dfs -put input.txt /user/hadoop/input
#change the directories for numpy and opencv in jobber.py
python3 jobber.py -r hadoop hdfs:///user/hadoop/input/input.txt
