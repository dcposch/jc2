# Source audit — Sigray Propositions 6.7 and 6.8

Date: 2026-08-28  
Lane: Sol Ultra, independent exact desk audit  
Source: `refs/sigray_full.pdf`, printed pp. 33--34 (the proof of Proposition
6.8 continues on PDF page 35 under the printed page-34 header)

## Terminal verdict

**REPAIR.**  Both propositions are mathematically correct, but neither printed
proof is sound as written.

- Proposition 6.7 uses Statement 3.9 with the derived polynomial `h=h_F`
  although its `kappa` is certified only for `f` and `g`.  This is exactly the
  auxiliary-`h` denominator defect exposed by the reviewed Statement 3.9
  ablation.  Its root-selection sentence also omits the reason that the
  inequality survives the root-of-unity rotation supplied by Statement 3.18.
  Both defects have short exact repairs: use corrected Statement 3.11 instead
  of exact Statement 3.9 for `h_F`, and insert the cyclic semi-invariance lemma
  for every residual polynomial `p_(h,F)` at a vertex.
- Proposition 6.8 depends on repaired Proposition 6.7 and prints the wrong
  termination bound

  ```text
  d_(F_n) <= u-n/kappa.
  ```

  The correct induction is

  ```text
  d_(F_n) <= d_F-n/kappa.
  ```

  With that replacement, the recursion terminates and its terminal pole is on
  one branch whose truncation at depth `u` is the original `F`.

No theorem conclusion or present campaign consumer needs to be rolled back.
The blast radius is documentary but broader than the existing Statement 6.2
consumer sweep records: Proposition 6.7 controls a one-grid-step child
`F*_(kappa)c`, not the next vertex denoted `F+c`.  Transport to that vertex
uses Proposition 6.8.  Thus every Statement 6.2 regularity consumer depends on
repaired Proposition 6.8 as well as repaired Proposition 6.7.

## 1. Custody and repaired dependencies

Live SHA-256 values at the start of this audit were:

```text
9bf9f0320497dd8d5da6d7fe68ec900c1879663e6f11c121853482ca7e1623ae  refs/sigray_full.pdf
5ef83d36484315d7a6798c048a270ac16464c2ef5c63d20a842b4b1339989e9d  ladder/SIGRAY-AUDIT.md
10bc55d53f9cf9a9e6a4535787f6e208a25f0ebfbd6dbd803f68b00f8ca8f5cd  xmodel/sigray-prop42-constant-shift-repair-sol-ultra-20260828.md
47f2b608f47bc7f426c6cf3e8634c8704bdd675aa909eb63e3f4c6861c21dfb1  xmodel/sigray-prop42-constant-shift-repair-hostile-review-opus5-20260828-r1.md
882485d623e9fc21ba0d52c1eea1f86c2902ff1e4e64d5543f86398a0afbac12  xmodel/ideation-20260828T1149Z-opus5.md
ca63eb5e75a1d67ac02c2f643aff82b14af3d94a35e26d78e6de523604348e18  xmodel/sigray-no-first-constant-corner-hostile-review-sol-ultra-20260828.md
d64b043c2d863cd5d844d42453f4c85d49b4716ef55eb2dfbd9e4135f0311c06  xmodel/sigray-st62-consumer-sweep-sol-ultra-20260828.md
```

The following corrected inputs are used and remain explicit hypotheses of the
repair.

1. The corrected Proposition 4.2 permits one terminal `(1,0,c)` corner, but a
   corner can occur only in `T_a^nearrow`, never in `T_a^searrow`.
2. The reviewed no-first-corner theorem says `(g-b)_F^+` is not a nonzero
   scalar for every `F in T_a^+` and every `b in C`.
3. Statement 3.9 is exact only when `kappa` has Proposition 3.1's pole-order
   property for the particular auxiliary polynomial.  Corrected Statement
   3.11 supplies denominator-independent inequalities.
4. Statement 3.18 must be read in its corrected form: for a nonzero root `c`
   the existing child is `F*(epsilon*c)` for a unique `nu_F`-th root of unity
   `epsilon`.
