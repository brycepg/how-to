#!/usr/bin/env python

"""Format string precedence

str(foo) calls foo.__str__ if available, then __repr__, then default
repr(foo) calls foo.__repr__ if available, then default
"{}".format(foo) calls foo.__format__ if available, then __str__, then __repr__, then default
"%s" % foo calls foo.__str__ if available, then __repr__, then default
"""

class Foo(object):
    def __str__(self):
        return "i am a __str__"
    def __repr__(self):
        return "representation of F"
    def __format__(self, str_):
        # wtf is this argument?
        return "serious formatting brah %s" % str_
    def foo(self):
        return "foo"

if __name__ == "__main__":
    print(" __format__ has highest precedence except for %:")
    foo = Foo()
    print("%s" % foo)
    print("{}".format(foo))
    delattr(Foo,"__format__")
    print("")

    print("__str__ next:")
    print("%s" % foo)
    print("{}".format(foo))
    delattr(Foo,"__str__")
    print("")

    print("__repr__ finally:")
    print("%s" % foo)
    print("{}".format(foo))
    delattr(Foo,"__repr__")
    print("")

    print("I have no idea where this is defined(in object?):")
    print("%s" % foo)
    print("{}".format(foo))
