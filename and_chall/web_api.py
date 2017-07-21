import urllib2
from xml.etree.ElementTree import parse
import re

u = urllib2.urlopen('https://news.google.com/?output=rss')
doc = parse(u)


def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', raw_html)
  return cleantext

for item in doc.iterfind('channel/item'):
    title = item.findtext('title')
    date = item.findtext('pubDate')
    link = item.findtext('link')
    desc = item.findtext('description')

    print(title)
    print(' ')
    print(cleanhtml(desc))
    print(' ')
    print(date)
    print('__________________________________________________________________________________')
    print(' ')

