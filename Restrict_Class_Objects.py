class object_restrict(object):
    _count = 0

    def __new__(cls):
        cls._count += 1
        if cls._count > 5:
            raise TypeError("Too many keys created")

        print (cls._count, "object created")

    def __init__(self):
        pass

k = object_restrict()
k1 = object_restrict()
k2 = object_restrict()
k3 = object_restrict()
k4 = object_restrict()
k5 = object_restrict()