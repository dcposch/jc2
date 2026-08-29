# Hostile review — affine-Faber `A` H16 equality-wall grade-48 direct unit

| Field | Value |
|---|---|
| Charged target | `xmodel/max12-812-order2-affine-faber-a-h16-q6-a4-grade48-direct-unit-theorem-20260826.md` |
| Target SHA-256 | `4748f3f1666ec0753035c4a79f5aa59376647283223ec9c432e8d7b2b4b31b10` |
| Overall verdict | **CONFIRMED** |
| Smallest failing identity | none |
| Smallest missing hypothesis | none inside the charged fixed integral family `(H,q,ord(a))=(16,6,4)` on `D(p*m)` |
| Reviewer / model | Grok 4.6 (xAI). Independent hostile reconstruction from frozen tails. Different model family from the producer. No producer status line, no charged `PASS`/`UNIT`/`ENDPOINT` token, no validator string, this prompt, and no fixed-slice emptiness is evidence |
| Method | SHA-256 of every charged pin and every freeze/evidence row before reading producer verdict prose; independent rebuild of the 10-slot coefficient-factor substitution; independent abstract collection of raw rows `1,3,5,7`; valuation cut at 48; moving-`E` sparse-series convolution of every survivor, including the grade-46 load terms; exact `G48-32F48`; modular reduction checked only as software control |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `418e413593120d19e15e6546eb50c985f4b1f038` |
| Date | 2026-08-26 |

Independently recomputed SHA-256 of the twelve files named in the review
prompt match those pins. Every freeze and evidence row of the V4 and V6
manifests matches the corresponding on-disk bytes. Producer verdict
language, `PASS-A-H16-Q6-A4-G48-SPARSE-DAG-V4`,
`PASS-A-H16-G48-SECONDARY-ODD-DAG-V6`, the V5 dual-AWS emptiness, the
two old witness values `-1/32`, and the four V6 Singular slice values
were not used as characteristic-zero evidence. Exact `Q` is the
mathematical lane. Characteristic 65521 is a software and support
control only. No file other than this review was written. The target,
producers, shared ledgers, and `jc2-lean` were not edited.

---

## Verdict

**CONFIRMED.**

On a characteristic-zero complete DVR with uniformizer `s`, in the
fixed integral delayed-load source family `H=16`, `q=6`, `ord_s(a)=4`
with the registered moving-discriminant graph, the two raw odd-row
combinations

```text
F = P7 - E(s)^2 P3/32 + E(s)^3 P1/64,
G = E(s)^2 P3 + 16 E(s) P5 + 96 P7
```

have independently recomputed grade-48 coefficients

```text
F48 = (3/32) a0 p^2 m^2 r00 - (3/32) a0 p^2 y0^2
      - (1/16) a0 p^4 d20 + (3/128) a0 p^6 d60 - (1/64) p^2 m^3,

G48 = 3 a0 p^2 m^2 r00 - 3 a0 p^2 y0^2
      - 2 a0 p^4 d20 + (3/4) a0 p^6 d60 - (5/2) p^2 m^3,
```

and therefore

```text
G48 - 32 F48 = -2 p^2 m^3.
```

If every raw ordinary-Faber coefficient through grade 48 vanishes, then
every non-negative-valuation series multiple of those rows vanishes
through grade 48, so the left side is zero. On `D(p*m)` the right side
is a unit. The argument uses the complete moving series `E(s)=p+s e1+\cdots`
and does not replace `E(s)` by `p`. It needs neither a grade-44
predecessor reduction nor a projective `D(x)/D(y)` split. The statement
is internal to this fixed integral source-graph family.

**CONFIRMED**

---

## Hashes and charged artifacts

Recomputed SHA-256, all matching the required pins:

