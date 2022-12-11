
from math import floor
from operator import mul, add
import re

import numpy as np

MONKEY_NO = re.compile('Monkey ([0-9]+)')
ITEMS = re.compile('Starting items: ?(.*)')
OPERATOR = re.compile('[*]|[+]')
OPERATOR_FACTOR = re.compile('Operation: new = old ?(.*)')
MOD_FACTOR = re.compile('Test: divisible by ?(.*)')
IF_TRUE = re.compile('If true: throw to monkey ?(.*)')
IF_FALSE = re.compile('If false: throw to monkey ?(.*)')

def get_input():
    return open('11/inputa.txt').read().splitlines()

class Monkey():
    def __init__(self, items, operator, operator_factor, mod_factor, monkey_tree):
        self.items = items
        self.operator = operator
        self.operator_factor = operator_factor
        self.mod_factor = int(mod_factor)
        self.monkey_tree = monkey_tree
        self.no_items_passed = 0

    def do_round(self):
        self.current_item = self.items[0]
        del self.items[0]

        self.preform_inspection()

        #self.current_item = floor(self.current_item / 3)
        return self.throw_item()

    def preform_inspection(self):
        self.no_items_passed += 1
        if self.operator_factor == 'old':
            self.current_item = self.operator(self.current_item, self.current_item)
        else:
            self.current_item = self.operator(self.current_item, int(self.operator_factor))

    def catch_item(self, item):
        self.items.append(item)

    def throw_item(self):
        if not self.current_item % self.mod_factor:
            return self.current_item, self.monkey_tree[0]
        return self.current_item, self.monkey_tree[1]

    def show(self):
        print(f'{self.items}: {self.current_item}')


def generate_monkeys(monkeys):

    instructions = get_input()
    i=0
    while i < len(instructions):
        a = MONKEY_NO.findall(instructions[i + 0])[0]
        b = [np.int64(x) for x in ITEMS.findall(instructions[i + 1])[0].split(',')]

        if OPERATOR.findall(instructions[i + 2]) == ['*']:
            c = mul
        else:
            c = add

        d = OPERATOR_FACTOR.findall(instructions[i + 2])[0][2:]
        e = MOD_FACTOR.findall(instructions[i + 3])[0]
        f = IF_TRUE.findall(instructions[i + 4])[0]
        g = IF_FALSE.findall(instructions[i + 5])[0]

        monkeys[a] = Monkey(b,c,d,e,[f,g])
        i += 7


def ass_1():
    monkeys = {}
    generate_monkeys(monkeys)

    for x in range(20):
        for key in monkeys.keys():
            for i in range(len(monkeys[key].items)):
                item, to_monkey = monkeys[key].do_round()
                monkeys[to_monkey].catch_item(item)

    scores = [monkeys[x].no_items_passed for x in monkeys.keys()]
    scores.sort()
    print(f'answer 1: {scores[-1] * scores[-2]}')

ass_1()
