# Sol 5.6 provisional hostile disposition — TD12-B25-RESROW/v1

Date: 2026-08-29  
Frozen Git basis: `92ebe92ad5986a47f01af9ed901260595dfed869`

## 0. Binary disposition

```text
RESROW_VACUOUS_ON_CLASS
FABLE_C1_TOP_SCALE_REPAIR_REQUIRED
FABLE_C4_INTEGRATING_FACTOR_REFUTED_AS_WRITTEN
FIRST_RESONANCE_TWO_RESIDUES_IDENTICALLY_ZERO
NO_ROUTE_KILL
NO_RESROW_DESCENDANT_LICENSED_AT_j=17
```

The proposed first post-landing obstruction does not exist.  After the
correct integrating factor is restored, the `j=17` right side is the
derivative of one explicit rational function.  Therefore both putative
deck-orbit residue functionals vanish identically wherever the preceding
rational tail is defined.  This remains true after intersecting with any
source-honest B pure-power child conditions.

There are two separate slips in the Fable report.  The first is a
repairable leading-scale normalization in C1.  The load-bearing error is in
C4(iii): its integrating-factor equation contains `p^(I-1)` where exact
coefficient collection gives `p^(I-i)`.  At the first resonance those are
`p^(i-1)` and `1`, respectively.  The erroneous extra factor is precisely
what turns an exact derivative into apparent residue conditions.

This report stops the proposed `s*+17` descendant.  It does not assess the
Fable source-bridge Theorems A/B, prove route occurrence, emit a source
packet, or alter any canonical campaign file.

## 1. Custody and notation firewall

Actually read and charged:

```text
0175063f5dcef9c3ba1c70d3ad883ad28f8757d514ec387b968b29324272274b  xmodel/td12-global-source-bridge-b-fable5-92e-20260829.md
1a60264334ae99f60ff79f1ed8b4a75cb42abf30f5e4ae8001a51b9064056d84  xmodel/td12-bchild-v1-primary-fable5-76c-20260829.md
876d1717efdc69865cfae6c8b5d4ef983440a5f0997a9edf3cf13a2a5cc70aab  xmodel/td12-bchild-v1-primary-fable5-hostile-disposition-r1-sol56-76c-20260829.md
97ba497fffcf0a0ee5c9ee259acc325810659a9fd5376a47b38c87476fd2c5b4  xmodel/td12-formal-cascade-rank-v1-coordinator-integration-sol56-20260829.md
1272b394387d744ae065680c8327ff79d0179fb994c6d03d6d8c27d41d371c61  xmodel/td12-inhomogeneous-row-first-invariant-sol56-20260829.md
```

History was searched for `TD12`, `BCHILD`, `deviation`, `landing`,
`resonance`, `residue`, `(V)/(W)`, and pure-power children.  The Fable
report is the only located file proposing a below-landing `j=17` residue
row.  The prior inhomogeneous-row report reaches the landing/Hermite class,
not this tail.

Keep the three integers distinct throughout:

```text
kappa_F  = chart denominator in the Jacobian coefficient equation;
nu       = 25, the B deck order and top-pattern lattice;
kbar     = 17, the B local state numerator.
```

Set

```text
D       = D_F = 25 i,
r       = 3i/2 in Z_(>0),
p       = (t-A)^2(t-B),       t=eta^25,
B/A     = 9/8,                A,B != 0,
q       = eta(t-A)(t-B),
P_0     = lambda_f p^i,       lambda_f != 0,
G_0     = c_g p^r,            c_g != 0.
```

No `i=6n` direct-entry rider is used.  The reviewed B window uses even
`i`, and its transparent depth-24 range uses `i>=16`; in particular the
exceptional value `i=1` cannot repair the exponent error below.

## 2. First repair: the deviation's leading scale

Use the Fable report's own convention

```text
(f^F)^rho has leading piece lambda_f^rho p^(i rho).
```

Then the leading term of `g^F-alpha(f^F)^(3/2)` cancels only for

```text
alpha = c_g lambda_f^(-3/2),                         (2.1)
```

with a consistent choice of the square root of `lambda_f`.  C1 instead
writes `g^F-c_g(f^F)^(3/2)` while retaining arbitrary `lambda_f` later.
Its literal top-cancellation assertion is therefore false unless
`lambda_f=1` has separately been normalized.  The clean repair is (2.1),
or an explicit globally propagated normalization `lambda_f=1`.

This slip is not the cause of the residue failure.  Let

```text
H(f^F) = alpha(f^F)^(3/2) + sum_ell C_ell(f^F)^(rho_ell)
Dev    = g^F-H(f^F),
```

where the `C_ell,rho_ell` are whatever earlier greedy-ledger constants and
exponents have actually been justified.  Every term of `H` is a formal
function of `f^F`, so

