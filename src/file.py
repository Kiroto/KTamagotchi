import pickle
import os
import re

from src.console import OpSys, CURRENT_OS

class File:
    BASE_FILE = os.getcwd()
    DATA_FILE = f".{os.sep}data{os.sep}"
    def __init__(self, path: str):
        path = path.replace("/", os.sep).replace("\\", os.sep)
        self.path: str = os.path.realpath(File.BASE_FILE)
        if CURRENT_OS == OpSys.WIN:
            if (re.search("^(([A-Z]|[a-z]):\\\\)", path)):
                self.path = path
            else:
                if (path.startswith("\\")):
                    self.path += path
                else:
                    self.path += f"\\{path}"
        else:
            if (path.startswith("/")):
                self.path = path
            else:
                self.path += f"/{path}"
        self.__normalizePath()

    def __normalizePath(self):
        layers = self.path.split(os.sep)
        try:
            prev = f"{os.sep}.."
            z = layers.index(prev)
            while z >= 1:
                layers.pop(z-1)
                layers.pop(z-1)
                z = layers.index(prev)
        except ValueError:
            pass

        try:
            this = f"{os.sep}."
            z = layers.index(this)
            while z >= 1:
                layers.pop(z)
                z = layers.index(this)
        except ValueError:
            pass
        self.path = os.sep.join(layers)

    def resolve(self, path) -> 'File':
        return File(os.path.join(self.path, path))

    def parent(self) -> 'File':
        return self.resolve("..")

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

    def pickleLoad(self) -> object:
        with open(self.path, "rb") as file:
            pet : object = pickle.load(file)
            return pet


