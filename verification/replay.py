"""Compare separately written enumerators with the stored triangle (n <= 7)."""
import csv
import json
import subprocess
from pathlib import Path

root = Path(__file__).resolve().parent.parent
with (root / 'data/rows.csv').open() as f:
    rows = list(csv.DictReader(f))
for n in range(1, 8):
    expected = [0] + [int(r['count']) for r in rows if int(r['n']) == n]
    programs = [('/tmp/c3_rows', str(n), '--shard', '0', '--shards', '1', '--split-rows', '0')]
    if n >= 2:
        programs.append(('/tmp/c3_det', str(n), '0', '1', '0'))
    for cmd in programs:
        p = subprocess.run(cmd, capture_output=True, text=True, check=True, timeout=590)
        actual = json.loads(p.stdout)['maximal_profile']
        if actual != expected:
            raise AssertionError((cmd, actual, expected))
        print(f"{Path(cmd[0]).name} n={n} maximal_profile={actual} OK", flush=True)
