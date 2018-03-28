# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import codecs
import json


class AutopjtPipeline(object):
    def __init__(self):
        """
            打开data.json文件
            /home/mata/dataex/data.json：数据存储于本地
        """
        self.file = codecs.open("/home/mata/dataex/data.json", "wb", encoding='utf-8')

    def process_item(self, item, spider):
        i = json.dumps(dict(item), ensure_ascii=False)
        line = i + '\n'
        # 把数据写入data.json
        self.file.write(line)
        return item

    def close_spider(self, spider):
        # 关闭data.json文件
        self.file.close()
