class PDA:
    def __init__(self, states, input_alphabet, stack_alphabet, transitions, start_state, start_stack_symbol, accept_states):
        self.states = states
        self.input_alphabet = input_alphabet
        self.stack_alphabet = stack_alphabet
        self.transitions = transitions
        self.start_state = start_state
        self.start_stack_symbol = start_stack_symbol
        self.accept_states = accept_states

    def simulate(self, input_string):
        stack = [self.start_stack_symbol]
        configurations = [(self.start_state, 0, stack[:])]

        while configurations:
            state, index, stack = configurations.pop()

            if index == len(input_string) and state in self.accept_states:
                return True

            input_symbol = input_string[index] if index < len(input_string) else ""
            top = stack[-1] if stack else ""

            for key in [(state, input_symbol, top), (state, "", top)]:
                if key in self.transitions:
                    for (next_state, push_symbols) in self.transitions[key]:
                        new_stack = stack[:-1] + push_symbols if top else stack + push_symbols
                        next_index = index + (1 if key[1] else 0)
                        configurations.append((next_state, next_index, new_stack))

        return False
