# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import re

class BookCleaningPipeline:
    def process_item(self, item, spider):
        # Parse price: "£45.17" -> 45.17
        price_str = item.get('price', '')
        match = re.search(r'[\d.]+', price_str)
        item['price'] = float(match.group()) if match else None

        stock_str = item.get('availability', '')
        match = re.search(r'\((\d+) available\)', stock_str)
        item['stock_count'] = int(match.group(1)) if match else 0
        item['availability'] = 'In stock' if 'in stock' in stock_str.lower() else 'Out of stock'


        # convert num_reviews to int
        try:
            item['num_reviews'] = int(item['num_reviews'])
        except (ValueError, TypeError):
            item['num_reviews'] = 0  # or None — your call, just be consistent
            spider.logger.warning(f"Bad num_reviews value: {item.get('num_reviews')!r} for {item.get('url')}")
        return item