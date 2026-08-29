# The frozen q1 proper-divisor D11 survivor dies at D12

Date: 2026-08-28  
Author: Sol Ultra  
Status: **EXACT PROVISIONAL PRODUCER / FIXTURE CLOSED**

## Verdict

The exact rational proper-divisor point which demonstrates that D10/D11 do
not force `A|W` has no legal extension to D12.  Two independent exact
certificates prove this: a characteristic quotient/remainder and a direct
raw-row affine dual functional.  No AWS computation is needed for this
point.

## Characteristic certificate

Keep the frozen `F0,...,F11` and `G0,...,G11`.  In the weight-12 recurrence
for `F^(3/2)`, let

```text
N12 = sum_(i=1)^11 ((5/2)i-12) F_i G_(12-i).
```

The omitted `i=12` term gives only

```text
(3/2) A^2 F12,
```

which is polynomial for every legal `F12`.  The mode born at weight 12 is
`c12*F^0=c12`, also a regular constant.  Thus neither can change the polar
class.

Exact division gives

```text
gcd(N12,A^4)=A B=C B^2,

g12_polar = Nred / (12 C^3 B^2),
gcd(Nred,A)=1.
```

At the `C=X-1` root, `Nred(1)=-12`.  More importantly for the proposed
single-root transport mechanism, the packet contains an explicit Bezout
identity

```text
s(X) Nred(X) + t(X) B(X) = 1.
```

Therefore `Nred` is a unit modulo `B`; since `C` is also a unit modulo `B`,
the `B^2` denominator gives a pole at each of the three B-roots independently
of the separate C-root failure.  For this fixture, every individual root is
already obstructed at D12.

## Independent direct raw-row certificate

The legal new slots are exactly

```text
F12: X^2,X^3,X^4       (3 variables),
G12: X^0,...,X^12      (13 variables).
```

The direct affine row is

```text
D12_base + 12 F12' G0 + 4 F12 G0' - 8 F0 G12'.
```

Across its 28 coefficient rows, the 16-column linear matrix has rank 12,
while the augmented matrix has rank 13.  Its homogeneous nullity four is
exactly compatible with three `F12` directions and the constant `c12`
direction (`G12[X^0]` has a zero column).

The particularly small dual functional

```text
Phi(P)=20 [X^0]P + 10 [X^4]P + 4 [X^8]P + [X^12]P
```

annihilates every one of the 16 legal new columns, while

```text
Phi(D12_base)=11009739/16384 != 0.
```

This is a direct no-extension certificate with no radical, localization, or
normalization step.

## Mutations and provenance

The checker pins the complete predecessor packet and the authoritative
generic raw-slot inventory.  It records the literal weight-12 slot names,
the full numerator/remainder hashes, the Bezout cofactors, the 28-by-16
matrix census, and the base-row hash.

Live mutations verify that:

- an arbitrary legal `F12=X^2+2X^3+3X^4` leaves the polar remainder
  unchanged;
- `c12=5` likewise leaves it unchanged;
- changing the load-bearing dual coefficient 20 to 19 makes the proposed
  functional nonzero on legal new columns.

## Scope firewall

This closes only the one explicit rational D11 prefix.  It does not show
that every proper-divisor prefix dies at D12, does not establish a universal
single-root transport theorem, and does not prove the endpoint branch empty
or settle JC2.  The useful new evidence is that the obstruction can be
strictly local at each B-root, independently of the C-root, in an honest
q1-compatible raw-window computation.

## Replay

```bash
cd cases/ggv_8_28_upper_endpoint_q1_post_d11_d12_obstruction_20260828
python3 -B verify_q1_d12_obstruction.py --check
shasum -a 256 -c SOURCE.sha256
shasum -a 256 -c EVIDENCE.sha256
```
