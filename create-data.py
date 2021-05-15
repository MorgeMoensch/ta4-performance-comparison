import uuid
import random
import string
import json


def random_string_generator():
    return ''.join(random.choice(string.ascii_letters) for x in range(25))

list = []

# Add new DummyObjects to List
for x in range(20):
    newObj = {
            'id': uuid.uuid4().__str__(),
            'name': random_string_generator()
            }
    list.append(newObj)


#Serializing JSON
json_object = json.dumps(list, indent = 4)

#Write to file
with open("test.json", "w") as outfile:
    outfile.write(json_object)
