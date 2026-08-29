# Hostile different-model review — K00 grade four over the rank-zero plane

Reviewer: Grok 4.6, equal-standing independent adversarial reviewer
Date: 2026-08-29
Frozen campaign basis: `40c1ab3448209e3d87173feb947a733f6fe54f7f`
  (`git rev-parse HEAD` at start of work)
Output: this file only.  Scratch lived under `/tmp/k00g4_rev_grok46/`.
No canonical, case, ladder, guardrail or operations file was edited.
No web, network, commit, push, AWS, remote shell, or `jc2-lean` access.
No exit price is asserted.

The producer is not a premise.  Every load-bearing identity below was
rebuilt from `exact_terms` with exact `Fraction` arithmetic in CPython
3.14.7, then checked in a separately authored Singular 4.4.1 session.
Producer `/tmp/k00g4/` was hashed as a custody artefact only; its scripts
were not executed as evidence.

## 0. Binary disposition

```text
REVIEW  PASS_WITH_REPAIR
  LOCALIZED_GRADE_FOUR_IDEAL        = PROPER (reduce(1,std I4)=1)
  GEOMETRIC_LOCUS                   = NONEMPTY, IRREDUCIBLE, dim 13
  SCHEME                            = NON-REDUCED (nilpotency index exactly 3)
  d*_3 AND k10_0 ON THE PLANE       = DISAPPEAR IDENTICALLY
  CLOSED FORM                       = GENERATORWISE IDENTITY (7/7)
  GRADE_FIVE_CENSUS                 = CONFIRMED
  CONDITIONAL BRANCH KILL           = NOT AVAILABLE
```

The repairs in §8 do not change the theorem in §7.  The disposition
fails closed on those repairs being adopted.  One sub-computation
(`primdecGTZ` of the eight-variable CORE) hit the 60 s CPU cap and is
not charged; the embedded-structure claim is carried by the six-variable
`Q2` decomposition plus the generatorwise closed form, which did finish.

## 1. Charged inputs (rehashed)

```text
sha256                                bytes  path
40c1ab3448209e3d87173feb947a733f6fe54f7f
       frozen campaign HEAD
0d2a9861126c8857e04a9170c8586b6b4eabe67d2e65d3b4d3b7e991774b614f
      40688  xmodel/k00-grade4-rank0-plane-primary-opus5-92e-20260829.md
d453b9563d8f6cc23319d6bc0d8edce8a83f657b9e3a60cb244b00f181459860
       6355  xmodel/k00-rank5-rankle1-coordinator-integration-sol56-20260829.md
d7ec6d18d58265421ff315fa00e38cd32992ac12f7d8166cf6c436e23bf06501
   62072089  .../ATLAS_EXACT_POLYNOMIALS.json
ce5063930117bc8fe9869dc80f1535459dd41209a35406ed7edacde1213618dd
       8553  .../P6_LITERAL_SOURCE_LABELS.json
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5
       1985  FALLACY-v2.md
24640d0dacec16b27b4c7eb83419188aa86e3fc80b481b0ba64aa136348fc892
      53609  compile_fitting_atlas_v26.py   (digest convention only)
```

Producer body (first `BODY-END` marker line, inclusive of its newline):
40012 bytes, SHA-256
`f6356d974f2f183d571297384d33f9161c2dd12d6a21c10a3fdc3200591cb6a2`,
matching its seal.  Coordinator body: 6036 bytes, SHA-256
`f288a1213feef1ca8c290fe08472b99a0cf90106738c947b84b41a249af148f1`,
matching its seal.  Atlas hash equals the value stored in
`COMPILED_SOURCE.sha256`.  `V24R2_DEPENDENCY.json` still records
`release_allowed=false` / `HELD_MISSING_EXACT_Q_V24R2_ENDPOINT`.

The producer charged the grade-three note
`e0947368509714aa96376789914a4dbfd7141b1f77832016bf4dbe7c3caa45e4`
only as a branch specification.  That is now superseded as a *locus
definition* by the coordinator integration, which is the binding
upstream for this review.  Exhaustiveness of `Pi` is consumed from the
coordinator, not re-proved here.