5. Proposition 5.1 uses the repaired, puncture-dependent centre.  Its finite
   thresholds lie in `T_a^-`; its pole thresholds lie in `T_a^+`.
6. The known Proposition 5.3(ii)/(viii) ratio is read in its corrected
   direction.  Only its integrality, simplicity and pole-prefix consequences
   are used below.

The source's `%` and `&` glyphs are respectively `nearrow` and `searrow`.

## 2. Proposition 6.7: exact repaired statement

Let `F in T_a^searrow`, `u=pi(F)`, and let `kappa` be common-suitable for
`f,g`, with `kappa*u in N`.  Assume `deg p_F>1`.  Then:

1. every defined one-step child `F*_(kappa)c` lies in `T_a^+`; and
2. some defined one-step child lies in `T_a^searrow`.

The added lattice hypothesis is required for typing: Notation 3.8 defines
`F*c` only after `kappa*pi(F) in N`.  The first clause is otherwise vacuous
when no child is defined, while the printed second clause asserts existence.
Proposition 6.8 already supplies this missing hypothesis explicitly.

Write

```text
d=d_F,       p=p_F,
e=d_(h,F),   q=p_(h,F),       h=h_F,
G=F*c,       m=mult(p,c).
```

Since `G` exists, `c` is a root of `p`, so `m>=1`.  Statement 3.9 is licensed
for `f` and gives

```text
deg p_G=m,              d_G=d-m/kappa.                 (2.1)
```

### 2.1 Every child is positive: the `h=g` branch

Here the Proposition 4.2 tower has length zero.  The assertion in the printed
proof that `F` is a pole vertex remains true, but after the Proposition 5.1
repair it needs one extra sentence.

Choose a puncture `P` representing `F` and put `b_P=g(P)` when finite.  If
`b_P` were finite, the nonzero leading Jacobian for `g` would also be the
nonzero leading Jacobian for `g-b_P`: a scalar leading part cannot be the
cause, by the reviewed no-first-corner theorem.  The repaired Proposition 5.1
would then identify `F` with the finite-puncture threshold, which lies in
`T_a^-`, contrary to `F in T_a^searrow subset T_a^+`.  Thus `P` is a `g`-pole.
Let its pole threshold be `F_P^*=I_P(v)`, with `v<=u`.  Proposition 5.3(v),
Statement 3.9 for `f`, and monotonicity say that every strict descendant
`I_P(w)`, `w>v`, has residual degree at most one.  Since the present
hypothesis is `deg p_F>1`, necessarily `u=v`; hence
`F=F_P^* in T_(a,pole)`.

Proposition 5.3(v) makes `m=1`, hence `d_G=d-1/kappa`.  If `kappa*d=1`, the
corrected pole ratio gives

```text
kappa*d_(g,F)=beta/alpha,
```

which is not an integer because `alpha,beta` are coprime and `alpha>=2`.
This contradicts Statement 3.8 integrality (a common-suitable `kappa` is a
multiple of the intrinsic denominator).  Thus `kappa*d>=2`, and `d_G>0`.

### 2.2 Every child is positive: the `h!=g` branch

The tower is nonempty.  Its first relation has positive exponents because a
first constant corner is excluded:

```text
(g_F^+)^r = s*(f_F^+)^t,       r,t in N*.             (2.2)
```

Only `f` and `g` occur here, so Statement 3.9 is licensed.  Applying it to
(2.2) across `F -> G` gives

```text
d_(g,G)=(t/r)*d_G
```

and both `p_G` and `p_(g,G)` have positive degree.  Since `F` is searrow,
`u<1`; integrality gives `u<=1-1/kappa`, so `1-pi(G)>=0`.  Condition (7) at
`G` holds because `p_(g,G)` is nonconstant.  Proposition 4.1 gives

```text
(1+t/r)*d_G >= 1-pi(G) >= 0.                           (2.3)
```

