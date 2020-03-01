"""
Retreive Classes for Web and Local
"""

import os
import bs4
import requests
import urllib
from .core.helpers import match

class RetrieveLocal:

    def retrieve_local_files(self, path, parameter, lookup):
        file_list = []
        for root, folders, files in os.walk(path):
            for file in files:
                abs_path = os.path.join(root, file)
                if parameter:
                    if match(file, parameter, lookup):
                        print("Found", abs_path)
                        file_list.append(abs_path)
                else:
                    print("Found", abs_path)
                    file_list.append(abs_path)
        return file_list

class RetrieveWeb:

    def retrieve_web_files(self, request_url, parameter, lookup):
        resp = requests.get(request_url)
        html = resp.text
        host = urllib.parse.urlparse(resp.url)
        hostname = host.hostname
        soup = bs4.BeautifulSoup(html,'html5lib')
        links = []
        for link in soup.select("[src^='http']"):
            if parameter:
                if match(link.get('src'), parameter, lookup):
                    print("Found", link.get('src'))
                    links.append(link.get('src'))
            else:
                print("Found", link.get('src'))
                links.append(link.get('src'))
        for link in soup.select("a[href^='/']"):
            src = link.get("src")
            if src:
                if src.startswith("/static"):
                    src = "https://" + hostname + src
                if src.startswith("//"):
                    src = "https://" + src[2:]
                if parameter:
                    if match(src, parameter, lookup):
                        print("Found", src)
                        links.append(src)
                else:
                    print("Found", src)
                    links.append(src)
        return links
