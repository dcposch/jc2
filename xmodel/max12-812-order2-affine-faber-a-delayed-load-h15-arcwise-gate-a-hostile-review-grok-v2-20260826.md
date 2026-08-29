# Hostile review V2 — delayed affine-Faber `A`, `H=15` arcwise Gate-A bridge

| Field | Value |
|---|---|
| Target | `xmodel/max12-812-order2-affine-faber-a-delayed-load-h15-arcwise-gate-a-theorem-20260826.md` |
| Target SHA-256 | `a1a2b098c43ad7bfa3d5a441b5efa30b7ac0fd6d0fefe21e784c392f80c79f25` |
| Overall verdict | **CONFIRMED** |
| Smallest failing identity | none |
| Smallest missing hypothesis | none that breaks a numbered claim |
| Reviewer / model | Grok 4.6 (xAI). Independent hostile rederivation of the Gate-A composition. Different model family from the producer. No producer status line, no charged `CONFIRMED`/`PASS`/`UNIT`/`ENDPOINT` token, and no validator string is evidence |
| Method | SHA-256 of every charged pin; hand and rational polynomial expansion of both directions of (2.1) and of (4.1)--(4.2); independent Euclidean division and UFD degree count for (3.4); independent load/target grade arithmetic under `Lambda=sigma^3`; matching of the resulting DVR arc against the promoted valuative chart, without substituting a global root of `Q` or a one-sided Rees quotient. Characteristic 65521 was not used. The earlier Claude launch failed on account quota before any mathematics; that log is not evidence and was not read as a verdict |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `418e413593120d19e15e6546eb50c985f4b1f038` |
| Date | 2026-08-26 |

Independently recomputed SHA-256 of the target and of every charged input named in the review prompt match those pins. Producer verdict language, the target's own status line, and both charged reviews' `CONFIRMED` tokens were not used as characteristic-zero evidence. The first-block lemma was consumed only after its numbered identities were re-expanded; the valuative composition was consumed only after the coefficient isomorphism, the closed point, and the chart weights were matched. No file other than this review was written. The target, producers, shared ledgers, and `jc2-lean` were not edited.

---

## Verdict

**CONFIRMED.**

On a complete characteristic-zero DVR, after the already permitted finite ramification `Lambda=sigma^3`, a literal delayed-load source arc with `ord_sigma(Delta)=15` and special fibre `Q0=z^2(z^2+p)`, `p` a unit, has first unloaded quadratic polar part exactly `(3/8)[N0^2/Q0]_-` at sigma grade 30. Delayed loads and `mu2` start at grade 42, the cubic normal at 45, later targets later still. Moving jets of `Q` and `N` and the lower-unitriangular Laurent-to-ordinary connection cannot occupy grade 30. The charged first-block equivalences therefore force `Q0|N0^2`. Unique factorization on the coprime squarefree type `A0=z`, `D0=z^2+p` then forces `N0=m z(z^2+p)` with `m` a unit. The maps (4.1) and (4.2) are inverse regular maps on `D(M)`, sending that closed point to `(a,E,U,R0,M,V,W0)=(0,p,0,0,m,0,0)`. Every DVR arc through that point therefore has `q=min(ord(U),ord(V))>0`. The bound `ord(a)>=5` is not produced by first-block divisibility; it remains the named Newton-cell hypothesis. Dividing `Delta` by `sigma^15` and placing a residual unit in `lam` or `M` supplies exactly the promoted delayed-load affine-Faber chart, with later center, tangent, kernel, complement, load, target, ramification, and deck data retained. The promoted theorem then kills the arc. This is a literal arcwise source exclusion on this one cell, not a normalized analogy and not a total-Rees atlas.

**CONFIRMED**

---

## Hashes and charged artifacts

Recomputed SHA-256:

| Artifact | SHA-256 | Role |
|---|---|---|
| Gate-A theorem (target) | `a1a2b098c43ad7bfa3d5a441b5efa30b7ac0fd6d0fefe21e784c392f80c79f25` | immutable composition (matches required pin) |
| first-block theorem | `56123a6f2b110284871fe65d664ffed89cb5004d1498e59a81719c2278c59f23` | charged elementary input (matches required pin) |
| first-block hostile review V2 | `85389a28a69b5e030fa689ccce9dcccee484dae9169679053d0870cfe1e9f0ff` | charged review bytes; verdict prose unused |
| valuative composition theorem | `fef0524a91c239b9086df8377e0b1270430b2fb164915eb8286bf52f9508cf32` | charged affine theorem (matches required pin) |
| valuative composition review | `a6d434b5342a32bcefc74b78fd4526eaf1a6556a73ddcc22b970c9958d248f18` | charged review bytes; verdict prose unused |
| valuative composition promotion | `0c4d242775572faef3578c42721c9d6cad483c3073dd9b98cffec5119783291c` | charged promotion (matches required pin) |

