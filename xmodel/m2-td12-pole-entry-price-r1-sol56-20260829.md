# td=12 symmetric pole-entry price — exact zero

Author: Sol 5.6, primary desk audit. Date: 2026-08-29 UTC.
Lifecycle: `PRODUCER_CHECKED`; different-model hostile review required.

## 0. Verdict

For each of the three source-pinned td=12 pole vertices with campaign entry
datum

```text
(alpha,beta)=(2,3),  (a_e,b_e,nu)=(1,2,3),
M=2,  w_0=3/2,  Lambda=4,
```

the literal Sigray charge and the repaired first-separation charge are both
**exactly zero**:

```text
Y(P_i)=empty,        lambda_(P_i)=0,
D_(P_i)^exit=empty,  lambda_(P_i)^exit=0.                 (PZ)
```

This is not an optimistic lower-floor convention and does not use symmetry.
It is a universal pole-purity consequence of Propositions 5.5 and 7.2.  It
holds for every pole vertex, independently of `b_e`, `M`, `w`, the number of
poles, or td.

Consequently the `+3` pole-price kill proposed in Section 9 of
`m2-td12-u1-trunk-consumer-hostile-review-opus5-20260829.md` is unavailable.
That review imported the genuine uncertainty of an **interior off-axis chain
vertex** into the **pole vertex** itself.  Its lead verdict is unchanged and
strengthened: the pole-zero premise it used for survival is derived.  The
first unresolved local price remains the trunk extra-branch cv jet, not the
pole entry.

Nothing here proves source/polynomial realizability, landing, a td=12 panel
exclusion, a counterexample, or JC2.

## 1. Custody and exact perimeter

Repository basis:

```text
cd770c92e8307cffe82e985e54ba99abf6713459
```

Pinned inputs read for this audit:

```text
9bf9f0320497dd8d5da6d7fe68ec900c1879663e6f11c121853482ca7e1623ae
  refs/sigray_full.pdf
110591663b4077509dee35f4c39daf687603c94cd3e20d559f78426da3ef6ca7
  xmodel/sigray-prop51-forced-puncture-shift-coordinator-integration-sol-ultra-20260828.md
0159cdf18f9ad1c986677d4631916dbbef0b5310829958f6dac192eab2795a31
  xmodel/sigray-section7-full-independent-audit-sol-ultra-20260828.md
af1ce600bff775bacee122bea3cd5a098ef6a457616273d8a0147c16438a0afe
  xmodel/sigray-section7-full-independent-audit-hostile-review-gpt5-20260828.md
c74fc0f99a830e3845e0821188c3f693b9b47d441e5c9f00716ac72ef2f09836
  xmodel/sigray-multipole-selected-orbit-attachment-coordinator-integration-20260828.md
859ff057586dc8aa2cbc0ff770a846b35e0a3d49ea8ea6e41b657f4ed531c1e8
  ladder/SHEET6-A2P-REVIEW.md
599e2a9123194c580b89b822f5b7a218fa5e9735b16bcb744e0f0e4231584271
  xmodel/m2-td12-u1-trunk-consumer-primary-grok46-20260829.md
91b36515950f038d08a444df16f9c09ee9763adb7950d46e9c50e43451f25c0f
  xmodel/m2-td12-u1-trunk-consumer-hostile-review-opus5-20260829.md
```

Primary-source pages were re-extracted directly: Proposition 5.3 and
Propositions 5.5--5.6 on pp. 25--27; Proposition 7.2 on p. 36; Notation 9.3
and Statements 9.3--9.5 on pp. 49--50.  The source's unproved Proposition
7.2 is used only through the campaign's proved and hostile-reviewed local
repair.  The Proposition-5.1 integration explicitly proves pole-set
non-leakage and leaves Propositions 5.3--5.8 unchanged.

No web, AWS, CAS, canonical edit, or heavy computation was used.  The
separately owned formalization repository was not accessed in any way.

## 2. The row really is the pole vertex

Write `F=P_i` for one of the three identical pole vertices and reserve
`a_e,b_e` for the entry integers, to avoid confusing `a_e` with the fibre
value.  The source-pinned row gives

```text
(D_F,D_(g,F))       = a_e*(alpha,beta) = (2,3),
(deg p_F,deg p_(g,F)) = b_e*(alpha,beta) = (4,6),
nu_F=3.
```

Hence, using Notation 8.1 and Statement 9.1,

