import random
import names


def generate_name_file(file_name, size):
    name_list = []
    for i in range(size):
        name_list.append(names.get_full_name())
    generate_file(file_name, name_list)


def generate_numbers_file(file_name, size):
    numbers_list = random.sample(range(0, 1000), size)
    generate_file(file_name, numbers_list)


def generate_file(file_name, list):
    with open(file_name, "w") as f:
        for item in list:
            f.write(str(item) + "\n")


# generate_numbers_file("100.txt", 100)
generate_name_file("names.txt", 100)
