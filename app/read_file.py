import os
import random

#for debug mod
# cwd = os.getcwd()
# print(os.listdir(cwd))

file = f'./app/resource/proverbs.txt'

encoding = 'utf8'
proverb_list = []

min_val = 0
max_val = 15


def read_file(file, list_storage):
    with open(file=file, encoding=encoding) as reader:
        lines = reader.readlines()
        for line in lines:
            if line[0] == '#':
                pass
            else:
                # print(line)
                list_storage.append(line)


def get_proverb():
    read_file(file=file, list_storage=proverb_list)
    value = random.randint(min_val, max_val)
    text = proverb_list[value]
    #for debug
    # cwd = os.getcwd()
    # return cwd
    return text

# example of usage
# print(get_proverb())