| Artifact | SHA-256 | Role |
|---|---|---|
| charged theorem | `4748f3f1666ec0753035c4a79f5aa59376647283223ec9c432e8d7b2b4b31b10` | immutable target |
| V4 `RESULT.md` | `3b99f6f198b8e149fbebac443ce4c59faed4fd2289275c6b4680cc673ed790bb` | charged; navigation only |
| V4 `EVIDENCE.sha256` | `922e10cab6f8b4b9ad9db45898721c68e4f6829b6e1e69ee2a51918cc4d89667` | charged |
| V4 `FREEZE.sha256` | `1a9411e67f2ef2efed48efffaf2afb066f2a5e8ab97d3ca5fe458693cbefaef6` | charged |
| V4 `RESULTS.sha256` | `4c9a9bebac582749688909c0048b960d2212e9563490b16f06278cbe135680ff` | charged |
| V4 exact-`Q` `grade48_sparse_polynomial.json` | `d71d23a8d88add84dc5e579b1fdcc3570fdde71c6d77440b68c5495f178f1386` | exact-`Q` F48 custody |
| V6 `RESULT.md` | `02a005dd4bac2db1ef891a55d4377148ce4a485ea0d61d9dd4bc73da541863af` | charged; navigation only |
| V6 `EVIDENCE.sha256` | `7524ed35265f551ea03034b16279bd219d243f3225e3764748166208e758c5c8` | charged |
| V6 `FREEZE.sha256` | `3b8c42ba206668298c65e725bc640461665c2aeacdf19128dc8499939f69ef94` | charged |
| V6 `RESULTS.sha256` | `32ffca9f138e9e8a9fe8178a923265c3238cb3f49ff04e92cb0f216657a8bcea` | charged |
| V6 exact-`Q` `grade48_secondary_sparse.json` | `da16e1ce0a309f6fde5d280493f162f88b1ba4317f80219e2e1e407ca771a264` | exact-`Q` G48 custody |
| V5 `RESULT.md` | `331a0bcc0488a2ec64950858b1130d6326529691dafb3a0e09e0ac06fb8eae80` | charged control pin only; not a Q identity |
| frozen tails `tails.json` | `d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848` | complete source tails |
| V4 engine `compute_sparse_dag_v4.py` | `c539fad9a47299faa4a9afe1dbf3ee6ac868f3e8ef7cdbe7bd277c1ddd4d36d2` | freeze pin; algebra rederived |
| V6 `compute_secondary_odd_v6.py` | `dd605e0a52f3b505a94bd30b783ca2461637beaeecc4a7c8788ea9b73a6f2fe3` | freeze pin; algebra rederived |

Every relative path in both `EVIDENCE.sha256` and both `FREEZE.sha256`
rehashes to the recorded digest. The F65521 grade-48 supports are the
same five exponent vectors as exact `Q`, with coefficients the reduction
of the displayed rationals; that agreement is a software control, not a
characteristic-zero proof.

---

## Attack 1 — coefficient-factor order, complete graph, no `E H3+H5`

The frozen tails are polynomials in a 10-slot exponent vector of width
exactly 10, with counts

```text
row 1: 36,  row 2: 54,  row 3: 58,  row 4: 81,
row 5: 89,  row 6: 120, row 7: 131.
```

Canonical JSON SHA-256 is
`6eed03d486e1cd9e8d990eed74a105293d383882bbae77d204eac190cce387e8`.
There is no `mu2`, `mu4`, `mu6`, or `J` slot. The compiler that emitted
these tails writes them in the ring `(a0,...,a6,k10,k6,k2)` and attaches
targets only afterwards:

```text
P1: 0,  P2: mu2,  P3: 0,  P4: mu4,
P5: 0,  P6: mu6,  P7: (j/4)(1+tau).
```

On the affine chart `tau=0` this is the `-J/4` convention. First frozen
terms match the 10-slot factor order

```text
B0 = qr^2 + n0,
B1 = 2 qc qr + n1,
B2 = qc^2 + 2 qp qr + n2,
B3 = 2 qp qc + n3,
B4 = qp^2 + 2 qr,
B5 = 2 qc,
B6 = 2 qp,
then K10, K6, K2:
```

