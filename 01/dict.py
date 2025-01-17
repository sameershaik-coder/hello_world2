def sample():
    context = {
        "name": "John Doe",
        "age": 30,
        "city": "New York",
        "is_student": True,
        "grades": [90, 80, 85, 92, 78],
        "address": {
            "street": "123 Main St",
            "city": "Cityville",
            "state": "NY",
            "zip": "12345"
        }
    }
    
    for items in context.items():
        print(items[1])
        # print(type(items))
        # print(items[0])
        # print(items[1])
        # print(type(items[0]))
        # print(type(items[1]))

sample()