

def get_input(file):
    f = open(file)
    input = []
    for line in f:
        input.append(line.replace('\n', '').split(' '))
    return input


def who_wins(bunny_a, bunny_b):
    """
    A,B.C == rock, paper, sciccors == 1,2,3
    X.Y,Z == rock, paper, sciccors == 1,2,3
    """

    if bunny_a == 'A':
        if bunny_b == 'X':
            return 3 + 1
        if bunny_b == 'Y':
            return 6 + 2
        if bunny_b == 'Z':
            return 0 + 3

    if bunny_a == 'B':
        if bunny_b == 'X':
            return 0 + 1
        if bunny_b == 'Y':
            return 3 + 2
        if bunny_b == 'Z':
            return 6 + 3

    if bunny_a == 'C':
        if bunny_b == 'X':
            return 6 + 1
        if bunny_b == 'Y':
            return 0 + 2
        if bunny_b == 'Z':
            return 3 + 3


def do_as_the_list_says(bunny_a, result):
    """
    A,B.C == rock, paper, sciccors == 1,2,3
    X.Y,Z == rock, paper, sciccors == 1,2,3
    X,Y,Z == lose, draw, win
    """

    if result == 'X':
        if bunny_a == 'A':
            return bunny_a, 'Z'
        if bunny_a == 'B':
            return bunny_a, 'X'
        if bunny_a == 'C':
            return bunny_a, 'Y'

    if result == 'Y':
        if bunny_a == 'A':
            return bunny_a, 'X'
        if bunny_a == 'B':
            return bunny_a, 'Y'
        if bunny_a == 'C':
            return bunny_a, 'Z'

    if result == 'Z':
        if bunny_a == 'A':
            return bunny_a, 'Y'
        if bunny_a == 'B':
            return bunny_a, 'Z'
        if bunny_a == 'C':
            return bunny_a, 'X'



if __name__ == '__main__':
    input = get_input('2/input.txt')

    score = 0
    for line in input:
        score += who_wins(line[0], line[1])

    print(f'ass1 score: {score}')

    score = 0
    for line in input:
        a, b = do_as_the_list_says(line[0], line[1])
        score += who_wins(a, b)

    print(f'ass2 score: {score}')
