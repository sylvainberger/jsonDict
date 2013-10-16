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
import unittest
from pprint import pprint
from hybride.jsonDict import JsonDict


class TestJsonDictAsserts(unittest.TestCase):
    # example
    jsonFile = os.path.join(os.path.dirname(__file__), 'jsonDict_example.json')
    tempJsonFile = os.path.join(os.path.dirname(__file__), 'tempJsonDict.json')

    def test_basic(self):
        print '\nTest Basic:'
        jdict = JsonDict()
        jdict['thisString'] = 'This is a jsonDict Test'
        jdict['thisInt'] = 426
        jdict['thisFloat'] = 67.1
        jdict.save(self.tempJsonFile)
        pprint(jdict)

        jdict2 = JsonDict.fromFile(self.tempJsonFile)
        self.assertIsInstance(jdict, JsonDict)
        self.assertIsInstance(jdict2, JsonDict)
        self.assertTrue(jdict, jdict2)
        self.assertNotEqual(jdict, {})

    def test_from_file(self):
        print '\nTest From File:'
        jdict = JsonDict.fromFile(self.jsonFile)
        pprint(jdict)
        jdict['newKey'] = 1
        # should be a jsonDict instance
        self.assertIsInstance(jdict, JsonDict)
        # read the source again
        jdict2 = JsonDict.fromFile(self.jsonFile)
        # should not be equal because we added data to the first dict
        self.assertNotEqual(jdict, jdict2)
        # should be equal now because we saved and reload
        jdict.save(self.tempJsonFile)
        jdict2 = JsonDict.fromFile(self.tempJsonFile)
        self.assertEqual(jdict, jdict2)


    def test_from_json(self):
        print '\nTest From Json:'
        myDict = {"someInt": 1, "someString": "This is fun", "someFloat": 2.1416}
        dictString = '{"someInt": 1, "someString": "This is fun", "someFloat": 2.1416}'
        jdict = JsonDict.fromJson(dictString)
        pprint(jdict)
        self.assertIsInstance(jdict, JsonDict)
        self.assertNotEqual(jdict, {})
        self.assertEqual(jdict, myDict)

        # test dumps
        dumpString = jdict.dumps()
        jdict2 = JsonDict.fromJson(dumpString)
        self.assertEqual(jdict, jdict2)

        dumpString = jdict.dumps().replace('\n', '')
        jdict2 = JsonDict.fromJson(dumpString)
        self.assertEqual(jdict, jdict2)

        # test toJson
        dumpString = jdict.toJson()
        jdict2 = JsonDict.fromJson(dumpString)
        self.assertEqual(jdict, jdict2)

    def tearDown(self):
        try:
            os.unlink(self.tempJsonFile)
        except:
            pass


if __name__ == '__main__':
    unittest.main()
