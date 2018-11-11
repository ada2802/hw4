## DATA622 HW #4
- Assigned on October 25, 2018
- Due on October 14, 2018 11:59 PM EST
- 15 points possible, worth 15% of your final grade

### Instructions:

Use the two resources below to complete both the critical thinking and applied parts of this assignment.

1. Listen to all the lectures in Udacity's [Intro to Hadoop and Mapreduce](https://www.udacity.com/course/intro-to-hadoop-and-mapreduce--ud617) course.  

2. Read [Hadoop A Definitive Guide Edition 4]( http://javaarm.com/file/apache/Hadoop/books/Hadoop-The.Definitive.Guide_4.edition_a_Tom.White_April-2015.pdf), Part I Chapters 1 - 3.

### Critical Thinking (10 points total)

Submit your answers by modifying this README.md file.

1. (1 points) What is Hadoop 1's single point of failure and why is this critical?  How is this alleviated in Hadoop 2?
Answer: a) The single point of failure in Hadoop v1 is NameNode. If NameNode gets fail the whole Hadoop cluster will not work. Actually, there will not any data loss only the cluster work will be shut down, because NameNode is only the point of contact to all DataNodes and if the NameNode fails all communication will stop.
b) To handle the single point of failure, we can use another setup configuration which can backup NameNode metadata. If the primary NameNode will fail our setup can switch to secondary (backup) and no any type to shutdown will happen for Hadoop cluster.
HDFS High Availability of Namenode is introduced with Hadoop 2. In this two separate machines are getting configured as NameNodes, where one NameNode always in working state and anther is in standby. Working Name node handling all clients request in the cluster where standby is behaving as the slave and maintaining enough state to provide a fast failover on Working Name node.

https://data-flair.training/forums/topic/what-is-single-point-of-failure-in-hadoop-1-and-how-it-is-resolved-in-hadoop-2/#post-5387

2. (2 points) What happens when a data node fails?
Answer: HDFS has master/slave architecture. An HDFS cluster consists of a single NameNode, a master server that manages the file system namespace and regulates access to files by clients.In addition, there are a number of DataNodes, usually one per node in the cluster, which manage storage attached to the nodes that they run on.
The NameNode and DataNode are pieces of software designed to run on commodity machines.NameNode periodically receives a Heartbeat and a Block report from each of the DataNodes in the cluster. Receipt of a Heartbeat implies that the DataNode is functioning properly.
A Blockreport contains a list of all blocks on a DataNode. When NameNode notices that it has not received a heartbeat message from a data node after a certain amount of time, the data node is marked as dead. Since blocks will be under replicated the system begins replicating the blocks that were stored on the dead DataNode.
The NameNode Orchestrates the replication of data blocks from one DataNode to another. The replication data transfer happens directly between DataNode and the data never passes through the NameNode.

https://www.quora.com/What-happens-when-datanode-fails

3. (1 point) What is a daemon?  Describe the role task trackers and job trackers play in the Hadoop environment.
Answer: a) A daemon (pronounced DEE-muhn) is a program that runs continuously and exists for the purpose of handling periodic service requests that a computer system expects to receive. The daemon program forwards the requests to other programs (or processes) as appropriate.

b)Job Tracker: NameNode and DataNodes store details and actual data on HDFS. This data is also required to process as per client’s requirements. A Developer writes a code to process the data. Processing of data can be done using MapReduce. MapReduce engine sends the code across DataNodes, creating jobs. These jobs are to be continuously monitored; Job tracker manages those jobs.
Task Tracker: The jobs given by Job trackers are actually performed by Task trackers. Each DataNode will have one task tracker. Task trackers communicate with Job trackers to send statuses of the jobs.

https://www.quora.com/What-are-the-various-Hadoop-daemons-and-their-roles-in-a-Hadoop-cluster

4. (1 point) Why is Cloudera's VM considered pseudo distributed computing?  How is it different from a true Hadoop cluster computing?
Answer:  a) Cloudera allows you to download a QuickStart Virtual machine which is great for developers, but this is of no use for the Operations team to start the planning and the building out of DEV / UAT and PROD environments within their organizations.
hosting all of Cloudera's processes as well as Hadoop's processes on one VM is not a model that any large organization can or should follow. The Hadoop services need to be split out across multiple VMs/Servers. In fact that's the whole point out Hadoop! 
After all, if you are developing against or operating a distributed environment, it needs to be tested. Tested in terms of the forcing various failure modes within the cluster and ensuing that the cluster can still respond to user requests. Killing the QuickStart VM destroys the entire cluster!

