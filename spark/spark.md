#### 应用程序(Application)
基于Spark的用户程序，包含了一个Driver Program 和集群中多个的Executor；  
#### 驱动(Driver)
运行Application的main()函数并且创建SparkContext;
#### 执行单元(Executor)
是为某Application运行在Worker Node上的一个进程，该进程负责运行Task，并且负责将数据存在内存或者磁盘上，每个Application都有各自独立的Executors;
#### 集群管理程序(Cluster Manager)
在集群上获取资源的外部服务(例如：Local、Standalone、Mesos或Yarn等集群管理系统)；
#### 操作(Operation)
作用于RDD的各种操作分为Transformation和Action.

### master worker
```
Master节点上常驻Master守护进程和Driver进程, Master负责将串行任务变成
可并行执行的任务集Tasks, 同时还负责出错问题处理等,而Worker节点上常驻
Worker守护进程, Master负载管理全部的Worker节点,而Worker节点负责执行任务. 
```

### shuffle过程
```
Spark是根据shuffle类算子来进行stage的划分。如果我们的代码中执行了某个
shuffle类算子（比如reduceByKey、join等），那么就会在该算子处，划分出
一个stage界限来。可以大致理解为，shuffle算子执行之前的代码会被划分为一
个stage，shuffle算子执行以及之后的代码会被划分为下一个stage。因此一个
stage刚开始执行的时候，它的每个Task可能都会从上一个stage的Task所在的
节点，去通过网络传输拉取需要自己处理的所有key，然后对拉取到的所有相同的
key使用我们自己编写的算子函数执行聚合操作（比如reduceByKey()算子接收
的函数）。这个过程就是shuffle。 
```
### RDD
```
RDD 是一种只读的数据块,可以从外部数据转换而来,你可以对RDD 进行函数操作
(Operation),包括 Transformation 和 Action. 在这里只读表示当你对一
个 RDD 进行了操作,那么结果将会是一个新的 RDD, 这种情况放在代码里,假设
变换前后都是使用同一个变量表示这一 RDD,RDD 里面的数据并不是真实的数据,
而是一些元数据信息,记录了该 RDD 是通过哪些 Transformation 得到的,在
计算机中使用 lineage 来表示这种血缘结构,lineage 形成一个有向无环图 
DAG, 整个计算过程中,将不需要将中间结果落地到 HDFS 进行容错,加入某个
节点出错,则只需要通过 lineage 关系重新计算即可

Transformation只记录操作，等待Action操作才执行计算过程，这样对应
形成有向无环图DAG
```
### shuffle和stage关系
```
Transformation分宽依赖和窄依赖，区别是否发生shuffle
```
