import unittest

from orm_model import *

from webserv import give_cats


input_data = [
    {},
    {'offset': 1, 'limit': 1, 'attribute': 'color',},
    {'offset': -1, 'limit': -1, 'attribute': 'color',},
]

class TestGiveCats(unittest.TestCase):
    def test_tt(self):
        for dict_ in input_data:
            print(res := give_cats(**dict_))
            print('*' * 50)
            self.assertIsInstance(res[0], dict)
        

if __name__ == '__main__':
    unittest.main()