https://www.udemy.com/real-world-hadoop-deploying-with-cloudera-manager/

5. (1 point) What is Hadoop streaming? What is the Hadoop Ecosystem?
Answer:  a) Hadoop streaming is a utility that comes with the Hadoop distribution. It can be used to execute programs for big data analysis. Hadoop streaming can be performed using languages like Python, Java, PHP, Scala, Perl, UNIX, and many more. The utility allows us to create and run Map/Reduce jobs with any executable or script as the mapper and/or the reducer.

Input is read from standard input and the output is emitted to standard output by Mapper and the Reducer. Utility creates a Map/Reduce job, submits the job to an appropriate cluster, and monitors the progress of the job until completion.
Every mapper task will launch the script as a separate process when the mapper is initialized after a script is specified for mappers. Mapper task inputs are converted into lines and fed to the standard input and Line oriented outputs are collected from the standard output of the procedure Mapper and every line is changed into a key, value pair which is collected as the outcome of the mapper.

Each reducer task will launch the script as a separate process and then the reducer is initialized after a script is specified for reducers. As the reducer task runs, reducer task input key/values pairs are converted into lines and feds to the standard input (STDIN) of the process.

Each line of the line-oriented outputs is converted into a key/value pair after it is collected from the standard output (STDOUT) of the process, which is then collected as the output of the reducer.
https://www.quora.com/What-is-Hadoop-Streaming

b) Hadoop is a framework. If Hadoop was a house, it wouldn’t be a very comfortable place to live. It would provide walls, windows, doors, pipes, and wires. The Hadoop ecosystem provides the furnishings that turn the framework into a comfortable home for big data activity that reflects your specific needs and tastes.

The Hadoop ecosystem includes both official Apache open source projects and a wide range of commercial tools and solutions. Some of the best-known open source examples include Spark, Hive, Pig, Oozie and Sqoop. Commercial Hadoop offerings are even more diverse and include platforms and packaged distributions from vendors such as Cloudera, Hortonworks, and MapR, plus a variety of tools for specific Hadoop development, production, and maintenance tasks.
http://www.bmc.com/guides/hadoop-ecosystem.html

6. (1 point) During a reducer job, why do we need to know the current key, current value, previous key, and cumulative value, but NOT the previous value?
Answer: The reducer’s job is to “fold” the current value into the accumulated value somehow. How is not specified, and specifying how is the purpose of the reducer function. The reducer returns the new accumulated value, and reduce() moves on to the next value in the array. The reducer may need an initial value to start with, so most implementations take an initial value as a parameter.
https://medium.com/javascript-scene/reduce-composing-software-fe22f0c39a1d

7. (3 points) A large international company wants to use Hadoop MapReduce to calculate the # of sales by location by day.  The logs data has one entry per location per day per sale.  Describe how MapReduce will work in this scenario, using key words like: intermediate records, shuffle and sort, mappers, reducers, sort, key/value, task tracker, job tracker.  
Answer: MapReduce is a programming framework that allows us to perform distributed and parallel processing on large data sets in a distributed environment.MapReduce consists of two distinct tasks – Map and Reduce. As the name MapReduce suggests, reducer phase takes place after mapper phase has been completed.
So, the first is the map job, where a block of data is read and processed to produce key-value pairs as intermediate outputs.
The output of a Mapper or map job (key-value pairs) is input to the Reducer.
The reducer receives the key-value pair from multiple map jobs.
Then, the reducer aggregates those intermediate data tuples (intermediate key-value pair) into a smaller set of tuples or key-value pairs which is the final output.

Unix command: 
cat purchases.txt | ./mapper.py | sort | ./reducer.py

### Applied (5 points total)

Submit the mapper.py and reducer.py and the output file (.csv or .txt) for the first question in lesson 6 for Udacity.  (The one labelled "Quiz: Sales per Category")  Instructions for how to get set up is inside the Udacity lectures.  
