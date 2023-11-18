from dataclasses import dataclass
from typing import Union


types = int, float, str, bool, list, dict, set, tuple, object


def length(c: str) -> int:
    return len(c)


falsy = 0, [], {}, "", False, None
something = "hello"

if something:
    print("yes")


# array vs list
# fixes vs dynamic size
# arrays are not a thing in python, only lists
self: list = [1, 2, 3]

self.append(4)

print(self[2])

# dicts
d: dict[str, int] = {"hello": 1, "mom": 2}

print(d["hello"])

# sets
s: set = set()


def unique(l: list) -> list:
    return list(set(l))


# tuples

t: tuple[int, str, list, bool] = (1, "hello", [], False)


def func(s: str) -> tuple[str, int]:
    return s + "hi", len(s)


a = 5
b = 1

b, a = a, b

print(a, b)
# print(func("hello"))


# linked lists


@dataclass
class LinkedList:
    element: int
    rest: Union["LinkedList", None]

    def sum(self) -> int:
        if self == None:
            return 0
        else:
            return self.element + linked_sum(self.rest)


# (element1, (rest -> (element2, (rest -> None)))


linked = LinkedList(1, LinkedList(2, LinkedList(3, None)))

print(linked.sum())


def linked_sum(l: LinkedList | None) -> int:
    if l == None:
        return 0
    else:
        return l.element + linked_sum(l.rest)


type File = list[File] | int  # directory or size

ex_f = [1, [2, 3]]
ex_f_2 = 4


def size(f: File) -> int:
    if isinstance(f, int):
        return f
    elif isinstance(f, list):
        # return sum(size(i) for i in f)
        return sum(map(size, f))
        # s: int = 0
        # for i in f:
        #     s += size(i)
        # return s
