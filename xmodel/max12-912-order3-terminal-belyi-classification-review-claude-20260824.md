# Hostile review: max12 `(9,12)` selected-Q8 terminal Belyi classification

| Field | Value |
|---|---|
| Reviewer | claude (different-model hostile reviewer) |
| Date | 2026-08-24 |
| Report under review | `xmodel/max12-912-order3-terminal-belyi-classification-20260824.md` |
| Case under review | `cases/max12_912_order3_terminal_belyi_classification_20260824/` |
| Parents audited for imports | global-quotient gate (+ its CONFIRMED review), leaf-4 descent jet (+ CONFIRMED review), normalization jet (CONFIRMED review), maximum-12 partial-`y` Kummer preflight, critical-value norm |
| Overall verdict | **CONFIRMED** (no false identity; one statable nondegeneracy hypothesis `Z != 0` missing from three sentences, discharged at the registered actual-trajectory scope — section 10; execution-side caveats in section 2, none charged to the artifact) |

All six case files and the charged report were read in full before any
verdict.  Every displayed identity was re-derived by hand in this review;
no PASS string was trusted.  No repository byte was modified other than the
creation of this file.

## 1. Charged hashes and read-only cross-pin audit

```text
report       5d8806db54eb2056dd7aafe6fb7dc342c68be1bef7cba06b96beeeaa765273fc
manifest     ff7e065845f064cf1cb25b35dea053dee5c72ee0540bf46a8f901d131b582b33
freeze       0c5b862fd4f784e3e258881c39a16dbd14d3c53f9aafe9426cfec8102f5018d9
replay       495844f1d51c0f230223d143f36b54679865244581fb60974c268da4c756a4bb
AWS output   4697899b8ba8e4780db56a7318911e4e463d9f0db4cea00392098a4f530c894e
```

Verified by reading: the charged report hash equals `MANIFEST.sha256` line 1
and `FREEZE.txt:report_sha256`; the charged replay hash equals manifest
line 4, `FREEZE.txt:replay_sha256`, and the report section 6 "source SHA256"
of the AWS run; the charged AWS-output hash equals manifest line 5 (the
frozen `replay.json`), `FREEZE.txt:replay_payload_sha256`, and the report
section 6 stdout hash — so the frozen payload is pinned byte-identical to
the attested off-host stdout; the charged manifest hash equals
`FREEZE.txt:manifest_sha256`; the registration and readme hashes agree
between manifest lines 2–3 and the FREEZE lines.  The recorded stderr hash
`e3b0c442…` is the SHA-256 of the empty byte string (a known constant), so
the empty-stderr claim is internally exact.  The only links not verifiable
by reading are the actual bytes-vs-hash checks and the self-referential
FREEZE hash `0c5b862f…`; the staged probe closes them.

## 2. Execution disclosure (reviewer-side, mandatory)

This review session has no shell: no Bash tool and no local computation.
Consequently I could **not** byte-execute `shasum -a 256 -c`, the
`replay.py | diff -u replay.json -` pipeline (the AWS `r6d` attestation with
`rc=0`, empty stderr, and matching source/stdout hashes was taken as frozen
evidence, per the charge, after checking its hashes against the lattice
above), or my independent probe.  The probe is staged at
`/tmp/q8_terminal_belyi_probe_claude.py` and, with an independent polynomial
engine and no reliance on any in-case string, re-checks: all five charged
byte hashes, the manifest, byte-equality of live stdout with the frozen
payload, the eleven control rows (including the full cross-multiplied
terminal identity `h^3 W^9 A^18 B^24 = A^24 B^36`, not just (1.4)), the
valuation uniqueness `3m+9(z-1)=8z <=> z=9-3m` over a rectangle, the
balanced count 10660, randomized Wronskian degree laws for (4.1)/(4.3), and
the section-10 degenerate exhibit.  The maintainer should run the two
report section 6 commands plus `python3 /tmp/q8_terminal_belyi_probe_claude.py`.
The verdict below rests on complete source reading, hand re-derivation of
every charged identity, and the internal consistency of the frozen
cross-pinned attestations.

