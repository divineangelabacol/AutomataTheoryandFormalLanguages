# ---------- DFA 1 ----------
dfa1 = {
    'A': {'a': 'A', '0': 'A', '1': 'B'},  # loop on a/0, move to B on 1
    'B': {'0': 'C'},                      # must see 0 after the 1
    'C': {'1': 'C'}                       # then only 1’s
}
start1, final1 = 'A', {'C'}

# ---------- DFA 2 ----------
dfa2 = {
    'q0': {'a': 'q1', 'b': 'q2'},
    'q1': {'a': 'q0', 'b': 'q3'},
    'q2': {'a': 'q3', 'b': 'q0'},
    'q3': {'a': 'q2', 'b': 'q1'}
}
start2, final2 = 'q0', {'q0'}

# ---------- Simulation Function ----------
def simulate(dfa, start, final, string):
    state = start
    for ch in string:
        if ch not in dfa[state]:
            return False
        state = dfa[state][ch]
    return state in final

# ---------- Test Cases ----------
strings1 = ["10", "101", "0010111", "1", "100", "000"]
strings2 = ["ab", "aa", "baba", "a", "b", "abba"]

print("DFA1 Results:")
for s in strings1:
    print(f"{s} → {simulate(dfa1, start1, final1, s)}")

print("\nDFA2 Results:")
for s in strings2:
    print(f"{s} → {simulate(dfa2, start2, final2, s)}")
