my_list = [1, 2, 3, 4]
my_iter = iter(my_list)

print(next(my_iter))  # Output: 1


def read_next_line():
    return input("Enter a line (or type 'end' to stop): ")

for line in iter(read_next_line, 'end'):
    print(f"Got line: {line}")