## 2. Independent reconstruction (not a producer replay)

Atlas records are `{Lambda_grade, row, poly:{exact_terms, singular,
sha256, terms}}`.  A term is `[ [name,exp], ... , numerator, denominator ]`.
Polynomials were rebuilt from `exact_terms` alone:

```text
monomial  = sorted (name,exp) pairs, zero exponents dropped
coefficient = Fraction(num, den)
payload   = compiler p_payload (sorted monomials, compact JSON + newline)
digest    = sha256(payload)     # convention read from compile_fitting_atlas_v26.py
text      = compiler p_text
```

```text
ALL_49_ROWS: digest 49/49, text 49/49, term-count 49/49
V27 singular_text_sha256 (sha256(text.strip()+"\n")): 49/49
```

Verified `(Lambda_grade,row)=(4,1..7)` digests, identical to the producer
table and to the V27 labels:

```text
(4,1) 45  bde3b17a9290c76d22c195a5c1bb71602982763d3ee7fbd9d8107ba468638080
          v27 36ac9bff314253b961354fbd69e80aa9f251f9c622d541501dddf08ec5b65365
(4,2) 60  1dc0a2b5a3dffc2be5eabe49171b69738946c44f74bdd09ff9060ea938d68d45
          v27 8681ae7b45d2e31defb3ee62965adbe1738d18c3725bc35ba43549f5c3a1ad7b
(4,3) 67  5f234759d02cc366d9ca4461f3bedbd784ff1669e225574f3d6eaf866acf845a
          v27 2f66480f54029493e688587773e025649c3327edcc1465d0ea4ae69635251986
(4,4) 84  612a801fbebb741c21b19a10e46811959abb307daa98da1349e51fb47ac70734
          v27 fbb8459dbca8ed0cf7337bdb8de5aadf96dc932eec98b3ad77878fa8fac0ecdb
(4,5) 86  ed7b1c2e27809edecf7eaf98e1954d71541d72e4fe764c99faba7e0a9dac0a30
          v27 003b823229943c0727eb863d22575f3f6a1ade02d32f035b175f5479b0ab9f8f
(4,6) 77  6f8899f20f7c80e9b270d739fce3a49a98cb921c19861f927f57623bdd624194
          v27 47cdb7dd4cd993b3ced088539b032b02ce4d5678cbe5cb65a6b6809ce47da1e1
(4,7) 99  cde66e7196d3b38a694e37083f3354d7265298c53778f119e464b6f909a90b3e
          v27 3b1c7822b7c419f1f4d0b6d2b73c01d2611e74f4b120d1cdf1d10361be123d09
```

`Q1_to_Q6` equals literal grade-two rows `(1,2,3,4,5,7)` in that order;
grade-two row 6 is the zero polynomial.  Closed-form `Q_r` below is the
literal row `Lambda_{2,r}`, not the compressed six-slot list.  Using
`Q1_to_Q6[6]` as if it were row 6 is the known `q6`/row-7 trap; the
producer did not fall into it.

Support of grades 0..4 is exactly the 19 names
`{d0_1..d5_1, d0_2..d5_2, d0_3..d5_3, k10_0}`.  Declared atlas names
absent from those grades: `d*_4, d*_5, k10_1, k10_2`.

Unmapped source variables raise `KeyError`.  No silent name coercion.

## 3. Declared ring maps (FALLACY-v2)

Coefficient field `Q` throughout.  No modular reduction, no floats.

Atlas `ring_variables` is component-major, 33 generators:

```text
d0_1, d0_2, d0_3, d0_4, d0_5, d1_1, d1_2, ... , d5_5, k10_0, k10_1, k10_2
```

The producer ring `S` is jet-major, 19 generators:

```text
d0_1, d1_1, d2_1, d3_1, d4_1, d5_1,
d0_2, d1_2, d2_2, d3_2, d4_2, d5_2,
d0_3, d1_3, d2_3, d3_3, d4_3, d5_3,
k10_0
```

These orders are **not** equal (`PRODUCER_S_EQUALS_ATLAS_ORDER = False`).
Matching names are not a map.  The reconstruction below is name-based.
The producer `map phi` is correct **only** in the jet-major order they
printed, with images checked as