namely

```text
row1: [0,0,0,0,0,1,0,0,0,1] * (1/4) = (1/4) B5 K2 = (1/2) qc K2,
row3: [0,0,0,0,0,1,1,0,0,1] * (-5/32) = (-5/32) B5 B6 K2,
row7: [0,0,0,0,0,1,3,0,0,1] * (-51/4096) = (-51/4096) B5 B6^3 K2.
```

The moving-discriminant graph used to expand those factors is

```text
qp = E - 6 a^2,
qc = 2 a (4 a^2 - E) + X + R1,
qr = a^2 (E - 3 a^2) + R0 - a (X + R1),
n3 = lambda M,
n2 = lambda a M,
n1 = lambda ((E - 5 a^2) M + Y + S1),
n0 = lambda (-a (E - 3 a^2) M - a Y + (1/2) M X + S0 - a S1),
```

with source series

```text
a     = s^4 (a0 + ... + s^6 a6),
E     = p + s e1 + ... + s^6 e6,     (moving; not frozen to p)
M     = m + s m1 + ... + s^4 m4,
X     = s^6 (x0 + ... + s^4 x4),
Y     = s^6 (y0 + ... + s^4 y4),
Ri,Si = s^12 (leading + relative 1..4),
lambda = s^16,
K10   = s^42 KK,
K6    = s^42 ((15/32) KK E^2 + D6),   D6 starts at relative 2
K2    = s^42 ((15/256) KK E^4 + D2),  D2 starts at relative 2
J     = s^57 jt.
```

Independent abstract collection of the raw tails, in this substitution,
gives supports `P1:106`, `P3:194`, `P5:379`, `P7:670`. The combinations
`F` and `G` have abstract supports 663 and 665. Neither sparse client
mentions `H3`, `H5`, or `mu2`/`mu4`; both evaluate raw rows `1,3,7` and
`3,5,7` respectively, then add the affine targets `-J/4` and `-24 J`.
They never substitute a target-bearing `E H3+H5` formula for the charged
raw rows.

`J` has valuation 57, so it is absent from every valuation-`<=48`
survivor. The V4/V6 engines zero the `J` series through grade 48; that
is equivalent, at this grade, to retaining `J=s^57 jt`.

---

## Attack 2 — independent `F48`, `G48`, moving-`E` convolution, `G-32F`

Valuation of an abstract monomial in
`(J,K2,K6,K10,S0,S1,R0,R1,Y,X,a,lambda,M,E)` against
`(57,42,42,42,12,12,12,12,6,6,4,16,0,0)` leaves exactly nine survivors
in each of `F` and `G`:

```text
F, val 46:  (-15/2048) K10 a E^8
             (  3/128) K6  a E^6
             ( -1/16 ) K2  a E^4
F, val 48:  ( -1/64 ) lambda^3 M^3 E^2
             ( -3/32 ) Y^2 a lambda^2 E^2
             (  3/32 ) R0 a lambda^2 M^2 E^2
             ( 15/4096) K10 X E^7
             ( -3/256) K6  X E^5
             (  1/32 ) K2  X E^3
```

and the same nine monomials in `G` with coefficients
`-15/64`, `3/4`, `-2`, `-5/2`, `-3`, `3`, `15/128`, `-3/8`, `1`.
No survivor contains `J`, `S0`, `S1`, or `R1`.

The three val-46 load monomials sit on the affine-Faber locus. Substituting
the locked leadings `K6=(15/32)K10 E^2` and `K2=(15/256)K10 E^4` gives

```text
K10 a E^8 [ -15/2048 + (3/128)(15/32) - (1/16)(15/256) ]
  = K10 a E^8 [ -15/2048 + 45/4096 - 15/4096 ]
  = K10 a E^8 [ -15/2048 + 15/2048 ] = 0.
```

The three val-48 `X`-load monomials cancel on the same locus:

