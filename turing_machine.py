# automata/turing_machine.py
class TuringMachine:
    def __init__(self, states, tape_alphabet, transitions, start_state, accept_state, blank_symbol="_"):
        self.states = states
        self.tape_alphabet = tape_alphabet
        self.transitions = transitions
        self.start_state = start_state
        self.accept_state = accept_state
        self.blank_symbol = blank_symbol

    def simulate(self, input_string):
        tape = list(input_string) + [self.blank_symbol]
        head = 0
        state = self.start_state

        while state != self.accept_state:
            symbol = tape[head] if head < len(tape) else self.blank_symbol
            key = (state, symbol)

            if key not in self.transitions:
                return False

            next_state, write_symbol, direction = self.transitions[key]
            tape[head] = write_symbol

            if direction == "R":
                head += 1
                if head == len(tape):
                    tape.append(self.blank_symbol)
            elif direction == "L":
                head = max(0, head - 1)

            state = next_state

        return True
