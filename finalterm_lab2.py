# Converted Moore Machine Implementation (7-State)

# Moore Machine Transitions: (Current State, Input) -> Next State
moore_transitions = {
    ('QA', '0'): 'QA',  ('QA', '1'): 'QB',  # From A, A
    ('QB', '0'): 'QC1', ('QB', '1'): 'QD1', # From B, B
    ('QC1', '0'): 'QD2',('QC1', '1'): 'QB',  # From C, A
    ('QD1', '0'): 'QB', ('QD1', '1'): 'QC2', # From D, D
    ('QD2', '0'): 'QB', ('QD2', '1'): 'QC2', # From D, C
    ('QC2', '0'): 'QD2',('QC2', '1'): 'QB',  # From C, C
    ('QE', '0'): 'QD2', ('QE', '1'): 'QE',  # From E, C
}

# Moore Machine Outputs: State -> Output (λ'(q'))
moore_outputs = {
    'QA': 'A', 'QB': 'B', 'QC1': 'A', 'QD1': 'D',
    'QD2': 'C', 'QC2': 'C', 'QE': 'C'
}

def process_input_moore(input_string, start_state='QA'):
    """
    Processes an input string using the converted Moore Machine.
    Output length is |input| + 1, starting with the initial state's output.
    """
    current_state = start_state
    # Initial output from the start state (Moore machine characteristic)
    output_sequence = [moore_outputs[current_state]] 
    
    for symbol in input_string:
        input_symbol = symbol
        
        # Determine the next state
        next_state = moore_transitions[(current_state, input_symbol)]
        current_state = next_state
        
        # Append the output of the new state
        output_sequence.append(moore_outputs[current_state])
        
    return "".join(output_sequence), output_sequence[-1]


# --- Process the given inputs ---
input_strings = ["00110", "11001", "1010110", "101111"]

print("\n--- Converted Moore Machine Processing Results ---")
print("Input | Final Output | Full Output Sequence (|Input|+1)")
print("------|--------------|--------------------------------")

for input_str in input_strings:
    full_output, final_output = process_input_moore(input_str)
    print(f"{input_str:<5} | {final_output:<12} | {full_output}")

# The required final outputs to fill the '?' in the table are:
# 00110 -> C
# 11001 -> A
# 1010110 -> B
# 101111 -> B