
import re

from math import floor

NUMBERS_RE = re.compile('-?[0-9]+')
prompt = input

def get_input():
    return open('10/input.txt').read().splitlines()

def ass_1():
    input = get_input()
    cycles = 0
    score = 1

    signal_strength = []

    for line in input:
        steps = NUMBERS_RE.findall(line)
        if steps:
            steps = int(steps[0])
            for i in range(2):
                cycles += 1
                if cycles in [20,60,100,140,180,220]:
                    signal_strength.append(score * cycles)

            score += steps

        else:
            cycles += 1
            if cycles in [20,60,100,140,180,220]:
                print(cycles)
                signal_strength.append(score * cycles)


    print(f'answer 1: {sum(signal_strength)}')


class Monitor():
    def __init__(self):
        self.cycle = 0
        self.score = 1
        self.split_lines = list(range(40,241,40))
        self.crt_lines = [[' '] * 40 for x in self.split_lines]

    def add_cycle(self):
        self.add_to_crt()
        self.cycle += 1
        # self.draw()
        # prompt(' ')

    def add_score(self, score):
        self.score += score

    def add_to_crt(self):
        modded_cycle = self.cycle % 40
        if self.score > modded_cycle - 2 and self.score < modded_cycle + 2:
            self.crt_lines[floor(self.cycle / 40)][modded_cycle] = '#'
        else:
            self.crt_lines[floor(self.cycle / 40)][modded_cycle] = ' '

    def draw(self):
        for i in self.crt_lines:
            print(''.join(i))


def ass_2():
    input = get_input()
    monitor = Monitor()
    score = 1

    signal_strength = []

    for line in input:
        steps = NUMBERS_RE.findall(line)
        if steps:
            steps = int(steps[0])
            for i in range(2):
                monitor.add_cycle()
            monitor.add_score(steps)
        else:
            monitor.add_cycle()

    print(f'answer 2:')
    monitor.draw()

if __name__ == '__main__':
    ass_1()
    ass_2()
