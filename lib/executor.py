
from copy import copy
from enum import Enum
import unittest


class Instruction(Enum):
    Add = 1
    Multiply = 2
    End = 99


BLOCK_LEN = 4

def execute(data):
    data = copy(data)
    instruction_pointer = 0
    while True:
        opt_code = Instruction(data[instruction_pointer])
        if opt_code == Instruction.End:
            return data

        first_param_pointer = data[instruction_pointer + 1]
        second_param_pointer = data[instruction_pointer + 2]
        result_pointer = data[instruction_pointer + 3]

        if opt_code == Instruction.Add:
            data[result_pointer] = data[first_param_pointer] + data[second_param_pointer]
        elif opt_code == Instruction.Multiply:
            data[result_pointer] = data[first_param_pointer] * data[second_param_pointer]

        instruction_pointer += BLOCK_LEN


class TestStringMethods(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(execute([1,0,0,0,99]), [2,0,0,0,99])

    def test_multiplication(self):
        self.assertEqual(execute([2,3,0,3,99]), [2,3,0,6,99])

    def test_combo(self):
        self.assertEqual(execute([2,4,4,5,99,0]), [2,4,4,5,99,9801])
        self.assertEqual(execute([1,1,1,4,99,5,6,0,99]), [30,1,1,4,2,5,6,0,99])
