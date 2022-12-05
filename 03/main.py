

def get_input(file):
    f = open(file)
    input = []
    for line in f:
        line = line.replace('\n', '')
        split = int(len(line)/2)
        input.append([line[:split], line[split:]])
    return input


def calculate_score(number_chars, input_a, input_b):
    overlap = set(input_a) & set(input_b)
    score = 0
    for char in overlap:
        score += number_chars[char]
    return score


def calculate_score_2(number_chars, input_a, input_b, input_c):
    overlap = set(input_a) & set(input_b) & set(input_c)
    score = 0
    for char in overlap:
        score += number_chars[char]
    return score


if __name__ == '__main__':
    input = get_input('3/input.txt')
    number_chars = {}
    for x in [x for x in zip(list(range(1,27)), list(range(ord('a'), ord('z')+1)))] + \
        [x for x in zip(list(range(27,53)), list(range(ord('A'), ord('Z')+1)))]:
        number_chars[chr(x[1])] = x[0]

    score = 0
    for line in input:
        score += calculate_score(number_chars, line[0], line[1])

    print(f'ass1: {score}')

    size = 3
    score = 0
    for i in range(0, len(input), size):
        #breakpoint()
        score += calculate_score_2(number_chars,
            ''.join(input[i:i+size][0]),
            ''.join(input[i:i+size][1]),
            ''.join(input[i:i+size][2]),
        )
    print(f'ass2: {score}')
