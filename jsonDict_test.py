"""
Test script for the JsonDict class.
"""
__author__ = "Sylvain Berger"
__email__ = "sylvain.berger@gmail.com"
__version__ = "1.0.0"
__status__ = "Production"

import os
from jsonDict import JsonDict

if __name__ == '__main__':
    validFilename = os.path.join(os.path.dirname(__file__), 'samples', 'sample.json')
    validFilename2 = os.path.join(os.path.dirname(__file__), 'samples', 'sample.json')
    invalidFilename = os.path.join(os.path.dirname(__file__), 'samples', 'noFile.json')

    sample = {
            "sample_string": "Default",
            "sample_bool": True,
            "sample_int": 12,
            "sample_float": 0.0123,
            "sample_list": [1,2,3,4],
            "sample_dict": {"a" : 1, "b": 2}
            }

    # save example
    a = JsonDict(validFilename)
    a.update(sample)
    a['sample_new'] = False
    print a.dumps()
    a.save()
    # save in a different file
    a.save(validFilename2)

    # load example
    # Init with a valid file
    a = JsonDict(validFilename, autoLoad=True)
    print a

    # init with invalid file
    a = JsonDict(invalidFilename, autoLoad=True)
    print a

    # init empty and load valid
    a = JsonDict()
    a.load(validFilename)
    print a

    # init empty and load invalid
    a = JsonDict()
    a.load(validFilename)
    print a

    # init empty and add from string
    a = JsonDict()
    a.loads('{"sample1": true,"sample_2":"somename"}')
    print a

    # dump to string
    b = a.dumps()
    print b
    c = a.toJson()
    print c

    # a = JsonDict.fromFile(validFilename)
    # print a
