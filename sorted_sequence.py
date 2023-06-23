import math
from typing import Union, List


def sorted_sequence(sequence: List[Union[List[float], float]]) -> list:
    def calculate_area(dimension: Union[List[float], float]) -> float:
        if isinstance(dimension, list):
            width, length = dimension
            return width * length
        if isinstance(dimension, float):
            return math.pi * (dimension**2)

    return sorted(sequence, key=calculate_area)


# Test 1
input_sequence = [[4.23, 6.43], 1.23, 3.444, [1.342, 3.212]]
expected_output = [[1.342, 3.212], 1.23, [4.23, 6.43], 3.444]
assert sorted_sequence(input_sequence) == expected_output

# Test 2
input_sequence = [[5.17, 3.22], 5.45, 8.321, [4.212, 3.544], 2.0, [2.5, 3.5]]
expected_output = [[2.5, 3.5], 2.0, [4.212, 3.544], [5.17, 3.22], 5.45, 8.321]
assert sorted_sequence(input_sequence) == expected_output

# Test 3
input_sequence = [1.0, [3.0, 4.0], 2.5, [2.0, 2.0]]
expected_output = [1.0, [2.0, 2.0], [3.0, 4.0], 2.5]
assert sorted_sequence(input_sequence) == expected_output

print("All tests passed successfully!")
