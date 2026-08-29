# Hostile review — affine-Faber `A` loaded relative-order-six kernel face

| Field | Value |
|---|---|
| Target | `cases/max12_812_order2_affine_faber_a_loaded_kernel_sigma45_20260826/` |
| Charged freeze | `FREEZE.sha256` = `50b6af9406bae9760f82d93dcd9ac6f274f384b3e1126fea4fb28455b152db0c` |
| Charged hand certificate | `HAND_CERTIFICATE.md` = `92b9c9fd8948e564e4110c8807d3f4ebadf3e289dcf55787b9482c8111829509` |
| Charged result | `RESULT.md` = `0a1a7fc9e22bf370b97c4342c67b59a79cac986c1b8ec65861ed33a44b3ad98e` |
| Overall verdict | **REPAIR** |
| Smallest failing identity | none |
| Smallest missing valuation face | omitted order-six moving-center / non-normalized Rees jet `a6` (and, after ramification, any intermediate center/source/complement/tangent jet that meets absolute weight 42); no two-sided absorption lemma is supplied |
| Reviewer / model | Grok 4.6 (xAI). Independent hostile rederivation. Different model family from the producer. No producer status line, no `PASS`/`UNIT`/`ENDPOINT` token, and no charged review token is evidence |
| Method | SHA-256 of every charged pin; independent reconstruction of all seven frozen ordinary-Faber tail strings; hand identities on the exact-`Q` grade-42 rows; source reading of the compiler, both exact-`Q` charts, and the parent sigma-45 erratum. Characteristic 65521 was not used as characteristic-zero algebra |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `418e413593120d19e15e6546eb50c985f4b1f038` |
| Date | 2026-08-26 |

Independently recomputed SHA-256 of the five files named in the review
prompt match those pins. Independently recomputed SHA-256 of every freeze,
evidence, and exact-`Q` artifact used below match the corresponding
manifest rows. Producer verdict language, `A_LK45_UNIT`,
`A_LK45_ENDPOINT`, validator `PASS_*` strings, and both F65521 lanes were
not used as characteristic-zero evidence. Exact `Q` is the mathematical
lane: the seven printed grade-42 polynomials and the two printed localized
bases. No file other than this review was written. `jc2-lean` and shared
ledgers were not touched.

---

## Verdict

**REPAIR.**

On the literal integral sigma face compiled here, the algebra is correct
and both registered projective charts are empty. The frozen compiler
rebuilds all seven ordinary-Faber tails from the charged `tails.json`,
retains every load, target, kernel, complement, and `(e,m)` jet that can
meet absolute grades 42--45 on that integer support, and prints seven
grade-42 rows that match the hand certificate termwise. The identity

```text
G3-(p/4)G1 = -(3/8)*m*x6*y6
```

holds over `Q`. On `D(m)` it forces `x6*y6=0`. The two charts `D(x6)` and
`D(y6)` then exhaust the nonzero leading kernel `P^1` of this integral
support, and `G6` followed by `G4` contradicts each chart with the stated
scalars and signs. The two exact-`Q` localized bases are the unit ideal;
that is scheme-theoretic corroboration, not an input to the hand proof.

The producer nevertheless claims that the **full** relative-order-six
kernel face is empty. That is a uniform theorem for every rational arc
with first transverse kernel order six, not a theorem about integer jets
in the family parameter `s`. The compiler truncates the moving center at
`aa=s^5*a5`, omits every non-integral relative order, and supplies no
two-sided moving-discriminant / K2 / Rees-coordinate lemma. The omitted
integral jet `a6` enters `QC` at the same order as `x6` and contributes
`N2` at the same order 21 as the kernel quadratic, so it is capable of
tying the first grade-42 face. After a ramification `s=t^e`, the same role
is played by any intermediate center, source, complement, or tangent jet
that meets total weight 42. Those arcs are not in the two-chart
certificate. No surviving residue was computed, and no printed identity
is false.

The `q=15/2` client remains separate and live. The `q>15/2` sigma-45
slice remains the strong normal-form identity quarantined by its erratum.
This review does not claim `m=0`, terminal or Taylor closure, order two,
maximum twelve, or JC2.

