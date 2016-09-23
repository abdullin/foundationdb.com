#!/usr/local/bin/python3


pages = [
    'https://web.archive.org/web/20150319133839/https://foundationdb.com/key-value-store/white-papers/the-transaction-manifesto',
    'https://web.archive.org/web/20150319133839/https://foundationdb.com/key-value-store/white-papers/the-layer-concept',
    'https://web.archive.org/web/20150319133839/https://foundationdb.com/key-value-store/white-papers/the-cap-theorem',
    'https://web.archive.org/web/20150319133839/https://foundationdb.com/key-value-store/white-papers/anti-features',
    'https://web.archive.org/web/20150325003224/https://foundationdb.com/key-value-store/documentation/data-modeling.html',
    'https://web.archive.org/web/20150325003222/https://foundationdb.com/key-value-store/documentation/command-line-interface.html',
    'https://web.archive.org/web/20150325003219/https://foundationdb.com/key-value-store/documentation/mr-status.html',
    'https://web.archive.org/web/20150325003222/https://foundationdb.com/key-value-store/documentation/tls.html',
    'https://web.archive.org/web/20150325003225/https://foundationdb.com/key-value-store/documentation/configuration.html',
    'https://web.archive.org/web/20150325003220/https://foundationdb.com/key-value-store/documentation/administration.html',
    'https://web.archive.org/web/20150325003228/https://foundationdb.com/key-value-store/documentation/backups.html',
    'https://web.archive.org/web/20150325003219/https://foundationdb.com/key-value-store/documentation/known-limitations.html',
    'https://web.archive.org/web/20150325003225/https://foundationdb.com/key-value-store/documentation/platforms.html',
    'https://web.archive.org/web/20150325003222/https://foundationdb.com/key-value-store/documentation/release-notes.html',
    'https://web.archive.org/web/20150325003224/https://foundationdb.com/key-value-store/documentation/building-cluster.html',
    'https://web.archive.org/web/20150325003219/https://foundationdb.com/key-value-store/documentation/developer-guide.html',
    'https://web.archive.org/web/20150325003218/https://foundationdb.com/key-value-store/documentation/api-c.html',
    'https://web.archive.org/web/20150325003220/https://foundationdb.com/key-value-store/documentation/api-php.html',
    'https://web.archive.org/web/20150325003516/https://foundationdb.com/key-value-store/recipes/administrator/moving-a-cluster-to-new-machines',
    'https://web.archive.org/web/20150325003516/https://foundationdb.com/key-value-store/recipes/administrator/setting-up-a-cluster-on-ec2',
    'https://web.archive.org/web/20150325003416/https://foundationdb.com/key-value-store/documentation/api-general.html',
    
    'https://web.archive.org/web/20150325003415/https://foundationdb.com/key-value-store/documentation/api-error-codes.html',
        'https://web.archive.org/web/20150325003227/https://foundationdb.com/key-value-store/documentation/api-python.html',

    # tutorials
    'https://web.archive.org/web/20150325003227/https://foundationdb.com/key-value-store/documentation/class-scheduling.html',
    'https://web.archive.org/web/20150325003512/https://foundationdb.com/key-value-store/documentation/class-scheduling-go.html',
    'https://web.archive.org/web/20150325003223/https://foundationdb.com/key-value-store/documentation/enron.html',
    'https://web.archive.org/web/20150325003224/https://foundationdb.com/key-value-store/documentation/largeval.html',
    'https://web.archive.org/web/20150325003221/https://foundationdb.com/key-value-store/documentation/datalog.html',
    'https://web.archive.org/web/20150325003228/https://foundationdb.com/key-value-store/recipes/developer/adaptive-sharding',
    'https://web.archive.org/web/20150325003513/https://foundationdb.com/key-value-store/recipes/developer/blob',
    'https://web.archive.org/web/20150325003514/https://foundationdb.com/key-value-store/recipes/developer/bulk-loading',
    'https://web.archive.org/web/20150325003228/https://foundationdb.com/key-value-store/recipes/developer/graph',
    'https://web.archive.org/web/20150325003228/https://foundationdb.com/key-value-store/recipes/developer/hierarchical-documents',
    'https://web.archive.org/web/20150325003228/https://foundationdb.com/key-value-store/recipes/developer/multimaps',
    'https://web.archive.org/web/20150325003228/https://foundationdb.com/key-value-store/recipes/developer/priority-queues',
    'https://web.archive.org/web/20150325003228/https://foundationdb.com/key-value-store/recipes/developer/queues',
    'https://web.archive.org/web/20150325003228/https://foundationdb.com/key-value-store/recipes/developer/ranked-sets',
    'https://web.archive.org/web/20150325003228/https://foundationdb.com/key-value-store/recipes/developer/segmented-range-reads',
    'https://web.archive.org/web/20150325003228/https://foundationdb.com/key-value-store/recipes/developer/simple-indexes',
    'https://web.archive.org/web/20150325003228/https://foundationdb.com/key-value-store/recipes/developer/spatial-indexing',
    'https://web.archive.org/web/20150325003228/https://foundationdb.com/key-value-store/recipes/developer/subspace-indirection',
    'https://web.archive.org/web/20150325003228/https://foundationdb.com/key-value-store/recipes/developer/tables',
    'https://web.archive.org/web/20150325003228/https://foundationdb.com/key-value-store/recipes/developer/vector',
    'https://web.archive.org/web/20150325003228/https://foundationdb.com/key-value-store/recipes',


    'https://web.archive.org/web/20150325003200/https://foundationdb.com/key-value-store/performance',
    'https://web.archive.org/web/20150325003219/https://foundationdb.com/key-value-store/documentation/known-limitations.html',

    # whitepapers
    'https://web.archive.org/web/20150325003232/https://foundationdb.com/key-value-store/white-papers/testing',
    'https://web.archive.org/web/20150325003158/https://foundationdb.com/key-value-store/white-papers/flow',
    'https://web.archive.org/web/20150325003158/https://foundationdb.com/key-value-store/white-papers/solid-state-drives',
    'https://web.archive.org/web/20150325003158/https://foundationdb.com/key-value-store/white-papers/fault-tolerance',
    'https://web.archive.org/web/20150325003158/https://foundationdb.com/key-value-store/white-papers/transaction-processing',
    'https://web.archive.org/web/20150325003158/https://foundationdb.com/key-value-store/white-papers/scalability',
    'https://web.archive.org/web/20150325003158/https://foundationdb.com/key-value-store/white-papers/sql-in-a-cloud-world',
    'https://web.archive.org/web/20150325003158/https://foundationdb.com/key-value-store/white-papers/future-of-nosql',
    'https://web.archive.org/web/20150325003158/https://foundationdb.com/key-value-store/white-papers/consistency',
    'https://web.archive.org/web/20150325003158/https://foundationdb.com/key-value-store/white-papers/anti-features',
    'https://web.archive.org/web/20150325003158/https://foundationdb.com/key-value-store/white-papers/the-cap-theorem',
    'https://web.archive.org/web/20150325003158/https://foundationdb.com/key-value-store/white-papers/the-layer-concept',
    'https://web.archive.org/web/20150325003158/https://foundationdb.com/key-value-store/white-papers/the-transaction-manifesto',


    # labs
    'https://web.archive.org/web/20150325003252/https://labs.foundationdb.com/celery-layer',
    'https://web.archive.org/web/20150325003252/https://labs.foundationdb.com/node-js-chat-app'
]