```text
phi(d0_1,...,d5_1) = (2s, t/8, s, t, s, 2t)
phi(di_2) = ui,   phi(di_3) = vi,   phi(k10_0) = k
```

A positional `map` against atlas `ring_variables` would send `d0_2` to
`t/8` and is forbidden.  This is Repair R1.

Working rings used here:

```text
T  = Q[s,t,u0..u5,v0..v5,k,z], dp     (16 gens)
C8 = Q[s,t,u0..u5], dp                (8 gens)
W  = Q[w0..w5], dp                    (6 gens)
```

Binding plane, from the coordinator (and equal as a set to the producer
branch specification):

```text
Pi: (d0_1,...,d5_1) = (2s, t/8, s, t, s, 2t)
```

This is exactly `V(J0)` for
`J0=(2 d3_1-d5_1, d2_1-d4_1, 16 d1_1-d5_1, d0_1-2 d4_1)`.
The coefficient `1/8` is forced by `16 d1_1 = d5_1 = 2t`.

Shift used in the closed form:

```text
mu(s,t) = (s^2, s t/8, 16 t^2, 0, 0, 0)
```

`Q_r(u-mu)` means the grade-two polynomial `Lambda_{2,r}` evaluated at
`d_i_1 |-> u_i - mu_i`.

## 4. Audit 1 — generatorwise closed form

Python substitution, all seven rows, `CLOSED_FORM_MISMATCHES = 0`:

```text
phi(Lambda_{4,r}) = Q_r(u - mu(s,t))     as polynomials, r=1..7
```

Row 6 is the identity `0=0`.  Image term counts
`16,21,20,24,19,0,14`.  The producer's machine-readable
`/tmp/k00g4/g4_sub.txt` (hash `38fc7287...`, custody-only) equals the
independently substituted rows coefficientwise in Singular
(`G_r - H_r == 0` for all seven, including the printed G1 sixteen-term
match and the distinctive G4 coefficients `u0^2 = s^4 = 3/524288`,
`t^4 = 3/128`).

Mutation of the `16` in `mu` to `15` breaks six of seven rows.
Adding an element of the plane `L = span{(2,0,1,0,1,0),(0,1/8,0,1,0,2)}`
to `mu` leaves the identity; an off-`L` shift `t^2 e_0` breaks six rows.
Derivations `D_a = 2 ∂_{u0} + ∂_{u2} + ∂_{u4}` and
`D_b = (1/8) ∂_{u1} + ∂_{u3} + 2 ∂_{u5}` annihilate all seven images.

This is an equality of generating sets, hence of ideals, not of radicals.
The triangular automorphism `σ:(s,t,u) ↦ (s,t, u-mu)` of `A^8` with
polynomial inverse identifies the `(s,t,u)`-content of grade four on
`Pi` with `A^2_{s,t} × V(Q2)`.

Grade-two and grade-three rows vanish identically on `Pi` with `u` free
(`7/7` and `7/7`).  That is an independent check of the coordinator's
`A=0` and `c3=0` on `Pi`; it is not a re-proof that `Pi` is the whole
rank-zero compatible locus.

## 5. Audit 2 — disappearance of `d*_3` and `k10_0`

Unsubstituted monomial shapes of the seven grade-four rows, with
`w(d*_j)=j` and `w(k10_0)=2`, are only

```text
d1^4 ,  d1^2 d2 ,  d2^2 ,  d1 d3 ,  d1^2 k10_0
```

Every `d*_3` and `k10_0` occurs to degree at most one.  Row 6 has no
`d*_3` at all (six zero slots identically, before any substitution).

Coefficient identity, 42 entries, exact `Fraction`:

```text
C_G4V_EQUALS_C_G3U = True
```

i.e. the coefficient of `d_j_3` in `Lambda_{4,r}` equals the coefficient
of `d_j_2` in `Lambda_{3,r}`.  That matrix is `C = A[:,1..6]` of the
grade-three note.  Because grade three vanishes on `Pi` with `u` free,
`C` vanishes on `Pi`, so the grade-four `d*_3` block vanishes on `Pi`.
This is a proof, not a coincidence.

