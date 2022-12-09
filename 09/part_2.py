

prompt = input

def get_input():
    return open('09/input.txt').read().splitlines()

class Rope():
    def __init__(self, x, y):
        self.tail_coordinates = [(x,y)]
        self.knots = {}

        for i in range(10):
            self.knots[f'{i}_x'] = x
            self.knots[f'{i}_y'] = y

        self.x_offset = 0
        self.y_offset = 0


    def move_head(self, direction, steps):
        for i in range(steps):
            if direction == 'R':
                self.knots['0_x'] += 1
            elif direction == 'L':
                self.knots['0_x']  -= 1
            elif direction == 'D':
                self.knots['0_y']  += 1
            elif direction == 'U':
                self.knots['0_y']  -= 1
            self.move_tails()
            # self._print_grid()
            # breakpoint()


    def move_tails(self): # cant use direction anymore
        for i in range(9):
            self._move_tail(f'{i}_x', f'{i}_y', f'{i+1}_x', f'{i+1}_y')
        self.tail_coordinates.append((self.knots['9_x'], self.knots['9_y']))
        # for key in self.knots.keys():
        #     print(f'{key}: {self.knots[key]}')
        # prompt('')

    def _move_tail(self, head_x, head_y, tail_x, tail_y):
        """
        als de totale som van verandering groter is dan 2 dan 2x 1
        """

        if abs(self.knots[head_x] - self.knots[tail_x]) + abs(self.knots[head_y] - self.knots[tail_y]) > 3:
            if self.knots[tail_x] > self.knots[head_x]:
                self.knots[tail_x] -= 1
            else:
                self.knots[tail_x] += 1
            if self.knots[tail_y] > self.knots[head_y]:
                self.knots[tail_y] -= 1
            else:
                self.knots[tail_y] += 1

        if abs(self.knots[head_x] - self.knots[tail_x]) > 1 and abs(self.knots[head_y] - self.knots[tail_y]) > 0:
            self.knots[tail_y] = self.knots[head_y]
        if self.knots[head_x] - self.knots[tail_x] > 1:
            self.knots[tail_x] += 1
        if self.knots[head_x] - self.knots[tail_x] < -1:
            self.knots[tail_x] -= 1

        if abs(self.knots[head_y] - self.knots[tail_y]) == 2 and abs(self.knots[head_x] - self.knots[tail_x]) > 0:
            self.knots[tail_x] = self.knots[head_x]
        if self.knots[head_y] - self.knots[tail_y] > 1:
            self.knots[tail_y] += 1
        if self.knots[head_y] - self.knots[tail_y] < -1:
            self.knots[tail_y] -= 1




    def _print_grid(self):
        x = []
        for i in range(15):
            x.append(['.'] * 15)
        for knot in range(10):
            x[self.knots[f'{knot}_y']][self.knots[f'{knot}_x']] = str(knot)
        for i in x:
            print(i)
        print('---')


if __name__ == "__main__":
    input = get_input()

    # arbitrary start point
    rope = Rope(5,5)

    for instruction in input:
        direction, steps = instruction.split(' ')
        rope.move_head(direction, int(steps))

    print(f'answer: {len(set(rope.tail_coordinates))}')
