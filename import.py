#!/usr/local/bin/python3


pages = [
    'https://web.archive.org/web/20150325003201/https://foundationdb.com/key-value-store/documentation/index.html',
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

from util import ensure_file,ensure_path
from urllib.parse import urlparse
from os.path import split,isfile, join,splitext,relpath,dirname
from pathlib import Path

import re
import os

map_regex = re.compile('(?P<url>\/web\/[\d]+(?P<kind>js_|cs_|im_|)\/(?P<src>.+?))')


def map_match(m):
    dict = m.groupdict()
    url = dict["src"]
    return url


def map_local_path(url):
    p = urlparse(url)
    # remove wayaback prefix
    clean = map_regex.sub(map_match,p.path)
    # parse the rest
    p2 = urlparse(clean)

    _,ext = splitext(p2.path)

    if len(ext) > 0:
        head, tail = split(p2.path)
        # filename, relpath
        return tail, p2.path.strip('/')

    # this could be google css
    if p2.path.endswith("css"):
        return "google.css",p2.path
    # no ext, then probably index.html

    joined = join(p2.path.strip('/'), "index.html")
    return 0,joined
   

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


ref_regex = re.compile('"(?P<url>\/web\/[\d]+(?P<kind>js_|cs_|im_|)\/(?P<src>.+?))"')




htmls = set()

def download_page(page):
    
    mapped = map_local_path(page)
    clean = mapped[0]
    target = join("doc",mapped[1])
    
    src = join("doc/orig", mapped[1])


    print("Downloading",page)
    if page in htmls:
        print("  skip inc")
        return mapped[1]
    if "//foundationdb.com" not in page:
        print("  skip not fdb")
        return page
    if ".pdf" in page:
        print("   skip pdf")
        return page
    if "javadoc" in page:
        print(" skip javadoc")
        return page

    
    ensure_file(page, src)
    
    htmls.add(page)

    links = set()


    
    def match(m):
        dict = m.groupdict()
        url = dict["url"]
        kind = dict["kind"]

        
        name = map_local_path(url)[0]
        full_url = "https://web.archive.org" + url

        if kind == "":
            print("Recur!!", full_url)
            full_local = download_page(full_url)
            print("Map", full_url, "to", full_local)
             
        else:
            full_local = kind + "/" + name
            ensure_file(full_url,"doc/" + full_local)
            print(full_local)

        # matching local path
        return relpath(full_local,dirname(mapped[1]))

    with open(src, 'r') as r:
        lines = list(r)
        clean_wb(lines)
        result = []
        for i,l in enumerate(lines):
            result.append(ref_regex.sub(match,l))

        print("Saving to ",target)
        ensure_path(target)
            
        with open(target, 'w') as w:
            w.writelines(result)
        return mapped[1]
            
for page in pages:
    download_page(page)
