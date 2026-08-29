# td12 U1 sibling: exact two-direction charge and twin depth-16 gates

Date: 2026-08-29  
Role: Sol 5.6 producer; exact desk arithmetic and theorem-interface pass  
Lifecycle: provisional pending different-model hostile review

## 0. Result

Consider the second P1-fitting first-trunk child of the reviewed `td=12`,
`m=3`, type-`(2,3)` U1 family. Its reduced data are

```text
(nu_F,dp,dq,E,kbar_F,X_F,w_F,M_F)=(17,68,52,36,13,17,3/4,4),
(l,k,Sm,eps,lex)=(2,2,2,0,0),  psi=3.
```

There are two distinct nonzero northeast directions, each of reduced
multiplicity one. Conditional on this reduced cell occurring in an actual
configuration, each direction has exactly one orbit-level critical-value
flag, no characteristic-denominator jump, normalized cv level `17`, and
actual charge exactly `4`. Thus the sibling's two-direction charge is exactly
`4+4=8`, saturating its entire shared budget

```text
sum lambda <= td-1-psi = 12-1-3 = 8.
```

Consequently both direction clusters must remain unchanged-denominator pure
`i`-th powers at normalized levels `1,...,16`. For the displayed direct-entry
family the same arrival count law gives `i=6n`, so each first-child scalar
test is `deg gcd(C_{j,1},C'_{j,1})=6n-1`, for `j=1,2`.

This does **not** kill the sibling. It replaces the proposed sibling-arity
kill by a knife-edge theorem and two simultaneous finite source gates. The
reduced Proposition 8.1(iv) / T1 solve for `(17,68,52)` remains earlier in the
execution order: if that system has no solution, no source-jet work is needed.

## 1. Pinned inputs and exact arithmetic

The reviewed first-trunk primary records exactly two P1-fitting children and
gives this sibling at `nu_F=17`, `k=2`, `(w,M)=(3/4,4)`, floor `8`,
`psi=3`, and budget `8`:

- `xmodel/m2-td12-u1-trunk-consumer-primary-grok46-20260829.md`, especially
  §§6.1 and 8;
- `xmodel/m2-td12-u1-trunk-consumer-hostile-review-opus5-20260829.md`,
  especially §§7.1 and 9.

The sibling fields reconstruct directly from P0. With parent
`(w_G,M_G)=(9/2,2)`, arrival multiplicity `l=2`, two simple extra roots,
and `nu=17`,

```text
s=1+k+lex=3,
dp=nu(l+Sm)=17(2+2)=68,
dq=1+nu*s=52,
E=l*dq-dp=36,
kbar=2*(9/2)*52/36=13,
X=kbar*dp/dq=17,
w_F=2*(9/2)*3/36=3/4,
M_F=gcd(68,52)=4.
```

Both extras have `m_j=1`; `eps=0` excludes a free zero direction. For a
full sheet index `i=i_F`, each extra direction therefore has full
multiplicity `i` and

```text
D_F/i=X_F=17,       delta_j=X_F/m_j-kbar_F=17-13=4.
```

The direct-entry relation used for the sibling has the same arrival
multiplicity `2` as the reviewed `nu=25` child. Hence
`2i=(6n)i_G`, `i_G=2`, and `i=6n`. The exact-charge proof below needs only
`i>0`; `i=6n` is used only in the displayed gcd degree.

The other budget terms are already reviewed: the U1 merge has charge zero,
and all three actual pole vertices have empty cv exit sets and price zero.
P1 at `w=3/4,M=4` has `j=M(1-w)=1` and `psi=3`, so Corollary 7.1 gives the
shared ceiling eight.

## 2. One direction costs at least four

Fix either extra direction. The positive gap `17-13=4` types it as an up
child. Proposition 6.6 plus the repaired Section-7 statements give every
physical place through that child a same-ray cv flag. Corrected Statement
9.3 gives every distinct such flag `H`

```text
wt(H)=kappa_H(pi(H)-1) >= D_F/i-kbar_F = 4.
```

