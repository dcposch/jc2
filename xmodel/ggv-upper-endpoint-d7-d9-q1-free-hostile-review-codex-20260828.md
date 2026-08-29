# Hostile review: the upper branch-P D7--D9 repair is q1-free

Date: 2026-08-28  
Reviewer: Codex hostile-review lane `d9_divisor_hostile`  
Charged producer: `ggv-upper-endpoint-q1-prefix-d7-d9-divisor-target-sol-ultra-20260828.md`  
Verdict: **REPAIR — EXACT; THE CLAIM IS TRUE AND STRICTLY STRONGER THAN STATED**

## 1. Adjudication

The producer's implication is correct, but its q1 label is not load-bearing.
Neither

```text
V0=A'R0+2AR0'
```

nor `R0`, the identity `gcd(A,V0)=gcd(A,R0)`, or the D23 row that licenses
q1 occurs in the D7--D9 proof.  The clean theorem is the following.

> Let the ground field have characteristic zero.  Let `A` be a monic
> squarefree quartic and assume the reviewed branch-P reduced prefix
>
> ```text
> F0=A^4,
> F1=A^2 V0,
> F2=(V0^2+A^2 Z)/4,
> F3=(V0 Z+A T)/8,
> ```
>
> with the literal raw bounds `deg(F_n)<=16-n`, `deg(G_n)<=24-n`, and the
> branch condition `c2=0 or A|V0`.  If the characteristic coefficients
> through weight nine are polynomial—equivalently, on the reviewed
> characteristic parametrization the raw rows `D1=...=D9=0` are
> solvable—then `A|T`.

This holds over any characteristic-zero field, not merely an algebraically
closed one: the argument may be made in the residue fields of the irreducible
factors of `A`, and divisibility descends to the ground field.

Thus there is no false mathematical consequence caused by the q1
over-specialization.  The necessary repair is to remove q1/R0/D23 from this
theorem's hypotheses and to retain q1 only as an optional later restriction.

## 2. Independent source and mode reconstruction

I used the literal source recurrence

```text
D_n=sum_(i+j=n) ((12-j)F_i'G_j+(i-8)F_iG_j')
```

and the raw windows

```text
deg F_n<=16-n,   deg G_n<=24-n.
```

The independent checker does not import producer code.  Instead of the
producer's differential recurrence for fractional coefficients, it expands
each power by the generalized binomial theorem after writing
`F=A^4(1+u)`.  Through weight nine it retains the complete born-mode expression

```text
G = F^(3/2)
  + c2 t^2 F^(5/4)
  + c4 t^4 F
  + c6 t^6 F^(3/4)
  + c8 t^8 F^(1/2)                 mod t^10.
```

The later legal modes at weights `10,12,14,16,18,20` are also registered but
are unborn here.  No mode was discarded merely because it is regular.

The degree firewall is automatic.  A principal monomial of weight `n` in
`F^(3/2)` has degree at most `24-n`.  A mode born at `m` has degree at most
`24-n-m`, hence is strictly inside the same raw upper window.  Consequently a
polynomial characteristic coefficient already lies in the literal raw
window; there is no hidden high-degree obstruction or cancellation.

The reconstructed polar formulas are as follows.  Put

```text
K4=64F4-Z^2.
```

On `c2=0`,

```text
g7^- = 3T(AK4-2TV0)/(2048A^2),

g8^- = 3/(32768A^4) * [
          (AK4-4TV0)^2-8A^2T^2Z
          +1024A^3(c6V0^2+F5T)
        ].
```

After D8 kills `c6` on every stratum where `B=A/gcd(A,V0)` is nonconstant,
the full c2-zero weight-nine polar part is `N9/(65536A^6)`, with

```text
N9=-48T^2V0^3+1536AF4TV0^2-24ATV0^2Z^2
   -12288A^2F4^2V0+384A^2F4V0Z^2+48A^2T^2V0Z
   -3A^2V0Z^4-768A^3F4TZ-8A^3T^3+12A^3TZ^3
   +768A^3F5(AK4-4TV0)+6144A^5F6T.
```

On the active branch `V0=AS`, all c2 terms at D7 are regular and

```text
g7^- = 3T(K4-2TS)/(2048A).
```

At D8 the complete negative part is

```text
3[(K4-4TS)^2-8T^2Z]/(32768A^2)
+5c2 P8/(65536A)+3F5T/(32A),

P8=-(S^2-2Z)^3-8(S^2-2Z)(K4-2TS)+32T^2.
```

The active A-adic mode census is decisive:

| row | term | smallest A-power |
|---:|---|---:|
| D7 | c2 | 0 |
| D8 | c2 | -1 |
| D8 | c6 | +1 |
| D9 | c2 | -2 |
| D9 | c6 | 0 |
| D9 | F5 | -2 |
| D9 | F6 | -1 |
| D9 | same-row F9 | +2 |

Thus none can touch the principal A^-3 class at D9.  The independently
reconstructed class, after `J=K4-2TS`, is

```text
[-3S J^2+12T J(S^2-Z)-12ST^2(S^2-2Z)-8T^3]/65536.
```

The regular `c4` and `c8` modes, `F7,F8,F9`, and the raw same-row correction
likewise cannot cancel either load-bearing class.  At odd weight nine there
is no polynomial homogeneous characteristic mode.

## 3. Divisor proof, including every endpoint

On `c2=0`, define without q1

```text
C=gcd(A,V0),  A=CB,  V0=CV1.
```

