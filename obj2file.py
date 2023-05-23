from pickle import *

class OTF:
    def __init__(self, path):
        self.path = path
        self.pack = list()

    def pack_obj(self, obj):
        self.pack.append(obj)

    def push_bulk(self):
        file = open(self.path, "wb")
        dump(self.pack, file)
        file.close()
        self.pack = list()
        
    def pull_bulk(self):
        file = open(self.path, "rb")
        l = load(file)
        file.close()
        return l
        
    def wipe_file(self):
        file = open(self.path, "w")
        file.seek(0)
        file.truncate() 
        file.close()