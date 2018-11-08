# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.pipelines.images import ImagesPipeline
import settings
import os
class AtezPipeline(object):
    def process_item(self, item, spider):
        return item


class AtezImagesPipeline(ImagesPipeline):

      def get_media_requests(self, item, info):
          requests = super(AtezImagesPipeline, self).get_media_requests(item,info)
          for request in requests:
              request.item = item
          return requests

      def file_path(self, request, response=None, info=None):
         def_file_path = super(AtezImagesPipeline, self).file_path(request,response,info)
         category = request.item.get('category')
         images_store = settings.IMAGES_STORE
         category_path = os.path.join(images_store,category)
         if not os.path.exists(category_path):
             os.mkdir(category_path)
         image_name = def_file_path.replace('full/','')
         image_path = os.path.join(category_path,image_name)
         return image_path


