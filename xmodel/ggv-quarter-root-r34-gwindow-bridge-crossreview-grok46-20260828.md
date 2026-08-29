# Hostile cross-review: row-34 zero-tail class-to-raw endpoint bridge

Reviewer: Grok 4.6 (xAI), different-model hostile referee  
Pinned model ID: `grok-4.6`  
CLI/version: `grok 1.0.5 (5115b46bc909)` (`/Users/dc/.grok/bin/grok`)  
Host: Python 3.14.6, Darwin 23.6.0 arm64  
Date: 2026-08-28 UTC  
Charged source:
`xmodel/ggv-quarter-root-r34-gwindow-bridge-r0-sol-ultra-20260828.md`  
Producer: Sol Ultra (different model family ⇒ this is a valid promotion
leg if it survives)

No JC2 theorem, face/family exclusion, landing claim, polynomial Keller
pair, or statement about any `F` other than the displayed zero-tail
section is made.  Parents keep their rollback labels.

## 0. Headline verdict

**Every charged exact atom survives independent rederivation.  Nothing
charged is REFUTED or REPAIRED.  No load-bearing GAP remains.**  Direct
attacks on lower/higher `X`-constants, on the `A` versus `X^4`
particular, and on nilpotent `G_16,G_18,G_20` all fail to cancel the
reduced weight-22 primitive or to invert `D_22-1`.

| # | Charged claim | Verdict |
|--:|---|---|
| 1 | Literal F/G windows, `G_21 in <X^3>`, `G_22=0`, `G_n=0` for `n>=22` | **CONFIRMED** |
| 2 | Full characteristic solution `(0.3)--(0.4)`, including `Phi(s)`, endpoint term, `c_0=1` | **CONFIRMED** |
| 3 | Reconstruction `G=P_hat^12 W(X,t/P_hat)` and every displayed exponent/sign | **CONFIRMED** |
| 4 | Reduction modulo `(u,v)`: characteristic constants cannot mix into or rescue weight 22 | **CONFIRMED** (also after the unreduced nilpotent mixing attack) |
| 5 | Raw `D_22` with every allowed `G_16,G_18,G_20`; unit ideal over `Q[u,v]/(uv,u^4,v^2)` | **CONFIRMED** |
| 6 | Endpoint emptiness is rollback-independent for the displayed `F`, while the row-34 class reading stays provisional | **CONFIRMED** |
| 7 | Firewalls: one zero-tail Artin slice, not a branch-P family, face exclusion, landing theorem, counterexample, or JC2 result | **CONFIRMED** |

Two independent emptiness certificates survive:

* characteristic, after reduction modulo `m=(u,v)`: `G_22 ≡ p^{-10}(c_22-(epsilon/8)J) (mod m)` cannot vanish;
* raw: `D_22 in m S[X]` for the polynomial ring `S` on allowed `G` coefficients, so `D_22-1` generates the unit ideal.

The second does not use the class descendant, Hensel uniqueness, or the
characteristic theorem.  That is the clean certificate.

**Narrowest promotion.** Promote the emptiness of the raw endpoint fibre
product of the displayed section

```text
F=A^4+4u A^2 B t^2+2u^2 B^2 t^4+v t^6
    in R[X,t],   R=Q[u,v]/(uv,u^4,v^2)
```

against the frozen `G` support window and the exact target `D_22=1`, at
desk-algebra scope, and nothing wider.  Do not promote the row-30/row-34
class ancestry, the 24-slot descendant, any other newest-slot section, or
any GGV/JC2 claim.

**Stop/continue.** **STOP this zero-tail Artin section.**  **CONTINUE**
the class-to-raw bridge only on a section whose reduced positive-weight
`F_i` are not all zero, so some pair `F_i G_(22-i)` can supply the
scalar endpoint without a forbidden `G_22`.

---

## 1. Custody

Charged SHA-256, recomputed on live bytes before the algebra below and
again immediately before this write:

```text
c068afae0b00f0017d886d28e8fa2797a03c1ca0f7ac2b8cd195bbf108f7e537
  xmodel/ggv-quarter-root-r34-gwindow-bridge-r0-sol-ultra-20260828.md
```

