import random
import string


def generate_random_code(length=6):
    return ''.join(random.sample(string.digits, length))


if __name__ == '__main__':
    code = generate_random_code()
    print(code)