All six files are presently untracked. `HEAD` at review time is `418e413593120d19e15e6546eb50c985f4b1f038`.

---

## Attack 1 — both directions of the centered-octic square-division map (2.1)

Write `C=z^8+C6 z^6+C5 z^5+C4 z^4+C3 z^3+C2 z^2+C1 z+C0` and `Q=z^4+q2 z^2+q1 z+q0`. Expanding over `Z[q2,q1,q0]` gives

```text
Q^2 = z^8 + 2 q2 z^6 + 2 q1 z^5 + (2 q0 + q2^2) z^4
        + 2 q2 q1 z^3 + (2 q2 q0 + q1^2) z^2 + 2 q1 q0 z + q0^2.
```

There is no `z^7` term because `Q` is depressed. Adding `Delta=Delta3 z^3+Delta2 z^2+Delta1 z+Delta0` and equating coefficients is exactly (2.1):

```text
C6=2 q2,                 q2=C6/2,
C5=2 q1,                 q1=C5/2,
C4=2 q0+q2^2,            q0=(C4-q2^2)/2,
C3=2 q2 q1+Delta3,       Delta3=C3-2 q2 q1,
C2=q1^2+2 q2 q0+Delta2,  Delta2=C2-q1^2-2 q2 q0,
C1=2 q1 q0+Delta1,       Delta1=C1-2 q1 q0,
C0=q0^2+Delta0,          Delta0=C0-q0^2.
```

