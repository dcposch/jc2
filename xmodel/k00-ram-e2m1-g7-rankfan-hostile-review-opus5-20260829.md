# Hostile review: exact G7 closure of `K00-V20R2-RAM-E2-M1-B11111/v1`

Date: 2026-08-29
Reviewer: Opus 5 (independent; producer was Sol 5.6 Ultra)
Reviewed object: `xmodel/k00-ram-e2m1-g7-rankfan-certificate-sol56-20260829.md`
Review basis commit: `9b64db896b65e100839f6d75fbeea661cd818b9c`

## Verdict

```text
CONFIRM_WITH_CORRECTIONS
```

Every mathematical assertion in the certificate that I could test — the exact
unloaded surface, the erratum, both complete rank fans, all seven labelled
rows, the opens, the radical usage, and the G7-to-G38 implication — is exactly
true and was reproduced clean-room from the 569 frozen tails and the literal
ramified load scale, without reading the producer replay's serialized rows.
The corrections are (a) two load-bearing definitions that the certificate uses
but never states, without which §2 is literally false as written, and (b) one
mis-justified control claim in §5. None of them touches the truth of (0.1).

I additionally re-derived the *promoted* G3 reduction from scratch, so the
fan's starting point no longer rests on an inherited claim within this scope.

## 0. Custody and execution boundary

All five pinned artifacts hash exactly as given. The replay additionally pins
four artifacts that were not in my packet; all four match the digests declared
inside it:

```text
2c918d5b0d165977bdd2b598cf48d90cf3d0dfe0922ce27213dfa01dc255e7c4  xmodel/k00-r2-full-rank-fan-replay-sol56-20260829.py      (ENGINE)
d453b9563d8f6cc23319d6bc0d8edce8a83f657b9e3a60cb244b00f181459860  xmodel/k00-rank5-rankle1-coordinator-integration-sol56-20260829.md  (G3_PROMOTION)
a6fd11f1c6d5b32cc2e497722245cbe7381356ffdbba02c6db050ad5fe67ced0  xmodel/k00-ram-e2m1-g5-prefix-certificate-sol56-20260829.md
b4fd505d0345b21a2978f06ff63cb0c9fcacd9d7226d7accaa0b2ab489b210ea  xmodel/k00-ram-e2m1-g5-prefix-replay-sol56-20260829.py
```

This session had a shell. All computation below is exact rational (and exact
Gaussian-rational) pure-Python-stdlib arithmetic, written by me, longest
single step ~8 s; no CAS, no network, no AWS. `Singular` and `msolve` exist on
this host and were **not** used. One mod-101 projective enumeration was used
for navigation only and its conclusion was then re-proved exactly over `Q`
(§4.1). `jc2-lean` was not inspected, listed, built, or controlled. `apply_patch`
is not exposed in this session; the deliverable was written with a Bash
heredoc, which is the same single-file create.

## 1. Clean-room rebuild of the source (attack 1)

I parsed `tails.json` directly and rebuilt everything from it.

```text
row              1   2   3   4   5   6   7      total
tail monomials  36  54  58  81  89 120 131        569
```

* Every monomial in row `l` has weight `12+l` under
  `w(C_i)=8-i, w(k10)=2, w(k6)=6, w(k2)=10`. No exception.
* Load-degree histogram over all 569 monomials is `{0: 280, 1: 289}`; maximum
  total degree in `(k10,k6,k2)` is `1`. Affine load-linearity holds literally,
  so the split `R / A10 / A6 / A2` is well defined.
* Applying the literal normalization (2.2) (`C0=(1+d0)/256, C1=d1,
  C2=(1+d2)/16, C3=d3, C4=(3+d4)/8, C5=d5, C6=1`) and reading off orders
  reproduces the stencil (3.1) exactly:

```text
ord_d R   = (2,2,2,2,2,3,2)
ord_d A10 = (2,2,2,2,2,2,2)
ord_d A6  = (1,1,1,2,1,2,1)
ord_d A2  = (1,1,1,1,1,1,1)
```

