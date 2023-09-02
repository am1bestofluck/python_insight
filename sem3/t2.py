"""
Создайте вручную кортеж содержащий элементы разных типов.
✔ Получите из него словарь списков, где:
ключ — тип элемента,
значение — список элементов данного типа.
"""

from collections import defaultdict

def empty():
    return []
def main():
    out = defaultdict(empty)
    _input = (1,2,3,4,5,False,False,True,1.2,1.4,1.6)
    for i in _input:
        out[type(i)].append(i)
    print(out)

"""
from pprint import pp

_tuple = (1,2,3,'1','2','3',True,False,None,[1])
out = dict()

for i in _tuple:
    if type(i) not in out:
        out[type(i)] = []
    out[type(i)].append(i)

pp(out)

"""
"""
from pprint import  pp
_tuple = (1,2,3,'1','2','3',True,False,None,[1])
out = dict()
for i in _tuple:
    out.setdefault(type(i),[])
    out[type(i)].append(i)

pp(out)
"""