import itertools
import re

def solve_cryptarithmetic():
    # Equation in words
    puzzle = 'SEND + MORE == MONEY'
    # Extract unique letters
    letters = sorted(set(re.findall(r'[A-Z]', puzzle)))
    
    assert len(letters) <= 10, "Too many letters (more than digits)"

    # Try all permutations of 0-9 for these letters
    for perm in itertools.permutations(range(10), len(letters)):
        letter_map = dict(zip(letters, perm))

        # Skip if any word starts with 0
        if letter_map['S'] == 0 or letter_map['M'] == 0:
            continue

        # Replace letters with digits in the equation
        expr = puzzle.translate(str.maketrans({ch: str(letter_map[ch]) for ch in letters}))

        if eval(expr):
            print(f"Solved: {expr}")
            print("Mapping:")
            for k, v in letter_map.items():
                print(f"  {k} = {v}")
            return

    print("No solution found.")

# Run it
solve_cryptarithmetic()
