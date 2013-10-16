"""
Unitest Module for JsonDict class
(not really a truly valid python unittest)
"""
__author__ = "Sylvain Berger"
__email__ = "sberger@hybride.com"
__copyright__ = "Copyright 2013, Hybride Technologies"
__version__ = "1.0.0"
__status__ = "Production"


import os
from pprint import pprint
from hybride.jsonDict import JsonDict

jsonFile = os.path.join(os.path.dirname(__file__), 'jsonDict_example.json')
tempJsonFile = os.path.join(os.path.dirname(__file__), 'tempJsonDict.json')

def testCreate():
    # save a dict as json file
    print 'Create an empty jsonDict and fill it:'
    jdict = JsonDict()
    jdict['thisString'] = 'This is a jsonDict Test'
    jdict['thisInt'] = 426
    jdict['thisFloat'] = 67.1
    jdict.save(tempJsonFile)
    pprint(jdict)

def testRead1():
    # Load a json file, modify the dictionary and save it back
    print '-' * 80
    print 'Re-open the previous json file, append data to it and save it back:'
    jdict2 = JsonDict().fromFile(tempJsonFile)
    jdict2['thisNewList'] = [1, 2, 3, 4, 5]
    jdict2.save()
    pprint(jdict2)

def testRead2():
    # Load a json file, modify the dictionary and save it back
    print '-' * 80
    print 'Open a manually created json file, append data to it and save it back:'
    jdict2 = JsonDict().fromFile(jsonFile)
    jdict2['thisNewData'] = ["LV", 426]
    jdict2.save()
    pprint(jdict2)

def testDump():
    # Load the modified json file and dump to string
    print '-' * 80
    print 'Re-open the previous json file and dunmp it to string:'
    jdict3 = JsonDict().fromFile(tempJsonFile)
    print jdict3.dumps()

def testFromJsonString():
    # create a json dict from a json string
    dictString = '{"someInt": 1, "someString": "This is fun", "someFloat": 2.1416}'
    print '-' * 80
    print 'Create a jsonDict from a string (method 1):'
    jdict4 = JsonDict()
    jdict4.loads(dictString)
    pprint(jdict4)

    print '-' * 80
    print 'Create a jsonDict from a string (method 2):'
    jdict5 = JsonDict().fromJson(dictString)
    pprint(jdict5)

def deleteTempFile():
    # remove the test file
    os.unlink(tempJsonFile)

if __name__ == '__main__':
    testCreate()
    testRead1()
    testRead2()
    testDump()
    testFromJsonString()
    deleteTempFile