Independently, each `k10_0` coefficient `M_r` (quadratic in `d*_1`)
evaluates to `0` on `Pi`, and after substitution

```text
P4_NONZERO_v_PARTIALS = 0
P4_NONZERO_k_PARTIALS = 0
P4_VARIABLES          = s,t,u0..u5
```

Plane-coefficient mutations, identity-level, all fire:

```text
BASE (2s,t/8,s,t,s,2t) : g2=7/7 g3=7/7 g4zero=1/7 v=0 k=0 CF=0
M1a  t/8 -> t/7        : g2=5/7 g3=0/7 g4zero=0/7 v=16 k=7 CF=7
M1b  2t  -> 3t         : g2=5/7 g3=0/7 g4zero=0/7 v=16 k=7 CF=7
M1c  2s  -> (2001/1000)s : g2=6/7 g3=1/7 g4zero=0/7 v=15 k=6 CF=7
M1d  s   -> 2s         : g2=5/7 g3=0/7 g4zero=0/7 v=16 k=7 CF=7
```

M1c used the exact rational `2001/1000`, not a float.  Literal-row
mutations of `(4,1)` hit the stored coefficients
`d4_1 d5_1^3 = 3/256`, `d0_1 d3_3 = 3/1024`,
`d0_1 d5_1 k10_0 = 5/4096`.  After doubling and substituting, with
localizer retained in `T`:

```text
M2a  v,k still drop;   NF1=1 DIM=12 MULT=16   (base 13, 8)
M2b  v3 reappears;     NF1=1 DIM=12 MULT=12
M2c  k  reappears;     NF1=1 DIM=12 MULT=8
```

matching the producer Groebner-level M2 table.  Support of the mutated
images is `C8`, `C8[v3]`, `C8[k]` respectively.

## 6. Audits 3–5 — scheme, nilradical, elimination

Singular 4.4.1, exact `Q`, `dp`, `option(redSB)`, `LIB "primdec.lib"`.
`sat()` was not used.  Positional loops bounded by `ncols`.  Per-process
`RLIMIT_CPU=60`; Darwin refused `RLIMIT_AS` (same kernel behaviour the
producer disclosed); RSS polled via `ps` against a 1 GiB kill.  Peak RSS
on finished jobs ≤ 1.2 MB except the killed CORE primdec at 151 MB.

### 6.1 Properness, dimension, radical, witnesses

```text
I4 = (phi(Lambda_{4,1..7})) + (z k - 1)  in T
I4_STD_NCOLS=22  I4_SLIM_NCOLS=22  mutual=1
I4_DIM=13  I4_MULT=8  reduce(1,std I4)=1
I4+(k) is the unit ideal
no localizer: DIM=14 MULT=4
```

`std` and `slimgb` agree by two-way reduction.  Forced-unit control
`ideal(1,s t)` reduces `1` to `0`; proper control `(s)` has `dim 15`.

```text
radical(I4) = (k z-1,
               2 s t - 16 u1 + 4 u3 - u5,          % = -RA
               s^2 - 64 t^2 - u0 + 4 u2 - 2 u4,    % = -RB
               128 t^3 + 2 t u0 - 16 s u1 - 8 t u2 + 4 s u3 + 4 t u4 - s u5)
```

The fourth generator is `2 t RB - s RA`.  Mutual reduction gives
`sqrt(I4) = (RA, RB, z k - 1)` with

```text
RA = 16 u1 - 4 u3 + u5 - 2 s t
RB = u0 - 4 u2 + 2 u4 - s^2 + 64 t^2
```

`primdecGTZ(sqrt(I4))` returns one component, `primary = prime`,
`dim 13`, `mult 8`.  Independent domain certificate: `RA` is degree 1
in `u1` with unit coefficient `16`, `RB` is degree 1 in `u0` with
coefficient `1`, so `T/(RA,RB)` is a polynomial ring in the remaining
fourteen generators and `T/(RA,RB,z k-1)` is the hypersurface `z k=1`
in that ring, a domain.  Jacobian of `(RA,RB,z k-1)` in `(u1,u0,z)` is
triangular with diagonal `(16,1,k)`, rank 3 on `D(k)`.  The reduced
locus is smooth, rational, isomorphic to `A^{12} × G_m` with free
coordinates `(s,t,u2,u3,u4,u5,v0..v5; k)` and `u0,u1,z` determined.
`dim = 12+1 = 13`.

