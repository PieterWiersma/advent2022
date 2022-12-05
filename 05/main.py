

#         [Q] [B]         [H]
#     [F] [W] [D] [Q]     [S]
#     [D] [C] [N] [S] [G] [F]
#     [R] [D] [L] [C] [N] [Q]     [R]
# [V] [W] [L] [M] [P] [S] [M]     [M]
# [J] [B] [F] [P] [B] [B] [P] [F] [F]
# [B] [V] [G] [J] [N] [D] [B] [L] [V]
# [D] [P] [R] [W] [H] [R] [Z] [W] [S]
#  1   2   3   4   5   6   7   8   9

import re
import math

def get_input():
    f = open('05/input.txt').read().splitlines()
    split_key = [3,1] * 9
    containers = {}
    for i in range(1,10): containers[i] = []

    for line in f[0:8]:
        for i, split in enumerate(split_key):
            processed = len(line[:sum(split_key[:i])])
            box = line[processed:processed+split]
            if i % 2 == 0 and box != '   ' and box:
                containers[math.ceil((i)/2) + 1].append(box)

    for container in containers: containers[container].reverse()
    input = [re.findall('[0-9]+', x) for x in f[10:]]
    return containers, input


def move_containers9000(containers, move_list):
    for move in move_list:
        for i in range(int(move[0])):
            x = containers[int(move[1])].pop()
            containers[int(move[2])].append(x)
    return containers


def move_containers9001(containers, move_list):
    for move in move_list:
        x = containers[int(move[1])][-int(move[0]):]
        del(containers[int(move[1])][-int(move[0]):])
        containers[int(move[2])] = containers[int(move[2])] + x
    return containers


if __name__ == '__main__':
    containers, input = get_input()
    containers_9000 = move_containers9000(containers, input)

    top_containers = ''
    for container in containers:
        top_containers += containers[container][-1].replace('[', '').replace(']', '')

    print(f'ass1: top_containers: {top_containers}')

    containers, input = get_input()
    containers = move_containers9001(containers, input)

    top_containers = ''
    for container in containers:
        if containers[container]:
            top_containers += containers[container][-1].replace('[', '').replace(']', '')

    print(f'ass1: top_containers: {top_containers}')
