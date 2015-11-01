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
from collections import Counter
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer
from feed_downloader import download_feeds, get_items_contents
from _collections import defaultdict

def cluster_news(data, stop_words='english', n_clusters=10):
    clus = KMeans(n_clusters, n_jobs=1)
    vectorizer = TfidfVectorizer(data, encoding='utf-8', stop_words=stop_words, ngram_range=(1, 2), max_df=0.1, min_df=2, binary=False, norm='l2', use_idf=True, sublinear_tf=True)
    X = vectorizer.fit_transform(data)
    clus.fit(X)
    return clus.labels_
    

if __name__ == '__main__':
    conf.init()
    feeds = download_feeds(conf.rss_urls)
    items = get_items_contents(feeds)
    #data = [r for r in items['title']+ ' ' + items['summary'] + ' ' + items['description']]
    data = [r for r in items['title']+ ' ***** ' + items['summary'] ]
    labels = cluster_news(data, conf.stop_persian, n_clusters=50)
    labels = labels.tolist()
    label_c = Counter(labels)
    label_items = defaultdict(list)
    for l in set(labels):
        label_items[l] = [i for i,x in enumerate(labels) if x == l]
    pdb.set_trace()