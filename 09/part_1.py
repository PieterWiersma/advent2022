

prompt = input

def get_input():
    return open('09/input.txt').read().splitlines()

class Rope():
    def __init__(self, x, y):
        self.head_x = self.tail_x = x
        self.head_y = self.tail_y = y
        self.tail_coordinates = [(x,y)]

        self.x_offset = 0
        self.y_offset = 0

        self.draw = False
        self.draw_slow = False


    def move_head(self, direction, steps):
        for i in range(steps):
            if direction == 'R':
                self.head_x += 1
            elif direction == 'L':
                self.head_x -= 1
            elif direction == 'D':
                self.head_y += 1
            elif direction == 'U':
                self.head_y -= 1
            self.move_tail(direction)

            if self.draw:
                self.print_grid()
                if self.draw_slow:
                    prompt('')


    def move_tail(self, direction):

        if abs(self.head_x - self.tail_x) == 2 and abs(self.head_y - self.tail_y) > 0:
            self.tail_y = self.head_y
        if self.head_x - self.tail_x > 1:
            self.tail_x += 1
        if self.head_x - self.tail_x < -1:
            self.tail_x -= 1


        if abs(self.head_y - self.tail_y) == 2 and abs(self.head_x - self.tail_x) > 0:
            self.tail_x = self.head_x
        if self.head_y - self.tail_y > 1:
            self.tail_y += 1
        if self.head_y - self.tail_y < -1:
            self.tail_y -= 1

        self.tail_coordinates.append((self.tail_x, self.tail_y))


    def _print_grid(self, x_offset, y_offset):
        x = []
        for i in range(15):
            x.append(['.'] * 15)
        for i in self.tail_coordinates:
            x[i[1]+ y_offset][i[0]+ x_offset] = '*'
        x[self.tail_y + y_offset][self.tail_x + x_offset] = 'T'
        x[self.head_y + y_offset][self.head_x + x_offset] = 'H'
        for i in x:
            print(i)
        print(f'h: {(self.head_x, self.head_y)} t: {(self.tail_x, self.tail_y)}')
        print('---')

    def print_grid(self):
        try:
            self._print_grid(self.x_offset, self.y_offset)
        except IndexError:
            self.x_offset = 0 - self.head_x
            self.y_offset = 0 - self.head_y
            self._print_grid(self.x_offset, self.y_offset)


if __name__ == "__main__":
    input = get_input()

    # arbitrary start point
    rope = Rope(5,5)

    for instruction in input:
        direction, steps = instruction.split(' ')
        rope.move_head(direction, int(steps))

    print(f'answer 1: {len(set(rope.tail_coordinates))}')
