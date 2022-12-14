import random
from typing import Union, List


class Arrays:
    def __init__(self):
        self.nesting = random.randint(50, 150)
        self.arrays = self.get_array(1)

    def get_array(self, step) -> Union[List[list], int]:
        if step <= self.nesting:
            return [self.get_array(step + 1)]
        else:
            return random.randint(1_000, 100_000)


nested_arrays = Arrays()


class Solution:

    def get_num(self, arrays):
        if type(arrays) == int:
            print(arrays)
        self.get_num(arrays[0])


Solution().get_num(nested_arrays.arrays)