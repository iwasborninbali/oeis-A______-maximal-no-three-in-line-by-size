"""Replay both complete n=8 enumerations and compare the stored row."""
import csv
import json
import subprocess
with open('data/rows.csv') as f:
    expected = [0] + [int(r['count']) for r in csv.DictReader(f) if r['n'] == '8']
for cmd in [('/tmp/c3_rows', '8', '--shard', '0', '--shards', '1', '--split-rows', '0'),
            ('/tmp/c3_det', '8', '0', '1', '0')]:
    p = subprocess.run(cmd, capture_output=True, text=True, check=True, timeout=590)
    result = json.loads(p.stdout)
    assert result['maximal_profile'] == expected
    print(cmd[0], 'n=8 maximal_profile=', result['maximal_profile'],
          'seconds=', round(result['seconds'], 2), 'OK', flush=True)
