
from urllib.request import urlretrieve
from os.path import isfile, dirname, exists
import os

def ensure_path(path):
    directory = dirname(path)
    if not exists(directory):
        os.makedirs(directory)
        
def ensure_file(url,local):
    if isfile(local):
        return local
    else:
        print("Doesn't exist", local)
        ensure_path(local)
        urlretrieve(url, local)
    return local



