import sys
from enum import Enum

class ComputerState(Enum):
    RUNNING = 0
    HALTED = 1

class Computer:
    def __init__(self, program: list):
        self.state = ComputerState.RUNNING
        self.ip = 0
        self.memory = program[:]
        self.opcode_map = {1: self.add, 2: self.multiply, 99: self.halt}
        return

    def __repr__(self):
        return f"""{repr(self.state)}
{self.memory_repr()}"""

    def memory_repr(self):
        "damn this is ugly"
        s = ""
        c = 0
        opcode = self.memory[c]
        while opcode != 99 and c < len(self.memory):
            s += f'{self.memory[c]},{self.memory[c+1]},{self.memory[c+2]},{self.memory[c+3]},\n'
            c += 4
            opcode = self.memory[c]

        if opcode == 99:
            s += '99,\n'
            c += 1

        if c < len(self.memory):
            while c < len(self.memory):
                s += f'{self.memory[c]},'
                c += 1
            s += '\n'

        return s

    @classmethod
    def from_program_string(cls, program_str):
        'instantiates a computer from a string formatted like "1,0,0,0,99"'
        return cls(list(map(lambda s: int(s), program_str.split(','))))

    def step(self):
        if self.state == ComputerState.HALTED:
            return ComputerState.HALTED

        opcode = self.memory[self.ip]
        op1, op2, op3 = 0, 0, 0
        if opcode != 99:
            op1 = self.memory[self.ip + 1]
            op2 = self.memory[self.ip + 2]
            op3 = self.memory[self.ip + 3]
        self.opcode_map[opcode](op1, op2, op3)
        self.ip += 4

        return self.state

    def run(self):
        state = self.step()
        while state != ComputerState.HALTED:
            state = self.step()
        return self

    def add(self, from1, from2, to):
        from1 = self.memory[from1]
        from2 = self.memory[from2]
        self.memory[to] = from1 + from2

    def multiply(self, from1, from2, to):
        from1 = self.memory[from1]
        from2 = self.memory[from2]
        self.memory[to] = from1 * from2

    def halt(self, _from1, _from2, _to):
        self.state = ComputerState.HALTED

def run_with_noun_verb(program, noun, verb):
    comp = Computer(program)
    comp.memory[1] = noun
    comp.memory[2] = verb
    try:
        comp.run()
    except:
        pass
    return comp.memory[0]


if __name__ == '__main__':
    program = sys.stdin.readline()
    program = list(map(lambda s: int(s), program.split(',')))

    solution = -1
    for noun in range(0, 100):
        for verb in range(0, 100):
            if run_with_noun_verb(program, noun, verb) == 19690720:
                solution = (noun, verb)
                break
        if solution != -1:
            break

    print(solution[0] * 100 + solution[1])