**REPAIR**

---

## Hashes and charged artifacts

Recomputed SHA-256:

| Artifact | SHA-256 | Role |
|---|---|---|
| `.../FREEZE.sha256` | `50b6af9406bae9760f82d93dcd9ac6f274f384b3e1126fea4fb28455b152db0c` | freeze manifest (matches required pin) |
| `.../HAND_CERTIFICATE.md` | `92b9c9fd8948e564e4110c8807d3f4ebadf3e289dcf55787b9482c8111829509` | hand source-row certificate (matches required pin) |
| `.../RESULT.md` | `0a1a7fc9e22bf370b97c4342c67b59a79cac986c1b8ec65861ed33a44b3ad98e` | producer result (matches required pin) |
| `.../EVIDENCE.sha256` | `55f8d39c6730fb312f449b42e3ae6cd893ad56a37516f6ab5657ea93ec7ffc15` | evidence manifest (matches required pin) |
| `.../RESULTS.sha256` | `2e7935083e513ad861c161389569527807da2af62080800f4e93335a79d464eb` | results manifest (matches required pin) |
| `.../REGISTRATION.md` | `940a19001b56a8738963ec817612c4a538ed09e1e3d5d228221d821a9f74ae6f` | registered charts and scope |
| `.../compile_loaded_kernel.py` | `a32372ce3fd088be74a3456f63c17bcb880c2eaf32c1856e86eb52d7b15f385a` | loaded-kernel compiler |
| `.../run_aws.sh` | `8dac13040bc92ba973f0f38380d0d7a9699a2dbdfa59dec51a421a76481421c2` | freeze pin |
| `.../launch_host.sh` | `d74a0a52ee3abe8db15e76d82c41050b3d22301779e2d02e763e51b48de452ea` | freeze pin |
| `cases/.../compile_sigma45.py` | `c19badfcfad44842f42118d031a5bfe92729d714e2a329b2af7097be629ea3d9` | frozen parent tail renderer |
| `cases/.../tails.json` | `d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848` | complete frozen ordinary-Faber tails |
| canonical `tails.json` | `6eed03d486e1cd9e8d990eed74a105293d383882bbae77d204eac190cce387e8` | matches parent `EXPECTED_CANONICAL` |
| exact-`Q` `q6x` `.sing` | `613bba4b237346208d0f5a657868d9bba0ced67e0461a441be04c8a3a5e6e703` | compiled source, chart `D(p*m*kk*x6)` |
| exact-`Q` `q6y` `.sing` | `247692eb7ad36880fc0622508273653d1df242ace7d08df42eda2fbda557cc72` | compiled source, chart `D(p*m*kk*y6)` |
| exact-`Q` `q6x` stdout | `ff25b14cc3aa2b479fd61b5bbd391a6d4df20ef4172bc0916358643296323a96` | printed G42 rows and localized basis |
| exact-`Q` `q6y` stdout | `ec3a889f84c6c5d6b35729f54e07682e010ae3b2bd3f74ad264a785006702be8` | printed G42 rows and localized basis |
| mixed sigma-45 `RESULT.md` | `923c21110de8227bfc6b92c12314dbfb68179b819e10412ea6ea58f972323582` | parent identity, opened only for the firewall |
| mixed sigma-45 `RESULT_SCOPE_ERRATUM.md` | `446720cf746c7c9b3176ad8c55b4f77715d24ea71cd16fa7f3fa03dccadcf641` | controlling quarantine of the `q>15/2` slice |

Every hash above matches the corresponding freeze or evidence row, or is
an auxiliary file opened only to check reconstruction or the scope
firewall. Characteristic-65521 stdout hashes appear in `RESULTS.sha256`
and were not opened as algebra.

---

## 1. Compiler reconstruction and the seven grade-42 rows

The loaded compiler pins the parent renderer
`compile_sigma45.py` at
`c19badfcfad44842f42118d031a5bfe92729d714e2a329b2af7097be629ea3d9`
and the frozen tails at
`d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848`.
Both exact-`Q` `.sing` files contain the seven tail polynomials `T1`..`T7`
obtained by rendering those tails on the ordinary-Faber monomials

