# Scrapy-Python-TheHinduDailyNews
Scrapy Crawler to Fetch Todays News From TheHindu.com, Easily Extendable, Simple yet Powerful

####Python Needed 3.*


####Python Module Needed 
>>Scrapy

>>socket

>>datetime

>>RAKE

### To Run crawler 
Go to Root Directory 

── __init__.py

├── __pycache__

│   ├── __init__.cpython-36.pyc

│   ├── items.cpython-36.pyc

│   └── settings.cpython-36.pyc

├── items.py

├── middlewares.py

├── pipelines.py

├── post.json

├── settings.py

├── spiders

│   ├── Post.py

│   ├── __init__.py

│   └── __pycache__

│       ├── Post.cpython-36.pyc

│       ├── __init__.cpython-36.pyc

│       └── check.cpython-36.pyc

└── stoplist.txt

>>scrapy crawl Post

>>Scrap crawl Post -o post.json #to log output into json file

#### Crawler will Crawl
LINK = Field()

TITLE = Field()

SUBHEADING = Field()

CONTENT = Field()

CATEGORY = Field()

######Calculated fields

IMAGE = Field()

TAGS = Field()

####From the Start URL #ex, /today's news

**For Tags, I am using RAKE, you can disable it in the crawler.**
You can genrate new spider for other pages with the same code.

Just Change name to any other

>>class PostSpider(scrapy.Spider):
>>
>>name = "MyOtherNewPage"