from collections import deque

def water_jug():
    q = deque()
    visited = set()
    q.append(((0, 0), []))  # current state: (A, B), path

    while q:
        (a, b), path = q.popleft()

        if (a, b) in visited:
            continue
        visited.add((a, b))

        path = path + [(a, b)]

        # Goal condition: 2 liters in jug A
        if a == 2:
            print("Steps to reach 2L in Jug A:")
            for step in path:
                print(f"A: {step[0]}, B: {step[1]}")
            return

        # All possible operations
        q.extend([
            ((4, b), path),  # Fill A
            ((a, 3), path),  # Fill B
            ((0, b), path),  # Empty A
            ((a, 0), path),  # Empty B
            ((min(a + b, 4), b - (min(a + b, 4) - a)), path),  # Pour B → A
            ((a - (min(a + b, 3) - b), min(a + b, 3)), path)   # Pour A → B
        ])

# Run it
water_jug()
