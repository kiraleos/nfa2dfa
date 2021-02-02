from powerset import powerset
from nfa import NFA
from dfa import DFA
from pprint import pprint
import sys


def main():
    if len(sys.argv) < 3:
        print("Missing arguments.\nUsage: python main.py <input> <output>")
        return
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    nfa1 = NFA(input_file)
    dfa1 = DFA(nfa1)
    dfa1.write_to_file("./output/" + output_file)
    # print(nfa1)
    # print()
    # print(dfa1)

    # nfa2 = NFA("nfa2.txt")
    # dfa2 = DFA(nfa2)
    # dfa2.write_to_file("dfa2.txt")
    # print(nfa2)
    # print()
    # print(dfa2)


if __name__ == "__main__":
    main()