```text
(qr^2+n0, 2*qc*qr+n1, qc^2+2*qp*qr+n2, 2*qp*qc+n3,
 qp^2+2*qr, 2*qc, 2*qp, k10, k6, k2).
```

Independent reconstruction of all seven strings matches both compiled
sources. The source substitutions are the complete delayed-load graph

```text
LK10 = s^42*(kk+s*k101+s^2*k102+s^3*k103),
LK6  = s^42*((15/32)*kk*p^2+s*k61+s^2*k62+s^3*k63),
LK2  = s^42*((15/256)*kk*p^4+s*k21+s^2*k22+s^3*k23),
MU2  = s^42*(mu20+s*mu21+s^2*mu22+s^3*mu23),
```

with kernel orders 6--9, complementary orders 12--15, `(e,m)` jets through
relative order three, and the `mu2` target subtracted only from row two.
Those are exactly the corrections that can meet grades 42--45 on this
integer support. Grade 43 of row two displays `k101`, `k61`, and `k21`
separately, so no delayed-load family was dropped; at grade 42 the three
leading loads are locked to the graph in `kk` and appear in `G2` together
with `-mu20`.

Both exact-`Q` runs print the same seven grade-42 rows, independently of
the chart generators:

```text
G1 = -3/8*r112*m^2+3/4*s012*m
G2 = -5/4096*kk*p^6-3/8*r012*m^2+3/8*y6^2-mu20
G3 = -3/32*r112*m^2*p-3/8*y6*x6*m+3/16*s012*m*p
G4 =  3/32*x6^2*m^2-3/16*r012*m^2*p-3/16*y6^2*p
G5 = -3/256*r112*m^2*p^2+3/32*y6*x6*m*p+3/128*s012*m*p^2
G6 = -3/64*r012*m^2*p^2+3/64*y6^2*p^2
G7 =  3/1024*r112*m^2*p^3-3/256*y6*x6*m*p^2-3/512*s012*m*p^3
```

These are the hand-certificate rows after the dictionary
`x=x6`, `y=y6`, `r1=r112`, `r0=r012`, `s0=s012`. No `a5`, `e1`, `m1`,
`s112`, or kernel jet of order `>=7` appears. Loads and the target occur
only in `G2`, which the hand obstruction does not use, so they were
retained rather than discarded. The exact-`Q` stdout does not reprint
coefficients of grades `0..41`; the hand identities among the printed
`G42` rows do not need those coefficients. Calling grade 42 the first
face of this integer support is consistent with the weights (loads at 42,
kernel through `s^15` then squared at 42, complement at 12 with the same
shift 30) and is not a coefficientwise listing.

---

## 2. Identity (1), the `G6` substitutions, and both `G4` residuals

Write `x=x6`, `y=y6`, `r1=r112`, `r0=r012`, `s0=s012`. From the printed
rows,

```text
(p/4)*G1 = -3*r1*m^2*p/32 + 3*s0*m*p/16,
```

hence

```text
G3-(p/4)*G1 = -3/8*m*x*y.
```

This is identity (1), including the sign. On `D(m)` it forces `x*y=0`.

On `D(x)`, identity (1) gives `y=0`. Then

```text
G6 = -3*r0*m^2*p^2/64.
```

The registered chart inverts `p` and `m`, so `r0=0`, and

```text
G4 = 3*x^2*m^2/32,
```

a unit times `x^2`. Scalar `+3/32`, sign positive.

On `D(y)`, identity (1) gives `x=0`. Then

```text
G6 = (3*p^2/64)*(y^2-r0*m^2),
```

so `r0*m^2=y^2`. Substitute into `G4`:

```text
G4 = -3*r0*m^2*p/16 - 3*y^2*p/16
   = -3*p/16*(y^2+y^2)
   = -3*p*y^2/8,
```

a unit times `y^2`. Scalar `-3/8`, sign negative, matching the
certificate.

No algebraic defect.

---