Because `A` is squarefree, `B` and `V1` are coprime.  D7 first forces
`B|T`: at each irreducible factor of `B`, `V0` is nonzero and the reduction
of `T(AK4-2TV0)` is `-2T^2V0`.  Write `T=BU`.  Exact cancellation gives

```text
C | U(K4-2UV1).                                           (D7-C)
```

D8 becomes

```text
A^2 | (K4-4UV1)^2-8B^2U^2Z
      +1024A(c6 C^2V1^2+F5BU).                            (D8-C)
```

If `B` is nonconstant, (D8-C) first makes `K4-4UV1` divisible by every
factor of `B`.  All other terms then have B-adic order at least two except
the c6 term, whose order is exactly one unless the scalar `c6` is zero.
Hence `c6=0`.  This is the active-c6 valuation step; it does not apply or
need to apply when `B=1`.

Substitution into the independently reconstructed `N9` gives

```text
N9=C^3B^2 P9,

P9=-3V1D^2-12B^2UZD-8B^4U^3
   +768CB^2F5D+6144C^2B^4F6U,
D=K4-4UV1.
```

Let `p` be any irreducible factor of `C`.  If `U` is nonzero in the residue
field `K[X]/(p)`, D7 gives `K4=2UV1`, so `D=-2UV1`.  D8 then gives the
division-free relation

```text
U^2(2B^2Z-V1^2)=0.
```

The D9 numerator reduces exactly to

```text
P9=12U^2V1(2B^2Z-V1^2)-8B^4U^3=-8B^4U^3,
```

which is nonzero.  This contradicts D9.  Notice that this calculation does
not divide by `V1`; it remains valid when `V1=0` at the C-root.  Therefore
every factor of `C` divides `U`, so squarefreeness gives `C|U` and hence
`A=CB | BU=T`.

The endpoint audit is complete:

- `C=1`: `B=A`, and D7 already gives `A|T`.
- `1<deg(C)<4`: the residue-field argument above gives `C|U`.
- `C=A`, including `V0=0`: write `V0=AS`.  If `T` is nonzero at an
  A-factor, D7 gives `J=0`, D8 gives `S^2=2Z`, and the uncancellable D9
  class is `-8T^3/65536`, a contradiction.
- `V1` a unit, zero, or vanishing only at selected C-roots: no separate
  assumption is used; the division-free formulas cover all three cases.
- `c2` and `c6` active: the displayed valuation table shows they cannot
  touch the A^-3 active obstruction.

## 4. Literal raw negative controls

The second checker engine constructs four exact raw fixtures with
`D0=...=D8=0`, all literal degree windows satisfied, and `A` not dividing
`T`.  Each is killed by a nonpolynomial weight-nine characteristic
coefficient:

1. proper `C=X-1`, `V1=1`, outside q1;
2. proper `C=X-1`, `V1=X-1`, outside q1 and with `V1=0` at the C-root;
3. active `C=A`, `V0=0`, with both `c2` and `c6` nonzero;
4. active `C=A`, `V0=A`, outside q1, again with both `c2` and `c6` nonzero.

For the active fixtures the exact choice `c2=1`, `c6=3`, `c4=2`, `c8=5`,
`F5=-5/192` deliberately exercises rather than deletes the lower-pole mode
cancellation at D8.  Exact q1 matrices have rank five; each non-q1 fixture
has augmented rank six.  A separate `C=1,V0=1,T=1` mutation fails already
at D7, as required.

These fixtures independently confirm both that q1 is unnecessary and that
the active-mode firewall is real rather than a prose valuation claim.

## 5. Field/radical and gauge firewalls

The theorem is an exact statement about solutions over fields.  In a
parameter scheme it gives a radical/field-point conclusion.  The proof
passes to reduced irreducible factors and uses that a nonzero residue is a
unit; it does not prove ideal membership expressing `A|T` over rings with
nilpotents.  No scheme-divisibility upgrade is licensed.

After `T=AU0`, the c2-zero computation is also q1-free.  D8 writes

```text
Delta4=F4-V0U0/16-Z^2/64=A W,
```

and D9 is exactly

```text
A^2 | W[-16V0W+A(64F5-U0Z)].
```

For `C=gcd(A,V0)` and `B=A/C`, this forces `B|W` at field points but does
not yet force `C|W`.  That is the clean post-D9 split.

No translation gauge is needed for the repaired theorem.  Conversely, this
review does not rehabilitate the failed translation: its raw-window leakage
and bound-G22 contribution remain genuine.  The active post-D9 block must
still be kept separate rather than normalized to `V0=0` by a shear.

## 6. Reproducibility and scope

Artifacts:

```text
cases/ggv_8_28_upper_endpoint_d7_d9_q1_free_hostile_review_20260828/
```

Replay:

```bash
cd cases/ggv_8_28_upper_endpoint_d7_d9_q1_free_hostile_review_20260828
PYTHONDONTWRITEBYTECODE=1 python3 -B verify_d7_d9_q1_free.py --check
shasum -a 256 -c SOURCE.sha256
shasum -a 256 -c EVIDENCE.sha256
```

This review proves only the q1-free D7--D9 divisor repair and the q1-free
c2-zero post-repair W split, under the reduced branch-P prefix.  It does not
prove scheme divisibility, solve the active post-D9 block, transport the
fixed `V0=1` D22 endpoint collapse, establish a raw/GGV landing, or imply a
Keller-pair or JC2 theorem.

