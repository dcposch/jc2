# Coordinator integration: all boundary faces of the first ramified K00 cell

Author: Sol 5.6 Ultra (coordinator)  
Date: 2026-08-29 UTC  
Lifecycle: **BINDING INTEGRATION / PROMOTED EXACT E2M1 ALL-FACE POINT-SET EMPTINESS / BANKED E3 G8 FIXTURE AND GRADIENT LEMMA**

## 0. Bound custody and review verdict

This integration binds the following sealed producer/reviewer pair:

```text
64eaafe3fe5aaa9238a338f2da045e302d9a239ac9c29312e39d5c545893d42c
  xmodel/k00-ram-e2m1-allfaces-uniformity-audit-sol56-20260829.md
  body: 13029 bytes, 5925efef3638ba5a0dcc8b855933fbc7c557ea82f8015edd5564496384c99c06

0ee84a0b98d30c4436461a09118961706d1f18fcfe9686684e7b1a27b5597feb
  xmodel/k00-ram-e2m1-allfaces-uniformity-hostile-review-fable5-20260829.md
  body: 22894 bytes, 57de629f083c4d2f7316726cd433d9ac9520a6836a2b478635587f0a79e49205
```

Both seals verify on basis
`9b64db896b65e100839f6d75fbeea661cd818b9c`.  The Fable lane
`k00-ram-e2m1-allfaces-uniformity-hostile-review-fable5-20260829` ended
`DONE`, exit 0.  Its prompt, run receipt, and log hashes are respectively
`0c388478a290d17bcd60b6baeb916d1a5fa59d9239497ed819b10281464785a8`,
`0a127823f7580bc1b0a4f17cf9b41ce1b6db8bda4c94ea3b4ec45bcb3285a116`,
and `65c38a4eacf9c8053b5861619ed91fbdc671d7042eb31dbb27039eb63deea63d`.
The run receipt's report hash is the pre-seal body hash; the displayed full
hash above is the later sealed file.

Fable returned `CONFIRM_WITH_CORRECTIONS` on both charged claims.  It parsed
the 569 frozen tails independently, used reviewer-owned exact `Q(i)`
arithmetic, reconstructed the complete G3--G7 kill rather than relying on
producer custody, checked all boundary calendars/opens and both signs, and
substituted the e3 fixture into the full literal source.  The corrections
F1--F5 below are binding.  Only the e2 all-face point-set theorem is
promoted.

The earlier corrected-G7 binding integration remains a licensed input only
at its stated point-set scope:

```text
0eb501b414f2162d14a73725a46410b7e799adc70932cdfb8a05f4196ff0bb1a
  xmodel/k00-ram-e2m1-g7-rankfan-coordinator-integration-sol56-20260829.md
  body: 4690 bytes, f779bac98cea2892513a7f6cd40708ec0d8fcb4e9f5426479595c083135c4270
```

The all-face replay is
`xmodel/k00-ram-m1-uniform-rankfan-replay-sol56-20260829.py`, SHA-256
`0e7f98d165bf60531f675bae948315211fd08fd466f21f98aa399cd5fb12457b`.
Its source custody is the 569-tail file
`d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848`
and compiler
`2ac7653cf0c7a39970d54286b85974b39a2e6deb116839720cb1ae91f8ad6d2b`.

## 1. Promoted maximum theorem

Let the normalized generic K00 ray be over an algebraic closure of a
characteristic-zero residue field, after the licensed finite/Kummer
extensions, with

```text
Lambda=tau^2,  ord_tau(d)=1,  C6=1,
ord_tau(k10)=ord_tau(Jdet)=0,
k6,k2,mu2,mu4,mu6 in tau*K[[tau]].
```

Each of the last five series may have any positive order or may be the zero
series.  Then

```text
V(G0,...,G7) intersect D(k10[0])
            intersect (union_i D(d_i[1])) = empty.              (1.1)
```

Therefore every exact boundary load-order face of this `e=2,m=1` normalized
source cell has empty field-valued point set, both in its full grade-38
truncation and in the formal source: any such point would restrict to the
impossible G0--G7 prefix while preserving the two used opens.  This is the
maximum promoted theorem here.

Equation (1.1) is stronger than needed with respect to the cell's Jdet open:
`D(Jdet[0])` is part of the cell definition but is not consumed by the kill.
No scheme-theoretic unit ideal or multiplicity statement is inferred.

## 2. Reviewed proof spine and face passage

At `e=2`, the literal source is

```text
R(d)+tau^4*k10*A10(d)+tau^12*k6*A6(d)
    +tau^20*k2*A2(d)-targets.
```

The exact stencil puts K6 at G14 or later, K2 at G22 or later, and the four
targets at G29, G33, G37, and G38 or later.  Thus every positive-or-infinite
boundary-order face has literally the same G0--G7 polynomials in the same
`d,k10` coefficients.  Extra exact-order opens only shrink those point sets,
and the faces partition the full boundary stratum.

The corrected G7 certificate then applies verbatim.  The centered variables
are

```text
mu=(s^2,s*t/8,16*t^2,0,0,0),  w=d[2]-mu,
```

and the corrected K10 term retains the cubic contribution

```text
[tau^3]A10(d)=DM4(ell)[u]+A10^[3](ell)
             =DM4(ell)[u-mu/2].
```

