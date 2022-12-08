
def get_input():
    f = open('08/input.txt').read()
    return f.splitlines()


def do_the_loop_thing(input, from_a, to_a, from_b, to_b, trees, incr=1):
    """
    a == outer loop
    b == inner loop
    """

    for i in range(from_a, to_a, incr):
        tallest_tree = -1
        for j in range(from_b, to_b, incr):
            if int(input[i][j]) > tallest_tree:
                tallest_tree = int(input[i][j])
                trees[f'{i}-{j}'] = input[i][j]

def do_the_loop_thing_2(input, from_a, to_a, from_b, to_b, trees, incr=1):
    """
    a == outer loop
    b == inner loop
    """

    for i in range(from_a, to_a, incr):
        tallest_tree = -1
        for j in range(from_b, to_b, incr):
            if int(input[j][i]) > tallest_tree:
                tallest_tree = int(input[j][i])
                trees[f'{j}-{i}'] = input[j][i]



if __name__ == '__main__':
    input = get_input()
    trees = {}

    do_the_loop_thing(input, 0, len(input), 0, len(input[0]), trees)
    do_the_loop_thing_2(input, 0, len(input), 0, len(input[0]), trees)

    do_the_loop_thing(input, len(input)-1, 0, len(input[0])-1, 0, trees, -1)
    do_the_loop_thing_2(input, len(input)-1, 0, len(input[0])-1, 0, trees, -1)


    print(f'answer 1: {len(trees)}')
    breakpoint()