Rational witnesses, exact substitution into the *literal* grade-two,
grade-three and grade-four source rows (no ideal machinery), each with
`k10_0 ≠ 0`:

```text
W0  s=t=0, u=0, v=0, k=1
W1  s=1, t=1, u=(-63,1/8,0,0,0,0), v=(7,-3,5/2,11,0,-1), k=2
W2  s=3, t=-2, u=(-247,-1/2,1,1,2,0), v=(1,2,3,4,5,6), k=-5/7
```

all give `RA=RB=0` and `Lambda_{2,r}=Lambda_{3,r}=Lambda_{4,r}=0` for
every `r`.  Negative controls: off-plane `d*_1=(1,0,0,0,0,0)` yields
`Lambda_{2,4}=3/524288`; a generic `RA=16, RB=0` point makes six of
seven grade-four images nonzero; `s=t=1, u=0` likewise.  The producer
N3 line "RA=0, RB=1 : rows 2 and 4 nonzero" is **point-dependent**:
`s=t=0, u0=1` fires only row 4; a more generic `RA=0, RB=1` point fires
six rows.  Directionally valid, not an invariant row list.  Repair R2.

### 6.2 Nilradical, index three, embedded structure, multiplicity

```text
RA, RA^2, RB, RB^2  not in I4
RA^3, RB^3, RA RB, RA^2 RB, RA RB^2  in I4
```

so `(RA,RB)^3 ⊂ I4` and `(RA,RB)^2 ⊄ I4`.  Since `z k-1 ∈ I4` already,
the nilpotency index of `sqrt(I4)/I4` is exactly 3.  Same memberships
hold for CORE in `C8`.  `mult(I4)=mult(sqrt(I4))=8` is consistent with
a generically reduced top component (three degree-2 leading terms under
`dp`) and is **not** by itself a reducedness proof.

Source of the thickening, independently decomposed in six variables:

```text
Q2 = (Lambda_{2,1..7}) in W
Q2_STD_NCOLS=6 = SLIM  mutual=1  DIM=4  MULT=1  NF1=1
Q2 ⊂ (A,B) = sqrt(Q2)   with A=16 w1-4 w3+w5, B=w0-4 w2+2 w4
Q2 ⊄ (A,B)^2   (5 of 6 generators violate)
A,B,A^2,B^2 not in Q2;  A B, A^3, B^3 in Q2
```

`primdecGTZ(Q2)`: three components.

```text
COMP 1  dim 4 mult 1  primary = prime = (A, B)
COMP 2  dim 3 mult 4  primary ≠ prime
        prime = (A, B, w2^2+64 w3^2-2 w2 w4+w4^2-64 w3 w5+16 w5^2)
COMP 3  dim 2 mult 5  primary ≠ prime
        prime = (2 w3-w5, w2-w4, 16 w1-w5, w0-2 w4)
```

Component 1 being reduced is the actual proof that the top-dimensional
part is generically reduced: `A` is nilpotent in `W/Q2` but becomes zero
after localizing at the minimal prime, exactly as in `(x^2, x y)`.
Component 3 is **literally** `J0` in `w`-coordinates, recovered from
grade-two quadrics rather than Fitting conditions.  That corroborates
the *definition* of the plane; it does not re-prove coordinator
exhaustiveness.

The producer printed associated primes of `Q2`, not the embedded
primaries.  The dim-4 line is both.  That is acceptable provided it is
read as primes; the dim-3 and dim-2 primaries are strictly larger than
the displayed primes.

CORE primdec in `C8` was killed at 60.20 s / 151 MB (`rc=-24`).  No
CORE/`I4` primary-decomposition claim is charged from that run.  The
generatorwise closed form plus the polynomial automorphism `σ` transport
the `Q2` decomposition to CORE; adjoining free `v` and the prime
`(z k-1)` (in variables disjoint from CORE) transports it to `I4`.
That transport is the charged embedded-structure argument.  A direct
`primdecGTZ(I4)` is a possible AWS replay, not a desk obligation.