```text
K10 X E^7 [ 15/4096 - (3/256)(15/32) + (1/32)(15/256) ]
  = K10 X E^7 [ 30/8192 - 45/8192 + 15/8192 ] = 0.
```

Thus only graph deviations `D2,D6` and the three non-load val-48 monomials
can survive. Moving-`E` convolution of the val-46 terms does produce
`e1,e2,kk,a1,a2` monomials at grade 48; they cancel in the same linear
combination, leaving only the deviations. Explicitly, the three val-46
`F` contributions sum to

```text
-(1/16) a0 p^4 d20 + (3/128) a0 p^6 d60
```

with every `e1^2 kk0`, `e1 kk1`, `e2 kk0`, `kk2`, `a1`, `a2` coefficient
zero. The three val-48 `X` contributions sum to `0`. The remaining three
val-48 monomials substitute on the nose, because `lambda=s^16` has no
higher terms and `Y,R0,a,M,E` are already at total valuation 48 on their
leadings:

```text
[s^48] lambda^3 M^3 E^2 = p^2 m^3,
[s^48] Y^2 a lambda^2 E^2 = a0 p^2 y0^2,
[s^48] R0 a lambda^2 M^2 E^2 = a0 p^2 m^2 r00.
```

Hence the five-term exact-`Q` polynomials displayed in the theorem,
written in leading jets. Then

```text
32 F48 = 3 a0 p^2 m^2 r00 - 3 a0 p^2 y0^2
         - 2 a0 p^4 d20 + (3/4) a0 p^6 d60 - (1/2) p^2 m^3,
G48 - 32 F48 = (-5/2 - (-1/2)) p^2 m^3 = -2 p^2 m^3.
```

Every one of the five coefficients was obtained from complete source.
Replacing `E(s)` by `p` would have dropped the val-46 moving-`E` feed
into grade 48; those terms cancel, so the displayed polynomials happen
to contain only `p`, but the computation that licenses them used the
moving series.

Reduction modulo `65521` of the five exact-`Q` coefficients is

```text
F:  3/32 -> 26618,  -3/32 -> 38903,  -1/16 -> 4095,
    3/128 -> 39415,  -1/64 -> 17404,
G:  3 -> 3,  -3 -> 65518,  -2 -> 65519,
    3/4 -> 16381,  -5/2 -> 32758.
```

These are the F65521 sparse polynomials byte-for-byte in exponent
vectors. They are not used to prove the `Q` identity.

---

## Attack 3 — targets, `-J/4`, loads, omitted modes

`P1,P3,P5` have compiler target `0`. They have no affine target. The
frozen 10-slot tails of those rows contain only `B0..B6,K10,K6,K2`.

`P7` carries `-(j/4)(1+tau)` in the Rees homogenization and `-J/4` on
the affine chart. That term is added to `F` as `-J/4` and to `G` as
`96*(-J/4)=-24 J`. The registered source is `J=s^57 jt`, valuation 57,
so neither copy enters grade 48. The displayed identity is therefore
insensitive to the difference between the affine `-J/4` and the Rees
factor `(1+tau)`.

Even-row targets `mu2,mu4,mu6` live only in `P2,P4,P6`. Those rows are
not summands of `F` or `G`. They cannot cancel `-2 p^2 m^3`.

Lower loads `K10,K6,K2` do enter the abstract survivors. On the
affine-Faber graph their locked leadings cancel, Attack 2. The free
graph corrections are `D6,D2` starting at relative order 2 (absolute
grades 44 through 48). They produce the displayed `d20,d60` terms in
`F48` and `G48`, and those terms cancel in `G-32F`. A relative-0
correction to `K6` or `K2` is not a free coordinate of the registered
family: it is already absorbed into `(15/32) KK E^2` and
`(15/256) KK E^4`. Even if it were free, it would first appear at
grade `42+4=46`, not in the grade-48 identity.

