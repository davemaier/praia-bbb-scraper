from kafka import KafkaConsumer

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

process = CrawlerProcess(get_project_settings())

consumer = KafkaConsumer("users",**{
                'bootstrap_servers': 'pkc-ewzgj.europe-west4.gcp.confluent.cloud:9092',
                'sasl_mechanism': 'PLAIN',
                'security_protocol': 'SASL_SSL',
                'sasl_plain_username': 'BJQ62HTRFKMKDCIM',
                'sasl_plain_password': 'C4PzwqbfC7YYXIFqvCtQxJ+BgcQDrQ+/5o8QE1JsVVk31456wdDbO7anO831q6Pp'
            })

for msg in consumer:

    
    process.crawl('route', msg.value)
    process.start()