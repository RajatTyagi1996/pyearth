"""
Retreive Classes for Web and Local
"""

import os
import bs4
import requests
from core.helpers import match

class RetrieveLocal:

    def retrieve_local_files(self, path, parameter, lookup):
        file_list = []
        for root, folders, files in os.walk(path):
            for file in files:
                abs_path = os.path.join(root, file)
                if parameter:
                    if match(file, parameter, lookup):
                        file_list.append(abs_path)
                else:
                    file_list.append(abs_path)
        return file_list


class RetrieveWeb:

    def retrieve_web_files(self, path, parameter, lookup):
        file_list = []
        pass
