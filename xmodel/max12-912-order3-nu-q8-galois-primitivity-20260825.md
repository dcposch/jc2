# Max12 `(9,12)` selected-Q8 Galois-primitivity reducer

Date: 2026-08-25  
Status: **producer-exact; hostile different-model review required**

## 1. Result and scope

The Galois action on the eight roots of the corrected octic

```text
Q8(v)=-999v^8-1539v^7+1782v^6+6498v^5+7320v^4
      +4428v^3+1548v^2+296v+24
```

is primitive.  Consequently, grouping the eight selected non-parity Q8
contacts by geometric irreducible component has only two possible forms:

```text
one component containing all eight contacts, or
eight conjugate components containing one contact each.               (1.1)
```

In particular the intermediate partitions `4+4` and `2+2+2+2` cannot
occur.  This is an exact group-theoretic reduction; it does **not** decide
which alternative in (1.1) occurs.

Combined conditionally with the separately frozen selected-Q8
infinity-contact theorem, the first alternative cannot carry an actual
trajectory: a single source point `infinity_x` cannot map to eight distinct
points of the target normalization.  The singleton alternative remains
fully open, as do coefficient-fibre/Taylor realization and all components
disjoint from the Q8 boundary.

## 2. Exact Frobenius certificates

Multiply `Q8` by `-1` to obtain the primitive integer polynomial with
low-to-high coefficient vector

```text
[-24,-296,-1548,-4428,-7320,-6498,-1782,1539,999].     (2.1)
```

Its integer content is one.  The AWS replay applies the Rabin
irreducibility criterion using exact polynomial arithmetic over finite
fields.

At `p=7`, the monic reduction is

```text
5 + v + 4v^2 + 2v^3 + 6v^4 + v^5 + 2v^6 + 4v^7 + v^8.
```

It satisfies

```text
gcd(Q8_bar, v^(7^4)-v)=1,
v^(7^8)-v == 0 mod Q8_bar.                              (2.2)
```

Thus the reduction is irreducible of degree eight.  Hence `Q8` is
irreducible over `Q`, its Galois action is transitive, and a Frobenius
element has cycle type `[8]`.

At `p=53`, the monic reduction has exactly the linear root `v=13` and the
degree-seven quotient

```text
12 + 47v + 3v^2 + 29v^3 + 46v^4 + 44v^5 + 26v^6 + v^7.
```

For that quotient the replay verifies

```text
gcd(F7, v^53-v)=1,
v^(53^7)-v == 0 mod F7.                                (2.3)
```

Thus `F7` is irreducible and the squarefree factorization pattern is
`[1,7]`.  Dedekind's theorem supplies a seven-cycle in the Galois group.

## 3. Why the action is primitive

A nontrivial block in a transitive action of degree eight has size two or
four.  A group preserving such a block system embeds respectively into

```text
S2 wr S4, of order 2^4*4! = 384,
S4 wr S2, of order (4!)^2*2 = 1152.                    (3.1)
```

Neither order is divisible by seven, so neither group contains a
seven-cycle.  The Galois action therefore preserves no nontrivial block
system and is primitive.

The reviewed corrected-Q8 formal theorem gives each Q8 coefficient point a
unique selected non-parity local branch, in addition to the parity branch.
Two contacts lie on the same selected geometric irreducible component iff
their unique non-parity branches do.  This equivalence relation is preserved
by Galois and hence its classes form a block system on the eight roots.
Primitivity proves (1.1).  Components disjoint from all Q8 contacts are not
classified.

## 4. Conditional trajectory consequence

The separately frozen infinity-contact successor says that if an actual
loaded order-three trajectory has nonconstant quotient image in a selected
Q8 component, every Q8 point of that component must be met from the sole
source point `infinity_x`.  Distinct Q8 coefficient points remain distinct
on the normalization.  Therefore a selected component containing two or
more Q8 contacts cannot carry such a trajectory.

With (1.1), this kills the entire eight-contact alternative at the exact
scope of that predecessor.  It does not kill the eight singleton components:
each could in principle use its one allowed contact at infinity.  No
trajectory, all-`(9,12)`, maximum-twelve, counterexample, or JC2 conclusion
is asserted here.

## 5. AWS provenance and replay

The bounded exact replay ran on AWS r6d host `ip-172-30-0-45`, tag
`q8_galois_primitivity_v2`, at `2026-08-25T01:04:58Z`.  It exited `0` in the
same UTC second.  The pinned hashes are

```text
replay.py       ad3e9383c98ddec1ac0d146da45af7ee08a895ef68f355a5c26ef0c7bff7e0ab
run_remote.sh   17579fed2d665ce496dd44051c4b5c17f8da8500fac32e7ba326d65c08a80f38
replay.json     f5b37f95d3966257517c67162469469a03d2d861a09af0ccf2701b82f642b0a2
stderr.log      e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
```

No substantive computation was run locally.  To reproduce on an allowed
remote worker:

```sh
python3 cases/max12_912_order3_nu_q8_galois_primitivity_aws_20260825/replay.py \
  | diff -u \
      cases/max12_912_order3_nu_q8_galois_primitivity_aws_20260825/replay.json -
shasum -a 256 -c \
  cases/max12_912_order3_nu_q8_galois_primitivity_aws_20260825/MANIFEST.sha256
```

