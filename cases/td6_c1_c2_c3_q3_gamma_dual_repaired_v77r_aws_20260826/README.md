# TD6 V77R: corrected pure-q3 scalar audit

Date: 2026-08-26  
Status: **PRODUCER-EXACT / DUAL-AWS PASS / HOSTILE REVIEW PENDING**

## Exact scope

V77R uses the fixed source-typed three-center section

```text
y=s^-1,
x=C*s+V*s^2+U*s^3+t*s^4,
p=t^15,
q=t+gamma*t^3+t^25
```

at `beta=0`, zero dead stretch, and frozen `F1`/pole data.  Its coefficient
ring is the square-zero extension by `gamma`, localized only on
`D(U*(C-3U^2)*B3)`.  This is a first-order source-support audit at the
already-empty fixed-A3 base; it is not a gamma-neighborhood or gamma-family
theorem.

The corrected source pins the V32 infrastructure (SHA-256
`dcc7003d...`), sets the legacy q2 coordinate `qd.B` to exact zero, retains
the singleton original transport key `('g','X',0,3)`, and includes the
direct q-prime term `3*gamma*t^2`.

## Result

Independent Box02 and r6d executions returned rc 0.  After deleting only
the three `aws_platform`, `aws_hostname`, and `aws_run_tag` environment
banner lines, their stdout bytes are identical with SHA-256

```text
f6aaf1c9f4e9f1e6961525a5cf79fd53ac4e3ee226520e34d652a7642fdabf1e
```

Load-bearing statements are:

- transport rank `3470/3602`, first rank `38/132`, and exact original-row
  replay;
- the selected first-minor q3 derivative is **exactly zero**.  Its
  `c0730f...` digest is the canonical serialization of zero, not evidence of
  nonzero rank growth;
- the genuine P12 base has 2,893 terms; its q3 derivative has four terms
  (SHA `70d253cd...`);
- exact reduction gives base remainder `-k/50` and a three-term affine q3
  derivative (SHA `3dd07bb5...`); the square-zero remainder is a unit because
  its base term already is a unit;
- 28 original first rows occur, 14 have lambda-prime support, and omitting
  lambda-prime breaks the source identity;
- the termwise replay covers 77,512 slots and every denominator radical is
  among `U`, `C-3U^2`, and `B3`.

The clean q3 P12 and remainder digests equal the old V77 mathematical
objects.  V77R corrects the old report's selected-minor interpretation and
adds an explicit source-coordinate audit; it does not broaden old scope.

## Controls

The producer proves that assigning a stale nonzero value to `qd.B` after
`Q_PRIME` has been replaced is semantically inert.  A genuine q2 leak is
therefore injected through `Q_PRIME[1]`, and that leak changes the rows.
Omitting the q3 transport source, direct q-prime term, an original source
row, or lambda-prime is also detected.

The first V79a launches are frozen under
`control_v79a_stale_B_miscontrol/`.  They stopped before q3 mathematics at
the invalid assertion `first_rows_q2_leak != first_rows`: that version
changed only stale `qd.B`.  They are software-control failure evidence, not
mathematical evidence.

## Custody

| object | SHA-256 |
|---|---|
| corrected source archive | `5973b82953c919df1a28b1b86eed40feafbe4a3ea69bde14e7df68374e83942d` |
| corrected SOURCE manifest bytes | `b1f1d48466b12748112dc054ee435051f1afdb67b816eaf1bc7c7ffe27742c2b` |
| corrected V77R source | `7a961c02002dabb5f8ae363e88a4a041b855ec03fc8ea370bea576ae12e47d80` |
| Box02 stdout / stderr | `9f3be97b...` / `0c9d05fa...` |
| r6d stdout / stderr | `1d05d1be...` / `b6238044...` |
| normalized stdout | `f6aaf1c9...` |

Box02 ran tag `td6_v79b_v77r_box02_20260826T0002Z` on
`ip-172-30-0-186`, 19m14s, maximum RSS 567,644 KiB.  r6d ran tag
`td6_v79b_v77r_r6d_20260826T0002Z` on `ip-172-30-0-45`, 19m21s,
maximum RSS 567,736 KiB.  Each launch used a 12-GiB address-space cap and a
four-hour timeout.

## Firewall

V77R does not prove a finite gamma neighborhood empty, does not kill the
gamma family or any higher-dimensional q family, does not cover remaining
TD6 source moduli, does not kill TD6 or SP-2, and does not resolve JC2.
