import uuid
import random
import string
import json
import datetime

def random_string_generator(length = 25):
    return ''.join(random.choice(string.ascii_letters) for x in range(length))

def generate_test_data(numberOfElements):

    list = []

    # Add new DummyObjects to List
    for x in range(numberOfElements):
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

    return list


def write_test_data_to_file(filename, numberOfElements):
    list = generate_test_data(numberOfElements)
    
    #Serializing JSON
    json_object = json.dumps(list, indent = 4)

    #Write to file
    with open(filename, "w") as outfile:
        outfile.write(json_object)

write_test_data_to_file("test-data-10.json", 10)
write_test_data_to_file("test-data-50.json", 50)
write_test_data_to_file("test-data-100.json", 100)
write_test_data_to_file("test-data-500.json", 500)
write_test_data_to_file("test-data-1000.json", 1000)
write_test_data_to_file("test-data-2000.json", 2000)
write_test_data_to_file("test-data-5000.json", 5000)
write_test_data_to_file("test-data-10000.json", 10000)