Fail-closed test: the hash equals the prompt pin.  Every additional
local file opened is one the charged report names.  Recomputed hashes
match the producer’s §1 block exactly:

```text
525c408e92b7f2cb11f5152e002e60a20a331d268283f1be30fb13b5a104b990
  xmodel/ggv-quarter-root-r34-algprim-artin-bridge-r0-sol-ultra-20260827.md
e5a2c968e516a40509d136cfd57613c8be84e50041444ce8146916b976bdf24c
  xmodel/ggv-quarter-root-r30-slice-descendant-r0-sol-ultra-20260827.md
9d35c678cfc257c5c518f87c19df25942cbaca3b5aa8186a22507f1f1e1f3ae1
  xmodel/ggv-quarter-root-characteristic-de-rham-tower-r7r1-sol-20260827.md
7ab758fa002c75cd28d81540e8f63fd8cd0de97fad791afedfeb5fb610c6cb29
  xmodel/ggv-quarter-root-characteristic-de-rham-tower-r7r1-hostile-review-fable5-20260827.md
28b9b05c02224aadec30d52b66ed22db80aabe416ffdc0186f6931f1978f1876
  cases/ggv_8_28_raw_to_global_m_cokernel_interface_d3_20260827/RAW_INPUT.json
f3c758e052d95252438fb9665ac2f2b27705019e91a41c2aa851dd41e9463bf4
  cases/ggv_8_28_raw_to_global_m_cokernel_interface_d3_20260827/compile_d3.py
f0fe0f5dd01d9d47f6b7ee58d3e3426e482a4f8c9d31a81bfa2094782d010e00
  xmodel/ggv-8_28-raw-global-determinant-d5g35-sol2-20260827.md
ba7162fe8fd7c4f607839ce2c18525c6aa21a322343a938f738d7ec514113a2d
  xmodel/ggv-8_28-raw-global-determinant-d5g35-hostile-review-grok-20260827.md
```

Licensed inputs used but not re-proved as general theorems: the R7R1
conjugacy `W_X|s=-(s^22/8)(Q+(s/2)Q_s)` as an identity over a
characteristic-zero field (Fable5 already confirmed it; it is re-checked
on this exact section in §3), and the parent claim that the displayed
`F` is a row-34 class-prefix section (unused by the raw certificate).
The `2S/3S` lattice inequalities are taken from the frozen compiler
`compile_d3.py` / D3 JSON maps and then used to rederive every window.

The producer replay was not executed as a block.  All identities below
are independent `fractions.Fraction` desk arithmetic in a five-tuple
sparse ring with a binary multiplier, plus a direct read of the frozen
`G` slot list.  No CAS, Groebner basis, random seed, AWS host, or hidden
file input.  No path under `jc2-lean` was listed, opened, searched,
read, built, statused, or modified.  No canonical ledger was read or
edited.  No unrelated ideation submission was opened.

This file is the only write.

---

## 2. Charge item 1 — literal F/G windows, especially `G_21` and `G_22`

**Verdict: CONFIRMED.**

Frozen D3 maps, read from `RAW_INPUT.json` and matching
`compile_d3.py`:

```text
x^i y^j |-> t^(8+3i-j) X^i     for F,
x^i y^j |-> t^(12+3i-j) X^i    for G.
```

The `2S/3S` lattice in the frozen compiler is

```text
F:  0 <= i <= 16,  max(0, 4i-8)  <= j <= 3i+8,   weight n=8+3i-j,
G:  0 <= i <= 24,  max(0, 4i-12) <= j <= 3i+12,  weight n=12+3i-j.
```

Eliminating `j` independently: `j=12+3i-n` for `G`, and the two
nontrivial inequalities collapse to

```text
max(0, ceil((n-12)/3))  <= i <= 24-n,
```

because `j <= 3i+12` is automatic.  The `F` analogue is
`max(0, ceil((n-8)/3)) <= i <= 16-n`.  This is the producer’s (2.1).
An empty interval means the coefficient is the zero polynomial.

Specializing:

```text
n=21:  lo=ceil(9/3)=3, hi=3  =>  G_21 in <X^3>,
n=22:  lo=ceil(10/3)=4, hi=2 =>  empty, so G_22=0.
```

