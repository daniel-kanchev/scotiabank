BOT_NAME = 'scotiabank'
SPIDER_MODULES = ['scotiabank.spiders']
NEWSPIDER_MODULE = 'scotiabank.spiders'
ROBOTSTXT_OBEY = True
LOG_LEVEL = 'WARNING'
ITEM_PIPELINES = {
   'scotiabank.pipelines.DatabasePipeline': 300,
}