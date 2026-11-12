# Prior art

The size profiles n=1..7 were already published as the lab's supporting table for [OEIS A398184](https://oeis.org/A398184/a398184.txt); its current OEIS copy, checked 2026-11-13, ends at n=7. The source repository snapshot contains rows through n=10; its README says those rows were uploaded to OEIS, but they are absent from the OEIS copy we fetched. The OEIS entry itself counts all labelled maximal subsets, i.e. row sums, rather than entries by size. [A398172](https://oeis.org/A398172) counts all safe subsets whether maximal or not. [A000755](https://oeis.org/A000755) concerns the extreme 2n-point case, and [A277433](https://oeis.org/A277433) concerns the least size of a maximal set. These differ from the whole triangle. The source credits Sean A. Irvine with the n=8 A398184 total and the lab with the n=9 and n=10 totals.

OEIS searches on 2026-11-13, `https://oeis.org/search` with `fmt=json`:

| Exact query | Returned count |
|---|---:|
| `1,0,0,0,0,1,0,0,0,5,16,2` | 0 |
| `0,0,0,1,0,0,0,5,16,2` | 0 |
| `5,16,2,2,8,210,116,11` | 0 |
| `maximal no-three-in-line subsets size triangle` | 0 |

The second query omits the first row and part of the next; the third searches the consecutive nonzero size profiles for n=3 and n=4, a different flattening. These searches do not prove novelty. The supporting source table is credited to Aleksei Kudriashov; its linked programs describe independent methods, and we make no priority claim for the already public profiles.