The two complete rank fans exhaust ranks 2, 1, and 0.  Their terminal G7
identities use `k10[0] != 0` exactly twice and the nonzero first-transverse
coefficient open; no K6, K2, target, or Jdet coefficient/equation/open is
used.  The face-uniform normalizations `C6=1` and `Lambda=tau^2` preserve
all boundary orders and face labels under the licensed root extensions.

## 3. Binding F1--F5 correction register

**F1 — replay-control erratum.**  Read the replay banner as follows.  The
only fired in-run negative controls are `SURFACE_16_TO_15`,
`STABLE_640_TO_639`, and `E3_SURFACE_COEFF`.  `CUSTODY` is a fail-closed hash
gate, `FINAL_SHIFT` is a positive equality assertion, and this replay has no
`K10_CUBIC` control.  The cubic is checked positively and the reviewer-owned
mutation harness detected sector perturbations, so this is a documentation
correction, not a mathematical gap.  This paragraph is the required F1
erratum; no canonical ledger is edited.

**F2 — fixture mutation.**  The producer prose's propagated change
`S: -4 -> -3` fails exactly at G8.  The replay instead edits one unpropagated
`d4[2]` slot and can already break G4--G7.  Both fail, but future controls
must prefer/name the propagated mutation so prose and code test the same
object.

**F3 — stable-shift mechanism.**  The replay sampled the general-`n` claim,
whereas Fable proved it for every `n>=3`: for the unloaded surface ideal
`J`, each `R_r` lies in `J^2`, hence all 42 gradient components vanish on
`D(S,T)`, and a deviation-grade census leaves exactly the displayed stable
fan/cokernel shapes.  The exact gradient lemma and census are **banked** as a
reusable algebraic mechanism.  This integration does not turn them into an
arc, lifting, or additional cell theorem.

**F4 — bounded G9 observation.**  In the Fable review, freezing every
displayed e3 fixture coefficient makes G9 inconsistent: the newest block has
rank one, `d[7]` is absent by the gradient lemma, and rows 4 and 6 are forced
constants.  This only says the particular frozen G8 jet cannot extend with
that retained block frozen; it is not a G9 cell verdict.

**F5 — units and usage.**  `Jdet`-unit status rides with the cell but is
unused in G0--G7.  `k10[0] != 0` is used exactly twice.  The `C6` unit is
used by the face-uniform Kummer normalization.  All theorem statements and
dependency inventories are read with those distinctions.

## 4. Banked e3 finite-jet counterfixture

Over `Q(i)`, the exact data

```text
Lambda=tau^3,  k10=Jdet=1,
k6=k2=mu2=mu4=mu6=0,
S=8*i*tau-4*tau^2,  T=tau,
d=D(S,T)+tau^3*w+tau^4*v+tau^5*z,
w=(16*i,0,0,1,-8*i,4),
v=(-320,0,0,0,0,24*i),
z=(-1088*i,0,0,0,0,0)
```

make all 63 literal row/grade coefficients G0--G8 vanish.  They satisfy the
`e=3,m=1` opens and boundary conditions, and they refute only the proposed
coefficient-blind induction which discarded the second surface coefficient.
This is banked as **EXACT FINITE-G8-JET / OLD-PASS COUNTERFIXTURE**.  It is
not a G9 lift, compatible all-order jet, formal arc, algebraic point, source
cell, map, counterexample, or attainment statement.

## 5. Later G9 evidence is outside this review

After the Fable lane finished, the separate same-model producer report

```text
bbe6ac2fa8ca7b53634e3c477d1cb2f4128e4e22e2a1cf5d4049db82402fe685
  xmodel/k00-ram-e3m1-g9-rankone-kill-sol56-20260829.md
  body: 9880 bytes, 0fe19184da754151933294aa7377273d03e07f4b7830ee430d20984c53827b36

3ef20945b4a009bba4dccbbf7a43461718feb8155e84f513f14c736ce45182e2
  xmodel/k00-ram-e3m1-g9-rankone-kill-replay-sol56-20260829.py
```

reported the stronger raw identity
`G9_6=epsilon*i*q^3/32` on `D(q)` for both signs of the reduced stable
rank-one G8-compatible family.  That packet is
`EXACT PRODUCER / PROVISIONAL / DIFFERENT-MODEL REVIEW REQUIRED`; it was not
in Fable's charge and is not consumed by (1.1).  It remains post-review
evidence only.  Even if later confirmed, its stated scope is one reduced
rank-one family, not the whole `e=3,m=1` cell or an arc theorem.

## 6. Scope firewall

Nothing here covers `m>=2`, the `C6=0` tip, `k10=0`, `Jdet=0`, any
`e>=3` cell, another K00 support/load ray, positive characteristic,
nonreduced scheme structure or multiplicities, compatible lifting outside
the exact e2 prefix implication, convergence, algebraization, polynomial
Keller maps, counterexamples, attainment, Gate T, order two, maximum twelve,
or JC2.  Floors and lower bounds are never read as attained exact orders.

No modular or msolve `[1]` output is consumed.  No explicit localized Bezout
identity is claimed: the theorem is independently reconstructed exact
field-valued point-set emptiness.  No canonical ledger, ideation file, AWS
host, or separate formalization instance was edited, built, or controlled.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `9174`.
- Body SHA-256:
  `624e3abb301d17136783d1acd870b195397182d5feb40818abb19861c6a9036c`.
- Frozen basis: `0f7ee003be45ee40d51d4048897cdacf63821172`.
