import sys
from typing import Hashable


data = [1, 2., '3', [4], (5,)]

for n, obj in enumerate(data, 1):
    print(f'{n} {obj} {id(obj)} {sys.getsizeof(obj)}', end=' ')
    print(hash(obj) if isinstance(obj, Hashable) else 'Объект нехэшируемый')
    