### 6.3 Localizer constant; ordinary versus optimized

```text
z k-1 and 1-z k generate the same ideal (mutual reduction)
z k+1 and z k-2 give different ideals, same open D(k) (gauge)
z k  (drop the -1): plus (k) stays proper, so k=0 is admitted
no localizer: dim 14
z k-1 not in (z k+1)
```

The `-1` is exactly the open condition.  The declared form is correct.
`std`/`slimgb` mutual reduction holds for `I4`, `Q2`, and `sqrt(I4)`.

### 6.4 Elimination versus lifts

Computed in `T`:

```text
I4 ∩ Q[s,t]      = (0)
I4 ∩ Q[u0..u5]   = (0)
I4 ∩ Q[v0..v5]   = (0)
I4 ∩ Q[k,z]      = (k z-1)
I4 ∩ Q[s,t,u]    : 21-generator GB; in C8 this is CORE, DIM=6 MULT=4 NF1=1
```

(The same elimination ideal, viewed in `T`, has `dim 14` because `v,k,z`
remain free; that is a ring-declaration artefact, not a producer error.
CORE dimension is the C8 figure.)

These are closures.  Surjectivity (lifts) is separate:

- `(s,t)`: polynomial section `u=mu(s,t)`, `v=0`, `k=z=1`.  Because
  each `Q_r` is homogeneous of degree 2, `Q_r(0)=0`.  A section, not a
  dominance slogan.
- `v`: section `s=t=0`, `u=0`, `v` arbitrary, `k=1`, `z=1`.
- `k ≠ 0`: section `s=t=0`, `u=v=0`, `z=1/k`.  `I4+(k)` unit confirms
  the open is cut out, not vacuous.
- `u ∈ A^6`: set `P=16 u1-4 u3+u5`, `Q=u0-4 u2+2 u4`.  A point over
  `u` needs `2 s t = P` and `s^2-64 t^2 = Q`.  In
  `Q[s,t,P,Q]/(P-2 s t, Q-(s^2-64 t^2))`:

  ```text
  eliminate s,t  = (0)                         % dominant
  s^4 - Q s^2 - 16 P^2     in the kernel       % monic in s over Q
  256 t^4 + 4 Q t^2 - P^2  in the kernel       % monic in t over Q
  ```

  Finite and dominant of relative dimension 0 over an algebraically
  closed field is surjective.  Directly: the quartic in `t` always has
  a root, and if every root is `t=0` then `P=0` and `Q=s^2` is solvable.

Joint `(s,t,u)` content is exactly the pair `RA=RB=0` set-theoretically
(codimension two) and the six quadrics `Q_r(u-mu)` scheme-theoretically.
The two descriptions are not interchangeable.  Neither projection to
`(s,t)` nor to `u` carries a constraint; the coupling is joint.

## 7. Audit 6 — grade-five census and successors

Raw support of `Lambda_{5,1..7}`:

```text
d*_1, d*_2, d*_3, d*_4, k10_0, k10_1
```

After `phi` (plane only, everything else free), image term counts
`42, 49, 57, 53, 64, 33, 61` and variables:

```text
x = d*_4   DISAPPEARS from all seven rows
k1 = k10_1 DISAPPEARS from all seven rows
k  = k10_0 SURVIVES in rows 1,2,3,5,7   (absent from 4 and 6)
v  = d*_3  SURVIVES in rows 1,2,3,4,5,7 (absent from row 6)
u,s,t      present in all seven (row 6 has only s,t,u)
```

Grade five is the first grade at which `k10_0` and `d*_3` are
load-bearing on this plane.  A nonempty stratum survives, so there is
no conditional branch kill.

The two proposed descendants — radical-level grade-four input
`(RA, RB, z k-1)` versus scheme-level input
`(Q_r(u-mu), z k-1)`, each plus `phi5(Lambda_{5,1..7})` — are the
smallest correctly typed *grade-four conditions*.  They must be run
separately because `I4 ≠ sqrt(I4)`.  The six quadrics are the smallest
generating set of the scheme-theoretic input (`Q2` itself has a
six-element `std` basis).

