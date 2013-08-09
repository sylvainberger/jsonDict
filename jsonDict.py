"""
Json dictionary class.
Use this to simplify the loading, saving of json data
"""
__author__ = "Sylvain Berger"
__email__ = "sylvain.berger@gmail.com"
__version__ = "1.0.0"
__status__ = "Production"

import os
import json

class JsonDict(dict):
    """ Dictionary that can load, save and perform different thing on json data """
    filename = None

    def __init__(self, filename=None, autoLoad=True):
        super(JsonDict, self).__init__()
        if filename:
            self.filename = filename
        if autoLoad and self.filename:
            self.load()

    @classmethod
    def fromFile(cls, filename):
        """ Constructor that create a jsonDict from a json file """
        inst = JsonDict()
        inst.load(filename=filename)
        return inst

    @classmethod
    def fromJson(cls, jsonString):
        """ Constructor that takes a json string as input data """
        inst = JsonDict()
        inst.loads(jsonString)
        return inst

    def load(self, filename=None):
        """ Load a json file from disk """
        if filename:
            self.filename = filename
        if not self.filename or not os.path.exists(self.filename):
            return
        f = open(self.filename, 'r')
        _json = json.load(f)
        self.update(_json)
        return self.filename

    def save(self, filename=None):
        """ Save the data in a json formated file on disk"""
        if filename:
            self.filename = filename
        if not self.filename:
            return
        f = open(self.filename, 'w')
        json.dump(self, f, indent=4, sort_keys=True)
        return self.filename

    def loads(self, jsonString):
        """ Load a json string """
        _json = json.loads(jsonString)
        self.update(_json)

    def dumps(self, indent=4):
        """ Return a json string of the data """
        return json.dumps(self, indent=indent, sort_keys=True)

    def toJson(self, *args, **kwargs):
        """ Return a json string of the data """
        return self.dumps(**kwargs)

