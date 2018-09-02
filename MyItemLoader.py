from scrapy.loader import ItemLoader
from scrapy.loader.processors import Identity,TakeFirst,MapCompose,Join

class MyItemLoader(ItemLoader):
	default_output_processor = Identity()
	default_input_processor = Identity()
