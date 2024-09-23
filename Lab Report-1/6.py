def random_number(min, max):
    return (id(hash(())) % (max - min + 1)) + min

print("Random number: ", random_number(1, 100))