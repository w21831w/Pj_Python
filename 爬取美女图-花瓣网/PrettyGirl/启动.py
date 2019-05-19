from scrapy.cmdline import execute
import os
curPath = os.path.realpath(__file__)[:-5]
os.chdir(curPath)
execute("scrapy crawl PrettyGirl".split())
