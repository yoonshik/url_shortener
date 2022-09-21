import string
import random


def generate_url_paths(count):
    url_paths = []
    for _ in range(count):
        n = random.randint(0, 50)
        url_paths.append(generate_random_string(n))
    return url_paths


# generate a random string of given length
def generate_random_string(length):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))
