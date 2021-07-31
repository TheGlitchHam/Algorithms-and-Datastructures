def load_numbers(file_name):
    numbers = []
    with open(file_name) as f:
        for line in f:
            numbers.append(int(line))
    return numbers


def load_string(file_name):
    names = []
    with open(file_name) as f:
        for line in f:
            names. append(str(line))
    return names
