# Max12 `(9,12)` Q8 leaf-4 local quotient and terminal descent

Date: 2026-08-24  
Status: **producer-exact; hostile different-model review required**

## 1. Exact scope and inputs

The corrected Q8 seven-row formal-branch theorem and the root-free
critical-value norm are different-model reviewed.  This report consumes
those reviewed statements and the separately frozen Q8 normalization/Taylor/
terminal jet.  The latter jet is still producer-tier; consequently every new
coefficient claim here remains producer-tier pending a fresh hostile review.

No quarantined Q12 artifact is used.  The conclusion is formal-local at the
eight Q8 contacts.  It neither computes a global leaf-4 quotient curve nor
constructs or excludes a rational Keller trajectory.

## 2. Kummer-fixed quotient coordinates

On the loaded chart `p!=0`, use the corrected second branch parameter
`t=a0`.  The integer weights are

```text
wt(a0)=9,        wt(p)=2,        wt(r8)=20.
```

Hence the following expressions have order-three Kummer character zero and
belong to `K=C(x)` along any actual order-three trajectory:

```text
theta = a0^2/p^9,
pi    = p^9,
q     = r8/p^10,
S     = r8^9 = pi^10*q^9.                             (2.1)
```

They also avoid a ninth or tenth root.  In the `p=1` local normalization,

```text
theta=t^2+O(t^4).                                      (2.2)
```

The identity for `S` in (2.1) is algebraic and holds off parity.  In
particular, it does not replace `pi` by a parity-only formula.

## 3. Mandatory parity-formula negative control

On the parity chart only, the reviewed genus-five calculation has

```text
r6=p^9*R6(v).
```

That expression is not an equation of the non-parity branch.  Reconstructing
the corrected jet and extending the invariant rational coordinate `v` gives

```text
p^9*R6(v)-nu = c*t^2+O(t^4),          c in E^*.        (3.1)
```

The replay Euclidean-certifies `gcd(c,Q8)=1` and an inverse modulo `Q8`.
Thus the tempting substitution `pi=nu/R6(v)` fails at the first nontrivial
order, uniformly over all Q8 conjugates.  No formula below uses it.  Away
from parity, `pi=p^9` is retained as its own invariant coordinate.

## 4. Root-free Hurwitz coordinates are etale

At the two roots of the Wronskian quadratic, let the critical values be
`beta_+` and `beta_-`.  Without choosing either root, the reviewed norm gives

```text
tau   = beta_+ + beta_-
      = 2*(G0*F0-s*G1*F1)/Norm(F),

Delta = (beta_+-beta_-)^2
      = 4*s*E^2/Norm(F)^2.                             (4.1)
```

Both have weight zero and descend to `K`.  Exact series substitution gives

```text
Delta = D1*theta+O(theta^2),
tau   = tau0+T1*theta+O(theta^2),
q     = q0+Q1*theta+O(theta^2),
S     = S0+S1*theta+O(theta^2),                         (4.2)
```

where all of

```text
D1, T1, Q1, S0, S1, and S1/D1
```

are units in `E=Q[v]/(Q8)`.  The replay records each residue and a Euclidean
inverse.  In particular:

```text
sha256(D1)=2c651a6265e650c5d72f409a46bb6fe3c572e2c51518ae9794f3b9b06dc9209e,
sha256(T1)=2011e1ea82ba014d14037329b91f2571f99199215d30314156c6d625614000fe,
sha256(Q1)=87b80678a4a92f8e768bc4cd4f118a425bc797cef61f720392e0ae8a716590cc,
sha256(S1)=30caa5eebba929de017fa52461483c602e14800541c1a308357186f70df4a2a3,
sha256(S1/D1)=386a59430805c0e74525cd485750c7267761ceef04153848e28b57002b297c15.
```

Thus `Delta` is an etale local coordinate on the parity-involution quotient
of the second branch.  The tail invariant `S`, the second symmetric Hurwitz
coordinate `tau`, and `q` are equally valid local coordinates.  This is the
precise sense in which the generic leaf-4 motion descends without selecting
a critical root.

## 5. Exact terminal descent

Retain the original terminal row and Kummer descent

```text
9*r8'=j/u,        r8=u^2*R,        u^3=h,
j in C^*,         R in K.                                  (5.1)
```

For `S=r8^9 in K`, differentiation gives

```text
S'=9*r8^8*r8'=j*r8^8/u=j*h^5*R^8.                    (5.2)
```

Raising (5.2) to the ninth power and using `S=h^6*R^9` yields the completely
root-free necessary differential identity

```text
h^3*(S')^9=j^9*S^8.                                   (5.3)
```

Every exponent in (5.2)--(5.3) is checked in the replay.  Since
`dS/dDelta` is a unit at each Q8 contact, (5.3) is locally a differential
equation in the unordered Hurwitz coordinate `Delta`.  Equation (5.3) is a
necessary consequence of (5.1), not a converse reconstruction of `r8`.

## 6. Taylor status and remaining global gate

The frozen predecessor reconstructs the complete original Taylor families
at the true center `r=A/9`:

```text
[y^ell]P=u^ell*f^(ell)(r)/ell!,
[y^ell]Q=u^ell*g^(ell)(r)/ell!.
```

Writing `r=u*R0`, these expressions descend coefficientwise, but the
high-row fibre does not determine the rational center `R0`.  Therefore the
Taylor families do not by themselves yield a formal-local leaf-4
contradiction.  Their polynomiality remains charged for the global
normalization.

The smallest remaining gate is the algebraic relation among `Delta`, `tau`,
`S`, and the descended Taylor center on the global leaf-4 quotient, followed
by its projective boundary/genus and (5.3).  Nothing here excludes the
punctured branch, a disjoint component, all `(9,12)`, maximum twelve, a
counterexample, or JC2.

## 7. Replay

```sh
shasum -a 256 -c cases/max12_912_order3_nu_q8_leaf4_descent_jet_20260824/MANIFEST.sha256
python3 cases/max12_912_order3_nu_q8_leaf4_descent_jet_20260824/replay.py \
  | diff -u cases/max12_912_order3_nu_q8_leaf4_descent_jet_20260824/replay.json -
```

The replay uses only the Python standard library, pins every frozen parent
byte, reconstructs the corrected jet from the original seven rows, verifies
the parity-formula failure at order `t^2`, and records unit inverses for all
four local quotient coordinates and for `dS/dDelta`.
