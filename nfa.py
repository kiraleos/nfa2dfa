class NFA:
    def __init__(self, input_file):
        f = open(input_file, "r")
        lines = [line.strip() for line in f.readlines()]
        self.num_of_states = int(lines[0])
        self.states = ["q" + str(i) for i in range(self.num_of_states)]
        self.alphabet = lines[1].split(" ")
        self.start_state = frozenset({"q" + lines[2]})
        self.end_states = ["q" + state for state in lines[3].split(" ")]
        self.transitions = {}
        for line in lines[4:]:
            line = line.split(" ")
            _from = frozenset({"q" + line[0]})
            _to = "q" + line[2]
            _with = line[1]
            if (_from, _with) not in self.transitions:
                self.transitions[_from, _with] = set()
            self.transitions[_from, _with].add(_to)
        f.close()

    def __repr__(self):
        import pprint

        repr_str = "---------- NFA ----------\n"
        repr_str += "States: " + str(self.states) + "\n"
        repr_str += "Alphabet: " + str(self.alphabet) + "\n"
        repr_str += "Start state: " + str(self.start_state) + "\n"
        repr_str += "End states: " + str(self.end_states) + "\n"
        repr_str += "Transitions:\n"

        pp = pprint.PrettyPrinter()
        repr_str += pp.pformat(self.transitions)
        return repr_str