## 3. Imported-hypothesis audit against the reviewed parents

The registration names the frozen selected-Q8 root-free terminal identity as
sole input.  Traced and checked:

- **(1.1) itself.**  `nu^10*h^3*(Z')^9=j^9*Z^8` is byte-identical to (5.2)
  of the reviewed global-quotient gate, which derived it (CONFIRMED review,
  exponent by exponent) from the leaf-4 row via `S=r8^9=pi^10*q^9=nu^10*Z`
  and `S'=nu^10*Z'` with `nu` constant in `x`.  The prime is `d/dx` along
  the trajectory throughout; no variable mismatch.
- **`h in C[x]`.**  The maximum-12 Kummer preflight freezes the `(9,12)`
  row `a_9=h^3`, `b_12=h^4` with `u^3=h`.  Since `a_9 in C[x]` and `C[x]`
  is integrally closed in `C(x)`, `h^3 in C[x]` forces `h in C[x]`.
- **`3|deg(h)`.**  The same preflight row freezes the residual history
  criterion `gcd(H,3)=3`, equivalently `3|H` with `H=deg h`, resting on the
  reviewed shear/UFD history artifacts it pins.
- **`h` noncube = the branch.**  The preflight's Kummer-order split for
  `d=3` is `e in {3,1}`; the "nontrivial order-three Kummer branch" is
  exactly order three, i.e. `h` not a cube in `C(x)` (the cube branch
  `h=c*q^3` is a different leaf, out of scope here).  Conditional import,
  faithfully stated.
- **`nu, j in C^*`.**  `nu=r6!=0` is the reviewed `k=mu=0, nu!=0` fibre
  load; `j in C^*` is the frozen terminal row `9*r8'=j/u` of the
  normalization jet (5.1) and leaf-4 (5.1), both CONFIRMED.
- **`Z in C(x)`.**  Automatic along an actual trajectory: `Z=S/nu^10` with
  `S=r8^9=h^6*R^9`, `R in K=C(x)`; also independently imposed by the
  report's own "rational solution" conditioning.  Honest either way.

No import is mis-stated or strengthened.  One import is *missing*; see
section 10.

## 4. Charge 1 — valuation argument and the divisor cube

Assume `Z` not identically zero (section 10); `h!=0` since `0=0^3` is a
cube and `h` is noncube.  Constant nonzero `Z` fails (1.1) outright
(`Z'=0` makes the left side zero, the right side nonzero), so `Z` is
nonconstant.  At a finite `a` with `m=ord_a(h)>=0`, `z=ord_a(Z)`:

- `z!=0`: in characteristic zero `ord_a(Z')=z-1` exactly (the local leading
  coefficient is multiplied by `z!=0`), valid for poles (`z<0`) as well.
  Valuations of (1.1): `3m+9(z-1)=8z`, i.e. `z=9-3m=3(3-m)`, so `3|z`.
  Hand-checked uniqueness both ways; the probe sweeps a rectangle.
- `z=0`: `Z` a local unit, `ord_a(Z')>=0`, and `3m+9*ord_a(Z')=0` with both
  terms nonnegative forces `m=ord_a(Z')=0`.  Correct.  (Byproduct: no finite
  point has `ord_a(h)=3`, exactly matching the section 3 order lists
  `{0,1,2}` and `{beta+3}` — a nontrivial internal consistency.)

Transfer to infinity is by the degree-zero principal-divisor identity, not
by differentiating at infinity — clean, since `d/dx` behaves differently
there: `ord_infinity(Z)=-sum` of finite orders `== 0 (mod 3)`.  Algebraic
closedness is invoked exactly where needed: `Z=c*prod(x-p_i)^(3n_i)` with
`c^(1/3) in C` gives `Z=T^3 in C(x)`.  (Over `Q` this fails — `2x^3` has a
`3`-divisible divisor but is no cube — so the hypothesis is load-bearing
and stated.)  `T` nonconstant iff `Z` nonconstant.  Charge discharged.

