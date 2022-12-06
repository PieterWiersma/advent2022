
def get_input():
    return open('06/input.txt').read()



if __name__ == '__main__':
    input = get_input()
    four = 4
    for i in range(len(input)):
        if len(input[i:i+four]) == len(set(input[i:i+four])):
            break
    print(f'ass1: key: {i+four}')

    fourteen = 14
    for i in range(len(input)):
        if len(input[i:i+fourteen]) == len(set(input[i:i+fourteen])):
            break
    print(f'ass2 key: {i+fourteen}')