```text
J(f^F,H(f^F))=0,        J(f^F,Dev)=J(f^F,g^F)=x^(-u). (2.2)
```

Consequently all `c_g,C_ell,rho_ell` dependence is absorbed into the
definition of the actual deviation pieces; none occurs explicitly in the
tail recurrence.  This cancellation is exact, not an omission of data.

For the rest of the audit it is enough to grant conditionally the repaired
landing asserted in C2/C3.  Write

```text
Dev = sum_(j>=0) T_j(eta) x^((kbar-D-j)/kappa_F),
T_0 = gamma q p^(-i),
gamma = kappa_F/(25 i lambda_f A B).                 (2.3)
```

Direct substitution in the landing row verifies (2.3) from
`25pq'-17p'q=25ABp`.  No C1--C4 recurrence is assumed below.

## 3. Independent coefficient derivation

Expand

```text
f^F = sum_(a>=0) P_a(eta) x^((D-a)/kappa_F).
```

Collecting the coefficient of the Jacobian of `f^F` and `Dev` at relative
tail order `j` gives, directly from (2.2),

```text
sum_(a+b=j)
  ((D-a)P_a T_b'-(kbar-D-b)P_a'T_b)
    = kappa_F * 1_(j=0).                             (3.1)
```

For `j>=1`, put

```text
R_j := -sum_(a=1)^j
  ((D-a)P_a T_(j-a)'
   -(kbar-D-j+a)P_a'T_(j-a)).                        (3.2)
```

The `a=0` term of (3.1), using `P_0=lambda_f p^i`, is exactly

```text
i lambda_f p^(i-1) L_j[T_j] = R_j,                  (3.3)

L_j[T] := 25pT' + (25i+j-17)p'T.                    (3.4)
```

Equations (3.1)--(3.4) rederive the recurrence from `J(f^F,Dev)=x^(-u)`;
they use neither the claimed C4 conjugation nor C1's normalization.

At a resonant index

```text
j=17+25m,       I=i+m,
```

one has the correct conjugation

```text
L_j[T] = 25 p^(1-I)(p^I T)'.                        (3.5)
```

Substitution of (3.5) into the *whole* fresh term (3.3), including its
outer `p^(i-1)`, gives

```text
25 i lambda_f p^(i-I)(p^I T_j)' = R_j,

(p^I T_j)' = p^(I-i) R_j/(25 i lambda_f)
            = p^m R_j/(25 i lambda_f).              (3.6)
```

Fable C4(iii) instead states

```text
(p^I T_j)' = p^(I-1) R_j/(25 i lambda_f).            (3.7; false)
```

The missed factor is the `p^(i-1)` already present in (3.3).  At `j=17`,
(3.6) has factor `p^0=1`, whereas (3.7) has `p^(i-1)`.  This is not a
gauge or notation difference: at `i=2`, for example, (3.3)--(3.5) read
`50 lambda_f(p^2T_17)'=R_17`, while (3.7) inserts an extra nonconstant
factor `p` on the right.

Thus the general C4 residue statement is repairable only after replacing
`p^(I-1)` by `p^(I-i)=p^m`.  Its specialization in Fable Section 5 is
invalid as written.

## 4. Exact expansion at the first resonance

Now set `j=kbar=17`.  For every `1<=a<=17`, the second coefficient in
(3.2) is

```text
kbar-D-j+a = a-D.
```

Therefore each summand, before any `(V)/(W)` specialization, is

```text
(D-a)P_a T_(17-a)'-(a-D)P_a'T_(17-a)
  = (D-a)(P_a T_(17-a))'.                           (4.1)
```

Define the completely typed rational tail expression

```text
S_17 := sum_(a=1)^17 (25i-a) P_a T_(17-a),          (4.2)
```

where `T_0` is (2.3), and `T_1,...,T_16`, when they exist, are the unique
rational solutions of (3.2)--(3.4) at the nonresonant preceding rows.
Then

```text
R_17 = -S_17'.                                      (4.3)
```

The corrected first-resonance equation is consequently

```text
(p^i T_17)' = -S_17'/(25 i lambda_f),                (4.4)

T_17 = -S_17/(25 i lambda_f p^i) + C_17 p^(-i),     (4.5)
```

with the expected one-dimensional resonant gauge `C_17 in C`.

This explicitly types every dependency requested by the proposed client:

- `P_1,...,P_17` occur in the finite bilinear expression (4.2);
- the rigid earlier tail is `T_0,...,T_16`, recursively typed by
  (2.3), (3.2)--(3.4);
- `kappa_F,A,B,i,lambda_f` enter through `T_0` and (4.4);
- `c_g` and all earlier ledger constants `C_ell,rho_ell` have no explicit
  dependence, for the exact reason (2.2); they only select the actual
  representative `Dev` whose pieces satisfy the recurrence;
