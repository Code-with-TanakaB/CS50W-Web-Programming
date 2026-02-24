people = [
    {"name": "Alice", "age": 30, "city": "New York"},
    {"name": "Bob", "age": 25, "city": "Los Angeles"},
    {"name": "Charlie", "age": 35, "city": "Chicago"}
] #creating a list of dictionaries called people. Each dictionary represents a person and contains three key-value pairs: "name", "age", and "city". The values for these keys are the name, age, and city of each person, respectively.

people.sort(key=lambda person: person["city"]) #sorting the list of dictionaries in place using the sort method. The key parameter is set to a lambda function that takes a person dictionary as an argument and returns the value associated with the "city" key. This means that the list will be sorted based on the city of each person in alphabetical order.
print(people)