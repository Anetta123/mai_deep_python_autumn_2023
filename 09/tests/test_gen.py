"""Test Generator"""
import random
import json
import string


def generate_random_string(length):
    """Generates random string with random length"""
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(length))


def generate_random_number(min_value, max_value):
    """Generate a random digit in a random range"""
    return random.randint(min_value, max_value)


def generate_random_json():
    """Generates a JSON-string"""
    random_json = {
        "name": generate_random_string(1000),
        "language": generate_random_string(1000),
        "id": generate_random_string(1000),
        "bio": generate_random_string(1000),
        "version": generate_random_number(1, 10)
    }
    return json.dumps(random_json)


with open('test.txt', 'w') as file:
    for i in range(50000):
        file.write(generate_random_json() + '\n')