## 5. Charge 2 — cancellation to `h=C*T^2/(T')^3`

`Z'=3T^2T'`, so (1.1) reads `nu^10*3^9*h^3*T^18*(T')^9=j^9*T^24`; dividing
by `T^18` (legal: `T!=0` in the field `C(x)`) gives
`h^3*(T')^9=const*T^6` with `const=j^9/(3^9*nu^10)!=0`.  Then
`g=h*(T')^3/T^2` satisfies `g^3=const`; factoring `Y^3-const` into linear
factors over `C` and using that `C(x)` is a domain forces `g` equal to one
constant root, i.e. `g=C in C`, and `C!=0` since `h!=0` and `T'!=0`
(characteristic zero, `T` nonconstant).  So `h=C*T^2/(T')^3`, and
`T'=W/B^2` gives (1.4) `h=C*A^2*B^4/W^3`.  No zero or pole case is lost:
`T` constant is excluded by `Z` nonconstant, `h=0` by noncube, and the only
root extraction anywhere is a cube root of a *constant*, which exists in
`C` — never of a function.  The converse is exact: `h=T^2/(T')^3`, `Z=T^3`
give `h^3*(Z')^9/Z^8=3^9` (hand-checked; the probe checks the
cross-multiplied polynomial form), and `C^3=j^9/(3^9*nu^10)` is solvable in
`C^*`, so every nonconstant-`T` datum yields a genuine (1.1) solution.
Charge discharged, subject only to section 10.

## 6. Charge 3 — Wronskian orders, exact polynomiality, cube class

With `T=A/B` reduced, `W=A'B-AB'`, and `W!=0` iff `T` nonconstant (char 0):

- At an `A`-root of multiplicity `alpha`: coprimality makes `B` a unit, so
  `ord(A'B)=alpha-1` exactly (char 0) and `ord(AB')>=alpha`; hence
  `ord(W)=alpha-1` and `ord(h)=2*alpha-3*(alpha-1)=3-alpha`.  (3.1) exact.
- At a `B`-root of multiplicity `beta`: symmetrically `ord(A'B)>=beta`,
  `ord(AB')=beta-1` exactly, so `ord(W)=beta-1` and
  `ord(h)=4*beta-3*(beta-1)=beta+3`.  (3.2) exact.
- Away from `A*B`: `ord(h)=-3*ord(W)`, so any `W`-root there is a pole of
  `h` of order a positive multiple of three.

The "if and only if" (3.3) holds in both directions: polynomiality forces
`alpha<=3` (from `3-alpha>=0`) and `support_finite(W) subset supp(A*B)`;
conversely those two make `h` finite-pole-free, and a rational function
regular on all of `A^1` is a polynomial.  `beta` is genuinely unrestricted.
Under (3.3) the orders above are exact and exhaustive, giving (3.4) and
`deg(W)=(a-r)+(b-s)`.  Cube class: `(T')^(-3)` is a cube and `C in C^*` is
a cube over `C`, so `[h]=[T^2]=[T]^(-1)` in `C(x)^*/C(x)^{*3}`, trivial iff
`T` is a cube.  Every use of coprimality (unit cofactors at each root) and
characteristic zero (`ord` drop by exactly one under `d/dx`; `W=0 <=> T`
constant) is correct and necessary.  Charge discharged.

## 7. Charge 4 — both infinity strata

