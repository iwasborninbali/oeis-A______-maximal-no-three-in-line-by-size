"""Audit the saved n=10 shards and compare their profile with this triangle."""
import csv
import json
import pathlib
import subprocess
import tarfile
import tempfile
root = pathlib.Path(__file__).resolve().parent.parent
with tempfile.TemporaryDirectory() as temp:
    directory = pathlib.Path(temp)
    with tarfile.open(root / 'verification/archive/shards-n10.tar.gz') as archive:
        for member in archive:
            if not member.isfile() or member.name.startswith('/') or '..' in pathlib.PurePosixPath(member.name).parts:
                raise ValueError(member.name)
            path = directory / member.name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(archive.extractfile(member).read())
    run = directory / 'run-n10'
    subprocess.run(['python3', '-I', str(root / 'verification/collect.py'), str(run), '--require-complete'], check=True)
    aggregate = json.loads((run / 'aggregate.json').read_text())
    with (root / 'data/rows.csv').open() as f:
        expected = [0] + [int(r['count']) for r in csv.DictReader(f) if r['n'] == '10']
    for program in ('row', 'det'):
        assert aggregate['programs'][program]['maximal_profile'] == expected
    print('n=10 stored profiles match data/rows.csv for both programs')