* No sector has a constant term, so the K00 point is a source point.
* Grading `d_i[n]` by `n` and `k10[j]` by `j`, and applying the literal
  ramified load scale `t^4*k10(t)*A10(d(t))` (`Lambda=t^2`), the grade census
  of the seven rows is

```text
G0,G1  all seven rows identically zero
G2     rows 1,2,3,4,5,7 begin; row 6 zero
G3..G7 all seven rows active
```

matching the source packet's calendar. `K6` cannot occur before `t^12*t^1*t^1
= t^14` and `K2` before `t^22`, so grades `<= 7` are `R + t^4*k10*A10` only.
I confirmed this independently in §5 by deleting the K6 and K2 sectors
outright.

Only after finishing the above did I compare against the replay's engine:
my `R, A10, A6, A2` dictionaries are **equal as exact rational dictionaries**
to `module.reconstruct_rows()` for all 7 rows x 4 sectors, and the engine's
`coordinate_images()` equals (2.2). The producer's reconstruction is faithful.

## 2. The erratum (attack 2)

**(1.2) is exactly true, for all seven rows.** Writing `d(t)=ell*t+u*t^2+...`:

* `[t^2]A10(d) = M4(ell) = 0` for **all seven rows** — verified. This, not any
  periodicity argument, is why K10 cannot appear at G6 and why `k10[1]` is
  absent at G7.
* `[t^3]A10(d) = DM4(ell)[u] + A10^[3](ell)` — verified, all seven rows.
* `= DM4(ell)[u - mu/2]` — verified, all seven rows, **with**
  `mu = (s^2, s*t/8, 16*t^2, 0, 0, 0)`.

**Correction C1.** `mu` is never defined anywhere in the certificate body.
(1.2) and (1.3) are unverifiable from the certificate alone. The value above
is the replay's `mu_vector`, and it is exactly the grade-2 centering of §2/§4
(see C2). Any reader reconstructing `mu` differently gets a false identity.

**(1.3) is exactly true.** At `s=1, t=0, u=mu`, row 2:

```text
DM4(ell)[mu]     =  5/32768      (the old, wrong polarization-only value)
A10^[3](ell)     = -5/65536      (the omitted cubic)
literal [t^3]A10 =  5/65536      (the corrected G7 load)
```

**Do the earlier G3–G5 conclusions survive?** Yes, and I checked each of the
three survival claims rather than accepting the reasoning:

1. *G3 nonzero-rank kill.* The K10 sector starts at grade 6, so G2/G3 contain
   no load at all. The cubic correction cannot reach them. I re-derived the
   entire G3 reduction independently anyway (§4.1) and it is unaffected.
2. *G4/G5 identities and the finite G5 witness.* Verified directly on the
   corrected source (§3); K10 is still absent from G4, G5 **and G6**, the last
   because `M4(ell)=0`.
3. *First nonzero K10 arrival at G7.* Verified: grade 6 would need
   `k10[0]*M4(ell)`, which vanishes identically.

The erratum therefore invalidates exactly the one displayed G7 coefficient it
claims to, and nothing upstream. The producer's scoping of the erratum is
accurate.

## 3. Both rank fans, signs, and exhaustiveness (attack 3)

All of the following are exact identities I reproduced symbolically.

### 3.1 The G4 cone

Setting `A(v)=16v1-4v3+v5`, `B(v)=v0-4v2+2v4`:

* After the centering `d[2] = nu2 + w`, **all seven** G4 rows are exactly the
  quadrics `Q_r(w)`, and those `Q_r` are literally the G2 quadratic forms.
* The parameterization (2.2) `w=(2b+2p,a,b,8a+q,b-p,16a+4q)` annihilates all
  seven `Q_r`, and satisfies `A(w)=B(w)=0`; the map `(a,b,p,q)->w` is
  injective with inverse `p=w2-w4, q=w3-8w1`, so the rank stratification by
  `(p,q)` is well defined and single-valued on the cone.
* **New exact certificate for the support claim.** `A*B` lies in the `Q`-span
  (coefficients `2048/3` on `Q_1`, `16384/3` on `Q_3`); `A^2, B^2` do **not**;
  `A^3, B^3` do lie in the degree-3 piece of `(Q_1,...,Q_7)`. Hence
  `A,B in sqrt(Q)` and `V(Q) = V(A,B)` exactly, and the ideal is nonreduced
  (it contains no linear form). §2's "reviewed reduced support" is confirmed
  with a self-contained proof.
* `rank DQ(w) = 2` on `D(Delta)`, `1` on `Delta=0,(p,q)!=0`, `0` at `p=q=0`:
  the `2x2` minor of `[alpha|beta]` on rows 1,2 is exactly `(9/2^24)*Delta`.
  Over an algebraic closure `Delta=0` factors as `(p-8iq)(p+8iq)`, and `q=0`
  there forces `p=0`, so the three strata are exhaustive and the two rank-one
  charts `p=eps*8i*q, q!=0, eps=+-1` are exhaustive within stratum 1.

### 3.2 First fan (G5)

`alpha, beta` as printed in (3.1) are exact; no coefficient direction outside
`X=A(v), Y=B(v)` occurs in any of the seven rows. All five identities (3.3)
verified with remainder exactly `0`:

```text
det([alpha,beta,N] rows 1,2,3) = (27/2^35)*Delta*C
G5_4                           = (3/2^15)*E
(3/128)G5_1+(1/8)G5_3+G5_5     = 0
G5_6                           = 0
(1/512)G5_1+(1/128)G5_3+G5_7   = 0
```

* **rank 2.** The `(s,t)`-coefficient determinant of `(C,E)` is exactly
  `-Delta^2` (3.4), so `s=t=0`. Contradicts the open. EMPTY.
* **rank 1.** Row 4 gives `E = 128q^2(s - eps*8i*t)`, so `s=eps*8i*t`; and
  imposing (3.5) `Y-eps*8i*X = -128tq` makes **all seven** G5 rows vanish
  identically. This is a genuine survivor, correctly not discarded. The sign
  is right: `beta_r/alpha_r = eps*i/8` on the chart for every row with
  `alpha_r != 0`, so (3.5) is both necessary (from row 1, `alpha_1 != 0`) and
  sufficient.
* **rank 0.** At `p=q=0`, `alpha=beta=N=0`: every one of the seven G5 rows is
  the zero polynomial and `d[3]` is entirely unconstrained. Correct.

At G6 on the rank-one branch, with `a,b`, all six `d[4]` components, `k10[0]`
and `k10[1]` all kept symbolic, the three combinations (3.6) come out exactly

```text
(3/128)G6_1+(1/8)G6_3+G6_5 = -q^3/16
G6_6                       = eps*i*q^3/32
(1/512)G6_1+(1/128)G6_3+G6_7 = q^3/128
```

with only `I, eps, q` surviving. Hence `q=0`, contradicting `q!=0`. EMPTY.

### 3.3 Second fan (centered G6 and literal G7)

* (4.1) `G6_r = Q_r(r)` exactly, for all seven rows, with arbitrary `r`,
  arbitrary `d[4]`, and arbitrary `k10` — no `s,t,a,b` and no load survive.
  So the G6 cone is again `V(A,B)`, parameterized as `ell(c,d)+rT` (again a
  bijective parameterization, `p=r2-r4, q=r3-8r1`).
* (4.4) verified in the operative sense: G7 depends on `z` only through
  `A(z),B(z)`, with the **same** `alpha,beta`; it is free of `a,b,c,d`; and
  `k10[1]` is exactly absent.
* (4.5) verified: `W_1=(5/4096)t(3s^2-64t^2)`, `W_2=(5/65536)s(s^2-192t^2)`,
  and additionally `W_4=W_6=0`, `W_3=-W_1/8`, `W_5=-W_1/128`,
  `W_7=-W_1/1024`. So `W_1,W_2` are not merely "sufficient" — they span the
  whole rank-zero load system.
* (4.6) verified with remainder exactly `0`: the corrected K10 load cancels
  from both the rank-two determinant and row 4.
* **G6 rank two.** `(C,E)` again with determinant `-Delta^2`, so `s=t=0`. EMPTY.
* **G6 rank one.** Row 4 forces `s=eps*8i*t`, hence `t!=0` on the open, and
  `G7_2+(eps*i/2)G7_1 = -(5/16)*i*eps*k*t^3` exactly, with only `I,eps,k0,t`
  surviving. `k` and `t` are units. EMPTY.
* **G6 rank zero.** At `p=q=0` the unloaded and new-coefficient parts of all
  seven G7 rows are exactly zero, leaving `G7 = k*W`. The two cubics have only
  the common zero `(0,0)`: `t=0 => s^3=0`; `s=0 => t^3=0`; both nonzero forces
  `3s^2=64t^2` and `s^2=192t^2`, i.e. `576t^2=64t^2`, i.e. `t=0`. EMPTY.

The three G6 strata exhaust the reduced cone, so (0.1) follows. Confirmed.

### 3.4 The reactivated row 6 — tested explicitly, and mis-justified

Row 6 does behave as advertised: `Q_6 == 0`, `G5_6 == 0` identically, `G7_6 ==
0`, and `G6_6 = eps*i*q^3/32 != 0` on the rank-one chart. All seven labelled
rows are retained in the serialization, and deleting row 6 from the source
does make the replay fail closed — I ran it, and it aborts at
`('rank1 sign 1 G6 row6', ...)`.

**Correction C3.** But the certificate's justification in §5 item 6 is wrong
in emphasis, and the banner `ZERO_ROW_REACTIVATION` overstates what is tested.

1. It is a positive assertion, not a designed negative control. The other five
   mutations each carry an explicit `fail("... mutation is invisible")` guard;
   this one has none. It detects a source edit, not a change of verdict.
2. Row 6 is **not load-bearing anywhere inside this certificate's scope**. The
   six branch kills use, respectively, rows `{1,2,3,4}`, `{1,3,5}`,
   `{1,2,3,4}`, `{1,2}`, `{1,2}`, and the G4/G6 cone is unchanged by deleting
   row 6 because `Q_6 == 0` identically. In particular the G5 rank-one branch
   already dies by `(3/128)G6_1+(1/8)G6_3+G6_5 = -q^3/16`, which does not
   mention row 6. Rows `{1,2,3,4,5}` alone close the whole post-G3 fan; rows 6
   and 7 are dispensable. (Deleting row 7 likewise only trips a positive
   assertion, `G5 S7`.)
3. Where row 6 *is* decisive is **G3** — see §4.1 — i.e. inside the promoted
   input, not inside this certificate.

Retaining the rows is still correct discipline. The claim to repair is the
reason given for it.

## 4. Surface, centering, opens, descent, radical, G38 (attack 4)

### 4.1 The exact unloaded surface, and an independent G3 re-derivation

`R_r(D(S,T)) = 0` identically for **all seven** `r` on
`D(S,T)=(2S+S^2,(1+S)T/8,S+16T^2,T,S,2T)` — confirmed; changing `16T^2` to
`15T^2` breaks six of the seven rows.

**Correction C6.** §2 says "the load polynomials do not vanish identically on
(2.1)". Collectively true, but **row 4 is a complete exception**: `A10_4`,
`A6_4` and `A2_4` all vanish identically on the surface. This is the reason
`W_4=0` and the reason row 4 stays load-free in (4.6); stating it converts a
coincidence into a mechanism.

**Correction C2 — the most material defect.** §2 says "Retain the G4 scheme
equations `Q_r(w)=0`" and never says what `w` is. Verbatim in the raw
coordinate `d[2]`, G4 is **not** a pure quadric: e.g. row 1 carries
`-3/512*s*t*w2 + 3/512*s*t*w4 - 3/1024*s^2*w3 + ... + 3/32*s*t^3`. G4 becomes
exactly `Q_r(w)` only after the unstated grade-2 centering

```text
w = d[2] - nu2,     nu2 = (s^2, s*t/8, 16*t^2, 0, 0, 0),
```

which is exactly the `t^2` coefficient of the surface, and exactly the `mu` of
C1. §4 defines `nu3` and `nu4` explicitly; `nu2` is the missing one, and it is
needed twice. Both `nu2` and `mu` must be added for the certificate to be
self-contained. With them added, §2 and §1 are exactly right.

**Independent G3 re-derivation.** Because the fan's exhaustiveness rests on
`d[1]=ell(s,t)`, I re-proved the promoted reduction rather than inheriting it.

* In coordinates `L1=x0-2x2, L2=x4-x2, L3=8x1-x3, L4=x5-2x3`, all seven G2
  rows are **pure quadratic forms in `L1..L4` alone** — no `s,t`.
* `V(G2)` is therefore a cone, and it is **strictly larger** than the
  `ell`-plane: exactly `V(A,B)`, the 4-plane `{L1+2L2=0, L4+2L3=0}`. (Found by
  a mod-101 enumeration in `P^3` giving exactly `p+1` points, then proved
  exactly over `Q` by substituting `L=(-2m,m,n,-2n)` into all seven rows, plus
  the `A^3,B^3 in (G2)` membership of §3.1.) So G2 alone does **not** give the
  reduction; G3 does real work. Consistently, `L_i^N` is not in `(G2)` for any
  `i` and `N<=5`.
* On `V(G2)` write `x = ell(s,t)+rT(p,q)`. Then G3 has the *same* `alpha,beta`
  shape, with rows 4 and 6 `y`-free:
  `N_6 = (p/65536)(192q^2-p^2)`, `N_4 = -(3/256)pqt-(21/512)pq^2
  -(3/32768)p^2 s+(3/32768)p^3+(3/512)q^2 s`.
  - *rank 1* (`p=eps*8i*q, q!=0`): `N_6 = eps*i*q^3/32 != 0`. EMPTY.
    (This is precisely where row 6 earns its keep.)
  - *rank 2, `p=0`*: `N_4=0` gives `s=0`; then the `(1,2,3)` and `(1,2,5)`
    minors give `3t+8q=0` and `t+4q=0` simultaneously, so `q=0`. EMPTY.
  - *rank 2, `p^2=192q^2`*: with `q=1`, the `(1,2,7)` and `(1,2,5)` minors give
    `g*s = 8t-48` and `g*s = 8t+80`. EMPTY.
  - *rank 0* (`p=q=0`): `d[1]=ell(s,t)`, and then **all seven G3 rows vanish
    identically for arbitrary `d[2]`**.
* Hence `V(G2,G3) inter {d[1]!=0}` is exactly `{d[1]=ell(s,t), (s,t)!=(0,0)}`
  with `d[2]` free. The promoted reduction is independently re-derived.

### 4.2 Opens

The cell opens (4.3) are `union_i D(d_i[1])` together with
`D(k10[0]*k6[1]*k2[1]*mu2[1]*mu4[1]*mu6[1]*Jdet[0])`. The certificate proves
emptiness on the **strictly larger** locus `D(k10[0]) inter (D(s) union D(t))`,
which is the correct (stronger) direction. Since `(s,t) -> ell(s,t)` is
injective, `union_i D(d_i[1])` and `D(s) union D(t)` agree.

**Correction C4 (minor).** `(0.1)` is written in `(s,t)`, coordinates that
exist only after the G3 reduction. The cell-level statement is
`V(G0..G7) inter D(k10[0]) inter (union_i D(d_i[1])) = empty`; the certificate
should say the two coincide on the reduction locus.

**Scope observation, asserted about this proof only.** The kill consumes
`Lambda=t^2`, `ord_t(d)=1` and `ord_t(k10)=0`. The remaining `B11111` labels
(`ord_t k6 = ord_t k2 = ord_t mu2 = ord_t mu4 = ord_t mu6 = 1`,
`ord_t Jdet = 0`) are never used, as §5 of this review confirms empirically. I
draw **no** conclusion about any other ramified cell, load-order label, K00
support, arc, attainment, polynomial map, or JC2 from this.

### 4.3 Algebraic-closure descent

Both rank-one strata need `i`. Working over an algebraic closure is the
strongest form and the right one: emptiness over `K-bar` implies emptiness over
every subfield, and the source packet's DVR comparison explicitly permits a
finite residue extension. The two charts `eps=+-1` are handled separately and
symmetrically, and I verified the sign in both. No descent gap.

### 4.4 Field-valued vs scheme-theoretic radical

§5 is correct and correctly limited. The only radical use is
`V(I)=V(sqrt(I))`, applied to replace `V(Q_1..Q_7)` by `V(A,B)` for point-set
purposes; my `A^3,B^3 in (Q)` computation licenses exactly that and no more.
The seven original G4 generators and all later labelled rows are retained.
The ideal is genuinely nonreduced (`A^2,B^2 not in (Q)`), and the certificate
correctly claims no multiplicity, embedded-prime, tangent, or lifting
consequence. This is clean against the `sat()`-wrapping and raw-remainder
fallacies.

### 4.5 G7 emptiness implies the G38 cell is empty

Sound. The `273 = 7*39` equations include the `56` equations of grades `0..7`
verbatim; a point of the full cell restricts (by forgetting the columns of
higher index) to a point of `V(G0..G7)`; and the full cell's opens imply
`D(k10[0])` and `union_i D(d_i[1])`. So the empty smaller set forces the
larger one empty. No properness, attainment, or lifting claim is needed or
made, and the certificate makes none.

## 5. Replay, and independent fixtures/mutations (attack 5)

Run after all clean-room work was complete.

```text
python3 -B    ...replay...   -> PASS   (2.9 s)
python3 -B -O ...replay...   -> PASS   (byte-identical output)
```

Both print `CERTIFICATE_BYTES=22819` and
`CERTIFICATE_SHA256=9a8e19ab5fc95b4039206029a33923dc7f080ed332e4788e465467296e72850c`.
The replay contains **zero** bare `assert` statements (it raises through
`fail()`), so `-O` is not a vacuous pass; the identical output confirms this.
The engine is hash-checked *before* `exec_module`, and it is guarded by
`if __name__ == "__main__"`, so there is no unpinned-import execution hole.

**No discrepancy of any kind** between the replay and my clean-room results.

My own mutations, injected below the custody check by patching
`reconstruct_rows`:

```text
perturb R sector, row 1        -> fails ('unloaded surface row 1')
perturb R sector, row 7        -> fails ('unloaded surface row 7')
perturb A10 sector, row 1      -> fails ('corrected K10 G7 row 1')
perturb A10 sector, row 4      -> fails ('K10 G6 row 4')
delete labelled row 6          -> fails ('rank1 sign 1 G6 row6')
delete labelled row 7          -> fails ('G5 S7')
perturb A6 sector, row 1       -> STILL PASSES
perturb A2 sector, row 1       -> STILL PASSES
delete the A6 sector entirely  -> STILL PASSES
delete the A2 sector entirely  -> STILL PASSES
```

Plus, in my own engine: a wrong ramified load scale (`t^4 -> t^3` or `t^5`)
breaks `G6=Q(rho)` and/or `W_1,W_2`; a mutated A10 coefficient breaks
`G6=Q(rho)`, the `a,b,c,d`-freeness of G7, and `W_1`.

**Correction C8 (scope note, not an error).** The four `STILL PASSES` lines
are mathematically *correct* — K6 and K2 cannot reach grade 7 — and are an
independent confirmation of §0's "No K6, K2, target, or late-column assumption
is needed for the kill". But they mean the replay's mathematical assertions
exercise only the `R` and `A10` sectors; the K6/K2/target columns are covered
by the `tails.json` custody hash alone. The certificate should say so.

**Correction C7 (custody wording).** §5 item 1 says the replay "fails closed on
drift in the tails, compiler, source packet, promoted G3 theorem, or immutable
prefix artifacts". True in the byte-custody sense only: `COMPILER`,
`VALUATIVE`, `G3_PROMOTION`, `PREFIX_REPORT`, `PREFIX_REPLAY` are hashed but
never used mathematically, and the replay does not re-derive the G3 promotion.
This is honest custody, not verification, and should not read as verification.
The residual risk is retired by my independent G3 re-derivation in §4.1.
Separately, the `custody mutation did not fire` guard only checks that
appending a newline changes a SHA-256; it is cosmetic.

## 6. Correction register

| id | severity | where | correction |
|---|---|---|---|
| C1 | material | (1.2),(1.3) | `mu` undefined. It is `mu=(s^2,s*t/8,16*t^2,0,0,0)`. |
| C2 | material | §2 | grade-2 centering `w=d[2]-nu2`, `nu2=mu`, is unstated; §2 is false as literally written without it. |
| C3 | material | §5 item 6 | row-6 control is a positive assertion, not a fired negative control; row 6 is not load-bearing post-G3 (rows `{1,2,3,4,5}` suffice). Its real work is at G3. |
| C4 | minor | (0.1) | `D(s) union D(t)` presumes post-G3 coordinates; state the identification with `union_i D(d_i[1])`. |
| C5 | minor | (4.4) | `c3` in `(1/2)D^2c3_r(ell)[rT,rT]` is undefined; naming only, operative content (4.6) verified. |
| C6 | minor | §2 | row 4 is a total exception: `A10_4,A6_4,A2_4` all vanish identically on the surface; this explains `W_4=0`. |
| C7 | minor | §5 item 1 | custody-only pins described as fail-closed verification. |
| C8 | minor | §5 | replay assertions do not exercise the K6/K2 sectors; say so. |

None of C1–C8 changes the truth value of (0.1) or of any branch.

## 7. Promotion recommendation

```text
PROMOTE (0.1) at EXACT / POINT-SET-EMPTY, conditional on C1-C3 being appended
as an erratum to the certificate before it enters AUDIT.md.
```

Exact scope to record, and nothing beyond it:

> For the normalized ramified cell `Lambda=t^2`, `ord_t(d)=1`, `ord_t(k10)=0`,
> load-order label `B11111` of `K00-V20R2-RAM-E2-M1-B11111/v1`:
> `V(G0,...,G7) inter D(k10[0]) inter (union_i D(d_i[1])) = empty` over an
> algebraic closure, hence the full 273-equation grade-38 cell is empty.

Also worth banking, as by-products of this review rather than of the
certificate: the promoted G3 reduction is now independently re-derived
(§4.1), and `V(G2)=V(G4-cone)=V(G6-cone)=V(A,B)` with `A^3,B^3` in the ideal
and `A^2,B^2` not, which is the reusable exact form of the "reduced support"
step.

C4–C8 are documentation debt, not promotion blockers.

## 8. Scope firewall for this review

This review confirms exactly the emptiness statement above and the exactness
of the certificate's displayed identities. It establishes nothing about any
other `(e,m,load-order)` cell, about whether ramified or integer cells exhaust
closure incidence, about `C6=0`, `k10=0`, other load rays, properness of the
full source incidence, Gate T, order two, maximum twelve, K00 as a whole, jet
lifting, attainment, arcs, Keller pairs, polynomial maps, counterexamples, or
JC2. A residual cell being empty is a negative local result and nothing more.

No new exit-price assertion is made anywhere in this review, so per
`FALLACY-v2.md` no `charge_basis` line is declared; adding one would be a
false declaration.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `23079`.
- Body SHA-256:
  `48734eae98a62b886e30b858a2c12055cb60d6877b02500be1f36e18e35dca8f`.
- Frozen basis: `9b64db896b65e100839f6d75fbeea661cd818b9c`.
