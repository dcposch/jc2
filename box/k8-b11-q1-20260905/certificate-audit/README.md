# K8, b=11, q1 certificate feasibility audit

This directory contains read-only algebraic screening of the frozen input
`../input/K8_B11_Q1_p0.ms`.  No msolve, Singular, or other CAS was invoked by
this audit.  The input is the 97-variable, 330-generator characteristic-zero
file with SHA-256
`66bb78cfec123e11c5b9c780056b5949aa1c5c198caeb3c668aab1973d6697eb`.

## Exact small identities

Generator numbers are one-based, `q=v95`, `r=v96`, and
`L=g330=q*r-1`.  `static_q3_span_audit.py` parses the source polynomials over
the integers and checks all of the following by direct sparse multiplication:

```text
g2  = g3 + g1
g36 = 99*g3 + 227*g1
g37 = 211*g3 + 120*g1
g38 = v7*g1
g39 = 3*v7*g3 + (3*v7-v14)*g1
g40 = 5*g4 + (7*v7-3*v14)*g3 - (3*v14+v20)*g1

A = q*g4 + 4*v55*g1 - 4*v20*q*g1 = q*v45^2
B = A - (v45+v14*q)*g3               = v14^2*q^3

v7 = r^2*g1 - v7*(q*r+1)*L
v45^2 = r*A - v45^2*L
v14^2 = r^3*B - v14^2*((q*r)^2+q*r+1)*L
```

Thus the displayed rows and the localizer give explicit polynomial cofactors
for membership of `v7`, `v45^2`, and `v14^2`.  They do **not** give `q^N`, and
hence do not give a unit certificate.  A radical-only continuation through
rows 6, 8, and 9 suggests `v55=2*v20*q`, `v64=2*v25*q`, and `v6=0`, but the
chain branches at row 10; these radical observations are not recorded as
ideal-membership identities.

Literal pure `q^3` terms occur only in rows 32, 33, 86, 87, and 88, with
coefficients `4,-4,-116,244,-128`.  Each of those rows also has many non-`q`
terms.

## Fixed-weight screen

The script constructs every monomial multiple of every homogeneous base row
of weight 11 through 15 that has total weight 15, excluding the inverse
variable `r`.  This is 5,853 columns and 198,105 input nonzeros.  A deterministic
sparse Gaussian reduction gives rank 2,418 and leaves a nonzero 688-term
remainder for `q^3`, led by `v62*v63`, over each of
`31991,32003,65521,1000003`.

This is a modular screen, not a proof over Q and not a NONUNIT verdict.  Its
proper use is narrower: there is no evidence for a minimal-weight linear
cofactor identity, so a hand-sized or solver-free unit certificate is not a
credible expectation.

Reproduce without a CAS:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 \
  box/k8-b11-q1-20260905/certificate-audit/static_q3_span_audit.py
```

The captured JSON is `static_q3_span_audit.json`; resource use is in
`static_q3_span_audit.time`.

## Search for a reusable q0 certificate

`search_q0_certificate.sh` searched the repository root while pruning `.git`,
`jc2-lean`, every `ideation-*` path, the active lane transcript, and this audit
directory (to avoid self-hits).  It searched case labels, the q0 source SHA
`e9278b6b...c012d`, the q0 body SHA `33e7f3e9...d5a`, and 6,316 paths whose
names suggest Singular/lift/cofactor/certificate material.

The six q0 filename hits resolve to metadata, old formation/solver records,
one retry log, and modular msolve output.  The round-2 metadata records an
msolve characteristic-zero `[1]` (1,257.441 s, 30,043,268 KiB), but the
repository has neither that emitted q0 `.ms`/full `.msout` nor a cofactor
column.  The earlier q0 exact record is a formation timeout; the retained
successful output is a characteristic-32003 `[1]` only.  No certificate-path
file contains the case label or either q0 digest; hashing all 532 retained
`.ms` files (1,608,720,229 bytes) found no file with the recorded q0 source
digest.  The recorded disposition is
therefore:

```text
NO_PREEXISTING_Q0_RATIONAL_COFACTOR_FOUND
```

Even a q0 identity could not be relabelled as q1: q0 has 98 variables and 336
generators, versus q1's 97 and 330, and the localizers differ.  A declared ring
map and generator-image checks would be required.

## One bounded Singular attempt, if time remains

The sound bounded experiment is a direct polynomial-ring `liftstd` on all 330
q1 generators, not an additional msolve deletion search.  The existing syntax
converter preserves variable and generator order and embeds a direct
`matrix(I)*T==1` check:

```bash
python3 box/k7-strata-gate-20260905/cert-audit/make_singular.py \
  box/k8-b11-q1-20260905/input/K8_B11_Q1_p0.ms \
  box/k8-b11-q1-20260905/certificate-audit/K8_B11_Q1_full_lift.sing \
  --lift

/usr/bin/time -v -o K8_B11_Q1_full_lift.time \
  timeout --signal=TERM --kill-after=30s 1800s \
  Singular --no-rc -q K8_B11_Q1_full_lift.sing \
  >K8_B11_Q1_full_lift.out 2>K8_B11_Q1_full_lift.stderr
```

Run it only after both requested msolve jobs have ended and only if at least
about 35 minutes remains for execution, harvest, and worker termination.  A
successful certificate requires all of `CERT__UNIT_CONSTANT 1`,
`CERT__UNIT 1`, `CERT__DIRECT_CHECK 1`, both cofactor delimiters, and 330
indexed cofactor lines.  Custody must include hashes of the source, emitted
`.sing`, Singular binary, stdout, and cofactor output; Singular version,
command, host, start/end time, rc, wall, and peak RSS must also be retained.

This attempt has material risk: the K7 gate's full 275-generator lift was
preempted after 38:49 at about 42.7 GiB even though the corresponding msolve
solve was much faster.  A timeout or partial cofactor stream is no verdict.
The Q(q) localized helper can be faster, but is sound for this chart only if
every coefficient denominator is a scalar times a power of q, a common `q^N`
is cleared, and a fresh polynomial-ring check with `q*r-1` returns literal 1;
an arbitrary denominator in Q[q] cannot be silently inverted.
