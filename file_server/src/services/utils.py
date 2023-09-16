import random
import string



def random_str(length: int):
    return ''.join(random.choice(string.ascii_letters) for i in range(length))