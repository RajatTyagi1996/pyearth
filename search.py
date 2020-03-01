
"""
sub module search has class Search, that is used to search for particular file
"""

import os
from retrieve import (
    RetrieveLocal,
    RetrieveWeb
)


class Search(RetrieveLocal,
             RetrieveWeb):

    def __init__(self, base_path=os.getcwd()):
        self.base_path = base_path

    @property
    def is_web(self):
        return self.base_path.startswith("http")

    def files(self, parameter=None, lookup="endswith"):
        if self.is_web:
            pass
        else:
            return self.retrieve_local_files(self.base_path,
                                             parameter,
                                             lookup)
