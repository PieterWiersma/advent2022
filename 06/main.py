
def get_input():
    return open('06/input.txt').read()



if __name__ == '__main__':
    input = get_input()

    four = 4
    for i in range(len(input)):
        if len(set(input[i:i+four])) == four:
            break
    print(f'ass1: key: {i+four}')

    fourteen = 14
    for i in range(len(input)):
        if len(set(input[i:i+fourteen])) == fourteen:
            break
    print(f'ass2 key: {i+fourteen}')
