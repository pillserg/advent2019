from copy import copy
from enum import Enum
import unittest

data = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,13,1,19,1,5,19,23,2,10,23,27,1,27,5,31,2,9,31,35,1,35,5,39,2,6,39,43,1,43,5,47,2,47,10,51,2,51,6,55,1,5,55,59,2,10,59,63,1,63,6,67,2,67,6,71,1,71,5,75,1,13,75,79,1,6,79,83,2,83,13,87,1,87,6,91,1,10,91,95,1,95,9,99,2,99,13,103,1,103,6,107,2,107,6,111,1,111,2,115,1,115,13,0,99,2,0,14,0]

fix_data = copy(data)
fix_data[1] = 12
fix_data[2] = 2

class OptCode(Enum):
    Add = 1
    Multiply = 2
    End = 99


BLOCK_LEN = 4

def execute(data):
    data = copy(data)
    pointer = 0
    while True:
        opt_code = OptCode(data[pointer])
        if opt_code == OptCode.End:
            return data

        first_arg_pointer = data[pointer + 1]
        second_arg_pointer = data[pointer + 2]
        result_pointer = data[pointer + 3]

        if opt_code == OptCode.Add:
            data[result_pointer] = data[first_arg_pointer] + data[second_arg_pointer]
        elif opt_code == OptCode.Multiply:
            data[result_pointer] = data[first_arg_pointer] * data[second_arg_pointer]

        pointer += BLOCK_LEN


class TestStringMethods(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(execute([1,0,0,0,99]), [2,0,0,0,99])

    def test_multiplication(self):
        self.assertEqual(execute([2,3,0,3,99]), [2,3,0,6,99])

    def test_combo(self):
        self.assertEqual(execute([2,4,4,5,99,0]), [2,4,4,5,99,9801])
        self.assertEqual(execute([1,1,1,4,99,5,6,0,99]), [30,1,1,4,2,5,6,0,99])

if __name__ == '__main__':
    print(f'result: {execute(fix_data)[0]}')
