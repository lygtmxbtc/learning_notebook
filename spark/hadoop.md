Hadoop 成为了典型的大数据批量处理架构,由 HDFS 负责静态数据的存储,并通过
MapReduce 将计算逻辑分配到各数据节点进行数据计算和价值发现.之后以
HDFS 和 MapReduce 为基础建立了很多项目,形成了 Hadoop 生态圈.  

hadoop mapreduce后将结果从内存写到磁盘，第二次mapreduce从磁盘读取；
spark将数据一直缓存在内存中，最后将结果写入磁盘
