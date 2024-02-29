import ipdb

def plus_two(num):
    ipdb.set_trace()
    result = num + 2
    return result

# Call the function
result = plus_two(5)
print(result)
