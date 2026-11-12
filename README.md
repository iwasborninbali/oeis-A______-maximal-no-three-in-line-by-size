# OEIS candidate (no A-number yet): maximal no-three-in-line subsets by size

<!-- oeis-status:begin -->
**OEIS status: not submitted.** (replaced by the registry tool)
<!-- oeis-status:end -->

## Definition

For n >= 1 and 1 <= k <= 2n, M(n,k) is the number of inclusion-maximal subsets of {0,...,n-1}² containing k points and no three distinct collinear points; points are labelled by coordinates. A set is maximal when adding any unselected grid point creates a collinear triple. List rows n=1,2,..., each at k=1,...,2n, including zeros; the flattened sequence has offset 1.

A grid row contains at most two selected points for n >= 2, so k > 2n cannot occur. At n=1, the unique maximal set contains the only grid point. Entry (n,k) has flattened index n(n-1)+k.

## Terms / result

In each row values are M(n,1),...,M(n,2n), in that order; zeros are included.

| n | Values by k |
|---|---|
| 1 | 1, 0 |
| 2 | 0, 0, 0, 1 |
| 3 | 0, 0, 0, 5, 16, 2 |
| 4 | 0, 0, 0, 2, 8, 210, 116, 11 |
| 5 | 0, 0, 0, 0, 0, 152, 1468, 3474, 520, 32 |
| 6 | 0, 0, 0, 0, 0, 8, 172, 11955, 49332, 49830, 5064, 50 |
| 7 | 0, 0, 0, 0, 0, 0, 0, 4136, 97712, 864918, 1158976, 305960, 13684, 132 |
| 8 | 0, 0, 0, 0, 0, 0, 0, 228, 8240, 728956, 9888900, 32215908, 20739920, 2853164, 73888, 380 |
| 9 | 0, 0, 0, 0, 0, 0, 0, 11, 396, 69326, 4366232, 110766708, 622544768, 848609530, 258109988, 17196815, 214044, 368 |
| 10 | 0, 0, 0, 0, 0, 0, 0, 4, 0, 2388, 283960, 36906832, 1226064676, 11500759134, 26269819804, 15105684331, 2192223828, 80475000, 667536, 1135 |

Machine-readable indexed terms are in `data/terms.txt` and coordinates in `data/rows.csv`.

## How it was obtained

The source's row-based program enumerates admissible row patterns, maintains occupancies of lines, and uses reflection and analytic completion of the last row. A separately developed program enumerates subsets point by point using determinant constraints and direct addability. Both count labelled sets and maximality by the absence of an addable point. For n=10 both were run in 512 shards; this repository includes the source's small archive of results and receipts.

## Verification

Both C enumerators have been replayed for n=2..7; n=1 was independently brute forced. The n=8 replay status, the archive audit for n=10 and the limits on n=9 are recorded in [CERTIFICATE.md](CERTIFICATE.md). Checks of stored outputs are not independent re-enumeration.

## Prior art and credit

The n=1..7 size profiles are public in the supporting table for [A398184](https://oeis.org/A398184); its current OEIS copy stops at n=7. The source repository also contains n=8..10. Row sums give A398184. Sean A. Irvine previously computed its n=8 total; the source credits the lab with n=9 and n=10. See [PRIOR-ART.md](PRIOR-ART.md).

## Reproduce

Requires a C compiler and Python 3.10 or later. The n<=7 replay takes under a minute on the test machine; brute force takes under a second; the archive check takes seconds. The optional n=8 run takes longer and has a 590-second per-process timeout.

```sh
cc -O3 -std=c11 programs/line_rows.c -o /tmp/c3_rows
cc -O3 -std=c11 verification/determinant_check.c -o /tmp/c3_det
python3 verification/bruteforce.py
python3 verification/replay.py
python3 verification/audit_archive.py
python3 verification/check_n8.py
```

Expected profile lines and archive results are in `verification/logs/`. Full n=9 and n=10 re-enumeration is not included in these commands.

## Provenance

Source: `projects/science/oeis-A398184`, commit `9e2359b0082971c18c87575f0987810cf2f09825`: `a398184.txt`, `programs/line_rows.c`, `programs/determinant_check.c`, `programs/collect.py`, `programs/reference/n9.json`, `programs/reference/determinant-n9.json`, `n10/shards-n10.tar.gz`. The original n=10 archive SHA-256 is `ae416edb0856c8c08c01b781cd2919ab2664ef516b5eb07644b925b3243d6044`. The source identifies `projects/science/no3-results` as its wider archive. No DOI has been established for these specific files.

## Author, licence

Aleksei Kudriashov (ORCID 0009-0006-8885-5338), Athanor lab, with AI assistance (OpenAI Codex cores; Claude Code as the lab's guide). Code: MIT; data and text: CC BY 4.0 (see LICENSE.md).