The proposed 22-generator ring
`Q[s,t,u0..u5,v0..v5,x0..x5,k,k1,z]` is first-occurrence typed: `x`
and `k1` first occur at grade five in the unsubstituted rows.  After
the vanishing census already computed, they are dummy free coordinates
and inflate dimension by seven relative to the smallest computational
ring `Q[s,t,u,v,k,z]`.  That is Repair R3, not a reason to skip either
variant.

## 8. Binding repairs (fail closed)

**R1. Ring order.**  Successors and replays must declare jet-major `S`
and name-based maps.  Atlas `ring_variables` order is not `phi`.

**R2. N3 row list.**  Replace the invariant-sounding "rows 2 and 4" by
a named point, or by "a generic `RA=0, RB=1` point makes six of seven
images nonzero".

**R3. Grade-five ring.**  Keep both scheme and radical inputs.  Either
omit `x,k1` after the vanishing census, or retain them and label them
dummy so dimension is not misread.  Do not treat their presence as an
open condition.

**R4. Scratch archival.**  All 24 hashed producer scripts currently
exist under `/tmp/k00g4/` and match the listed digests, as do
`main{1..6}.out`.  They are not in the repository.  `/tmp` is not
custody.  Same class of defect the coordinator already recorded for the
rank-five 6,985-byte transcript: future certificates archive
serializations or the complete generating script in-tree.  This review's
own scratch is `/tmp/k00g4_rev_grok46/` and is likewise not in-tree;
the reconstruction procedure in §2 is the archival substitute.

**R5. Seal wording.**  The producer (and the coordinator) claim a unique
`BODY-END` marker; the string occurs again quoted in the seal section.
Body hashes using the *first* marker line match the seals.  Successors
should not quote the marker after the body.

**R6. Status, not algebra.**  The producer correctly refused to treat
plane exhaustiveness as a premise.  The coordinator has since promoted

```text
V(B, P3_1, ..., P3_7) = Pi × A^6_u
```

set-theoretically over an algebraic closure, with `R0=J0` as an ideal
equality and `sqrt(R1)=J0` only as a radical equality.  Composition with
grade four is now licensed.  If a later repair narrows `Pi`, §4–§6 must
be re-derived on the repaired locus; the identities transfer to any
plane on which `A=0` and `c3=0`.

Non-claims, unchanged: not a later-grade lift; not a formal or
convergent arc; not source-reachability; not a counterexample; not an
order-two or max-twelve exclusion; not a Keller pair; not a JC2
conclusion; not an equality of `I4` with `sqrt(I4)`; not a scheme
equality `R1=J0`.

## 9. Maximum safe theorem

Work over an algebraic closure.  Consume the coordinator: every
grade-three solution of `P3=0` over `V(B)` lies on `Pi`, with `u` free,
and conversely `P3` vanishes identically on `Pi × A^6_u`.  Independently,
the seven literal grade-four rows satisfy the polynomial identities

```text
phi(Lambda_{4,r}) = Q_r(u - (s^2, s t/8, 16 t^2, 0, 0, 0)),   r=1..7,
```

contain no `d*_3` and no `k10_0`, and generate, together with
`z k10_0 - 1`, a proper ideal `I4 ⊂ T` of affine dimension 13 and
multiplicity 8, with

```text
sqrt(I4) = (RA, RB, z k - 1)
```

prime.  Set-theoretically

```text
V(I4) = { RA = RB = 0,  k ≠ 0 }  ⊂  A^{15} × D(k)
```

is irreducible, smooth, rational, isomorphic to `A^{12} × G_m`.
Scheme-theoretically `I4` is a multiplicity-preserving thickening of
index exactly 3, transported from `Q2`, whose unique minimal prime is
the reduced 4-plane `(A,B)` and whose dimension-2 embedded prime is
`J0`.  Grade four imposes no separate constraint on `(s,t)`, on `u`,
on `v`, or on `k10_0 ≠ 0`; the whole content is the joint pair
`RA=RB=0`.  A nonempty stratum survives, so the live K00 branch is the
literal grade-five system on this plane, with `k10_0` and `d*_3` now
load-bearing.