**Unequal (`a!=b`).**  The Wronskian leading coefficient is
`(a-b)*A0*B0!=0` in characteristic zero, so `deg(W)=a+b-1` (also exact when
one of `a,b` is zero: `W=A'B` or `-AB'`).  Equating with (3.4)'s
`a+b-r-s` gives `r+s=1`, so exactly one of `A,B` is constant and the other
is `(x-c)^D` up to scalars.  Case `a>b` (so `B` constant): `alpha=D<=3` by
(3.3), `h=c'*(x-a0)^(3-D)`, and `3|(3-D)` forces `D=3`, where `h` is a
nonzero constant, hence a cube over `C` — killed by noncube.  Case `b>a`
(`A` constant): `h=c'*(x-b0)^(D+3)` with **no** upper bound on `D`;
`3|deg(h)` forces `3|D`, so the sole multiplicity `D+3` is `0 (mod 3)` and
`h` is a cube (constant absorbed, `C` algebraically closed) — killed by
noncube, for **every** such `D`, not only the replayed samples `{3,6,9}`.
So both unequal strata are empty at the exact noncube, `3|deg(h)` scope,
and the report correctly notes they are nonempty without those hypotheses
(the frozen control tables exhibit exactly the two failure modes).

**Balanced (`a=b=D`).**  `lambda=A0/B0 in C^*` is forced (both leading
coefficients nonzero), so `T(infinity)` is neither `0` nor `infinity`.
With `G=A-lambda*B` (nonzero since `T` nonconstant), `e=D-deg(G)`, so
`1<=e<=D` as claimed.  Since `W=(A-lambda*B)'B-(A-lambda*B)B'=G'B-GB'`, the
leading coefficient is `(deg(G)-D)*G0*B0=-e*G0*B0!=0`, giving
`deg(W)=deg(G)+D-1=2D-e-1`; the report's route via
`ord_infinity(T')=e+1` and `deg(W)=2D-ord_infinity(W)`-bookkeeping gives
the same value (differentiation raises the infinity order by one:
`d/dx=-s^2*d/ds`).  Equating with (3.4) gives `r+s=e+1`, and
`deg(h)=2D+4D-3*(2D-e-1)=3(e+1)=3(r+s)`.  Independent cross-check from the
local orders: `sum(3-alpha_i)+sum(beta_j+3)=3r-D+D+3s=3(r+s)`.  All of
(4.2)–(4.4) exact.  Charge discharged.

## 8. Charge 5 — passport completeness and Riemann–Hurwitz

Fibres of the degree-`D` map `T` in the balanced stratum: over `0` exactly
the `A`-roots `(alpha_i)`, `alpha_i<=3`, `sum=D`; over `infinity` exactly
the `B`-roots `(beta_j)`, `sum=D` (the point `x=infinity` lies over
`lambda`, not here); over `lambda`: the `D-e` finite roots of `G` (coprime
to `B` since `gcd(A,B)=1`) plus `x=infinity` with multiplicity `e`.  Hidden
ramification is excluded twice:

1. **Directly by (3.3).**  A finite critical point `c` over any value
   outside `{0,infinity}` has `A(c)*B(c)!=0` and `W(c)=0`, contradicting
   `support_finite(W) subset supp(A*B)`.  In particular every finite
   `lambda`-preimage is simple (a multiple root `c` of `G` has
   `W(c)=G'(c)B(c)=0` with `A(c)=lambda*B(c)!=0`), and no fourth branch
   value can carry any ramification.
2. **By the Riemann–Hurwitz saturation (4.6).**  The listed contributions
   sum to `(D-r)+(D-s)+(e-1)=2D-(e+1)+e-1=2D-2`, which in characteristic
   zero (separability free) is the *entire* ramification total for a
   degree-`D` map `P^1 -> P^1`; every unlisted point would add a positive
   amount.  Not circular: the listed orders were computed exactly, so the
   remainder is forced to zero.

`lambda in C^*` means the three values `0, lambda, infinity` are genuinely
distinct, and post-composing with `z -> z/lambda` (a Möbius map fixing `0`
and `infinity`) scales `lambda` to `1`: a three-point Belyi passport, as a
necessary target only.  Cancellation at infinity is exactly the `e`
bookkeeping of section 7; there is no inseparability in characteristic
zero; no omitted branch value survives the two arguments above.  Charge
discharged.

## 9. Charge 6 — controls, frozen replay content, and scope