Complement and transverse jets `R1,S0,S1` have valuation 12. The only
abstract monomials of total valuation `<=48` that could carry them do
not occur in `F` or `G`. `R0` appears, at leading jet `r00` only,
because `12+4+32=48` is exact. Higher relative jets of every displayed
variable overshoot grade 48.

No omitted mode in the registered graph evades `G48-32F48=-2 p^2 m^3`.

---

## Attack 4 — ideal membership, lower coefficients, characteristic, `D(p*m)`

Write `Pj=sum_{n>=0} p_{j,n} s^n` and `E(s)=sum_{k>=0} e_k s^k` with
`e_0=p`. Then

```text
[s^48](E(s)^k Pj) = sum_{i=0}^{48} [s^i](E^k) p_{j,48-i}.
```

Every summand uses a coefficient of `Pj` of degree at most 48. The
theorem hypothesizes that every raw-row coefficient through grade 48
vanishes, i.e. `p_{j,n}=0` for all `n<=48` and all seven rows. Under
that hypothesis every convolution vanishes, so `F48=G48=0`. This is
not a silent extra appeal to a grade-44 predecessor: it is literally
the stated hypothesis, applied to series-linear combinations with
coefficients of non-negative valuation. A separate predecessor
reduction is unnecessary, and is not used.

Conversely, vanishing of only the grade-48 raw coefficients, with
lower coefficients free, would not force `F48=0`, because moving `E`
feeds lower `Pj` into grade 48. The theorem does not claim that weaker
statement.

Characteristic zero is required: the Faber tails and the combinations
`F,G` have denominators `32,64,128`, and the unit is `-2 p^2 m^3`. A
complete DVR of residue characteristic zero inverts `2`. Localization
`D(p*m)` is exactly the open on which `-2 p^2 m^3` is a unit. On
`p=0` or `m=0` the identity is `0=0` and supplies no obstruction;
those factor-degenerate opens are firewalled.

Even rows `P2,P4,P6` are not needed for the contradiction. Simultaneous
vanishing of all seven rows through grade 48 implies vanishing of the
odd rows, hence of `F48` and `G48`.

---

## Attack 5 — scope and coordinate access

The source substitutions lock `lambda=s^16`, `min(ord X, ord Y)=6`, and
`ord a=4`. The identity is a computation in that fixed integral family,
on the internal moving-discriminant graph, after localizing at `p m`.
It does not vary `(H,q,ord(a))`, does not regrade, and does not pass to
a neighboring equality wall. It does not prove rational-regrading
invariance, literal total-Rees coverage, factor-degenerate opens,
order two, maximum twelve, or JC2.

The obstruction `-2 p^2 m^3` is already a unit on `D(p*m)`. A
projective `D(x)/D(y)` split is not required and is not used. The
V5 fixed slices, which kill `F48` by moving `d20,d60` and then see
`C3+16 C5+96 C7=-2` at `p=m=1`, are specializations of the same
identity. They are controls. They are not a proof of the unspecialized
polynomial, and they are not used as one.

---

## Attack 6 — strongest licensed theorem

The strongest theorem licensed by the frozen tails and the independent
exact-`Q` reconstruction is exactly the charged statement:

on a characteristic-zero complete DVR, in the fixed integral family
`(H,q,ord_s(a))=(16,6,4)` with the registered moving-discriminant graph
and target convention `-J/4` on `P7`, simultaneous vanishing of the
seven raw ordinary-Faber coefficients through absolute grade 48 is
impossible on `D(p*m)`, because it would force
`[s^48](G-32 F)=-2 p^2 m^3=0`.

There is no wrong coefficient among the five displayed terms of `F48`
or of `G48`. There is no omitted registered mode that survives
`G-32F`. There is no missing hypothesis inside that family. The
identity is a source-coefficient computation, not a scope-only claim
waiting on a predecessor or a chart split.

Do not upgrade the statement. Do not treat the F65521 reduction, the
V5 emptiness, or the old witness value `-1/32` as characteristic-zero
evidence.

**CONFIRMED**
