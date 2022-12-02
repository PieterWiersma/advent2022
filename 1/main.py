
def get_input():
    f = open('1/input.txt')
    input = []
    for line in f:
        input.append(line.replace('\n', ''))
    return input

def create_list_per_bunny(input):
    container = []
    tmp = []
    for cell in input:
        if cell:
            tmp.append(int(cell))
        else:
            container.append(tmp)
            tmp = []
    container.append(tmp) # last run isn't in loop
    return container


if __name__ == '__main__':
    input = get_input()
    container = create_list_per_bunny(input)

    sum_cont = []
    for bunny in container:
        sum_cont.append(sum(bunny))

    print(f'most calories: {max(sum_cont)}')

    sum_cont.sort()
    print(f'sum of the three most: {sum(sum_cont[-3:])}')
