
"""
sub module search has class Search, that is used to search for particular file
"""

import os
import shutil
import requests
from .retrieve import (
    RetrieveLocal,
    RetrieveWeb
)
from .core.frames import FileFrame
from .core.helpers import filter_list


class Files(RetrieveLocal,
            RetrieveWeb):

    abspath = False
    match = None
    lookup = "endswith"
    save_path = os.getcwd()
    def __init__(self, base_path=os.getcwd()):
        self.base_path = base_path
        self.is_web = self.base_path.startswith("http")
        self.fileframe = self.to_fileframe()
        self.d_match = self.match
        self.d_lookup = self.lookup
        self.d_abspath = self.abspath

    def __repr__(self):
        if self.is_any_change:
            self.fileframe = self.to_fileframe()
        return repr(self.fileframe)


    @property
    def is_any_change(self):
        if self.d_match == self.match and self.d_abspath == self.abspath and self.d_lookup == self.lookup:
            return False
        else:
            self.d_match = self.match
            self.d_lookup = self.lookup
            self.d_abspath = self.abspath
            return True

    
    def to_list(self):
        if self.is_web:
            return filter_list(self.retrieve_web_files(self.base_path,
                                                       self.match,
                                                       self.lookup), self.abspath)
        else:
            return filter_list(self.retrieve_local_files(self.base_path,
                                            self.match,
                                            self.lookup), self.abspath)
    def to_fileframe(self):
        return FileFrame([{"File":n} for n in self.to_list()])

    def filter(self, match=match, lookup="icontains"):
        old_match = self.match
        old_lookup = self.lookup
        self.match = match
        self.lookup = lookup
        ff = self.to_fileframe()
        self.match = old_match
        self.lookup = old_lookup
        return ff
    def save(self, save_path=save_path):
        self.abspath = True
        for f in self.to_list():
            name = os.path.split(f)[-1].split("?")[0]
            full_name = os.path.join(save_path, name)
            if not self.is_web:
                shutil.copy(f, full_name)
            else:
                resp = requests.get(f)
                content = resp.content
                with open(full_name, "wb") as wb:
                    wb.write(content)
        self.abspath = self.d_abspath
        return True



