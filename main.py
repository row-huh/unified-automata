# main.py
from dfa import DFA
from nfa import NFA
from epsilon_nfa import EpsilonNFA
from pda import PDA
from turing_machine import TuringMachine

input_str = str(input("Enter a string: "))

# DFA Definition
dfa_def = {
    "states": {"q0", "q1"},
    "alphabet": {"0", "1"},
    "transitions": {
        ("q0", "0"): "q0",
        ("q0", "1"): "q1",
        ("q1", "0"): "q1",
        ("q1", "1"): "q0",
    },
    "start_state": "q0",
    "accept_states": {"q1"},
}
dfa = DFA(**dfa_def)
print("DFA Result:", dfa.simulate(input_str))

# NFA Definition
nfa_def = {
    "states": {"q0", "q1"},
    "alphabet": {"0", "1"},
    "transitions": {
        ("q0", "0"): {"q0", "q1"},
        ("q0", "1"): {"q0"},
        ("q1", "1"): {"q1"},
    },
    "start_state": "q0",
    "accept_states": {"q1"},
}
nfa = NFA(**nfa_def)
print("NFA Result:", nfa.simulate(input_str))

# ε-NFA Definition
epsilon_nfa_def = {
    "states": {"q0", "q1", "q2"},
    "alphabet": {"0", "1"},
    "transitions": {
        ("q0", ""): {"q1"},
        ("q1", "0"): {"q1"},
        ("q1", "1"): {"q2"},
    },
    "start_state": "q0",
    "accept_states": {"q2"},
}
epsilon_nfa = EpsilonNFA(**epsilon_nfa_def)
print("ε-NFA Result:", epsilon_nfa.simulate(input_str))

# PDA Definition
pda_def = {
    "states": {"q0", "q1", "q2"},
    "input_alphabet": {"a", "b"},
    "stack_alphabet": {"Z", "A"},
    "transitions": {
        ("q0", "a", "Z"): [("q0", ["A", "Z"])],
        ("q0", "a", "A"): [("q0", ["A", "A"])],
        ("q0", "b", "A"): [("q1", [])],
        ("q1", "b", "A"): [("q1", [])],
        ("q1", "", "Z"): [("q2", ["Z"])],
    },
    "start_state": "q0",
    "start_stack_symbol": "Z",
    "accept_states": {"q2"},
}
pda = PDA(**pda_def)
print("PDA Result:", pda.simulate("aaabbb"))

# Turing Machine Definition
tm_def = {
    "states": {"q0", "q1", "halt"},
    "tape_alphabet": {"0", "1", "_"},
    "blank_symbol": "_",
    "transitions": {
        ("q0", "1"): ("q0", "1", "R"),
        ("q0", "0"): ("q0", "0", "R"),
        ("q0", "_"): ("q1", "_", "L"),
        ("q1", "1"): ("halt", "1", "N"),
    },
    "start_state": "q0",
    "accept_state": "halt",
}
tm = TuringMachine(**tm_def)
print("TM Result:", tm.simulate("101"))