## 3. Exhaustion of the leading exceptional divisor, and chart licenses

After (1) and `m` a unit, the leading kernel satisfies `x6*y6=0`. The
nonzero locus in the leading plane is then the union of the two axes minus
the origin. That is covered by `D(x6)` and `D(y6)`. The origin is
zero-kernel and is a later face.

The compiled ideals are exactly the registered charts:

```text
q6x:  y6=0,  satu*p*m*kk*x6-1
q6y:  x6=0,  satu*p*m*kk*y6-1
```

Every inversion used in the hand proof is licensed:

| Inversion | Used on | Licensed by |
|---|---|---|
| `m` | (1) and both `G4` residuals | both charts |
| `p` | `G6` on `D(x6)`; residual `G4=-3*p*y6^2/8` on `D(y6)` | both charts |
| `x6` | residual `3*x6^2*m^2/32` | `q6x` |
| `y6` | residual `-3*p*y6^2/8` | `q6y` |
| `kk` | not used in the hand contradiction | both charts, harmless |

The compiler also contains navigation-only integral `q=7` and zero-kernel
modes. They were not launched as theorem lanes and are not substitutes
for `6<q<15/2` or `q=15/2`.

This exhaustion is the leading `P^1` of the **integral** jet support. It
is not yet exhaustion of every rational arc of relative order six; that
is §5.

---

## 4. Scheme versus set, and the two exact-`Q` bases

The hand proof is set-theoretic on `D(p*m)`: units times `x6^2` or
`y6^2`. It does not consume a standard basis. The certificate states
this correctly.

Each exact-`Q` run prints, between `A_LK45_STD_BEGIN` and
`A_LK45_STD_END`, the single polynomial `1`. That is the localized
Groebner basis of

```text
(G_ell,grade for ell=1..7, grade=42..45) + (chart generators)
```

over `Q`, hence the unit ideal, including nilpotents. The two printed
bases therefore agree with the hand emptiness of the two charts, and are
strictly stronger (scheme-theoretic, and they use grades 43--45). They
are corroboration only. The tokens `A_LK45_UNIT=1` and
`A_LK45_ENDPOINT=PASS_*` were ignored.

The two solver charts do **not** themselves prove exhaustion: there is no
`D(x6*y6)` lane. Exhaustion of the leading `P^1` is the hand identity
(1). That is the correct division of labour on the integral face, and
the two methods agree there. Characteristic 65521 was not used.

---

## 5. Valuative scope

This is the defect.

The compiler expands in the integral parameter `s` with integer jets

```text
aa = s^5*a5,
EE = p + s*e1 + s^2*e2 + s^3*e3,
MM = m + s*m1 + s^2*m2 + s^3*m3,
XX = s^6*x6 + ... + s^9*x9,
YY = s^6*y6 + ... + s^9*y9,
RR*, SS* starting at s^12,
loads and mu2 starting at s^42.
```

On that support, every retained jet of order strictly larger than its
leading valuation contributes to a strictly later grade. In particular
`e1`, `m1`, `x7`, `y7`, and complementary order 13 do not enter `G42`,
so they cannot cancel the two `G4` units. A uniformly ramified pullback
`s=t^e` of an integral arc, with no extra intermediate jets, has the
same initial form at weight `42e`. For that subclass the two-chart
argument survives.

The claimed theorem is not that subclass. The hand certificate says the
**full** relative-order-six kernel face is empty. That is a statement
about every characteristic-zero DVR with first transverse kernel order
exactly six, in whatever source coordinates the arc arrives.

The compiled center is truncated at `a5`. The next integral jet `a6`
is not in the ring. It meets the first quadratic face:

```text
QC = 2*aa*(4*aa^2-EE) + XX + RR1
   = -2*p*a5*s^5 + (x6-2*p*a6)*s^6 + ...,
N2 = s^15*aa*MM  =>  [s^21] N2 contains a6*m,
N0 = s^15*(-aa*DD*MM + (MM*XX)/2 + ...)
   =>  [s^21] N0 contains m*x6/2 - a6*p*m.
```

