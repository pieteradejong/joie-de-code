import random


def generate_Z():
    while True:
        yield random.choice([-1, 1])


def generate_random_walk(steps):
    gen, sum = generate_Z(), 0
    for _ in xrange(steps):
        z = next(gen, None)
        sum += z
        if sum == 0:
            print
            'o'
        elif sum < 0:
            print
            '<' * abs(sum)
        else:
            print
            '>' * sum


generate_random_walk(100)
