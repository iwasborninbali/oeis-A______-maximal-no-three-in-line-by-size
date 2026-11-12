"""Independent brute force for n <= 4; Codex, 2026-11-13."""
from itertools import combinations

for n in range(1, 5):
    points = list(range(n*n))
    bad = []
    for a, b, c in combinations(points, 3):
        x1, y1 = divmod(a, n); x2, y2 = divmod(b, n); x3, y3 = divmod(c, n)
        if (x2-x1)*(y3-y1) == (y2-y1)*(x3-x1):
            bad.append((1 << a) | (1 << b) | (1 << c))
    safe = [False] * (1 << (n*n))
    for mask in range(len(safe)):
        safe[mask] = all(mask & b != b for b in bad)
    profile = [0] * (2*n+1)
    for mask in range(len(safe)):
        if safe[mask] and all((mask >> i) & 1 or not safe[mask | (1 << i)] for i in points):
            profile[mask.bit_count()] += 1
    print(f'n={n} maximal_profile={profile}')
