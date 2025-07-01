# Variables and domains
variables = ['A', 'B', 'C', 'D', 'E']
domains = {v: ['Red', 'Green', 'Blue'] for v in variables}

# Adjacency list
neighbors = {
    'A': ['B', 'C', 'D'],
    'B': ['A', 'C', 'E'],
    'C': ['A', 'B', 'D', 'E'],
    'D': ['A', 'C', 'E'],
    'E': ['B', 'C', 'D']
}

# Constraint: adjacent regions must have different colors
def is_valid(assignment, var, color):
    return all(assignment.get(n) != color for n in neighbors[var])

# Backtracking CSP solver
def csp_backtrack(assignment):
    if len(assignment) == len(variables):
        return assignment
    var = next(v for v in variables if v not in assignment)
    for color in domains[var]:
        if is_valid(assignment, var, color):
            assignment[var] = color
            result = csp_backtrack(assignment)
            if result: return result
            del assignment[var]
    return None

# Solve and print
solution = csp_backtrack({})
print("Solution:", solution if solution else "No solution")
