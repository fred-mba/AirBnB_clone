import json

data = {'name': 'John', 'age': 30, 'city': 'Nakuru'}

serialized_data = json.dumps(data)
print("Serialized_data: ", serialized_data)
print("======")
deserialized_data = json.loads(serialized_data)
print("Deserialized_data: ", deserialized_data)