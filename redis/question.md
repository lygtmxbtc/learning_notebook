### 为什么使用redis
1 性能  
结果放入缓存，请求去缓存中读取，快速响应
2 并发  
redis作为缓冲
### 单线程redis为什么快
1 纯内存操作 2 单线程 3 I/O多路复用
### redis数据类型
1 string  
set/get  复杂计数功能的缓存（set key "1"，get key得到1，incr key，get key得到2）  
2 hash  
hmset/hgetall 单点登录，存储用户信息，cookie id为key  
3 list  
lpush/blpop 消息队列  
4 set  
sadd/smembers  去重  
5 sorted set  
zadd key score value/zrange key 0 10 withscores 排行榜
### redis过期策略和内存淘汰机制
定期删除+惰性删除  
定时随机检查key过期，惰性删除当获取key检查是否过期，过期删除  
内存淘汰机制  
maxmemory-policy  
allkeys-lru 内存不足新数据，移出最近最少使用的key  
### 什么是Redis持久化？Redis有哪几种持久化方式？优缺点是什么？
RDB  
每特定时间，在进行数据持久化，fork子进程，将数据快照形式写入
临时文件，完成后替换上次的快照文件。更高效，但不保证数据完整
性，因为在持久化期间的数据会丢失  
AOF  
记录redis的所有操作指令，AOF文件当磁盘满了，启用AOF压缩机制，
但这样速度较慢
### 主从同步原理
服务器向主服务器发送SYNC指令，主服务器发送BGSAVE创建子进程，
将主服务器数据写入RDB，期间并将执行指令缓存到内存中（类似AOF）
完成后，RDB分发给子服务器，缓存操作指令以redis协议格式发给子
服务器
### 缓存雪崩 缓存穿透
缓存雪崩  
高峰请求时，缓存机器挂掉，请求落到数据库，造成数据库挂了  
redis 高可用，限流降级，redis持久化  
缓存穿透  
请求不在缓存中，便去数据库请求，大量请求造成数据库挂了
缓存不存在的key为空值，bloomfilter  

如果请求量大的某个key失效了，建立互斥锁，其他请求处于等待