The forward map is polynomial over `Z[1/2]`. The inverse is the polynomial expansion of `Q^2+Delta`, defined over `Z`. Substituting either composite is the identity on the seven-tuples `(C6,...,C0)` and `(q2,q1,q0,Delta3,...,Delta0)`. The Jacobian in the `q`-block is triangular with diagonal `2`, hence invertible over `Q`. This is a literal polynomial coefficient isomorphism over `Q` (and over any complete characteristic-zero DVR after the target's written localization `R[1/2]`). There is no blowup, symmetric algebra, or torsion in the fibres.

The same expansion was recomputed as a multivariate polynomial identity in `(z,q2,q1,q0,Delta_i)` and inverted on independent `(C6,...,C0)`. Both composites are the zero polynomial.

What this does not do: it does not identify the original source octic with an affine-Faber chart, does not force `Q0` to have a repeated factor, and does not invert `2` in residue characteristic two. The target already writes `R[1/2]`. Residue characteristic two is outside the written ring, not a hole in (2.1).

---

## Attack 2 — timings under `Lambda=sigma^3`, and why nothing else occupies grade 30

The one-parameter source is

```text
Phi_l = r_l(C, Lambda^2 k10, Lambda^6 k6, Lambda^10 k2)
        - Lambda^{12+l} delta_l,
(delta_1,...,delta_7)=(0, mu2, 0, mu4, 0, mu6, J/4).
```

The delayed graph `k10=Lambda^{12} K10`, `k6=Lambda^8 K6`, `k2=Lambda^4 K2` puts every effective lower-load slot at `Lambda^{14}`:

```text
Lambda^2  * Lambda^{12} K10 = Lambda^{14} K10,
Lambda^6  * Lambda^8  K6    = Lambda^{14} K6,
Lambda^{10}* Lambda^4  K2    = Lambda^{14} K2.
```

With `Lambda=sigma^3` this is sigma grade 42. Affine-linearity of `r_l` in the three lower loads (the generating function is `g=F12+k10 F10+k6 F6+k2 F2`) puts quadratic load monomials at `Lambda^{28}=sigma^{84}`, far after the window. Target grades from the same source:

| datum | source power | sigma grade |
|---|---:|---:|
| delayed loads `(K10,K6,K2)` | `Lambda^{14}` | 42 |
| `mu2` in row 2 | `Lambda^{14}` | 42 |
| `mu4` in row 4 | `Lambda^{16}` | 48 |
| `mu6` in row 6 | `Lambda^{18}` | 54 |
| `J/4` in row 7 | `Lambda^{19}` | 57 |

Odd targets are identically zero.

At fixed `z`, with `C=Q^2+Delta` and `ord(Delta)=15`, the binomial series in characteristic zero is

```text
(Q^2+Delta)^{3/2}
  = Q^3 + (3/2) Q Delta + (3/8) Delta^2/Q - (1/16) Delta^3/Q^3 + ....
```

`Q^3` and `(3/2) Q Delta` are polynomials in `z`. Write `Delta=sigma^{15} N` with `N0=N mod sigma !=0`. Then:

- `(3/8) Delta^2/Q` has exact grade 30, polar part `(3/8) N0^2/Q0`;
- `-(1/16) Delta^3/Q^3` has grade 45;
- every later binomial term has grade at least 60.

Moving jets: `Q=Q0+sigma Q'` and `N=N0+sigma N'` produce

```text
Delta^2/Q = sigma^{30} N0^2/Q0 * (1 + O(sigma)),
```

so every correction to (3.2) has grade at least 31. Loads and `mu2` cannot meet grade 30 because `42>30`. The cubic cannot meet grade 30 because `45>30`. Later targets are later still.

Laurent-to-ordinary connection. The first possible negative `z`-principal part of `C^{3/2}` is the grade-30 polar part of `(3/8) Delta^2/Q`. Polynomial summands contribute nothing to `h_j` for `j>=1`. The charged first-block lemma supplies a lower-unitriangular diagonal-one map from `(h1,...,h4)` to the first four ordinary rows, with `Phi_k` independent of `h_j` for `j>k`. A complete initial ordinary block of length four at grade 30 therefore vanishes if and only if `h1=h2=h3=h4=0` at that grade. Moving connection coefficients (functions of `Q=Q0+sigma Q'`) multiply already-vanishing earlier negative `z`-coefficients, of which there are none, or else raise the grade. The connection cannot tie grade 30.

The coefficient `3/8` is a unit in `Q`. On an equicharacteristic-zero DVR, and on any mixed-characteristic DVR of residue characteristic not `2` or `3`, it preserves grade 30. The target already localizes at `2`. Residue characteristic three would collapse the displayed binomial and is outside the charged characteristic-zero composition being consumed; it is not a missing hypothesis inside that neighbourhood.

---

## Attack 3 — derivation of `N0=m z(z^2+p)` from the first-block lemma

The charged first-block statement, re-expanded rather than taken from review prose:

Euclidean division `N^2=A Q+R` with `deg R<=3` and the reciprocal

```text
1/Q = z^{-4}(1 - q2 z^{-2} - q1 z^{-3} + O(z^{-4}))
```

give the triangular identities

```text
h1=r3,  h2=r2,  h3=r1-q2 r3,  h4=r0-q2 r2-q1 r3
```

with diagonal one over `Z[q2,q1]`. Thus `h1=h2=h3=h4=0` if and only if `R=0` if and only if `Q|N^2`, and then every later negative coefficient vanishes as well. Independently recomputed on `Q=z^4+11 z^2+13 z+17`, `N=2z^3+3z^2+5z+7` over `Q`: remainder `-126 z^3+8 z^2+61 z+304`, and the series of `N^2/Q` at infinity reproduces `(h1,h2,h3,h4)=(-126,8,1447,1854)` from both the triangular formulae and the reciprocal series.

Over the UFD `k[z]`, `Q|N^2` if and only if `Q_half|N` with `Q_half=prod_f f^{ceil(e_f/2)}`. Under the hypotheses

```text
Q=A^2 D,  deg A=1,  deg D=2,  gcd(A,D)=1,  D squarefree,
```

one has `Q_half=A D` of degree three. A degree-three divisor of a polynomial of degree at most three is a scalar multiple, uniquely `N=M A D`.

Apply this on the residue field of the DVR, to `Q0=z^2(z^2+p)` with `p` a unit and `deg N0<=3` (because `deg Delta<=3`). Set `A0=z` and `D0=z^2+p`. Then:

- `gcd(A0,D0)=1` because `D0(0)=p!=0`;
- `D0` is squarefree because its discriminant is `-4p!=0` after inverting `2`, equivalently because a square linear would force `p=0`;
- `deg N0<=3=deg(A0 D0)`.

The first-block criterion therefore yields `N0=m z(z^2+p)` for a unique scalar `m` in the residue field. The definition `N0!=0` in (2.2) forces `m!=0`, hence `n3 mod sigma=m` is a unit of the DVR. This is (3.4).

Hypotheses that cannot be dropped:

- squarefreeness of `D0`: if `D0=B^2` then `Q0=A0^2 B^2` requires only `A0 B|N0`. Explicit control over `Q`: `Q=(z^2-1)^2`, `N=z^2-1` satisfies `Q|N^2`, while `A D=(z-1)(z+1)^2` does not divide `N`. This is the `p=0` / double-double / Pell collision, already routed in Section 6.
- degree: if `deg N0>3` the scalar conclusion fails. Square division forbids this.
- `m!=0`: if `m=0` then `N0=0`, contradicting the declared order `15`. Route: raise `H`.

If `Q0` is squarefree then `Q_half` has degree four, so `N0=0`, contradicting (2.2). If `Q0` is a square, or `D0` collides with `A0`, the type is not the coprime squarefree repeated-`A` cell. Section 6 records those receivers. The implication (3.3) `=>` (3.4) is therefore exact on the written type, and is a kernel statement, not an analogy with the affine-Faber normal.

The gcd hypothesis is automatic on this cell once `p` is a unit. It is essential for isolating the coprime type from the triple-plus-simple overlap `A0|D0`; that overlap is already a separate receiver in the first-block classifier and in Section 6.

---

## Attack 4 — both directions of (4.1)--(4.2), the closed point, `q>0`, and `v(a)>=5`

Let `A=z-a` and `D=A^2+4 a A+E`. Expanding in `z` over `Q[a,E,U,R0,M,V,W0]`:

```text
A^2 D = z^4 + (E-6 a^2) z^2 + 2a(4a^2-E) z + a^2(E-3 a^2),
A D   = z^3 + a z^2 + (E-5 a^2) z - a(E-3 a^2).
```

(The `z^3` coefficient of `A^2 D` cancels, so `Q` remains depressed.) Adding `U A+R0` and `M(A D)+V A+M U/2+W0` is exactly (4.2), and produces

```text
q2=E-6 a^2,
q1=2a(4a^2-E)+U,
q0=a^2(E-3 a^2)+R0-a U,
n3=M,
n2=a M,
n1=(E-5 a^2)M+V,
n0=-a(E-3 a^2)M-a V+M U/2+W0.
```

These are polynomial identities. On `D(M)` they invert regularly by (4.1): `a=n2/M`, then `E=q2+6 a^2`, then `U=q1-2a(4a^2-E)`, then `R0=q0-a^2(E-3 a^2)+a U`, then `V=n1-(E-5 a^2)M`, then `W0=n0+a(E-3 a^2)M+a V-M U/2`. Substituting (4.2) into (4.1) is the identity on `(a,E,U,R0,M,V,W0)`. Substituting (4.1) into (4.2) and clearing the denominator `M` is the identity on `(q2,q1,q0,n3,n2,n1,n0)`. Both composites were recomputed as multivariate polynomials over `Q` and are zero. This is a coefficient-coordinate isomorphism of affine charts, not an endpoint projection and not a Rees-torsion statement.

No root of the moving quartic is adjoined. The coordinate `a=n2/M` is regular on `D(n3)`. On the kernel it happens to equal the double root, but that equality is not used to construct the chart.

Closed point. From (1.2) and (3.4),

```text
Q0=z^4+p z^2,     N0=m z^3 + m p z,
```

so `(q2,q1,q0,n3,n2,n1,n0)=(p,0,0,m,0,m p,0)`. Then (4.1) returns

```text
M=m,
a=0,
E=p,
U=0,
R0=0,
V=n1-(E)M=m p-p m=0,
W0=0.
```

This is (4.3). Independently, `Q0=A^2 D` and `N0=M A D` at `A=z`, `D=z^2+p`, `M=m` is the same point.

Why `q>0`. The closed point lies in the maximal ideal generated by `(U,V,R0,W0,a)` together with the higher jets of `E-p` and `M-m`. Hypothesis (1.2) plus (3.4) say that the special fibre of the DVR arc is exactly that point. Therefore `U` and `V` vanish in the residue field, so `ord_sigma(U)>=1` and `ord_sigma(V)>=1`, or both series vanish identically. Hence `q=min(ord(U),ord(V))>0`, with `q=infinity` allowed. This is a consequence of the central ideal of a centered DVR arc, not an extra chart axiom. It would fail for a Zariski point of `D(p*m*K10)` that did not specialize to the repeated-root origin (the `q=0` receiver: unit leading `U`, equivalently a squarefree or square special fibre). The theorem is the DVR neighbourhood of (4.3), which is exactly the cell (1.2).

Why `v(a)>=5` is not derived. The same special fibre gives `a=n2/M ≡ 0 mod sigma`, hence only `ord(a)>=1`. First-block divisibility never sees the higher jets of `n2`. Cells with `1<=ord(a)<=4` are compatible with (3.4) and (4.3) and must be routed to their earlier center faces, as Section 6 does. The bound `ord(a)>=5` is the remaining registered weight of the promoted affine theorem, and the target correctly leaves it as a hypothesis in Section 1.

On this cell `E≡p` is a unit as soon as `ord(a)>=1`, because `E=q2+6 a^2` and `q2≡p`, `ord(a^2)>=2`. Localizing at `E` is therefore free on the written cell and does not secretly force `ord(a)>=5`.

---

## Attack 5 — dividing `Delta` by `sigma^{15}` supplies the promoted affine theorem

The promoted statement, consumed as a charged theorem rather than as review prose: on the delayed-load ray with `Lambda=sigma^3`, there is no formal or Puiseux source arc on `D(p*m*K10)` with chart weights `v(a)>=5` and `q=min(v(U),v(V))>0`. Every rational `0<q<6` dies at the unloaded face of grade `30+2q`; every `q>=6`, including unequal orders and `q=infinity`, dies by the unit

```text
[sigma^{45}](E H3+H5)=-E lam^3 M^3/16
```

on `D(E lam M)`.

Matching, item by item.

- Normal scale. Gate (2.2) writes `Delta=sigma^{15} N` with `N0!=0`. The promoted chart extracts a normal factor `sigma^{15} lam` from the cubic. A residual unit of `N` may be placed in `lam` or absorbed into `M`: if `n3=u m` with `u` a one-unit, set `lam=u` and `M_shape=n3/u`, or set `lam=1` and `M=n3`. The monomial `lam^3 M^3` is invariant under `lam |-> lam u`, `M |-> M/u`. Either normalization is the promoted scale. No jet of `N` is discarded: (4.1) is applied to the full series `N=Delta/sigma^{15}`.
- Coordinates. Gate (4.1)--(4.2) are the unique seven-tuple of the valuative chart on `D(M)`, with the splitting `R1=S1=0`, `X=U`, `Y=V`. Existence of some splitting is all the valuative argument uses. Complements `R0,W0`, kernel `U,V`, center `a`, and tangents `E,M` are the full coefficient jets of `(Q,N)`.
- Open `D(p*m*K10)`. Here `p` is a unit by (1.2), `m` is a unit by (3.4), and `K10` is a unit by the written delayed ray.
- Weights. `q>0` is derived in Attack 4. `v(a)>=5` is the remaining named hypothesis. Loads, `mu2`, and later targets are the same delayed graph as in the promoted theorem.
- Ramification and deck. Both statements permit a finite ramification making `Lambda=sigma^3`. Uniqueness of `sigma` is not required. Cube-root deck transformations act by units on the uniformizer and do not leave the cell; exclusion of every such arc excludes every deck transform.
- `0<q<6` versus `q>=6`. After the kernel (3.4) is imposed, the next unloaded polar part is the kernel/complement face of grade `30+2q`. For rational `q<6` one has `30+2q<42`, so that face is still unloaded; the promoted complete-tail rows apply to the image arc. For `q>=6` the same image arc meets the weight bounds that license substitution into the direct-unit identity. The case `q=infinity` is `U=V=0`, which still hits the cubic unit at grade 45.

Hidden global-root map: none. The coordinate `a` is `n2/M` on `D(M)`, not a root extracted from `Q`. The first-block incidence chart `A=z-a` is not used as a function of quartic coefficients.

Hidden one-sided Rees map: none. Square division (2.1) is a two-sided polynomial isomorphism. The `D(M)` chart (4.1)--(4.2) is a two-sided regular isomorphism. The delayed-load substitution is the same closed graph already present in the promoted theorem, not a new associated-graded quotient, not a saturation-commutation, and not a total-Rees atlas. The argument never identifies `Proj` of a Rees algebra with a source chart, and never deletes later jets by passing to an associated graded.

The image arc is therefore a literal point of the promoted weighted neighbourhood. The promoted exclusion applies, and contradicts the seven source rows.

---

## Attack 6 — literal arcwise exclusion versus analogy; firewalls

The chain is a sequence of literal maps on one complete DVR:

```text
source octic C
  --(2.1), polynomial iso--> (Q, Delta)
  --divide by sigma^{15}-->  (Q, N)
  --first-block + UFD-->     special fibre (3.4)
  --(4.1), regular on D(M)--> affine-Faber 7-tuple through (4.3)
  --promoted theorem-->      empty.
```

Every arrow is an identity or a regular isomorphism on the written open, except the last, which is the charged exclusion. This is a genuine arcwise source exclusion on the Newton cell

```text
delayed-load ray,  H=15,  Q0=z^2(z^2+p) with p unit,
K10 unit,  ord(a)>=5.
```

It is not a scheme-level statement, not a normalized leading-term analogy, and not an identification of pairwise chart overlaps.

Firewalls, enforced rather than treated as extra theorems:

| Boundary | Why it is outside |
|---|---|
| `H!=15`, still `H<21` | First-block routing remains, but the promoted scale-15 identity and the weights `a:5`, `U,V:6` do not apply. Quadratic grade is `2H`, cubic grade `3H`. |
| `H>=21` | Loads/`mu2` at 42 can tie or precede the quadratic block; forcing must be retained. |
| `0<ord(a)<5` | Compatible with (3.4); earlier center face. |
| `ord(a)=0` with double root off the origin | `Q0` would have a unit `q1`; not cell (1.2). Translation by a unit leaves the centered octic chart. |
| `q=0` | Complementary first-normal open: unit leading `U`, squarefree or square special fibre. |
| `p=0`, `m=0`, `K10=0` | Degenerate factor, wrong first normal, or zero-load ray. |
| `Q0` squarefree | Forces `N0=0`, contradicting (2.2); reset `H`. |
| `Q0` a square, `D0` not squarefree, `A0` not coprime to `D0` | Square/Pell, triple, quadruple, or collision receivers. |
| other load slopes | Different `Lambda`-weights; grade 42 is special to this graph. |
| total-Rees / saturation | The proof uses coefficient isomorphisms on one DVR. It does not commute saturation with specialization, prove flatness or torsion, or cover the original source boundary. |
| terminal / Taylor | Later targets start at grade 48 and beyond; not evaluated. |
| order two, `(8,12)`, maximum twelve, JC2 | Campaign scope labels. The algebra is this cell of this delayed ray. |

The coefficient `3/8` is used as a grade-preserving unit, as in the charged characteristic-zero composition. Mixed residue characteristic three is not a written cell of that composition.

---

## Strongest exact theorem that survives

Let `R` be a complete DVR of equicharacteristic zero, or of mixed characteristic with `2` and `3` units, after a finite ramification `Lambda=sigma^3`. Let a literal solution of the seven delayed-load source rows

```text
k10=Lambda^{12} K10,  k6=Lambda^8 K6,  k2=Lambda^4 K2,  K10 a unit
```

have centered octic `C=Q^2+Delta` via (2.1), with `ord_sigma(Delta)=15` and `Q mod sigma=z^2(z^2+p)` for a unit `p`. Then `N0=m z(z^2+p)` with `m` a unit. The regular map (4.1) on `D(n3)` sends the arc into the promoted delayed-load affine-Faber neighbourhood of `(0,p,0,0,m,0,0)`, with `q=min(ord(U),ord(V))>0`. If in addition `ord_sigma(a)>=5`, the promoted theorem excludes the arc. Therefore no such source arc exists.

This is an internal composition of a polynomial square-division isomorphism, a first-block UFD kernel, a regular `D(M)` coefficient isomorphism, and one already promoted affine-Faber exclusion. It is not a two-sided total-Rees atlas, and it does not close any routed boundary in Section 6, terminal/Taylor, order two, `(8,12)`, maximum twelve, or JC2.

**CONFIRMED**
