import uuid
import random
import string

print(uuid.uuid4())

def random_string_generator():
    return ''.join(random.choice(string.ascii_letters) for x in range(25))

for x in range(20):
    print(random_string_generator())