**Controls, hand-recomputed.**  For `A=x^D`, `B=(x-1)^D`:
`W=-D*x^(D-1)*(x-1)^(D-1)`, so `W^3=-D^3*(…)`, and
`h=-(1/D^3)*x^(3-D)*(x-1)^(D+3)` satisfies `h*W^3=A^2*B^4` exactly — the
replay's scalar `-1/D^3` and `verify_h` assertion are correct, as are
`W_degree in {0,2,4}` (`=2D-2`, matching `e=1` in (4.3)) and the
multiplicity pairs `(2,4), (1,5), (0,6)`.  Cube flags: `(2,4) == (2,1)` and
`(1,5) == (1,2) (mod 3)` are noncube; `(0,6)` is a cube with the constant
absorbed (e.g. `-1/27=(-1/3)^3`); the reciprocal rows' constants are cubes
over `Q` already (`-1/216=(-1/6)^3`, `-1/729=(-1/9)^3`).  The polynomial
and reciprocal pure-power rows all satisfy `h*W^3=A^2*B^4` by the same hand
algebra.  Both hypotheses `3|deg(h)` and noncube fail in every unequal-row
sample exactly as frozen, and `D=1,2` cyclic rows satisfy both — so the
equation (1.1) *has* nonconstant rational solutions at the charged scope
and no exclusion can be promoted.  The replay verifies (1.4); the section 2
converse (`3^9` constant, hand-verified here and in the staged probe's
cross-multiplied form) lifts these to genuine (1.1) solutions.

**Frozen payload consistency.**  `checked_integer_strata=10660` equals the
hand sum `sum_{D=1..39} D(D+1)/2=(20540+780)/2`; the loop's `s>D` guard is
dead code (`s=e+1-r<=e<=D`), so nothing is silently skipped — harmless,
worth a comment.  The valuation loop is (2.1) verbatim.  All JSON keys are
in the `sort_keys` ASCII order with the frozen indentation (including
`"W_degree"` before `"degree"`), consistent with the pinned stdout hash.
The replay is correctly framed as proof support; the divisor argument is
the theorem, and the replay never claims the strata classification itself.

**Scope.**  Report section 1 and 5, README, REGISTRATION, FREEZE, and the
payload `scope` string all restrict to a necessary classification on the
selected corrected-Q8 `k=mu=0, nu!=0` branch and disclaim coefficient-fibre
realization, Taylor integrality, the original-terminal converse (the
ninth-power identity does not reconstruct `9*r8'=j/u`), trajectory
existence/nonexistence, all-`(9,12)`, maximum-twelve, counterexample, and
JC2.  Section 5's successor list (quotient lift, scale reconstruction, six
high rows plus original terminal row, both Taylor families, coprimality and
boundaries) is the honest residue.  No overreaching byte found in any
charged file.  Charge discharged.

## 10. Smallest false identity or missing hypothesis

**No false identity.  One missing nondegeneracy hypothesis: `Z != 0`.**

The pair `(Z,h)=(0, x^2*(x-1)^4)` satisfies every stated hypothesis —
`h in C[x]`, `deg(h)=6` divisible by three, `h` noncube, `nu,j in C^*` —
and satisfies (1.1) trivially (both sides are the zero function), yet admits
no nonconstant `T` with `Z=T^3`, and `h=C*T^2/(T')^3` is undefined for it.
Hence three sentences are literally false as quantified:

1. report section 1: "Every rational solution of (1.1) has (1.2) … for a
   nonconstant `T`";
2. report section 2: "the classification loses no rational solution of the
   terminal equation" (it loses exactly the `Z=0` family);
3. FREEZE verdict line: "EVERY RATIONAL TERMINAL SURVIVOR IS Z=T^3 …".

