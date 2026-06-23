if __name__ == "__main__":
    import random
    from tree import *

    min_range = 1
    max_range = 10
    rand = random.randint(min_range, max_range)
    len = 5
    list = random.sample(range(min_range, max_range), len)
    print(list)
    t = tree(list)
    print(t.traverse())
    print(t.search(rand))