For every `n>=22`, `lo >= 4` and `hi=24-n <= 2`, so the interval stays
empty.  A full lattice scan over `0 <= n <= 79` (no `n<=22` cutoff)
gives maximum `G` weight 21, maximum `F` weight 14, 141 `F` slots and
301 `G` slots, and no slot of weight `>=22`.  The D3 dump
`raw_slots_through_weight_22` is therefore a complete polygon, not a
truncation.

Frozen JSON independently: `G` weights present are `0..21`; the unique
weight-21 slot is `g_3_0` with chart image `t^21*X^3`; weight 22 has
count 0.  Allowed endpoint-adjacent windows used in §6:

```text
G_16: deg in {2,3,4,5,6,7,8}     (JSON count 7),
G_18: deg in {2,3,4,5,6}         (JSON count 5),
G_20: deg in {3,4}               (JSON count 2).
```

Displayed `F` respects the `F` windows: `deg(A^2 B)=11 <= 14`,
`deg(B^2)=6 <= 12`, `deg(v)=0 <= 10`.  The only support fact needed for
emptiness is `G_22=0`.  The `G_21` claim is true and unused by `D_22`
on this `F`, because `F_1=0`.

---

## 3. Charge item 2 — full characteristic solution, `Phi(s)`, endpoint, `c_0=1`

**Verdict: CONFIRMED.**

Write `A=X^4-1`, `B=A'=4X^3`, `J=X^5/5-X`, so `J'=A`.  The parent
whole-series identity, rechecked as an exact sparse identity in
`R[X,s]/(epsilon^2-1)`, is

```text
Q = epsilon A + u B s^2 + (v/4) s^6.                 (Q)
```

The implicit equation `Q^4 = A^4 + 4u A^2 B s^2 Q + 2u^2 B^2 s^4 Q^2
+ v s^6 Q^3` holds with zero remainder.  At `s=0`, `Q=epsilon A=p^2`.
The `Q`-derivative of the implicit left-minus-right side at that point
is `4 epsilon A^3`, a unit in `R(X)`.  Formal uniqueness in `R(X)[[s]]`
therefore identifies `(Q)` with the selected branch.  This desk check
does not promote the class-prefix reading of `F`.

R7R1 conjugacy, specialized and then re-expanded:

```text
Q + (s/2) Q_s
  = epsilon A + u B s^2 + (v/4) s^6
    + (s/2)(2u B s + (3v/2) s^5)
  = epsilon A + 2u B s^2 + v s^6.
```

Hence

```text
W_X|s = -(s^22/8)(epsilon A + 2u B s^2 + v s^6)
      = -(epsilon/8) A s^22 - (u/4) B s^24 - (v/8) s^28.
```

Coefficientwise integration in `X`, `s` held constant, using `J'=A`,
`A'=B`, and `1'=0`, produces exactly

```text
W = Phi(s)
    - (epsilon/8) J s^22
    - (u/4) A s^24
    - (v/8) X s^28,
Phi(s) = sum_(m>=0) c_m s^m,   c_m in ker(d/dX).
```

There are no further particular terms: `(Q)` has only `q_0,q_2,q_6`
nonzero, and the R7R1 coefficient law `w_(n+22)'=-(n+2)q_n/16`
reproduces the same three antiderivatives

```text
n=0:  w_22' = -q_0/8 = -(epsilon/8) A,
n=2:  w_24' = -q_2/4 = -(u/4) B,
n=6:  w_28' = -q_6/2 = -v/8.
```

The homogeneous equation is `W_X=0`.  Over any `Q`-algebra, in
characteristic zero, `ker(d/dX)` on `R[X]`, `R(X)`, or the algebraic
function field of `p^2=epsilon A` is the constant ring.  Nilpotents do
not create extra kernel: `(u X)'=u != 0`.  Writing `ker(d/dX)` rather
than `R` only allows a harmless extension of the ground constants, as
the producer states.

**Attack: `A` versus `X^4` in the `u`-term.**  Replacing `A` by `X^4`
yields another particular solution, because `(X^4)'=B=A'`.  The
difference is `(u/4)s^24`, an `X`-constant, hence absorbed in `Phi`.
The displayed representative is legitimate.  Not a repair.

