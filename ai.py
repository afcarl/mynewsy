'''
Created on 31 Oct 2015

@author: af
'''
import conf
import feedparser
import sys
import logging
import pdb
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer
from feed_downloader import download_feeds, get_items_contents

def cluster_news(data, n_clusters=10):
    clus = KMeans(n_clusters, n_jobs=1)
    vectorizer = TfidfVectorizer(data, encoding='utf-8', stop_words='english', ngram_range=(1, 2), max_df=0.5, min_df=2, binary=True, norm='l2', use_idf=True, sublinear_tf=True)
    X = vectorizer.fit_transform(data)
    clus.fit(X)
    return clus.labels_
    

if __name__ == '__main__':
    conf.init()
    feeds = download_feeds(conf.rss_urls)
    items = get_items_contents(feeds)
    data = [r for r in items['title']+ ' ' + items['summary'] + ' ' + items['description']]
    #data = [r for r in items['title']+ ' ' + items['summary'] ]
    labels = cluster_news(data, n_clusters=50)
    pdb.set_trace()