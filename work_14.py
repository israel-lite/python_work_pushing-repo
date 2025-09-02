"""
add = lambda x, y: x + y
result = add(5, 3)
print(result)
"""
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=30, City="New York")
