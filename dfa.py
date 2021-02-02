from powerset import powerset
from collections import deque


class DFA:
    def __init__(self, nfa):
        # DFA's states are the powerset of NFA's states
        self.states = sorted(
            [frozenset(state) for state in powerset(nfa.states)],
            key=lambda state: len(state),
        )

        # Alphabet remains the same
        self.alphabet = nfa.alphabet

        # Starting state remains the same
        self.start_state = nfa.start_state

        # Construct the DFA's transition function dict.
        #
        # Part 1
        self.transitions = {}
        for state in self.states:
            for symbol in self.alphabet:
                if (state, symbol) in nfa.transitions:
                    self.transitions[state, symbol] = frozenset(
                        state for state in nfa.transitions[state, symbol]
                    )
                else:
                    self.transitions[state, symbol] = frozenset()
        # Part 2
        for state in self.states:
            for symbol in self.alphabet:
                if self.transitions[state, symbol] == frozenset():
                    result = frozenset()
                    for sub_state in state:
                        sub_state = frozenset({sub_state})
                        result |= self.transitions[sub_state, symbol]
                    self.transitions[state, symbol] = result

        # Find the accessible states
        s = deque({self.start_state})
        seen = set()
        while len(s) > 0:
            current = s.pop()
            if current not in seen:
                seen.add(current)
                for symbol in self.alphabet:
                    s.append(self.transitions[current, symbol])
        self.accessible = seen

        # Keep only the accessible states
        for state in self.transitions.copy():
            if state[0] not in self.accessible:
                del self.transitions[state]
                if state[0] in self.states:
                    self.states.remove(state[0])

        # Number of states is the length of the new set of states
        self.num_of_states = len(self.states)

        # Find the end states
        self.end_states = []
        for end_state in nfa.end_states:
            for state in self.accessible:
                if end_state in state:
                    self.end_states.append(state)

    def write_to_file(self, of_name):
        f = open(of_name, "w")
        str_builder = ""
        str_builder += str(self.num_of_states) + "\n"
        for symbol in self.alphabet:
            str_builder += symbol + " "
        str_builder += "\n" + list(self.start_state)[0].strip("q") + "\n"
        for state_set in self.end_states:
            state_str = ""
            for state in list(state_set):
                state_str += str(state).strip("q")
            str_builder += "".join(sorted(state_str)) + " "
        str_builder += "\n"
        for k, v in self.transitions.items():
            state_str_from = ""
            for state in list(k[0]):
                state_str_from += str(state).strip("q")
            state_str_to = ""
            for state in list(v):
                state_str_to += str(state).strip("q")
            if state_str_from == "":
                state_str_from = "∅"
            if state_str_to == "":
                state_str_to = "∅"
            str_builder += (
                "".join(sorted(state_str_from))
                + " "
                + k[1]
                + " "
                + "".join(sorted(state_str_to))
            )
            str_builder += "\n"

        str_builder = str_builder[:-1]  # remove trailing newline
        f.write(str_builder)
        f.close()

    def __repr__(self):
        import pprint

        pp = pprint.PrettyPrinter()
        repr_str = "---------- DFA ----------\n"
        repr_str += "States:\n" + pp.pformat(self.states) + "\n"
        repr_str += "\nAlphabet:\n" + str(self.alphabet) + "\n"
        repr_str += "\nStart state:\n" + str(self.start_state) + "\n"
        repr_str += "\nTransitions:\n"
        repr_str += pp.pformat(self.transitions)
        repr_str += "\n\nAccessible:\n"
        repr_str += pp.pformat(self.accessible)
        repr_str += "\n\nEnd states:\n " + pp.pformat(self.end_states)
        return repr_str

    def to_file(self):
        pass