Thus `d_G>=0`.  If `d_G=0`, both sides of (2.3) force `pi(G)=1`, and the
equality branch of Proposition 4.1 says the leading Jacobian is a nonzero
multiple of `xi^-1`.  Equation (2.2) makes the same leading Jacobian zero, a
contradiction.  Hence `d_G>0`.

This checks the source's terse `d_G!=0` argument and makes its missing
condition-(7) licence explicit.

## 3. Proposition 6.7: existence of a searrow child

### 3.1 A strict root exists

Proposition 6.4 and `F in T_a^searrow` give

```text
deg q <= (e/d)*deg p.                                  (3.1)
```

Here `e>0`.  Indeed (3.1) gives `e>=0`; if `e=0`, then `q` is constant and
the terminal bracket `d*p*q'-e*p'*q` is zero, contradicting the defining
terminal identity for `h_F`.

There is a root `c` of `p` such that

```text
n:=mult(q,c) < (e/d)*m,      m:=mult(p,c).             (3.2)
```

Otherwise, summing the reverse inequalities over all roots of `p` and using
(3.1) forces equality everywhere, no `q`-roots away from the `p`-roots, and
proportional root divisors.  After clearing the denominators of `d,e`, this
gives `q^(D*d)=C*p^(D*e)`, hence `d*p*q'-e*p'*q=0`, again contradicting
terminality.  This is the complete counting argument hidden in the printed
sentence `p^(d_h)!=q^(d_F)`.

### 3.2 Root-of-unity rotation is harmless, but not for the printed reason

If `c=0`, corrected Statement 3.18 directly supplies `F*0`.  If `p` has only
one distinct root, the next coefficient of any branch representing `F` must
be that root, so a child exists directly.

Suppose `p` has more than one root.  Statement 3.16 makes `F` a vertex and
writes `p(eta)=eta^j*p_0(eta^nu)`, where `nu=nu_F`.  Corrected Statement 3.18
may replace a nonzero `c` by `epsilon*c`, with `epsilon^nu=1`, before the
child exists.  Statement 3.16 by itself preserves `mult(p,c)` under this
rotation, but says nothing printed about `q=p_(h_F,F)`.  The source therefore
omits a needed line.

The missing line is true for every auxiliary polynomial `H`:

> **Cyclic residual lemma.**  At a vertex `F`, the leading residual polynomial
> `p_(H,F)` is semi-invariant under the cyclic stabilizer of the truncated
> Puiseux prefix.  Thus
> `p_(H,F)(epsilon*eta)=chi(epsilon)*p_(H,F)(eta)` for a character `chi`, and
> the multiplicity of every nonzero root is constant on its `mu_nu` orbit.

To prove it, pass to a common tame parameter `t` with `x=t^-kappa`.  The
stabilizer of the prefix acts by `t -> zeta*t` and on the residual coordinate
by `eta -> epsilon*eta`.  Since `H(x,y)` is invariant and its top `t`-order is
one character, comparison of that top coefficient gives the displayed
semi-invariance.  Enlarging `kappa` does not change the intrinsic residual or
its root multiplicities.  This is the standard deck-equivariance behind
Statement 3.16, now applied to the arbitrary polynomial `H=h_F`.

Consequently (3.2) survives the unique rotation selected by Statement 3.18.
Rename that realizable root `c`.

### 3.3 Statement 3.11 repairs the illegal Statement 3.9 step

The printed proof next uses exact Statement 3.9 on `h=h_F`.  This is illegal:
`kappa` was required to be suitable only for `f,g`, and the exact ablation
example in `882485d6...` shows that a derived polynomial can have new pole
denominators.

No enlargement or subdivision argument is needed.  Put

```text
r=deg p_(h,G),       e_G=d_(h,G).
```

Corrected Statement 3.11 gives the denominator-independent bounds

```text
r <= n,              e_G >= e-n/kappa.               (3.3)
```

Together with (2.1) and (3.2),

```text
m*(e-n/kappa)-n*(d-m/kappa)=m*e-n*d>0,                (3.4)
```

