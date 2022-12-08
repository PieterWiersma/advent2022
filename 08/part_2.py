
def get_input():
    f = open('08/input.txt').read()
    return f.splitlines()


def do_the_loop_thing(input, coordinates, trees):
    """
    a == outer loop
    b == inner loop
    """

    i,j = coordinates
    current_tree_size = int(input[i][j])
    trees[f'{i},{j}'] = [0,0,0,0]


    for x in range(i+1, len(input), 1):
        trees[f'{i},{j}'][0] += 1
        if int(input[x][j]) >= current_tree_size:
            break

    for x in range(i-1, -1, -1):
        trees[f'{i},{j}'][1] += 1
        if int(input[x][j]) >= current_tree_size:
            break

    for x in range(j+1, len(input[0]), 1):
        trees[f'{i},{j}'][2] += 1
        if int(input[i][x]) >= current_tree_size:
            break

    for x in range(j-1, -1, -1):
        trees[f'{i},{j}'][3] += 1
        if int(input[i][x]) >= current_tree_size:
            break



if __name__ == '__main__':
    input = get_input()
    trees = {}

    for i in range(len(input)):
        for j in range(len(input)):
            do_the_loop_thing(input, (i,j), trees)

    highest_value = 0
    for tree in trees.keys():
        x = trees[tree][0] * trees[tree][1] * trees[tree][2] * trees[tree][3]
        if x > highest_value:
            highest_value = x


    print(f'answer 2: {highest_value}')
    breakpoint()
