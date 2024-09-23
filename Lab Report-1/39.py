import random
import string

def generate_random_string(length):
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))
print("Random string of length 5: ", generate_random_string(5))