so

```text
e_G/d_G > n/m >= r/m = deg p_(h,G)/deg p_G.           (3.5)
```

In the source's route, (13) fails by (3.2), hence (14) holds; Proposition 6.3
identifies the terminal member at `G` with `h`, and Proposition 6.4 then turns
(3.5) into `G in T_a^searrow`.  Equivalently, one can avoid the last citation:
if `h` were nonterminal at `G`, the zero-bracket trichotomy with
`d_G,e_G>0` would force equality of the two order/degree ratios in (3.5), a
contradiction.  Hence `h=h_G`, and Proposition 6.4 applies.

This proves the existence clause without ever applying exact Statement 3.9
to the derived polynomial.

## 4. Proposition 6.8: repaired recursion

Let `F in T_a^searrow`, `u=pi(F)`, and `deg p_F!=1`.  Choose `kappa`
common-suitable for `f,g` with `kappa*u in N`.  Since every positive-tree
fiber residual is nonconstant, `deg p_F>=1`; the hypothesis therefore means
`deg p_F>1`.

Set `F_0=F`.  If `F_n` is a pole, stop.  Otherwise:

1. `F_n` cannot have `deg p_(F_n)=1`.  Lemma 6.1 would give `m_(F_n)=0`, so
   the repaired `h=g` argument of Section 2.1 identifies the unique threshold
   on its representing branch as a pole at a `kappa`-grid depth no later than
   `F_n`.  Proposition 5.3(iv),(v) and Statement 3.9 for `f,g` then put that
   pole at some already visited `F_j`, `j<n`, contradicting the stopping rule.
2. Hence `deg p_(F_n)>1`, and repaired Proposition 6.7 supplies `c_n` with

   ```text
   F_(n+1)=F_n*c_n in T_a^searrow.                    (4.1)
   ```

   The PDF prints `F*c_n`; this is a harmless subscript typo.

For termination, let `m_n=mult(p_(F_n),c_n)>=1`.  Exact Statement 3.9 for the
fixed fiber polynomial `f` is licensed and gives

```text
d_(F_(n+1))=d_(F_n)-m_n/kappa <= d_(F_n)-1/kappa.
```

Therefore

```text
d_(F_n) <= d_F-n/kappa,                               (4.2)
```

not the printed `u-n/kappa`.  Every `F_n` lies in `T_a^searrow subset T_a^+`,
so `d_(F_n)>0`; (4.2) bounds `n<kappa*d_F`.  The recursion is finite and can
stop only at a pole.

Finally, let `F_N=I_P(v)` be the terminal pole, with
`v=u+N/kappa`.  Statement 3.5 says `(F_(j+1))^0=F_j`.  Reading ancestors of
the single final branch `P` gives

```text
F_j=I_P(u+j/kappa)       for every 0<=j<=N,
```

and in particular `F=I_P(u)`.  Thus the pole is genuinely on the same branch,
not merely somewhere above the same equivalence class.

## 5. Microstep versus next vertex: the Statement 6.2 bridge

There are two different operations in the source:

- `G*_(kappa)c` is the one-grid-step point at depth `pi(G)+1/kappa`
  (Notation 3.8);
- `H=G+c` labels the next **vertex** in direction `c` (Proposition 3.2).

They need not be the same point.  Therefore Proposition 6.7's first clause,
by itself, does **not** establish the missing `H in T_a^+` hypothesis in the
repaired last clause of Statement 6.2.  The earlier consumer sweep conflates
these two meanings.

The desired vertex statement is nevertheless true after composing the two
repaired propositions.  Let `G in V_a cap T_a^searrow`, let `H=G+c` be the
next vertex in a root direction, put `m=mult(p_G,c)`, and suppose the raw
Statement 6.2 inequality holds:

```text
d_G < (1-pi(G))*m.                                    (5.1)
```

Choose `kappa` common-suitable and fine enough for the named depths, and let
`E=G*_(kappa)c` be the realizable representative selected by corrected
Statement 3.18.  Exact Statement 3.9 for `f` gives