This is a statement about the full actual flag set. It does not claim that a
selected MFE subset exhausts Puiseux series or places, and it never identifies
a physical flag with a conjugate Puiseux series.

The two reduced extra roots are distinct direction-orbits. Their cv flags are
therefore distinct Corollary-7.1 summands. Selecting one flag from each gives
total weight at least `4+4=8`.

## 3. Budget saturation forces one unramified flag per direction

Write

```text
q_H=kappa_H/kappa_F in N*,
tau_0(H)=kappa_F(pi(H)-pi(F)).
```

For a flag in either multiplicity-`i` direction, the exact descent law gives

```text
tau_0 >= D_F/i=17,
wt(H)=q_H(tau_0-13).
```

Now use the other direction's mandatory weight-four flag.

- If some flag in the chosen direction has `q_H>=2`, it alone costs at least
  `2(17-13)=8`; adding the other direction gives at least `12>8`.
- If the chosen direction produces two distinct place/direction-orbit flags,
  they cost at least `4+4`; adding the other direction again gives at least
  `12>8`.

Thus each direction has one flag and `q=1`. The strict type distinction is
load-bearing: `q=1` excludes conjugate shedding, while uniqueness of the full
actual flag excludes a distinct-place split strictly below the cv level.
Hence the full Puiseux-series count in that direction stays `N(tau)=i` for
`0<tau<tau_0`. The exact area identity now gives

```text
17i=D_F=integral_0^tau0 i dtau=i*tau_0,
```

so `tau_0=17`, and the unique flag has exact weight
`1*(17-13)=4`. Applying this independently to both directions proves total
charge exactly eight.

At the endpoint, a distinct-place/direction-orbit split may occur at level
`17` because the places can share the endpoint flag. Conjugate shedding there
would still force `q>=2` and overrun the saturated budget, so it is excluded.

## 4. Twin finite source gates

For direction `j in {1,2}`, let `C_{j,r}(z)` be the normalized degree-`i`
child polynomial at integer level `r` after the standard recentering. No loss
of series and no denominator jump before level `17` force

```text
C_{j,r}(z)=a_{j,r}(z-b_{j,r})^i,  a_{j,r}!=0,
for r=1,...,16.
```

Equivalently, at each level either the binomial identities hold or

```text
deg gcd(C_{j,r}, dC_{j,r}/dz)=i-1.
```

For direct entries this degree is `6n-1`. A failure in either direction at
any of the 32 direction-level tests kills this sibling. Passing all of them is
only necessary formal source compatibility; it neither supplies the coupled
Keller recurrence nor constructs a germ or polynomial pair.

The smallest execution order is:

1. solve the still-open reduced T1 system on the sibling cell
   `(nu,dp,dq)=(17,68,52)` with its two extra roots;
2. if T1 is alive, extract both first-child coefficient vectors from the
   exact source/Keller identities;
3. run the two level-one gcd/binomial tests;
4. recurse only on a passing direction, stopping at the first failure or
   after level `16`.

## 5. Scope and negative control

This theorem is conditional on the reviewed reduced sibling cell and on its
occurrence in an actual configuration. It proves no T1 existence, source
realization, full-book exclusion, landing, `G2-PSC`, `G2-BD`, degree ceiling,
counterexample, or JC2 consequence.

Negative control: replacing either integral defect `4` by a nonintegral
defect must not be priced by the numerator of that fraction. Integrality is
imposed on `q(tau_0-kbar)`, not on `q*delta` at the lower bound. This report
uses only the integral case, where budget saturation forces the exact value.

*End of sealed report body.*

---

Report-body bytes: `6907` (all bytes before the separator above).  
Report-body SHA-256:
`306d69f61eb4b9345bcc2bb09dde41411c8762be5203be905eecb108415bba02`.

Verify the full file with:

```sh
shasum -a 256 xmodel/m2-td12-u1-sibling-exact-charge-r1-sol56-20260829.md
```