**Endpoint restoration.**  The parent assembled primitive
`beta=-(u/4)A s^24-(v/8)X s^28` starts at order 24 and omits `w_22`.
Imposing `D_22=1` rather than only post-endpoint class exactness adds
precisely `w_22=c_22-(epsilon/8)J`.  Confirmed.

**Normalization `c_0=1`.**  At `s=0` the particular solution vanishes,
so `W(X,0)=c_0`.  Then `G_0=p^{12} c_0`.  Now `p^{12}=(p^2)^6=
(epsilon A)^6=A^6` because `epsilon^2=1`.  The condition `G_0=A^6`
is exactly `c_0=1`.  It does not constrain `c_22`.

R7R1 is stated over a field; the calculation above is an identity in
the Artin ring `R`, obtained by direct expansion, not by an illicit
invocation of a field-only existence theorem.

---

## 4. Charge item 3 — original-coordinate reconstruction and exponents

**Verdict: CONFIRMED.**

With `P_hat^8=F`, `P_hat(X,0)=p`, and `s=t/P_hat`, substitute (0.3)
into `G=P_hat^{12} W(X,t/P_hat)`:

```text
G = sum_m c_m t^m P_hat^{12-m}
    - (epsilon/8) J t^22 P_hat^{12-22}
    - (u/4) A t^24 P_hat^{12-24}
    - (v/8) X t^28 P_hat^{12-28}
  = sum_m c_m t^m P_hat^{12-m}
    - (epsilon/8) J t^22 P_hat^{-10}
    - (u/4) A t^24 P_hat^{-12}
    - (v/8) X t^28 P_hat^{-16}.
```

Every exponent and every sign matches (0.5).  Negative powers of
`P_hat` are formal power series in `t` because the constant term `p`
is nonzero; they are not polynomial descent.

**Attack: formula (4.2).**  Clearing `A^5` in the displayed square-root
formula and raising to the fourth power recovers `F` identically after
multiplying through by `A^{20}`.  The apparent `u^3 t^6` contributions
in `(A+delta)^4` are

```text
4 A^3 * (2u^3 B^3/A^5) =  8 u^3 B^3 / A^2,
6 A^2 * 2 alpha_2 alpha_4 = -12 u^3 B^3 / A^2,
4 A * alpha_2^3         =  4 u^3 B^3 / A^2,
```

and `8-12+4=0`.  Only `v` remains at `t^6`.  Formula (4.2) is correct
and is not needed for the endpoint decision, which uses only
`P_hat ≡ p (mod m)`.

The three categories in the producer’s §4 are distinct and correctly
typed: (0.3) is an exact formal characteristic solution; (0.5) is an
algebraic formal series in the original coordinate; a campaign client
must still lie in the literal polynomial module with coefficients in
(2.1).  The last fails.

---

## 5. Charge item 4 — reduction modulo `(u,v)` and mixing of constants

**Verdict: CONFIRMED.**

Modulo `m=(u,v)`, `F ≡ A^4`, so `P_hat^8 ≡ A^4`.  Combined with
`P_hat(X,0)=p` and `p^8=A^4`, formal uniqueness of the binomial eighth
root gives `P_hat ≡ p`, independent of `t`.  The `u` and `v` terms of
(0.5) vanish, and

```text
G_bar = p^{12} Phi_bar(t/p) - (epsilon/8) J t^22 p^{-10}.
```

Because `p` has no positive `t`-coefficients after reduction, weights
do not mix:

```text
G_22 ≡ p^{-10}(c_22 - (epsilon/8) J)  (mod m).
```

The frozen window forces `G_22=0`.  Since `p^{-10} != 0` in the
function field, this requires `c_22=(epsilon/8)J`.  The left side is
killed by `d/dX`; the right side has derivative `epsilon A/8 != 0`.
Both signs `epsilon in {+1,-1}` fail.

**Attack: lower `c_m` before reduction.**  Unreduced, `P_hat=p+O_t(m)`,
so for `m<22`

```text
[t^{22}] (c_m t^m P_hat^{12-m})
  = c_m [t^{22-m}] P_hat^{12-m}  in m
```

