import os
import pkgutil

class DataFile:
    allPackages = pkgutil.walk_packages()

    def __init__(self: 'DataFile', path: str, preload: bool = False):
        self.path = path
        self.data: bytes = None
        if (preload):
            self.load()

    def fileName(self):
        return self.path.split(os.sep)[-1]

    def load(self: 'DataFile', force : bool = False):
        if (self.data == None or force):
            self.data = pkgutil.get_data(__name__, self.path)

    def getBin(self):
        if self.data == None:
            self.load()
        return self.data