```text
d_E=d_G-m/kappa,
deg p_E=m,
pi(E)=pi(G)+1/kappa.
```

Thus (5.1) says exactly

```text
d_E < (1-pi(E))*deg p_E,
```

so `E in T_a^searrow`.  Moreover `m>1`: the next vertex `H` is neither root
axis and Statement 3.16 gives `deg p_H>1`, while the branch-count
monotonicity of Statement 3.10/Proposition 3.1 gives
`deg p_H<=deg p_E=m`.

Repaired Proposition 6.8 therefore gives a pole above `E` on one branch in
this direction.  The final pole branch has all its `kappa`-grid ancestors in
`T_a^searrow` by the repaired recursion.  Its first vertex above `G` is
precisely `H`, so `H in T_a^searrow`.

This composition proves more than the missing positivity: the next vertex is
itself searrow.  It also shows that Proposition 6.8 is load-bearing for every
campaign use of Statement 6.2's alternative-child regularity argument, not
only for the later pole manufacture in `SHEET6-MULTIPOLE.md`.

## 6. Source-status and blast radius

### Proposition 6.7

Recommended ledger status: **ERRATUM — COMPLETE REPAIR**.

- add `kappa*pi(F) in N` to type the statement;
- in the `h=g` branch use the repaired sided Proposition 5.1 and corrected
  Proposition 5.3 ratio;
- state the condition-(7) licence in the `d_G=0` argument;
- insert the cyclic residual lemma after Statements 3.16/3.18;
- replace exact Statement 3.9 on `h_F` by corrected Statement 3.11 and (3.4).

### Proposition 6.8

Recommended ledger status: **ERRATUM — COMPLETE REPAIR**.

- replace `F*c_n` by `F_n*c_n` and `deg p_F>1` by `deg p_(F_n)>1` in the
  recursive paragraph;
- replace `d_(F_n)<=u-n/kappa` by (4.2);
- make the final ancestor argument explicit;
- cite repaired Proposition 6.7.

### Campaign consumers

No current mathematical conclusion is invalidated, because both source
theorems survive with the same statements (apart from Proposition 6.7's
missing lattice rider, which every concrete child construction already
satisfies).

The composition in Section 5, not Proposition 6.7 alone, discharges the
conditional next-vertex positivity dependency recorded by the Statement 6.2
consumer sweep for:

- `SHEET6-AF2.md`, `SHEET6-III.md`, and `SHEET6-A2P-REVIEW.md`;
- the alternative-root steps in `SHEET6-MULTIPOLE.md`;
- the Statements 9.6--9.11 root-pattern template in `SHEET6-CAMPAIGN.md`.

The source proof of Corollary 6.1 uses repaired Proposition 6.7 directly at
one-grid-step roots and does not need the Section 5 bridge.

Accordingly repaired Proposition 6.8 is load-bearing both for every
Statement 6.2 next-vertex group above and for the explicit same-branch pole
constructor used by:

- `SHEET6-MULTIPOLE.md` for pole-chain coverage, unique-predecessor arguments,
  and the `k=0` pole manufacture;
- `SHEET6-2POLE.md` and `SHEET6-L1.md` for third-pole contradictions;
- `SHEET6-H3.md` and the A2P/MP reviews for pole-chain exhaustion;
- the source's Proposition 8.4 chain construction.

These consumers should be relabelled as depending on this repair packet.
Nothing here audits the remaining statements of Sections 7--9, proves the
mass formula, landing, a Keller contradiction, or JC2.

The Statement 6.2 consumer sweep should be amended at its AF2, III, A2P,
MULTIPOLE and Statements 9.6--9.11 rows to name the Section 5 composition.

## 7. Audit method

This was a source proof audit, not an experiment.  The key repairs are exact
one-line inequalities (3.4) and (4.2); a numerical checker would add no
evidence, so none was created.  No CAS, AWS, web access, or heavy local
computation was used.  No canonical campaign file was edited.
