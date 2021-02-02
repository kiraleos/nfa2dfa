# NFA2DFA
A non-deterministic finite automaton to deterministic finite automaton converter.

## Usage
`python main.py <input> <output>` 
where `input` is a text file describing the NFA in the form:
```
3      Number of states
0 1    Alphabet
0      Starting state
2      Final State
0 0 1  Transition function (e.g from state 0 with symbol '0' to state 1)
0 0 0
0 1 0
1 1 2
```
The output file is a DFA described in the same way as the input file. Some of the DFA's state's names are a concatenation of the NFA's state's names. For example, `01` is a valid DFA state name. 

#### Disclaimer
This was made in one day for a university course. Don't expect high quality code.
