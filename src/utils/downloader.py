#!/usr/bin/env python
from pdb import set_trace as dbg

import urllib2
import json


class SyncDownloader(object):

    def get_data_from_url(self, url):
        response = urllib2.urlopen(url)
        data = response.read()

    def download_from_url(self, url, file_name):
        data = self.get_data_from_url(url)
        with open(file_name, 'wb') as f:
            f.write(data)



