import os
import unittest

from davidkhala.amap import API

key = os.environ.get('KEY')
api = API(key)


class TipsTestCase(unittest.TestCase):
    def test_edu(self):
        r = api.search('Tsinghua University')
        print(r)


if __name__ == '__main__':
    unittest.main()