```text
M_F    = gcd(4,6) = 2,
kbar_F = D_F+D_(g,F) = 5,
rho_F  = D_F/deg p_F = 1/2,
w_F    = (kbar_F-rho_F)/nu_F = 3/2,
Lambda(F) = D_(g,F)*deg p_F/nu_F = 4.
```

Thus `(1,2,3), M=2, w=3/2` is data at `F in T_(a,pole)`, not data at an
unnamed first child below it.  Pole vertices lie in `V_a intersect
T_a^searrow`, so Notation 9.3 types `Y(F)` and `lambda_F` there.  This
typing is also used by the source's characteristic-sequence Statement 9.5.

## 3. Universal pole-zero lemma

**Lemma (`POLE-EXIT-ZERO`).**  Let `F` be any y-side pole vertex of a
Sigray-normalized Keller counterexample on the fibre `f=a`.  Then

```text
Y(F)=empty and lambda_F=0.
```

**Proof.**  Suppose `H in Y(F)`.  Literal Notation 9.3 supplies one
puncture `P` and heights `u,pi(H)` on its ray such that

```text
F=I_P(u),             H=I_P(pi(H)),       H in T_(a,cv).   (1)
```

Because `F in T_(a,pole)` lies on this same ray, Proposition 5.5 gives

```text
g(P)=infinity.                                             (2)
```

Because the ray contains the critical-value flag `H`, repaired Proposition
7.2 gives

```text
g(P) in C.                                                 (3)
```

Equations (2) and (3) contradict one another.  Therefore `Y(F)` is empty,
and its defining sum in Notation 9.3 is exactly zero. QED.

This proof uses neither Statement 9.3's lower bound nor a budget ceiling.
It does not use regularity, `M=1`, a chain normal form, symmetry, or the
withdrawn Euler equality (22).  In particular nothing changes when
`b_e=M=2`.

The same proof is valid under the promoted first-separation replacement.
Indeed, a selected exit at `F` with cv witness `H(F,d)=I_P(v)` has by
construction `F=I_P(u)` on that very ray.  Proposition 5.5 again says
`g(P)=infinity`, while `H(F,d) in T_(a,cv)` and Proposition 7.2 say
`g(P) in C`.  Therefore there is no selected priced direction at a pole:

```text
D_F^exit=empty,        lambda_F^exit=0.                    (4)
```

This also disposes of the apparent pole-endpoint branch discussed in the
hostile review of the attachment lemma.  A ray may be an abstract contact
continuation beyond an endpoint of the truncated pole union, but if it
actually passes through a vertex in `T_(a,pole)`, it cannot carry a cv flag.
The attachment/MFE theorem only becomes easier: its selected set shrinks.

## 4. Exhaustion of the `(1,2,3)` pole directions

The row admits no hidden third branch type.  Since `nu_F=3` divides
`beta=3` and `deg p_F-1=3`, Statement 5.2 and Proposition 5.4 force the
second semi-invariant form.  Proposition 5.3(v) makes `p_F` squarefree, so,
up to a nonzero scalar,

```text
p_F(eta) = eta*(eta^3-A),             A != 0.              (5)
```

Corrected Statement 3.18 therefore gives exactly two effective root
directions:

1. the fixed zero orbit `c=0`;
2. one nonzero `mu_3` orbit, represented by `c!=0` with `c^3=A`.

Every puncture in either direction has a ray through `F`, hence is a pole
of `g` by Proposition 5.5.  Its formula (18) gives the two pole orders

```text
c=0:     D_(g,F)/nu_F = 3/3 = 1,
c!=0:    D_(g,F)             = 3.
```

They sum to `1+3=4=Lambda(F)`, exactly Proposition 5.6.  Thus both
effective `p`-directions are pole directions and neither can support a
finite critical-value witness.  Roots of `p_(g,F)` off `p_F` do not define
tree directions: Statement 3.18 realizes roots of `p_F`, not q-only roots.
This exhausts the zero branch, the nonzero cyclic branch, and the possible
q-only residue.

## 5. The scope boundary that caused the regression

`BOOK-OFFAXIS.md` Section 2(c1) says something different and remains
correct: at an **interior merge-free segment vertex below a pole**, `M>=2`
does not exclude a separating ray, so that interior vertex can have a
nonempty exit set; neither zero nor a positive lower bound is automatic.
A finite puncture may share such a lower flag and split away before ever
reaching the pole vertex.  Proposition 5.5 then does not force it to be a
pole.