## 10. Launch / stop

Launch, desk-scale, both variants of `K00-G5-RANK0-PLANE` as in §7,
with Repair R3 in the prompt, the same plane map, the same localizer,
and the same mutation battery (plane coefficients, one literal
grade-five coefficient, localizer `-1`, `std` versus `slimgb`).
Questions: unit/proper; dimension; whether `k10_0` or `d*_3` is forced;
whether the two plane directions inside `u` survive; scheme versus
radical input as separate answers.

Stop: rank-three/four/five Fitting and localizer jobs (already stopped
by the coordinator); rank-two charts; selected rank-one `I2(E3)` charts;
any grade-six job; any attempt to collapse the two grade-five variants
into one; any exit-price declaration.

Do not relabel historical capped jobs.  A Linux replay of `primdecGTZ`
on CORE or `I4` is optional and not blocking.

## 11. Resources (this review)

Engine: Singular 4.4.1 (44105, arm64-Darwin), GMP 6.3.0, NTL 11.6.0,
FLINT 3.6.0; CPython 3.14.7, `fractions.Fraction`.  Producer used
CPython 3.9.6; the two Python versions plus independently written
scripts are the different-model split.

```text
run        rc    wall_s   rss_peak_kb  note
recon.py    0     1.1        n/a       identities, census, witnesses
ctl         0     0.22       1120
finite      0     0.21        864
q2          0     0.22       1136      includes primdecGTZ(Q2)
i4          0     0.22       1120      includes radical(I4), loc variants
elim        0     0.21       1120
compareG    0     0.22        864      g4_sub.txt vs independent
mut2loc     0     0.21        864      M2 with localizer
coreprim  -24    60.20     151264      SIGXCPU; not charged
```

Independent scratch hashes (`/tmp/k00g4_rev_grok46/`):

```text
3c29d982558c67b9a59adc2b51c907980e805a707d4a820e3ac5427753640032  recon.py
7099412193007a66af24972e9946222e879fa7755110167830f61321e385aa1e  q2.sing
21b29467628a70af505705c51dc131e8b0bb0b5a038910ff181d98e9eaa75ba1  i4.sing
dcb09c53d7cc6575a039b7fe40ba84a22f92c4398b478be468ec5b1d12acc51b  elim.sing
a8508f3e08926d09d89670106a3d1d9f7ad31ad7b47345de0e0c9bef58c919fc  g4_sub.json
69061229126e337e154703d91eebbdc1a1aefeeb7d85c53d5fdcb30510ddda78  q2.out
250c0c1fc2c83b8ecf7e6f94c922f28830799011d443ed0cae0ae04276e7efba  i4.out
19f687cd7069729b460c5f4474e6060f4cc868ec5cec1694703a8a20f24accd1  elim.out
```

Producer `/tmp/k00g4/` listed hashes: 24/24 match at review time,
including `raw19.sing = d743bd9d...` and `g4_sub.txt = 38fc7287...`.
That match is custody of an unarchived tree, not an independent
reconstruction (Repair R4).

<!-- BODY-END -->

## Seal

- Body definition: every byte of this file from offset 0 through the end
  of the unique HTML comment marker line that closes the body, including
  that line's terminating newline.  That marker occurs once.  This seal
  is outside the body.
- Body bytes: `25176`
- Body SHA-256: `41da5999a230115a8a63bc0b7793534dd9ab39800aa5ed77ce493381cbb479c2`
- Frozen campaign basis: `40c1ab3448209e3d87173feb947a733f6fe54f7f`
- Producer full SHA-256: `0d2a9861126c8857e04a9170c8586b6b4eabe67d2e65d3b4d3b7e991774b614f`
- Coordinator full SHA-256: `d453b9563d8f6cc23319d6bc0d8edce8a83f657b9e3a60cb244b00f181459860`
- Atlas SHA-256: `d7ec6d18d58265421ff315fa00e38cd32992ac12f7d8166cf6c436e23bf06501`
- Disposition: `PASS_WITH_REPAIR`
- Exit-price declaration: absent (no new exit price asserted)
- Fail mode: closed
