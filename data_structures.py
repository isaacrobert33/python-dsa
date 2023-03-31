from collections import deque, ChainMap, Counter, OrderedDict, defaultdict, namedtuple
import array
import sys

############ Deques ############
dq = deque("abc")
dq.append("d")
dq.extend("defghijk")
dq.extendleft("12345")
print(dq)

############ ChainMaps ############
defaults = {
    "fname": "Isaac",
    "lname": "Robert",
    "hobby": "coding",
    "langiage": "python",
    "framework": "Flask",
}
cm = ChainMap(defaults)
cm2 = cm.new_child({"age": "xx", "lname": "Tommy"})
print(cm2.maps)

############ Counter ############
ct = Counter("anysequence")
ct1 = Counter({"a": 1, "b": 2, "c": 3})
ct2 = Counter(a=1, b=2, c=3, d=4, e=5)
print(ct2["a"])

############ Ordered Dictionaries ############
""" 
They keep items according to their insertion order
"""
od = OrderedDict()
od["three"] = 3
od["four"] = 4
od["one"] = 1
od["two"] = 2
print(od)

############ Defaultdict ############
dd = defaultdict(int)
words = str.split("Hello world, this is me!")
for word in words:
    dd[word] += 1

print(dd.keys())

############ NamedTuples ############
space = namedtuple("space", "x y z")
sl = space(x=1.0, y=2.0, z=4.0)

ar = sl.x * sl.y * sl.z
print(ar)

############ Arrays ############
arr = array.array("i", range(100))
larr = list(range(100))
print(sys.getsizeof(arr), sys.getsizeof(larr))
