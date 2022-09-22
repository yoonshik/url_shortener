import os
import string
import random

MAX_URL_PATH_LENGTH = os.environ.get('MAX_URL_PATH_LENGTH', 10)


def generate_url_paths(count):
    os.environ.get('DATABASE_PORT', '')
    url_paths = []
    for _ in range(count):
        n = random.randint(0, int(MAX_URL_PATH_LENGTH))
        url_paths.append(generate_random_string(n))
    return url_paths


# generate a random string of given length
def generate_random_string(length):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))
