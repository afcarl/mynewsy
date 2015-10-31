'''
Created on 31 Oct 2015

@author: af
'''
import conf
import feedparser
import sys
import logging
import numpy as np
import pdb
import pandas as pd

def download_feeds(urls):
    feeds = {}
    feedparser._HTMLSanitizer.acceptable_elements = []
    for u in urls:
        try:
            d = feedparser.parse(u)
            feeds[u] = d 
        except:
            logging.warn(str(sys.exc_info()))
    return feeds
def get_items_contents(feeds):
    entries = []
    for url, feed in feeds.iteritems():
        for entry in feed.entries:
            try:
                id = entry.id
                link = entry.link
                title = entry.title
                summary = entry.summary
                description = entry.description
                entries.append((url, id , link, title, summary, description))
            except:
                logging.warn(sys.exc_info())
    data = np.ndarray((len(entries), 6), dtype=np.dtype(object))
    data[:] = entries
    df = pd.DataFrame(data, columns=['url', 'id', 'link', 'title', 'summary', 'description'])
    return df
    
            

if __name__ == '__main__':
    conf.init()
    feeds = download_feeds(conf.rss_urls)
    df = get_items_contents(feeds)
    pdb.set_trace()
    