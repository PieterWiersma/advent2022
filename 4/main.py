
import re

def ass_1():
    counter = 0
    for tasks in open('4/input.txt').read().splitlines():
        numbers = [int(x) for x in re.findall('[0-9]+', tasks)]
        x = set(range(numbers[0], numbers[1] + 1))
        y = set(range(numbers[2], numbers[3] + 1))
        if (x.intersection(y) == y or y.intersection(x) == x):
            counter += 1

    print(f'score = {counter}')

def ass_2():
    counter = 0
    for tasks in open('4/input.txt').read().splitlines():
        numbers = [int(x) for x in re.findall('[0-9]+', tasks)]
        x = set(range(numbers[0], numbers[1] + 1))
        y = set(range(numbers[2], numbers[3] + 1))
        if (len(x.intersection(y)) > 0):
            counter += 1

    print(f'score = {counter}')



if __name__ == "__main__":
    ass_1()
    ass_2()