Redefining `x6` clears the order-six slot in `QC` and the displayed
`N0` pairing, but it does not clear `[s^21]N2=a6*m`. The ordinary-Faber
tails contain `n2`, so `a6` is capable of tying grade 42. After
`s=t^e`, any intermediate center, source/Rees, complement, or tangent
jet whose weights sum to `42e` plays the same role. Complementary order
strictly less than 12, or tangent order strictly less than 1, is a
different (earlier) Newton face and is outside the stated `q=6` cut,
but it is exactly the class of extra jets that can retie weight 42 if
they are not absorbed.

No two-sided lemma is present that every delayed-load repeated-root `A`
arc of first kernel order six admits moving-discriminant / K2 / Rees
coordinates in which

```text
aa = s^5*a5,
v(EE-p) >= v(s),
v(MM-m) >= v(s),
v(XX), v(YY) >= 6 v(s)  with minimum exactly 6 v(s),
v(RR*), v(SS*) >= 12 v(s),
v(loads) >= 42 v(s),
```

and `(x6,y6)!=(0,0)` on `D(p*m*kk)`. The parent mixed sigma-45 result
already recorded that promotion off the registered normal form requires
such a valuative chart and an absorption map for `a(s),e(s),m(s)`, and
required that argument to be hostile-reviewed separately. The loaded
successor retains `(e,m)` through relative order three, which do not
enter `G42`, and still truncates `a(s)` at `a5`.

The smallest explicit counterface is therefore this omitted order-six
center jet, or after ramification the same jet in the uniformizer. It
is a missing initial-form support, not a computed surviving point and
not a false scalar in `G4`. Fractional exhaustiveness cannot be inferred
from the integral compiler.

---

## 6. Scope firewall

Registration, `RESULT.md`, and the hand certificate all keep `q=15/2`
and `6<q<15/2` as later gates. The parent identity
`[s^45]H3=-m^3/16` remains a strong normal-form slice; its controlling
erratum still quarantines the `q>15/2` sigma-45 claim, and the omitted
family named there is precisely the kernel face under review, not a
licence to reopen the late slice. This review claims none of `m=0`,
terminal or Taylor receivers, order two, maximum twelve, or JC2.

---

## Strongest exact theorem that survives

Work over a field of characteristic zero, on the delayed-load
repeated-root `A` source with the compiler's **integral** jet support:

```text
aa=s^5*a5,
EE=p+O(s),   MM=m+O(s),
XX=s^6*x6+O(s^7),   YY=s^6*y6+O(s^7),
RR*,SS*=O(s^12),
k10=s^42*kk+O(s^43),
k6=s^42*(15/32)*kk*p^2+O(s^43),
k2=s^42*(15/256)*kk*p^4+O(s^43),
mu2=s^42*mu20+O(s^43).
```

On `D(p*m*kk)`, the seven exact-`Q` grade-42 rows displayed in §1 hold.
They imply `G3-(p/4)G1=-(3/8)*m*x6*y6`, hence `x6*y6=0`. On the chart
`y6=0`, `D(x6)` one has `G6` forcing `r012=0` and then
`G4=3*x6^2*m^2/32`. On the chart `x6=0`, `D(y6)` one has `G6` forcing
`r012*m^2=y6^2` and then `G4=-3*p*y6^2/8`. Both charts are empty. The
two exact-`Q` localized bases equal `(1)`, which corroborates the same
emptiness scheme-theoretically on this integral support.

This is not a theorem for all rational arcs of relative order six, not a
theorem after arbitrary finite ramification with extra intermediate
jets, and not a substitute for the missing two-sided
moving-discriminant / K2 / Rees-coordinate lemma. It does not empty
`6<q<15/2`, `q=15/2`, the quarantined `q>15/2` slice, `m=0`,
terminal/Taylor receivers, order two, maximum twelve, or JC2.

Repair: prove the normalized-coordinate lemma, or retain `a6` (and the
ramified intermediate jets of the same weight) and replay the first
quadratic face. Filling that one support restores the stated
relative-order-six emptiness on `D(p*m*kk)`.

REPAIR