from urllib.parse import urlparse
from os.path import split,isfile
from pathlib import Path
import os


import urllib.request

def ensure_path(path):
    directory = os.path.dirname(path)
    if not os.path.exists(directory):
        os.makedirs(directory)

def map_local_path(url):
    p = urlparse(url)
    head, tail = split(p.path)
    return tail

def ensure_file(url,local):
    if isfile(local):
        return local
    else:
        print("Doesn't exist", local)
        ensure_path(local)
        urllib.request.urlretrieve(url, local)
    return local

wayback_start = '<!-- BEGIN WAYBACK TOOLBAR INSERT -->'

def contains(lst,text):
    for l in lst:
        if l.find(text) >= 0:
            return True
    return False

def clean_wb(lst):
    out = []
    for i,l in enumerate(lst):
        if l.find("WAYBACK")>=0:
            out.append(i)
    if len(out) == 0:
        return lst
    del lst[out[0]:out[1]+1]
    return lst
import re
pattern = re.compile('"(?P<url>\/web\/[\d]+(?P<kind>js_|cs_|im_)\/(?P<src>.+?))"')
def match(m):
    dict = m.groupdict()
    url = dict["url"]
    kind = dict["kind"]
    name = map_local_path(url)
    full_url = "https://web.archive.org" + url
    full_local = kind + "/" + name

    ensure_file(full_url,"doc/" + full_local)
    print(full_local)
    

    
    return full_local

    

for page in pages:
    clean = map_local_path(page)
    target = "doc/" + clean 
    src = "doc/orig/" + clean
    ensure_file(page, src)

    if not(target.endswith(".html")):
        target = target + ".html"

    with open(src, 'r') as r:
        lines = list(r)
        clean_wb(lines)
        result = []
        for i,l in enumerate(lines):
            result.append(pattern.sub(match,l))

        print("Saving to ",target)
            
        with open(target, 'w') as w:
            w.writelines(result)
            
