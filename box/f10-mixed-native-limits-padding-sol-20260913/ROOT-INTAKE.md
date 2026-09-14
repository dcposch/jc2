# ROOT FIRST: correct Linux limits padding without weakening the limits

September13. CONDITIONAL STATIC CONFIRMED for corrected observer
40bd1116e4cb1bfbfc684afe1d0b0a334af10ed0b719f528efa4ee4a41b483d9.
No live observer, qualification, dummy or algebra success is established.

ROOT independently identified the defect before assigning the minimal Sol
correction. Linux proc_pid_limits writes the units using %-10s, so bytes
is followed by five spaces. Both old regexes end in bytes$ and reject those
lines. Same-kernel7.0.0-1011-aws administrative /proc/self/limits inspection
using sed-l and od showed the padding. The primary
[Linux source](https://github.com/torvalds/linux/blob/master/fs/proc/base.c)
independently confirms that formatter. This is not a read of V4's vanished
process or proof of its exclusive first failure cause.

The exact diff changes only two suffixes to bytes[[:blank:]]*$, preserving
both start anchors, the exact soft/hard integers, exact units and end anchors.
With bound LC_ALL=C, optional horizontal blanks do not admit nonblank junk,
alternate units or changed limits. There is no resource increase, predicate
deletion, new target control, source interpreter or retry loop.

ROOT read the complete corrected187-line source and independently ran tiny
administrative formatter/grep fixtures, NOT the observer. For BOTH file size
4194304 and address space1073741824, the kernel-shaped padded row gave
old exit1/corrected exit0. Wrong soft, wrong hard, wrong units and trailing
nonblank junk each gave corrected exit1 for BOTH fields. These are bounded
parser checks, not live-unit, native, dummy or scientific qualification.

Sol first01:37:01.395186381, independently confirmed terminal by agent-list
after final ALL WRITERS IDLE01:39:13.165535021UTC, before original01:45
reserve/01:48HARD. Elapsed131.770348640seconds is not CPU/billing/credits.
Custody5505dc794dec8ac3a85f5b35a8a359ff03e70c96036bec346c6df15bc1ddc4e2,
PINS6094e25a7740fd310c97edf2197d083ae364d49e5462e42a9a34ecd682bfe9fe,
report51da7e9576c92e0a66cc3fbf4e60451954a1447c6eded9964ebd6e7921a00bd7,
manifest79d18d057ac0e167792621ca0cfc73c1a5b0bd300b0b1b39def069d016224398.
All four input and four output postpins passed strict verification. Expected
basis/manifest verification passed; complete report/source/PINS/custody/
manifest were read. ROOT initially guessed nonexistent CUSTODY.md/PINS.sha256
names and read the report before finding the actual JSON custody files;
therefore this is NOT claimed as custody-first intake. The author was already
independently terminal; validation and this FIRST followed actual JSON custody
and strict pins. No live partial was consumed or unverified source executed.

All original ROOT observer qualifications remain binding: trusted PATH and
LC_ALL=C, physical/source pins before use, actual successful capture inside
the original60seconds and qualification cutoff, timeout STOP without retry,
no remote-descendant-lifetime guarantee from foreground SSH timeout, and
the recorded cmdline/post-argument and normalized-LF qualifications.

The V4 runtime failure remains CLOSED, with exact first failed predicate
unknown. This concrete formatter incompatibility explains why an unchanged
observer cannot pass on the standard limits output. It supplies a justified
source delta for a separately registered later execution, not a new worker,
clock, native manifest or mathematical authority. Original PREPARE, dummy,
science UNIT, six phases, whole-parameter target and caps are unchanged.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `3541`.
- Body SHA-256:
  `ab14a786134550100dbbe546774303bca4240ed47ef5e1b124fb4acb745bdd2a`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
