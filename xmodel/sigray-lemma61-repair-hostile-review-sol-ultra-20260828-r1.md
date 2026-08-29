# Hostile review — Sigray Lemma 6.1 short repair

Reviewer: Sol Ultra, independent re-derivation

Date: 2026-08-28

## Verdict

**REPAIR.**  Lemma 6.1 is true, the producer has the correct exponent
orientation and the correct terminal conclusion, and no corner, target-shift,
condition-(7), or chart counterexample survives.  But the sentence that
Propositions 4.4--4.5 carry the first pair from an arbitrary `F` to an axis
omits one necessary gate: every intervening positive flag must still have a
nonempty tower.  Proposition 4.4 compares only a flag with its one-grid-step
predecessor, and an empty intermediate tower would erase the first pair.  A
short `rho` monotonicity argument closes the gap below.

## 1. Frozen inputs and source custody

The charged producer hash matched before review:

```text
651231a80274de4d684076c4b238be38b98e3a4ad704e750a06fa23c43ef6e5f  xmodel/sigray-lemma61-repair-sol-ultra-20260828.md
9bf9f0320497dd8d5da6d7fe68ec900c1879663e6f11c121853482ca7e1623ae  refs/sigray_full.pdf
10bc55d53f9cf9a9e6a4535787f6e208a25f0ebfbd6dbd803f68b00f8ca8f5cd  xmodel/sigray-prop42-constant-shift-repair-sol-ultra-20260828.md
47f2b608f47bc7f426c6cf3e8634c8704bdd675aa909eb63e3f4c6861c21dfb1  xmodel/sigray-prop42-constant-shift-repair-hostile-review-opus5-20260828-r1.md
ca63eb5e75a1d67ac02c2f643aff82b14af3d94a35e26d78e6de523604348e18  xmodel/sigray-no-first-constant-corner-hostile-review-sol-ultra-20260828.md
```

Primary anchors re-read: Lemma 2.1 and Notation 2.4 on pp. 8--9;
Statements 3.9--3.10 and 3.18 on pp. 15--18; Proposition 4.1 on p. 18;
Propositions 4.2 and 4.4--4.5 on pp. 19--22; and Lemma 6.1 plus its use in
Proposition 6.8 on p. 34.

## 2. The printed defect is real

The printed maximal-grid proof obtains `deg p_(g,F)=0` and immediately
asserts a nonzero leading Jacobian.  Write

```text
f_F^+ = xi^d p(eta),       g_F^+ = xi^e q,
deg p = 1,                 q in C*.
```

Its residual bracket is `-e*p'*q`.  It is nonzero only if `e!=0`; at `e=0`,
`g_F^+=q` is a scalar and the bracket vanishes.  The thesis does not exclude
that branch there.  The reviewed no-first-corner theorem now excludes it on
`T_a^+`, but that is a genuine repair, not a validation of the printed
inference.

## 3. First relation at the charged flag

Assume `m_F>0`.  The reviewed theorem says `g_F^+` is not a nonzero scalar,
so condition (7) holds and index zero cannot be the repaired `(1,0,c)`
corner.  Corrected Proposition 4.2 therefore legally gives

```text
(g_F^+)^k = s*(f_F^+)^l,   k,l in N*, gcd(k,l)=1.          (3.1)
```

No later tower member enters.  Thus neither a derived-`h` suitability rider
nor Proposition 4.3's negative-side target shift is relevant here.

## 4. The missing transport gate and its repair

Proposition 4.4 is local: in its proof `F=F'*c`, and it compares relations at
that adjacent pair.  Its tower-prefix conclusion permits the abstract pattern
`nonempty -> empty -> nonempty`; at the last transition the first pair is not
constrained by the first.  Hence Propositions 4.4--4.5 alone do not justify
the producer's displayed `(k,l)=(alpha,beta)`.

Here is the smallest exact patch.  Write `F=I_P(u)`.  Choose one `K` suitable
for the chart, with `Ku in N`, and satisfying Statement 3.9 for the fixed
polynomials `f-a` and `g`.  Put

```text
F_j=I_P(j/K),
rho(F_j)=d_(f-a,F_j)+d_(g,F_j)+j/K-1.
```

Every `F_j` with `j<=Ku` lies in `T_a^+`, since Statement 3.10 makes the
`f-a` order nonincreasing as the parameter grows.  At `F`, `m_F>0` means the
initial leading Jacobian vanishes; condition (7) and Proposition 4.1 then
give `rho(F)>0`.

For `F_{j+1}=F_j*c_j`, let

```text
r_j=mult(p_(f-a,F_j),c_j),  t_j=mult(p_(g,F_j),c_j).
```

Statement 3.18 gives `r_j>=1` (on `T_a^+`, the leading polynomials of
`f-a` and `f` agree), while `t_j>=0`.  Statement 3.9(iii) gives the exact
edge law

```text
rho(F_{j+1})-rho(F_j)=(1-r_j-t_j)/K <= 0.                 (4.1)
```

Consequently every ancestor satisfies `rho(F_j)>=rho(F)>0`.  Proposition
4.1 and corrected Proposition 4.2 now show `m_(F_j)>0` at every ancestor;
the no-first-corner theorem makes every first relation ordinary.  Proposition
4.4 can therefore transport `(k,l,s)` through the whole finite chain to its
axis.  This use of Statement 3.9 involves only the fixed pair `{f-a,g}` and a
single common lcm, never a derived tower polynomial.

## 5. Axis orientation and degree contradiction

At either root chart, the order ratio is

```text
d_f/d_g = k_f/k_g = l_f/l_g = alpha/beta.
```

Indeed, Notation 3.12 selects the appropriate Newton-axis order, while Lemma
2.1(ii) makes the two displayed coordinate ratios equal.  In a relation
`(g^+)^k=s(f^+)^l`, order comparison is `k*d_g=l*d_f`, so

```text
k/l=d_f/d_g=alpha/beta,
```

not its reciprocal.  Coprimality gives `(k,l)=(alpha,beta)`; Proposition 4.5
confirms consistency between the two axes.  Returning along the chain and
comparing residual polynomials gives

```text
p_(g,F)^alpha=s*p_F^beta.
```

With `deg p_F=1`, this says `alpha*deg p_(g,F)=beta`, hence `alpha|beta`.
Since `gcd(alpha,beta)=1`, `alpha=1`, contradicting Statement 2.1.  Thus
`m_F=0`.

## 6. Terminal clause and consumer

For `m_F=0`, corrected Proposition 4.2 has `h_m=h_0=g` and `mu_F=0`; its
terminal clause is exactly

```text
J(f_F^+,g_F^+) = C*xi^(-u),   C in C*.
```

This proves Lemma 6.1.  Proposition 6.8 uses only the equivalent conclusion
`m_F=0` to exclude a degree-one intermediate non-pole, so its repaired use is
sound after inserting Section 4's transport paragraph.

Required producer edits are therefore local: insert (4.1) and the ancestor
nonemptiness argument before the exponent pin; add Propositions 4.1,
Statements 3.9--3.10/3.18, and fixed-`{f-a,g}` common-`K` typing to the
dependency list; and delete the claim that no grid induction or Statement
3.9 use occurs.  No conclusion is rolled back.
