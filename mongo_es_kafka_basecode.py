# 以下為mongodb基本指令
import pymongo
from pymongo import MongoClient
# client = MongoClient()
client = MongoClient('mongodb://18.181.219.11:27017')
db = client.yun
my_set = db.test
post = {"windows": "10",
	          "author": "yunshen",
              "task": ["localhost","25000", "to", "docker container mongo",27017]}

my_set.insert(post)
# a=my_set.find()
# for a in a:
#     print(a)


# 以下為Elasticsearch基本指令
from elasticsearch import Elasticsearch
es=Elasticsearch('http://192.168.60.128:9200')
print(es)
doc={'author':'yunshen',
     'title':'test elasticsearch',
     'where':'kafka 128'}
res=es.index(index='test',doc_type='elk',body=doc)


# 以下為kafka基本指令
# #
# # Licensed under the Apache License, Version 2.0 (the "License");
# # you may not use this file except in compliance with the License.
# # You may obtain a copy of the License at
# #
# # http://www.apache.org/licenses/LICENSE-2.0
# #
# # Unless required by applicable law or agreed to in writing, software
# # distributed under the License is distributed on an "AS IS" BASIS,
# # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# # See the License for the specific language governing permissions and
# # limitations under the License.
# #
#
# from confluent_kafka import Producer
# import sys
# import time
#
#
# # 用來接收從Consumer instance發出的error訊息
# def error_cb(err):
#     print('Error: %s' % err)
#
#
# # 主程式進入點
# if __name__ == '__main__':
#     # 步驟1. 設定要連線到Kafka集群的相關設定
#     props = {
#         # Kafka集群在那裡?
#         'bootstrap.servers': '192.168.60.128:9092',  # <-- 置換成要連接的Kafka集群
#         'error_cb': error_cb  # 設定接收error訊息的callback函數
#     }
#     # 步驟2. 產生一個Kafka的Producer的實例
#     producer = Producer(props)
#     # 步驟3. 指定想要發佈訊息的topic名稱
#     topicName = 'yunshen'
#     msgCounter = 0
#     try:
#         # produce(topic, [value], [key], [partition], [on_delivery], [timestamp], [headers])
#         producer.produce(topicName, key='whereami', value='yun_1')
#         producer.produce(topicName, 'shen_2')
#         producer.produce(topicName, 'work_3')
#         producer.produce(topicName, 'it is ok')
#         producer.flush()
#         msgCounter += 4
#         print('Send ' + str(msgCounter) + ' messages to Kafka')
#     except BufferError as e:
#         # 錯誤處理
#         sys.stderr.write('%% Local producer queue is full ({} messages awaiting delivery): try again\n'
#                          .format(len(producer)))
#     except Exception as e:
#         print(e)
#     # 步驟5. 確認所在Buffer的訊息都己經送出去給Kafka了
#     producer.flush()


#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from confluent_kafka import Consumer, KafkaException, KafkaError
import sys


# 用來接收從Consumer instance發出的error訊息
def error_cb(err):
    print('Error: %s' % err)


# 轉換msgKey或msgValue成為utf-8的字串
def try_decode_utf8(data):
    if data:
        return data.decode('utf-8')
    else:
        return None


# 指定要從哪個partition, offset開始讀資料
def my_assign(consumer_instance, partitions):
    for p in partitions:
        p.offset = 0
    print('assign', partitions)
    consumer_instance.assign(partitions)


if __name__ == '__main__':
    # 步驟1.設定要連線到Kafka集群的相關設定
    # Consumer configuration
    # See https://github.com/edenhill/librdkafka/blob/master/CONFIGURATION.md
    props = {
        'bootstrap.servers': '192.168.60.128:9092',       # Kafka集群在那裡? (置換成要連接的Kafka集群)
        'group.id': 'STUDENT_ID',                     # ConsumerGroup的名稱 (置換成你/妳的學員ID)
        'auto.offset.reset': 'earliest',             # Offset從最前面開始
        'session.timeout.ms': 6000,                  # consumer超過6000ms沒有與kafka連線，會被認為掛掉了
        'error_cb': error_cb                         # 設定接收error訊息的callback函數
    }
    # 步驟2. 產生一個Kafka的Consumer的實例
    consumer = Consumer(props)
    # 步驟3. 指定想要訂閱訊息的topic名稱
    topicName = "yunshen"
    # 步驟4. 讓Consumer向Kafka集群訂閱指定的topic
    consumer.subscribe([topicName], on_assign=my_assign)
    # 步驟5. 持續的拉取Kafka有進來的訊息
    count = 0
    try:
        while True:
            # 請求Kafka把新的訊息吐出來
            records = consumer.consume(num_messages=500, timeout=1.0)  # 批次讀取
            if records is None:
                continue

            for record in records:
                # 檢查是否有錯誤
                if record is None:
                    continue
                if record.error():
                    # Error or event
                    if record.error().code() == KafkaError._PARTITION_EOF:
                        # End of partition event
                        sys.stderr.write('%% {} [{}] reached end at offset {} - {}\n'.format(record.topic(),
                                                                                             record.partition(),
                                                                                             record.offset()))

                    else:
                        # Error
                        raise KafkaException(record.error())
                else:
                    # ** 在這裡進行商業邏輯與訊息處理 **
                    # 取出相關的metadata
                    topic = record.topic()
                    partition = record.partition()
                    offset = record.offset()
                    timestamp = record.timestamp()
                    # 取出msgKey與msgValue
                    msgKey = try_decode_utf8(record.key())
                    msgValue = try_decode_utf8(record.value())

                    # 秀出metadata與msgKey & msgValue訊息
                    count += 1
                    print('{}-{}-{} : ({} , {})'.format(topic, partition, offset, msgKey, msgValue))
    except KeyboardInterrupt as e:
        sys.stderr.write('Aborted by user\n')
    except Exception as e:
        sys.stderr.write(e)

    finally:
        # 步驟6.關掉Consumer實例的連線
        consumer.close()
