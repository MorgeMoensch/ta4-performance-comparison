import uuid
import random
import string
import json
import datetime

def random_string_generator(length = 25):
    return ''.join(random.choice(string.ascii_letters) for x in range(length))

list = []

# Add new DummyObjects to List
for x in range(2000):
    newObj = {
            'id': uuid.uuid4().__str__(),
            'a': random_string_generator(),
            'createdAt': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'bd': {
                    'tN': random_string_generator(),
                    's': random_string_generator(10),
                    'id': uuid.uuid4().__str__(),
                    'ap': {
                        'n': random_string_generator(),
                        'abbr': random_string_generator(6),
                        'id': uuid.uuid4().__str__()
                    }

                }
            }
    list.append(newObj)


#Serializing JSON
json_object = json.dumps(list, indent = 4)

#Write to file
with open("test.json", "w") as outfile:
    outfile.write(json_object)
