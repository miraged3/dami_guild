import os
import random

path = '/usr/local/dami/res/'


def summon():
    result = random.randint(1, 1000)
    if result < 762:
        return path + 'R/' + random.choice(os.listdir(f'{path}R'))
    elif result < 962:
        return path + 'SR/' + random.choice(os.listdir(f'{path}SR'))
    elif result < 987:
        return path + 'SSR/' + random.choice(os.listdir(f'{path}SSR'))
    else:
        return path + 'SP/' + random.choice(os.listdir(f'{path}SP'))
