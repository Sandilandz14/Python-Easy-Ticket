# def max_num_in_list( list ):
#     max = list[ 0 ]
#     for a in list:
#         if a > max:
#             max = a
#     return max
# print(max_num_in_list([1, 2, -8, 0]))



import unittest
from unittesting_1 import max_number
from unittesting_1 import decending_list


a=[1,2,3,4,5,78]
class Max_decend(unittest.TestCase):
    def test_maximum_num(self):
        assert max_number(a)==78, "Maximum number is 78"


    def test_decending_list(self):
        assert decending_list(a)==[78,5,4,3,2,1], "that is the decending list"