- `nu=25`, `kbar=17`, and `kappa_F` have not been identified.

## 5. The two deck-orbit functionals

Choose any eta-roots `zeta_A^25=A` and `zeta_B^25=B`.  The two candidate
orbit functionals supplied by the *correct* first-resonance equation are

```text
Res_A(P_1,...,P_17;T_0,...,T_16)
 := Res_(eta=zeta_A) [R_17/(25 i lambda_f) d eta]
  = -Res_(eta=zeta_A) [dS_17/(25 i lambda_f)]
  = 0,                                                (5.1)

Res_B(P_1,...,P_17;T_0,...,T_16)
 := Res_(eta=zeta_B) [R_17/(25 i lambda_f) d eta]
  = -Res_(eta=zeta_B) [dS_17/(25 i lambda_f)]
  = 0.                                                (5.2)
```

The residue of the derivative of a rational function is zero at every
point, so (5.1)--(5.2) do not merely agree along each deck orbit: every one
of the fifty point residues vanishes separately.  They are **identically
zero functionals**, not nonzero constraints and not an inconsistency.

The result is fail-closed with respect to the reviewed `(V)/(W)` class.
That class by itself supplies f-side polynomials, not existence of the
rational deviation tail through rows `1,...,16`.  If an earlier row has no
rational solution, the member never reaches RESROW.  On the entire domain
that does reach row 17, however, (4.1) is formal and the two residues are
identities.  Hence row 17 cannot furnish a new obstruction on the class.

Likewise, any source-honest B pure-power child constraints merely cut down
the allowed `P_a`.  Since (5.1)--(5.2) hold before specialization, their
intersection with that subset is still identically zero.  No child value,
completion datum, occurrence witness, or unattested transport map is
invented to reach this conclusion.

## 6. Precise disposition of the Fable claims

Repairable without changing the landing result:

1. C1's first subtraction becomes
   `c_g lambda_f^(-3/2)(f^F)^(3/2)` (or one must state and propagate
   `lambda_f=1`).
2. At `j=17+25m`, C4(iii)'s candidate residue form becomes
   `p^m R_j/(25 i lambda_f)d eta`, not
   `p^(I-1)R_j/(25 i lambda_f)d eta`.
3. C4(ii)'s existence remains actual-pair conditional.  Nonresonance gives
   uniqueness in the rational class; it does not by itself give existence
   for every arbitrary `(V)/(W)` jet.

Invalidated as written:

1. the verdict that `s*+17` is the first genuinely unspent consequence;
2. C4(iii)/Section 5's displayed first-resonance 1-form;
3. the claim of two nontrivial residue conditions coupling
   `P_1,...,P_17` to the rigid tail;
4. the proposed `TD12-B25-RESROW/v1` kill/emission descendant at `j=17`.

The general resonance locations from C4(i) survive the algebraic audit.
At `j=17+25m`, (3.2) can be rewritten

```text
R_j = -sum_(a=1)^j [(D-a)(P_aT_(j-a))'
                    +25m P_a'T_(j-a)].              (6.1)
```

Thus the total-derivative collapse is special to `m=0`.  A later row may
carry genuine corrected residues; the next candidate is `j=42`, and it
would consume data through `P_42`, not the B24 window.  This observation is
only frontier guidance, not a new descendant or nonvacuity claim.

## 7. Controls and scope

Exact desk controls:

```text
top scale:
  lead(alpha f^(3/2)) = alpha lambda_f^(3/2) p^r
  equals c_g p^r iff alpha=c_g lambda_f^(-3/2).

integrating factor:
  i lambda_f p^(i-1) * 25 p^(1-I)(p^I T)'
    =25 i lambda_f p^(i-I)(p^I T)'.

i=2, m=0 mutation:
  exact fresh term =50 lambda_f(p^2T_17)';
  Fable's formula differs by the nonconstant multiplier p.

first resonance:
  kbar-D-17+a=a-D forces every cross term to
  (D-a)(P_aT_(17-a))'; residue of its sum is zero pointwise.

general-resonance mutation:
  replacing j=17+25m by j=17 gives exactly the disappearance of the
  25m P_a'T_(j-a) terms in (6.1).
```

No checker was needed: all controls are one-line identities in a
differential field.  No web, AWS, remote shell, CAS, heavy local process,
or canonical edit was used.  `jc2-lean` was not accessed.  This is the only
repository file written by this lane.  No commit or push was performed.

## Seal

Git basis `92ebe92ad5986a47f01af9ed901260595dfed869`, rechecked before
sealing.  Body = all bytes of this file before the literal `## Seal`
heading.

```text
report_body_bytes = 11988
report_body_sha256 = 9c72c20e02efcb74fd351f7ac820268386a625dbfc60b855dc18a1e212766b4f
```
