from locale import normalize
import pickle
import os
import re
from .utils.consolequirks import OpSys, currentOS

class File:
    def __init__(self, path: str):
        self.path:str = os.path.realpath(__file__)
        if currentOS == OpSys.WIN:
            if (re.search("^([A-Z]:\\\\)", path)):
                self.path: str = path
            else:
                if (path.startswith("/")):
                    self.path += path
                else:
                    self.path += f"/{path}"
        else:
            if (path.startswith("/")):
                self.path = path
            else:
                self.path += f"/{path}"
        self.__normalizePath()

    def __normalizePath(self):
        layers = self.path.split("/")
        try:
            z = layers.index("/..")
            while z >= 1:
                layers.pop(z-1)
                layers.pop(z-1)
                z = layers.index("/..")
        except ValueError:
            pass

        try:
            z = layers.index("/.")
            while z >= 1:
                layers.pop(z)
                z = layers.index("/.")
        except ValueError:
            pass
        self.path = "/".join(layers)

    def resolve(self, path):
        return File(os.path.join(self.path, path))

    def exists(self):
        return os.path.exists(self.path)

    def isFile(self):
        return os.path.isfile(self.path)

    def isDirectory(self):
        return os.path.isdir(self.path)

    def mkDir(self):
        created = False
        if (not self.isDirectory):
            os.mkdir(self.path)
            created = True
        return created

    def mkFile(self):
        with open(self.path, 'a'):
            pass

    def overwrite(self, contents: str):
        with open(self.path, 'w') as f:
            f.write(contents)

    def pickleDump(self, contents: object):
        with open(self.path, "wb") as file:
            pickle.dump(contents, file)

    def pickleLoad(self):
        with open(self.path, "rb") as file:
            return pickle.load(file)

    def resolve(self, path: str):
        return File(self.path + os.path.sep + path)