At the pole vertex itself, no ray has that escape: sharing the pole flag is
already the hypothesis of Proposition 5.5.  Therefore:

```text
pole F=P_i with datum (a_e,b_e,nu):     exact price 0;
unnamed interior child/segment vertex:  not priced by the entry tuple alone.
```

The Opus trunk review quotes the interior-segment warning and applies it to
the three pole vertices.  That step is false.  The older hostile-reviewed
two-pole audit already records the correct source consequence
`lambda_pole=0`; the value never depended on `b=1`.

If “pole-entry exit” were intended to mean a first **interior child** rather
than `P_i`, the tuple `(1,2,3),M=2,w=3/2` is insufficient: one must supply
that child's `Q`-datum, its realized direction orbits, and whether the route
actually inserts it.  Such a child is a different object and is not one of
the three “pole entry vertices” charged by the reviewed td=12 report.

## 6. Consequence for the td=12 U1 route

For the displayed symmetric route, the three pole contributions are now
derived:

```text
sum_(i=1)^3 lambda_(P_i)^exit = 0.                         (6)
```

The merge price `lambda_G=0` was separately derived from the U1 merge
normal form.  Hence no base charge changes the reviewed first-trunk budget.
For the `(2/3,3)@nu_F=25` trunk cell, the lower floor remains 8 and the
terminal ceiling remains 9, so its possible exact charge is still `{8,9}`.
For the `(3/4,4)@nu_F=17` sibling, floor and ceiling both equal 8.

What changes is epistemic and strategic:

- the pole-zero assumption is discharged at reviewed source tier;
- symmetry cannot amplify an unknown pole unit into `+3`;
- the proposed pole-price discriminator is closed with a zero result;
- the best remaining local discriminator is the extra-branch trunk cv jet
  (or a separate interior chain vertex if a longer entry route inserts one).

Thus this computation strengthens `FAMILY_SURVIVES_FIRST_TRUNK`; it does
not kill that family.

## 7. Hypotheses, exclusions, and review risks

The exact hypothesis chain is:

1. a Sigray-normalized polynomial Keller counterexample and a fixed fibre;
2. `F in T_(a,pole)` with the reviewed pole-set non-leakage repair, so
   Propositions 5.3--5.8 retain their intended pole meaning;
3. repaired Proposition 7.2: a puncture is finite-valued exactly when its
   ray contains a critical-value flag;
4. literal Notation 9.3, or its promoted first-separation replacement.

The raw thesis prints Proposition 7.2 without proof.  The Section-7 audit
proves it from the centred threshold and leading-bracket equation, and its
hostile review accepts that local repair; the hostile review's material
qualification concerns the later Euler ledger, not Proposition 7.2.  A
consumer refusing campaign repairs must therefore label (PZ) conditional
on the printed Proposition 7.2, not “unknown in both directions.”

The proof does **not** use literal Proposition 7.5 (22), per-puncture
`delta`, `(22-cl)`, cross-fibre `kappa`, an equality/slack upgrade, MP8's
old no-refinement claim, or a complete off-axis chain grammar.  It must not
be extended from poles to arbitrary `M>=2` chain vertices.

Reviewers should attack four points explicitly:

1. whether Notation 9.3's witnessing puncture is indeed the same puncture
   to which Propositions 5.5 and 7.2 apply;
2. whether the Proposition-5.1 non-leakage repair really preserves the
   identification of `T_(a,pole)` used by Proposition 5.5;
3. whether a selected first-exit witness at a pole can avoid passing through
   its base flag (it cannot by definition); and
4. whether “pole entry” has silently been redefined to mean an interior
   child rather than the source datum at `P_i`.

## 8. Maximum safe consequence

At the reviewed Sigray/source-repair tier:

> Every actual pole vertex has empty literal and selected critical-value
> exit sets, hence exact lambda zero.  In particular each of the three
> td=12 type-`(2,3)` poles with `(a_e,b_e,nu)=(1,2,3)`, `M=2`, `w=3/2`
> contributes zero to the shared first-separation budget.  This removes the
> proposed symmetric `+3` kill and leaves the reviewed U1 first-trunk family
> alive, subject to its already recorded trunk-jet, transport, landing, and
> realizability gaps.

---

Report-body SHA-256 (computed as the bytes before the separator line above):
`9fcc2c5c1f987189cc1eaf0dcc98a6748da4b6ba4a67b2969c24f05340e1dcd7`.