because `22-m>0`.  Higher `c_m` (`m>22`) start at `t^m` since `P_hat`
has a nonzero constant term and no negative `t`-powers.  The `u` and
`v` particular terms start at `t^{24}` and `t^{28}`.  Therefore

```text
G_22 = p^{-10}(c_22 - (epsilon/8)J) + (element of m).
```

A nilpotent correction cannot cancel a reduced term that is nonzero in
`Q(X,p)`.  Choosing `c_m` in a larger constant ring does not help:
every `c_m` remains `X`-constant.  Choosing `c_22` with nilpotent
`X`-dependence still cannot make `c_22-(epsilon/8)J` have vanishing
derivative, because `J'` is the non-nilpotent polynomial `A`.

**Attack: polynomial-surviving lower constants.**  After reduction,
`[t^n](p^{12} Phi_bar(t/p))=c_n p^{12-n}`.  Even `n=0,2,...,12` with
`c_0=1` can be polynomial (`p^{12-n}=(epsilon A)^{6-n/2}` lies in the
`G_n` window).  Odd `n` and even `n=14,16,18,20` are forced to
`c_n=0` by polynomial descent.  None of these contributes to reduced
weight 22.  The obstruction (0.6) is not an artifact of setting `Phi=1`.

Dropping the post-endpoint `u,v` terms of `W` likewise cannot rescue
`G_22`: those terms do not meet weight 22.

---

## 6. Charge item 5 — raw `D_22`, allowed `G_16,G_18,G_20`, unit ideal

**Verdict: CONFIRMED.**

Chart `x=t^3 X`, `y=t^{-1}`, `F=t^8 f`, `G=t^{12} g`.  The coordinate
Jacobian is `-t`.  Direct expansion of `[f,g]_(x,y)` produces

```text
E = 12 F_X G - 8 F G_X - t(F_X G_t - F_t G_X) = sum_n D_n t^n,
```

and the coefficient of `t^n` is

```text
D_n = sum_{i+j=n} ((12-j) F_i' G_j + (i-8) F_i G_j').
```

On the displayed `F`, the `t`-support is `{0,2,4,6}`.  Literal
`G_22=0` kills the pair `(i,j)=(0,22)`.  The only surviving pairs at
weight 22 are `(2,20)`, `(4,18)`, `(6,16)`:

```text
(2,20): (12-20) F_2' G_20 + (2-8) F_2 G_20'
      = -8 (4u A^2 B)' G_20 - 6 (4u A^2 B) G_20'
      = -32u (A^2 B)' G_20 - 24u A^2 B G_20',

(4,18): (12-18) F_4' G_18 + (4-8) F_4 G_18'
      = -6 (2u^2 B^2)' G_18 - 4 (2u^2 B^2) G_18'
      = -12 u^2 (B^2)' G_18 - 8 u^2 B^2 G_18',

(6,16): (12-16) F_6' G_16 + (6-8) F_6 G_16'
      = -4 v' G_16 - 2 v G_16'
      = -2v G_16',
```

using `F_6=v` constant in `X`.  This is the producer’s (6.2).  It
allows every frozen-window coefficient of `G_16,G_18,G_20`; no lower
determinant row is used.

Independent check: fill every allowed monomial of `G_0,...,G_21` with
coefficient `1` and compute `E` from the Jacobian.  The extracted
`D_22` has 18 terms, all in `m`, and equals (6.2) on that
specialization.  Filling the same legal `G` slots on the reduced
origin `F=A^4` yields `D_22=0` identically.

**Attack: illegal `G_22`.**  Adjoining the non-window monomial `X^2 t^{22}`
produces a nonzero reduced `D_22`, equal to the pair
`(12-22)(A^4)' G_22 + (0-8) A^4 G_22'`.  A weight-22 slot would change
the problem.  The frozen polygon does not have one.

**Unit ideal.**  Let `S` be the polynomial ring over `R` on all allowed
`G` coefficients.  Then `D_22 in m S[X]`.  The equation `D_22=1` is the
coefficient ideal

```text
I = (n_0 - 1, n_1, n_2, ...) subset S,    n_k in m S.
```

