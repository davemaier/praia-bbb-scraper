# # -*- coding: utf-8 -*-

# # Define your item pipelines here
# #
# # Don't forget to add your pipeline to the ITEM_PIPELINES setting
# # See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# from kafka import KafkaProducer
# import json


# class KafkaSendPipeline(object):

#     def open_spider(self, spider):
#         self.kafka_producer = KafkaProducer(
#             **{
#                 'bootstrap_servers': 'pkc-ewzgj.europe-west4.gcp.confluent.cloud:9092',
#                 'sasl_mechanism': 'PLAIN',
#                 'security_protocol': 'SASL_SSL',
#                 'sasl_plain_username': 'BJQ62HTRFKMKDCIM',
#                 'sasl_plain_password': 'C4PzwqbfC7YYXIFqvCtQxJ+BgcQDrQ+/5o8QE1JsVVk31456wdDbO7anO831q6Pp'
#             },
#             value_serializer=lambda v: json.dumps(v).encode('utf-8'),
#             key_serializer=str.encode)


#     def process_item(self, item, spider):

#         self.kafka_producer.send("pt-info", item, item.get("id", ""))

#         return item