Section 2's setup `z=ord_a(Z)` silently assumes the order is finite, i.e.
`Z != 0`.  The registered theorem itself is **unaffected**: REGISTRATION
quantifies over "every **actual** selected-Q8 rational terminal solution",
and along any actual trajectory `Z != 0` is forced by the reviewed frozen
parents in two independent ways: (i) leaf-4 (5.1)–(5.2): if `S` were
constant then `S'=j*h^5*R^8=0` forces `R=0`, hence `r8=u^2*R=0` and
`9*r8'=0=j/u`, contradicting `j in C^*`; so `S=r8^9`, and with it
`Z=S/nu^10`, is nonconstant; (ii) the gate's frozen unit constants `q0,n0`
make `Z=q^9/n^10` a unit at every Q8 contact.  Required one-line erratum in
any successor or promotion: add the hypothesis "`Z` not identically zero
(equivalently nonconstant), supplied along any actual trajectory by the
frozen terminal row `9*r8'=j/u` with `j in C^*`".  With that line, every
statement in the report is exact.  Non-blocking at the registered scope.

Minor non-blocking remarks: (i) `h != 0` is used but never stated — it does
follow from "noncube" since `0=0^3`; (ii) `1<=e<=D` tacitly uses
`A-lambda*B != 0`, i.e. the same nondegeneracy root; (iii) the replay's
dead `s>D` guard and the odd control label
`h_is_cube_when_residual_degree_allowed` merit cosmetic cleanup; (iv) the
FREEZE self-hash is unverifiable without a shell (probe stages the check).

## 11. Promotable sentence and strict scope

Promotable (after the one-line erratum of section 10):

> On the selected corrected-Q8 `k=mu=0, nu!=0` branch, every rational pair
> `(Z,h)` with `Z in C(x)` not identically zero and `h in C[x]` satisfying
> `nu^10*h^3*(Z')^9=j^9*Z^8` (`nu,j in C^*`) has `Z=T^3` and
> `h=C*T^2/(T')^3=C*A^2*B^4/W^3` for a nonconstant reduced `T=A/B`,
> `W=A'B-AB'`, `C in C^*`; `h` is a polynomial exactly when every finite
> root of `W` lies in `supp(A*B)` and every `A`-root multiplicity is at
> most three; adding the frozen Kummer hypotheses `3|deg(h)` and `h`
> noncube empties both unequal-degree strata and forces
> `deg(A)=deg(B)=D`, `lambda=T(infinity) in C^*`,
> `e=ord_infinity(T-lambda) in [1,D]`, `r+s=e+1`, `deg(h)=3(e+1)`, with
> `T` (after scaling `lambda` to one) a three-branch-value map of complete
> passport `(alpha_i<=3)` over `0`, `(beta_j)` over `infinity`,
> `(e,1^(D-e))` over `1`, saturating Riemann–Hurwitz `2D-2`; the
> nondegeneracy `Z != 0` holds along every actual trajectory by the frozen
> row `9*r8'=j/u`, `j in C^*`, and the cyclic rows `D=1,2` of (4.7) are
> noncube positive controls, so the classification is necessary only and
> excludes no trajectory.

Strict scope: a necessary classification of rational solutions of the
descended ninth-power terminal identity on the stated branch, conditional
on the reviewed frozen import chain.  Not promotable: any coefficient-fibre
or passport realization, any lift through the exact Q8 quotient, Taylor
integrality at `r=A_source/9`, the original-terminal converse, any
trajectory existence or nonexistence, any statement on the removed
boundaries, all-`(9,12)`, maximum-twelve, counterexample, or JC2
conclusion.

## 12. Residual conditions

This confirmation is conditional on a shell-bearing session running: the
two report section 6 commands (manifest check and replay diff) and
`python3 /tmp/q8_terminal_belyi_probe_claude.py` from the repository root
(charged hashes including the FREEZE self-hash `0c5b862f…`, frozen-stdout
byte equality, and the independent recomputations of section 2 above).
Every hash relation checkable by reading is consistent; a failure of any of
these commands, or of the section 10 erratum to be recorded before any
promotion that quantifies over non-actual solutions, would reopen this
review.

CONFIRMED
