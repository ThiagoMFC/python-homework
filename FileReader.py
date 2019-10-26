filepath = 'housing.data'
index = 1
file = open(filepath, "r")
for line in file:
    value = line.split()
    print(f"List {index}: {value}")
    index += 1