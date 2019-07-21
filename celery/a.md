### broker
消息传输中间件，应用程序调用celery异步任务时候，向broker发送消息，worker获取消息。方案有RabbitMQ，Redis
### backend
存储程序发送的消息，以及执行的结果。
## celery架构
broker

worker

backend