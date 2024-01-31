import string
import random


def generate_random_username():
    letters = string.ascii_uppercase
    rand_string = ''.join(random.choice(letters) for _ in range(8))
    return rand_string
