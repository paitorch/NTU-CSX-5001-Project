# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 16:12:30 2018

@author: Louis  github: paitorch
"""


from urllib.request import Request
from urllib.request import urlopen
from urllib.request import urljoin
from urllib.parse import urlparse
from urllib.error import URLError
from html.parser import HTMLParser


# get input url from command line — takes only one url at a time

"""
if len(sys.argv) == 1 or len(sys.argv) > 2:
    print("Error: Need 1 Input URL")
    sys.exit(0)
else:
    url = sys.argv[1].lower()
    print("Input URL:", url)
"""
# in order to run in spyder, predefine the url
url = "http://24h.pchome.com.tw"

if not url.startswith('http://'):
    url = 'http://' + url
if not url.endswith('/'):
    url += '/'

class crawlLink(object):
 
    def __init__(self, url):
        self.toUrl = url
        self.toVisit = [url, ]
        self.visited = []
        self.fullData = {}
        
class parsePage(HTMLParser):
    toUrl = ''
    currentUrl = ''
    parsedText = {}
 
    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for (key, value) in attrs:
                if key == 'href':
                    if self.toUrl not in value:
                        addUrl = urljoin(self.toUrl, value)
                    else:
                        addUrl = value
                    self.links.append(addUrl)
 
    def handle_data(self, data):
        dictKey = self.currentUrl.split('://')[1]
        if data.strip():
            if dictKey in self.parsedText:
                self.parsedText[dictKey] += (';' + data.strip())
            else:
                self.parsedText[dictKey] = data.strip()
 
    def extractLinks(self, url, base):
        self.links = []
        self.toUrl = base
        self.currentUrl = url
        self.headers = {}
        self.headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux x86_64; rv:43.0) Gecko/20100101 Firefox/43.0'
        req = Request(self.toUrl, headers = self.headers)
        try:
            resp = urlopen(req)
        except URLError:
            return self.parsedText, self.links
 
        if 'text/html' in resp.getheader('Content-Type'):
        # get html response as string, response is in bytes
            try: 
                respData = resp.read().decode('utf-8')
            except UnicodeDecodeError:
            # cater for encoding errors in webpages
                respData = resp.read().decode('ISO-8859–1')
 
            self.feed(respData)
 
            # return only unique links
            self.links = list(set(self.links))
            return self.parsedText, self.links
        else:
            return self.parsedText, self.links

# spider method
# def spider(url):
"""Basic Crawler
Input: main url
Output: html of all parsed urls
Method: Iterate over list of URLs until list is exhausted.
"""
 
# check for full-url, if not add http://
# check for valid urls — use urlparse
if not url.startswith('http://'):
    url = 'http://' + url
if not url.endswith('/'):
    url += '/'
totalLinks = 0
crawling = crawlLink(url)
filename = urlparse(crawling.toUrl).netloc + '.txt'
 
while crawling.toVisit != []:
    
    totalLinks += 1
    activeUrl = crawling.toVisit[0]
   

    crawling.toVisit = crawling.toVisit[1:]
    print(">>> Crawling URL '%s' " % activeUrl)
 
    parser = parsePage()
    pData, pLinks = parser.extractLinks(activeUrl, url)
    if pLinks != [] or pData != {}:
        # add text data
        crawling.fullData.update(pData)
 
        # add urls to list — toVisit
        # also, check for redundant links in toVisit and visited
        crawling.toVisit += pLinks
        crawling.visited.append(activeUrl)
 
        # remove duplicate links in toVisit
        crawling.toVisit = list(set(crawling.toVisit))
 
        # remove links that are already visited
        visitedSet = set(crawling.visited)
        newToVisit = [link for link in crawling.toVisit if link not in visitedSet]
        crawling.toVisit = newToVisit
 
        # remove links that are redirecting to other sites
        crawling.toVisit = [link for link in crawling.toVisit if url in link]
 
        print(">>> Links remaining %d" % len(crawling.toVisit))
 
# save data to file
# writing to file with ‘w’, updating everything after each crawl
with open(filename, mode='w', encoding='utf-8') as txtFile:
    for (key, value) in crawling.fullData.items():
        txtFile.write('-'*10)
        txtFile.write(key + '\n')
        txtFile.write(value + '\n')

print("Total Links crawled = %d" % totalLinks)