Already `n_0-1=-1+n` with `n in m S`.  In `R`, `m=(u,v)` satisfies
`m^2=(u^2)`, `m^3=(u^3)`, `m^4=0` because `uv=v^2=u^4=0`.  For any
such `n`, `n^2 in (u^2)S`, `n^4=0`, and

```text
(-1+n) * (-(1+n+n^2+n^3)) = (1-n)(1+n+n^2+n^3) = 1-n^4 = 1.
```

So `-1+n` is a unit of `S` and `I=(1)`.  The endpoint fibre product is
the empty scheme, not merely a scheme without `Q`-points and not merely
a tangent-space vanishing.  The same geometric series shows that even
the single scalar equation `u Y=1` is already empty over this Artin
base; nilpotent `G` directions cannot invert `u` or `v`.

If the target were changed from `D_22=1` to `D_22=0`, the unit
obstruction would disappear, while the class/primitive tail would be
unchanged.  That distinction is correct.

The producer’s phrase “the scalar coefficient equation” is a gloss for
this coefficient-ideal argument.  The algebra is the same; not a
repair.

A cokernel weakening of the target (D3 Morse seven-vector) cannot
rescue the slice either: the reduced identity would still be `0=1`.

---

## 7. Charge item 6 — rollback independence for the displayed `F`

**Verdict: CONFIRMED.**

Section 6 of the producer uses only: the displayed polynomial `F`, the
displayed ring `R` with `m=(u,v)`, the frozen support fact `G_22=0`,
and the determinant recurrence.  It does not use the class descendant,
Hensel uniqueness, `Q`, `W`, or `Phi`.

Consequently a future repair of the *interpretation* of this `F` as a
row-34 class section would not alter the algebraic emptiness statement
about this coefficient problem.  The row-30/row-34 ancestry remains
provisional, as charged, and is not used.

Two layers should be kept distinct:

* reduced-origin emptiness (`D_22 ≡ 0 != 1 (mod m)`) uses only that
  every positive-weight coefficient of the displayed `F` lies in `m`;
* scheme-theoretic emptiness (`I=(1)`) uses `m^4=0`.

Both are statements about the displayed pair `(F,R)`.  If a parent
rollback replaces `R` or `(0.1)`, the unit inverse must be recomputed;
the characteristic formulae `(0.3)--(0.6)` must be recomputed if `(0.2)`
changes.  That is exactly the producer’s rollback clause.  It is not a
gap in the charged emptiness of the displayed slice.

---

## 8. Charge item 7 — firewalls

**Verdict: CONFIRMED.**

The report decides, on this exact zero-tail Artin section, that the
raw endpoint intersection with the frozen `G` window is empty.  It
does not:

* promote the provisional row-30/row-34 class-scheme ancestry;
* exclude the other 24 newest `F` slots, another class-prefix section,
  or the full branch-`P` family;
* say anything about a polynomial `G` if the source polygon is enlarged
  to admit weight 22;
* contradict passage of class rows or of `GATE-ALG-PRIM` (those are
  necessary shadows that do not encode this support failure);
* export a raw solution, endpoint normalization for other slices, face
  or family exclusion, GGV landing, counterexample, or JC2 conclusion.

The global GGV leading forms `F_0=(X^8-1)^2`, `G_0=(X^8-1)^3` of the
D3 weight-zero specialization are a different problem.  The charged
section uses branch-`P` leading data `H=A^2`, `F_0=A^4`, `G_0=A^6`,
which fit the same *support* windows.  Emptiness of `D_22=1` does not
depend on `G_0`.  No overclaim is made.

---

## 9. Stop/continue and narrowest promotion

**STOP this zero-tail Artin section.**  Later class rows and a larger
raw elimination on the same `F` cannot add information: the endpoint
ideal is already `(1)`.

**CONTINUE the class-to-raw bridge on a section with a genuine reduced
raw endpoint point.**  The useful prerequisite is that some
positive-weight `F_i` remain nonnilpotent after reduction, so a pair
`F_i G_(22-i)` with `i>0` and `22-i<=21` can produce the scalar `1`
without a `G_22` slot.  Only after that reduced test passes is it
worth solving lower raw rows or the full polynomial-window descent.

