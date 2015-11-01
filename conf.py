'''
Created on 31 Oct 2015

@author: af
'''
import codecs
import logging
from xml.etree import ElementTree

def extract_rss_urls_plain_text(rss_file):
    urls = []
    with codecs.open(rss_file, 'r', encoding='utf-8') as url_file:
        for url in url_file:
            urls.append(url)
    return urls
def extract_rss_urls_from_opml(filename):
    urls = []
    with open(filename, 'rt') as f:
        tree = ElementTree.parse(f)
    for node in tree.findall('.//outline'):
        url = node.attrib.get('xmlUrl')
        if url:
            urls.append(url)
    return urls
def read_stop_words(filename='stops.txt'):
    stops = set()
    with codecs.open(filename, 'r', 'utf-8') as inf:
        for l in inf:
            stops.add(l.strip())
    return stops    
def init():
    global rss_file
    global rss_urls
    global stop_persian
    rss_file_plain_text = 'urls.txt'
    rss_file_opml = 'urls.xml'
    #rss_urls = extract_rss_urls_plain_text(rss_file_plain_text)
    rss_urls = extract_rss_urls_from_opml(rss_file_opml)
    stop_persian = read_stop_words('stops.txt')