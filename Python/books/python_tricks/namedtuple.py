from typing import Tuple, Any
from collections import namedtuple
from sys import getsizeof

# Regular tuple
instance_1: Tuple = (10, 20, 30)
print(f'Instance: {instance_1}, Size: {getsizeof(instance_1)} bytes')

# NamedTuple
# If you use namedtuple to define your named tuple, all the items are assumed to have Any types.
# That is, mypy doesn’t know anything about item types.
Point: Any = namedtuple('Point', ['a', 'b', 'c'])
instance_2_item: Point = Point(10, 20, 30)
print(f'Instance: {instance_2_item}, Size: {getsizeof(instance_2_item)} bytes')

# Named tuple instances have a nice repr
print(f'Beautiful representation: {instance_2_item}')

# Named tuple instances have accessing fields
print(f'The "a" field of the named tuple instance: {instance_2_item.a}')
