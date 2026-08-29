# Cap-free incoming-index bound at every two-pole case-III merge

Date: 2026-08-29 UTC. Producer: Sol Ultra integration lane. Lifecycle:
`PROVISIONAL / DIFFERENT-MODEL REVIEW REQUIRED`.

## Result

Conditional on the literal case-II/case-III handshakes and merge pattern in
`ladder/BOOK-OFFAXIS.md` R2.1--R2.2, the incoming zero-edge index
`h=nu_H` at a two-pole case-III merge has an explicit finite bound. This
closes the mathematical reason for the old `NUCAP=500` fallback in the
`mu0>mu>=2` branch of `cases/book_offaxis.py:solve_arr`; the production
engine is not changed pending hostile review.

This index is not the merge-local pattern index `nu_G`. Opus5's provisional
Theorem 2.4/4 argument in
`xmodel/m2-budget-quotient-primary-research-opus5-20260829.md` correctly
bounds the `nu` that occurs in

```text
dp = eps + nu*P,  dq = 1 + nu*s,
```

namely `nu_G`. Its later prose identifies that symbol with the incoming
case-III `nu_H`; that identification is not licensed. The theorem below
supplies the missing incoming-index bound directly.

## Theorem

Let one nonzero edge arrive with multiplicity `mu>=1` and invariant `w>0`.
Let the zero-direction edge arrive with multiplicity `mu0>=1`, invariant
`w0>0`, and incoming index `h`. Write the two-pole merge pattern as

```text
dp = mu0 + n*(mu + Sm),
dq = 1 + n*(1 + k + lex),
Sm = sum_j m_j,
```

where `n=nu_G`, the `k` nonchain p-orbits have positive multiplicities
`m_j`, and `lex` counts q-only extra orbits. Then:

1. If `mu0<mu`, positivity of `kbar` gives

   ```text
   h < mu*w/(mu0*w0).
   ```

2. If `mu0=mu`, the two handshakes force

   ```text
   h*w0 = w,
   ```

   so there is at most one integral `h`.

3. If `mu0>mu`, put `delta=mu0-mu`. Then

   ```text
   kbar <= mu*w*(2*delta+3),
   h <= mu*w*(delta*(2*delta+3)+1)/(mu0*w0).
   ```

All bounds are rational-exact and require no numerical search cap.

## Proof of the difficult regime

Assume `delta=mu0-mu>0`. The nonzero arriving edge is searrow, so

```text
D := mu*dq-dp > 0.
```

Every nonchain p-root is strictly northeast:
`m_j*dq < dp < mu*dq`. Hence each `m_j<=mu-1`. With

```text
s := k+lex,
A := mu*s-Sm,
```

we have `A>=k+mu*lex>=s`. Also `s>=1`, since `s=0` would give
`D=-delta`. Direct substitution gives

```text
D = n*A-delta,
dq = 1+n*(1+s).
```

The elementary uniform estimate is

```text
dq/D <= 2*delta+3.
```

Indeed, if `n*s<=delta`, then `n<=delta` and
`dq<=1+2*delta`, while `D>=1`. If `n*s>=delta+1`, then

```text
dq/D <= (1+n+n*s)/(n*s-delta)
       <= (1+2*n*s)/(n*s-delta)
       <= 2*delta+3.
```

The nonzero-edge handshake and ratio equation are

```text
X = mu*(kbar-w),       X/kbar = dp/dq.
```

Therefore

```text
kbar = mu*w*dq/D <= mu*w*(2*delta+3).
```

Eliminating `X` between that handshake and the case-III zero-edge handshake
`X=mu0*(kbar-h*w0)` gives

```text
mu0*h*w0 = delta*kbar + mu*w,
```

which yields the displayed `h` bound. For `mu0<mu`, the same identity and
`kbar>0` give the strict bound in item 1. For `mu0=mu`, compare the two
handshakes directly to obtain item 2.

The constant is sharp at this level: `delta=1`, `n=2`, one nonchain orbit
of multiplicity `mu-1`, and `lex=0` gives `dq/D=5=2*delta+3`.

## Charged discriminator

For the known td-7 neutral ray

```text
(mu,w)=(1,2),  (mu0,w0)=(2,3/2),  h odd and h>=3,
```

the theorem gives `kbar<=10` and `h<=4`. Thus only `h=3` remains. Its exact
pattern has `n=3,k=0,lex=1` and

```text
(dp,dq,D,kbar,X,h) = (5,7,2,7,5,3),
M=gcd(5,7)=1,
```

so MP2 kills it. Every odd `h>=5`, including the old S5 discriminator, is
excluded before a cell solve. This recovers the narrower special-ray result
by a general two-pole theorem.

## Exact packet and tests

Packet: `cases/m2_caseiii_two_pole_nuh_bound_r1_20260829/`.

```text
fdefd72969523a5ff3bfe333693a32a9ce859c90f4427f2c74fdeb7feb6e435f  caseiii_two_pole_bound_r1.py
3b3dd42e0f1d3767244a175f74e1eaf8aa91d9f496898a92b6f6be6491f4579b  test_caseiii_two_pole_bound_r1.py
d986025364de51e5b6396e5b1ddd5dd7940698a427d5a4d26baa8491ea5e0689  README.md
12a3f6b7fedfc5d6e9b40edebf53c453482829c019248c37d8ca8c85f95fb037  charged JSON output
```

Ordinary and optimized tests each pass 130,095 checks. They exhaust the
degree-gap lemma over small `mu,delta,n,k,lex` boxes and every allowed
multiplicity tuple, verify the sharpness fixture, scan rational handshake
grids, reproduce the charged `(5,7)` cell, reject invalid inputs, and compare
the optimized certificate byte-semantically. No Singular or other CAS ran.

## Consequence and remaining wall

Once differently reviewed, the theorem can replace the `NUCAP=500` fallback
for every two-pole case-III arrangement, including the previously OPEN
`mu0>mu>=2` branch. Together with the separately provisional finite reduced
P0-chain skeleton, it makes every two-pole case-III consumer finite at fixed
budget.

It does not bound the equal-`(mu,w)` nonzero-arrival case-I/II join, where
`kbar` can remain affine and unbounded; does not handle multipole or inner
merge trees; and does not certify the legacy `cell_check` grammar. Those are
the next M2 quotient obligations.

## Scope firewall

This is a conditional merge-arithmetic theorem. It proves no source landing,
full configuration cover, cofinal topological-degree bound, realizability,
Keller counterexample, or JC2 result.

---
Report-body SHA-256 (bytes before the separator line above): `8a16cad9cc3211f90e86b1cc31a3fe2991f3817138ae9da4f6dbc56ddf7b5c43`