**Promote, at desk-algebra scope and nothing wider:** emptiness of the
raw endpoint fibre product of the displayed `(F,R)` against the frozen
`G` window and `D_22=1`.  The characteristic reconstruction and the
`mod m` incompatibility of `G_22=0` with the endpoint primitive are
confirmed on this same displayed section, and may be cited as such.
Do not promote parents, other sections, or any campaign-level theorem.

---

## 10. Independent replay

Binary-multiplier sparse ring, `uv=u^4=v^2=0`, `epsilon^2=1`.  This is
not the producer script: it also checks (4.2), the Jacobian versus
(6.2), the lattice-versus-formula windows, frozen JSON `G_22`, and the
unit inverse.

```bash
python3 - <<'PY'
from fractions import Fraction as F
from collections import Counter
import json

def N(d):
    o={}
    for (x,t,u,v,e),c in d.items():
        c=F(c)
        if not c or u>=4 or v>=2 or (u and v):
            continue
        k=(x,t,u,v,e%2)
        o[k]=o.get(k,F(0))+c
        if not o[k]: del o[k]
    return o
def add(*ps):
    o={}
    for p in ps:
        for k,c in p.items(): o[k]=o.get(k,F(0))+c
    return N(o)
def mul(p,q):
    o={}
    for a,ca in p.items():
        for b,cb in q.items():
            k=(a[0]+b[0],a[1]+b[1],a[2]+b[2],a[3]+b[3],a[4]+b[4])
            o[k]=o.get(k,F(0))+ca*cb
    return N(o)
def prod(*ps):
    r={(0,0,0,0,0):F(1)}
    for p in ps: r=mul(r,p)
    return r
def smul(s,p): return N({k:F(s)*c for k,c in p.items()})
def mpow(p,n):
    r={(0,0,0,0,0):F(1)}
    for _ in range(n): r=mul(r,p)
    return r
def dX(p): return N({(x-1,t,u,v,e):c*x for (x,t,u,v,e),c in p.items() if x})
def dT(p): return N({(x,t-1,u,v,e):c*t for (x,t,u,v,e),c in p.items() if t})
def mon(c=1,**kw):
    return N({(kw.get('X',0),kw.get('T',0),kw.get('u',0),kw.get('v',0),kw.get('e',0)):F(c)})

X,T,U,V,Eps,one=mon(X=1),mon(T=1),mon(u=1),mon(v=1),mon(e=1),mon()
A=add(mpow(X,4),smul(-1,one)); B=dX(A)
J=add(smul(F(1,5),mpow(X,5)),smul(-1,X))
assert dX(J)==A and B==smul(4,mpow(X,3))

Qs=add(prod(Eps,A),prod(U,B,mpow(T,2)),smul(F(1,4),prod(V,mpow(T,6))))
rhs=add(mpow(A,4),
        smul(4,prod(U,mpow(A,2),B,mpow(T,2),Qs)),
        smul(2,prod(mpow(U,2),mpow(B,2),mpow(T,4),mpow(Qs,2))),
        prod(V,mpow(T,6),mpow(Qs,3)))
assert add(mpow(Qs,4),smul(-1,rhs))=={}

combo=add(Qs,smul(F(1,2),mul(T,dT(Qs))))
assert add(combo,smul(-1,add(prod(Eps,A),smul(2,prod(U,B,mpow(T,2))),prod(V,mpow(T,6)))))=={}
Wpart=add(smul(F(-1,8),prod(Eps,J,mpow(T,22))),
          smul(F(-1,4),prod(U,A,mpow(T,24))),
          smul(F(-1,8),prod(V,X,mpow(T,28))))
assert add(dX(Wpart),smul(-1,smul(F(-1,8),mul(mpow(T,22),combo))))=={}
# A vs X^4 is an X-constant:
Walt=add(smul(F(-1,8),prod(Eps,J,mpow(T,22))),
         smul(F(-1,4),prod(U,mpow(X,4),mpow(T,24))),
         smul(F(-1,8),prod(V,X,mpow(T,28))))
assert dX(add(Wpart,smul(-1,Walt)))=={}

ZA5=mul(Eps,add(mpow(A,6),prod(U,B,mpow(A,4),mpow(T,2)),
         smul(-1,prod(mpow(U,2),mpow(B,2),mpow(A,2),mpow(T,4))),
         mul(add(smul(2,prod(mpow(U,3),mpow(B,3))),
                 smul(F(1,4),prod(V,mpow(A,2)))),mpow(T,6))))
Fpoly=add(mpow(A,4),smul(4,prod(U,mpow(A,2),B,mpow(T,2))),
          smul(2,prod(mpow(U,2),mpow(B,2),mpow(T,4))),prod(V,mpow(T,6)))
assert add(mpow(ZA5,4),smul(-1,mul(Fpoly,mpow(A,20))))=={}
assert 12-22==-10 and 12-24==-12 and 12-28==-16 and 8-12+4==0

def ceil_div(a,b): return -((-a)//b)
def G_degs(n):
    return [i for i in range(25)
            if max(0,4*i-12) <= 12+3*i-n <= 3*i+12]
def formula_G(n):
    lo,hi=max(0,ceil_div(n-12,3)),24-n
    return list(range(lo,hi+1)) if lo<=hi else []
assert all(G_degs(n)==formula_G(n) for n in range(80))
assert G_degs(21)==[3] and G_degs(22)==[] and G_degs(16)==list(range(2,9))
assert max(n for n in range(80) if G_degs(n))==21

G=mpow(A,6)
for n in range(1,22):
    for d in G_degs(n): G=add(G,mon(1,X=d,T=n))
FX,GX,FT,GT=dX(Fpoly),dX(G),dT(Fpoly),dT(G)
E=add(smul(12,mul(FX,G)),smul(-8,mul(Fpoly,GX)),
      smul(-1,mul(T,add(mul(FX,GT),smul(-1,mul(FT,GX))))))
D22=N({(x,0,u,v,e):c for (x,t,u,v,e),c in E.items() if t==22})
assert D22 and all(u or v for (x,t,u,v,e) in D22)
G20=N({(x,0,u,v,e):c for (x,t,u,v,e),c in G.items() if t==20})
G18=N({(x,0,u,v,e):c for (x,t,u,v,e),c in G.items() if t==18})
G16=N({(x,0,u,v,e):c for (x,t,u,v,e),c in G.items() if t==16})
A2B,B2=mul(mpow(A,2),B),mpow(B,2)
eq62=add(smul(-32,prod(U,dX(A2B),G20)),smul(-24,prod(U,A2B,dX(G20))),
         smul(-12,prod(mpow(U,2),dX(B2),G18)),smul(-8,prod(mpow(U,2),B2,dX(G18))),
         smul(-2,prod(V,dX(G16))))
assert add(D22,smul(-1,eq62))=={}

# reduced origin, all legal G filled
Fred=mpow(A,4)
FX,GX,FT,GT=dX(Fred),dX(G),dT(Fred),dT(G)
E0=add(smul(12,mul(FX,G)),smul(-8,mul(Fred,GX)),
       smul(-1,mul(T,add(mul(FX,GT),smul(-1,mul(FT,GX))))))
assert N({(x,0,u,v,e):c for (x,t,u,v,e),c in E0.items() if t==22})=={}

# unit inverse over R: n=u, n^4=0
assert mpow(U,4)=={} and mpow(V,2)=={} and mul(U,V)=={}
n=U
inv=smul(-1,add(mon(),n,mpow(n,2),mpow(n,3)))
assert mul(add(smul(-1,mon()),n),inv)==mon()

raw=json.load(open('cases/ggv_8_28_raw_to_global_m_cokernel_interface_d3_20260827/RAW_INPUT.json'))
Gw=Counter(s['weight'] for s in raw['raw_slots_through_weight_22']['G'])
assert Gw.get(22,0)==0 and [s['slot'] for s in raw['raw_slots_through_weight_22']['G'] if s['weight']==21]==['g_3_0']
print('independent: Q, W_X, (4.2), windows, (6.2), reduced origin, unit, JSON G22: PASS')
PY
```

Exact output:

```text
independent: Q, W_X, (4.2), windows, (6.2), reduced origin, unit, JSON G22: PASS
```

No AWS resource was used.  No heavy local CAS ran.  No path under
`jc2-lean` was listed, searched, read, built, statused, or modified.
This report is the only write.
