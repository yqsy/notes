

<!-- TOC -->

- [1. 说明](#1-说明)
- [2. 安装](#2-安装)
- [3. 使用](#3-使用)
- [4. 说明](#4-说明)

<!-- /TOC -->


<a id="markdown-1-说明" name="1-说明"></a>
# 1. 说明

* 有序 - 同一个分区同一个客户端写入是按顺序来的
* 可靠 - acks=all + 集群可以保证把消息投递到brocker. (可以不存储到磁盘). at least once
* 去重 - 业务幂等就可以

<a id="markdown-2-安装" name="2-安装"></a>
# 2. 安装


```bash
mkdir -p ~/env

wget http://mirrors.shu.edu.cn/apache/kafka/2.2.0/kafka_2.12-2.2.0.tgz -O /tmp/kafka_2.12-2.2.0.tgz
tar -xvzf /tmp/kafka_2.12-2.2.0.tgz -C ~/env
cd ~/env
mv kafka_2.12-2.2.0 kafka

# 开启
~/env/kafka/bin/kafka-server-start.sh ~/env/kafka/config/server.properties

# 关闭
~/env/kafka/bin/kafka-server-stop.sh


# 删除持久数据
rm -rf /tmp/kafka-logs
```

<a id="markdown-3-使用" name="3-使用"></a>
# 3. 使用


主题:
```bash
# 增题
~/env/kafka/bin/kafka-topics.sh --create --zookeeper localhost:2181 --topic my-topic --replication-factor 1 --partitions 3 

# 查主题
~/env/kafka/bin/kafka-topics.sh --list --zookeeper localhost:2181

# 改主题
~/env/kafka/bin/kafka-topics.sh --alter --zookeeper localhost:2181 --topic my-topic --partitions 16

# 删主题
~/env/kafka/bin/kafka-topics.sh --delete  --zookeeper localhost:2181 --topic my-topic

# 查主题[详细]
~/env/kafka/bin/kafka-topics.sh --describe --zookeeper localhost:2181/kafka-cluster 

# 主题
~/env/kafka/bin/kafka-topics.sh --describe --zookeeper localhost:2181/kafka-cluster --under-replicated-partitions
```

生产者:
```bash
# 发布
~/env/kafka/bin/kafka-console-producer.sh --broker-list localhost:9092 --topic my-topic

# 发布[文件]
~/env/kafka/bin/kafka-console-producer.sh --broker-list localhost:9092 --topic my-topic < messages.txt

# 发布[avro]
~/env/kafka/bin/kafka-console-producer.sh --broker-list localhost:9092 --topic my.Topic --property value.schema='{"type":"record","name":"myrecord","fields":[{"name":"f1","type":"string"}]}' --property schema.registry.url=http://localhost:8081
```

消费者:
```bash
# 消费消息
~/env/kafka/bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic my-topic --from-beginning

# 消费消息[1个]
~/env/kafka/bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic my-topic  --max-messages 1

# 消费消息[指定偏移]
~/env/kafka/bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic __consumer_offsets --formatter 'kafka.coordinator.GroupMetadataManager$OffsetsMessageFormatter' --max-messages 1

# 消费消息[组]
~/env/kafka/bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic my-topic --new-consumer --consumer-property group.id=my-group

# 消费消息[avro]
~/env/kafka/bin/kafka-avro-console-consumer.sh --bootstrap-server localhost:9092 --topic position-reports --new-consumer  --from-beginning --property schema.registry.url=localhost:8081 --max-messages 10

# 消费消息[avro]
~/env/kafka/bin/kafka-avro-console-consumer.sh  --topic position-reports --new-consumer --bootstrap-server localhost:9092 --from-beginning --property schema.registry.url=localhost:8081
```

消费者群组:
```bash
# 查
~/env/kafka/bin/kafka-consumer-groups.sh --bootstrap-server localhost:9092 --new-consumer --list 

# 查[详细]
~/env/kafka/bin/kafka-consumer-groups.sh --bootstrap-server --describe localhost:9092 --group testgroup

```

配置:
```bash
# 增
~/env/kafka/bin/kafka-configs.sh --zookeeper localhost:2181 --alter --entity-type topics --entity-name my-topic --add-config retention.ms=3600000
# 查
~/env/kafka/bin/kafka-configs.sh --zookeeper localhost:2181 --describe --entity-type topics --entity-name my-topic
# 删
~/env/kafka/bin/kafka-configs.sh --zookeeper localhost:2181 --alter --entity-type topics --entity-name my-topic --delete-config retention.ms 
```

性能:
```bash
~/env/kafka/bin/kafka-producer-perf-test.sh --topic position-reports --throughput 10000 --record-size 300 --num-records 20000 --producer-props bootstrap.servers="localhost:9092"
```

acls:
```bash
~/env/kafka/bin/kafka-acls.sh --authorizer-properties zookeeper.connect=localhost:2181 --add --allow-principal User:Bob --consumer --topic topicA --group groupA
~/env/kafka/bin/kafka-acls.sh --authorizer-properties zookeeper.connect=localhost:2181 --add --allow-principal User:Bob --producer --topic topicA
~/env/kafka/bin/kafka-acls.sh --authorizer-properties zookeeper.connect=localhost:2181 --list --topic topicA
```

<a id="markdown-4-说明" name="4-说明"></a>
# 4. 说明

* https://github.com/Landoop/kafka-cheat-sheet (cheat sheet)
