**Child integrality on the twenty retained prefixes — 2026-09-06**

**VERDICT: 20 SURVIVES; 0 DEAD; 0 undetermined major-sum verdicts.** There are
35 necessary patterns with complete final-major coverage. Their child sums are
integral and equal to `u_s` times the corresponding integral parent sums.
Four rows have several possible major sums: R023, R024, R035, R049. Neither a
polynomial realization nor an actual descent is asserted by SURVIVES.

**Every child assertion below is CONDITIONAL on
`OPEN[PROP6.3-RADIUS-US>1]`: the parent principal minor radius
`delta*_(s-1) >= v_s/u_s`.** Moh Proposition 6.3, printed p.197, requires that
hypothesis. Proposition 6.4, pp.198–199, supplies it automatically only at
`u_s=1`. Thus a hypothetical DEAD verdict in this lane would have to name this
same condition; it would exclude the licensed D2 branch, not the surviving ES
branches. Here there is no such kill, conditional or unconditional.

**Custody and scope.** The receipt
`xmodel/child-integrality-prefixes-astra-20260906.run.v2` was parsed with `awk`,
pairing `charged_input_<i>_sha256` and `_basename` by index. `sha256sum -c`
on the resulting manifest verified **9/9 frozen inputs** before mathematical
reads. The frozen input directory is `/tmp/jc2-lane.ZUsUCw/inputs`.
The read-only mount required placing the manifest in the driver directory.

The actual frozen `descend_own.py` was executed with `radius_licensed=False`.
Its required mechanical dependency, the uncharged `box/lib/own_v_routes.py`,
was read and hash-pinned to
`f07dd9b0e38118132ed2ec2e5e7e972f98ba8f223213062fed356a30188b3bf3`.
This dependency supplies first-support compatibility; complete packet
enumeration is implemented here from the printed formulas. No capped closure,
uncharged mathematical report, ledger edit, `jc2-lean`, `ideation-*` input,
fleet computation, or artifact tree was used. Drivers and JSON are in
`box/child-integrality-prefixes-20260906/`.

Source keys below refer to frozen copies: **M** is Moh's PDF, **X** Xu's PDF
(printed pages); **D** is `descent-partition-theorem-astra-20260906.md`;
**G** is `r063-ell-gate-sol56-20260906.md`; **O** is `descend_own.py`.
The R063 identification dispute is outside these twenty rows; only the
source-checked map/shift arguments are consumed.

**What the prefix determines.** All twenty calls return one own vector and
one first-support route, starting at source index 2. They retain
`characteristic_scope="retained prefix only"`,
`top_license="OPEN_CHILD_TERMINAL_IDENTIFICATION"`, and terminal prefix gcd
`d'_(s'+1)=u_s>1` (O:249–268). No child terminal label or `V'_(s'+1)` is supplied.
The table records `M'` after its compulsory first entry `-m'`; compute every
`d'` by successive gcds of `n'` and this displayed prefix. Radii are the local
inverse metric, not Definition 5.1 applied to an invented complete child.

| Row | `(n',m')` | remaining `M'` | own `V'` | metric `delta'` | `u,ell` |
|---|---|---|---|---|---|
| R012 | 24,16 | 18 | 7 | 0,-1 | 2,4 |
| R015 | 27,18 | 21 | 8 | 0,-1 | 3,4 |
| R016 | 48,32 | 38 | 3 | 4/3,-1/3 | 2,2 |
| R023 | 30,20 | 22 | 2 | 11/3,-1 | 2,6 |
| R024 | 30,20 | 22 | 3 | 2,-1 | 2,6 |
| R029 | 63,42 | 54 | 5 | 3/4,-1/4 | 3,1 |
| R035 | 32,24 | 26 | 3 | 3/2,-1 | 2,4 |
| R038 | 36,24 | 28 | 8 | 1/3,-1 | 4,6 |
| R043 | 36,24 | 27 | 7 | 1/2,-1 | 3,7 |
| R044 | 42,12 | 38 | 4 | 3/7,-1 | 2,2 |
| R045 | 42,18 | 38 | 5 | 1/7,-1 | 2,2 |
| R049 | 42,28 | 36 | 5 | 5/3,-1 | 2,4 |
| R051 | 40,32 | 34 | 5 | 1/2,-1 | 2,4 |
| R052 | 45,27 | 39 | 7 | 1/5,-1 | 3,4 |
| R053 | 60,45 | 51 | 7 | 1/2,-1/2 | 3,3 |
| R054 | 50,20 | 46 | 8 | 1/5,-1 | 2,2 |
| R055 | 45,30 | 35 | 8 | 2/3,-1 | 5,8 |
| R062 | 48,36 | 40 | 11 | 0,-1 | 4,6 |
| R065 | 45,30 | 42 | 11 | 1,-3 | 3,5 |
| R066 | 36,24 | 28,34 | 8,3 | 5/3,1,-5 | 2,4 |

**The complete-major certificate.** Work over characteristic-zero `k`, in
Xu's orientation: parent `f=T_1^psi`, `g`, degrees `m<n`; child `(F,G)` in
`k[gamma,pi]`, degrees `(m',n')`. A prime denotes generation. With harmless
normalizing constants `b0 != 0,e0` and the prescribed truncation `c(gamma)`,
the ordered map is

```text
k[x,y] -> k[gamma,gamma^(-1),pi]
y -> gamma^(-u),
x -> (gamma^(-u)-e0-c(gamma)-gamma^v*pi)/b0.
```

Under the radius hypothesis M Prop.6.3(1),(2) makes `F,G` polynomial and monic
in `pi`; (3), p.197, gives `J(F,G)=C gamma^ell`, `ell=v-u-1`. The contradictory
reciprocal printed in the p.198 calculation is not used (D:36–59).
Use generic target translations, so all minor orders are zero. Exceptional
fixed fibres require the boundary/positive-order correction in D:205–212.

For nineteen rows `s=3`. Set `e=delta_2=a/b`,
`P=V_3 d_2/d_3`, `Q=V_3(n-M_2)/d_3`, `h=P/Q=d_2/(n-M_2)`.
Enumerate exactly

```text
p_2 = pi^z product_j (pi^b-c_j)^r_j,
z+b sum r_j=P,   [z>0]+b #j <= Q,   V_2 in {r_j}.
```

The `c_j` are distinct, nonzero and unspecified. M Prop.4.6(1)–(5),
pp.170–171, gives these degree/containment
conditions, with `q` squarefree. Its differential equation (M Prop.A.3 p.205),
`P p (dq/dpi)-Q q (dp/dpi)=c p`, `c!=0`, excludes **each** `r=P/Q`:
at a root the leading coefficient is proportional to `P-Qr`. Checking only
the whole pattern's non-power condition is insufficient. None of the 35
retained patterns has this equality.

An entirely zero-centred major is excluded by reducedness (M Prop.5.6,
pp.188–190). Thus `z<h`. Every nonzero `r>h` follows the printed fixed list
from `D_2` directly to final `D_1` (M Prop.5.3 pp.180–182 and Prop.4.6 at
index 1). Its counts are `rho_f=mr/d_2`, `rho_g=nr/d_2`; its final radius
is Definition 5.1 with that sibling's `V_2=r`. There is no unexamined major
level and no free `M` or `W` insertion. Its actual centre stabilizer is `L=b`.
For `A=den(L delta_fin)`, the final constant nonzero Wronskian requires

```text
(rho_f-1) = rho_g = 0 mod A,  OR  rho_f = (rho_g-1) = 0 mod A.
```

These are M's printed bottom conditions (12)/(13), pp.201–202. Zero
coefficients add no denominator; `(0,0)` alone is not allowed for `A>1`.
The frozen roster has no parent packet-completeness field: this certificate
is recomputed, not inferred from its `NONEMPTY` tag.

R066 is the one `s=4` row. At `D_3`, `(P,Q,b)=(14,7,6)` and selected
multiplicity 8 force `p_3=pi^8(pi^6-c)`. The nonzero factor is minor (`1<2`).
The zero major legitimately continues to `D_2`, where `(24,16,3)` and selected
8 force `p_2=(pi^3-d)^8`. This exhausts its major siblings. Its three parent
finals have `(rho_f,rho_g)=(16,24)`, `e=1/3`, `delta=4/9`, and orders
`(-2/9,-1/3)`. The actual final modulus is 3, with residues `(1,0)`.

For a parent final-major orbit of `N` discs and first nonzero exponent
`0<e<delta`, D:79–116 proves the transverse inverse rule

```text
N'=e N;  rho'_f=rho_f;  rho'_g=rho_g;
delta'=H+(u/e)(delta-1);  lambda'_(f,g)=(u/e)lambda_(f,g),
H=1+ell=v-u.
```

There is **no extra u in the disc count**. D:167–191 proves every child pole
is covered: finite parent `x` supplies no pole, and minors retain zero order.
This transports the **complete major list** while the characteristic prefix
remains incomplete. M p.171 and X Lemma4.1/Thm5.1, pp.4/7
(G:233–251), now applies without any terminal-child assumption:

```text
I'_M = n'/(n'+m') sum N' rho_f (H-delta')
     = sum -N' rho_f lambda'_g
     = u sum -N rho_f lambda_g = u I_M.
```

**All allowed top patterns and child major packets.** In the next table `O`
is the nonzero parent orbit multiplicity multiset; powers denote repetition,
not multiplication. Semicolons separate correlated alternatives. For s=3,
every multiplicity above `h` uses one packet group from the following table;
multiplicity 1 is minor, and R049's multiplicity 2 is also minor. R066 lists
its top and lower patterns separately. These are finite necessary
alternatives, not existence assertions about coefficients or polynomial pairs.

| Row | `z; O` alternatives |
|---|---|
| R012 | (0; 7) |
| R015 | (0; 8) |
| R016 | (0; 1^2 3) |
| R023 | (0; 1^5 2^2); (0; 1^4 2 3); (0; 1^3 2^3); (0; 1^2 2^2 3); (0; 1 2^4); (0; 1 2 3^2); (0; 2^3 3) |
| R024 | (0; 1^6 3); (0; 1^4 2 3); (0; 1^3 3^2); (0; 1^2 2^2 3); (0; 1 2 3^2); (0; 2^3 3); (0; 3^3) |
| R029 | (0; 5) |
| R035 | (0; 1^4 3); (0; 1 3^2) |
| R038 | (0; 1^3 8) |
| R043 | (0; 1^4 7) |
| R044 | (0; 1 4) |
| R045 | (0; 5) |
| R049 | (1; 1^2 5^2); (1; 1 2^3 5); (1; 2 5^2) |
| R051 | (0; 1^2 5) |
| R052 | (0; 1 7) |
| R053 | (0; 7) |
| R054 | (1; 8) |
| R055 | (0; 1^6 8) |
| R062 | (0; 11) |
| R065 | (1; 11) |
| R066 | D3: 8; 1. D2: 0; 8 |

Each entry below gives **one** group for each occurrence of `r` in `O`.
`N' × rho_f` is discs times actual `F-xi` roots per disc; `rho_g` is the
corresponding degree of the leading `G` polynomial. The two lambda columns
are polynomial orders on the disc, not the value of `F-xi` on one of its roots.
The final column already sums that group. It determines every major count,
order and contribution in all 35 patterns.

| Row | `r` | `N' × rho_f; rho_g` | `delta'` | `(lambda'_f,lambda'_g)` | group sum |
|---|---:|---|---:|---|---:|
| R012 | 7 | 1 × 14; 21 | 0 | -2,-3 | 42 |
| R015 | 8 | 1 × 16; 24 | 0 | -2,-3 | 48 |
| R016 | 3 | 3 × 6; 9 | 4/3 | -2/3,-1 | 18 |
| R023 | 2 | 1 × 4; 6 | 11/3 | -4/3,-2 | 8 |
| R023 | 3 | 1 × 6; 9 | 2 | -2,-3 | 18 |
| R024 | 2 | 1 × 4; 6 | 11/3 | -4/3,-2 | 8 |
| R024 | 3 | 1 × 6; 9 | 2 | -2,-3 | 18 |
| R029 | 5 | 4 × 10; 15 | 3/4 | -1/2,-3/4 | 30 |
| R035 | 3 | 1 × 9; 12 | 3/2 | -3/2,-2 | 18 |
| R038 | 8 | 1 × 16; 24 | 1/3 | -8/3,-4 | 64 |
| R043 | 7 | 1 × 14; 21 | 1/2 | -3,-9/2 | 63 |
| R044 | 4 | 1 × 8; 28 | 3/7 | -4/7,-2 | 16 |
| R045 | 5 | 1 × 15; 35 | 1/7 | -6/7,-2 | 30 |
| R049 | 5 | 1 × 10; 15 | 5/3 | -4/3,-2 | 20 |
| R051 | 5 | 1 × 20; 25 | 1/2 | -2,-5/2 | 50 |
| R052 | 7 | 1 × 21; 35 | 1/5 | -9/5,-3 | 63 |
| R053 | 7 | 2 × 21; 28 | 1/2 | -3/2,-2 | 84 |
| R054 | 8 | 1 × 16; 40 | 1/5 | -4/5,-2 | 32 |
| R055 | 8 | 1 × 16; 24 | 2/3 | -10/3,-5 | 80 |
| R062 | 11 | 1 × 33; 44 | 0 | -3,-4 | 132 |
| R065 | 11 | 1 × 22; 33 | 1 | -2,-3 | 66 |
| R066 | 8 | 1 × 16; 24 | 5/3 | -4/3,-2 | 32 |

**Minor information, including what remains undetermined.** All following
orders are `(0,0)`; `N×rho@delta` denotes final discs, unless explicitly called
an unresolved group. They contribute zero to the major sum.

A simple reduced minor factor cannot split while its orders remain negative:
M Prop.6.1(2), p.191, preserves its distribution detector; Definition 3.1 and
Remark, p.161, give common polynomial degree
`gcd(n/d_r,-mu_1/d_r,...,-mu_(r-1)/d_r)=1`. Its final source radius is
`d_m=e+[d_r/(n-M_r)](1-e)`. At zero order a generic fibre polynomial is
squarefree. Thus simple nonzero minor counts/radii, as well as major counts,
are determined. This local observation does not license the global descent.

In the table `j` is the number of multiplicity-1 entries in that pattern's
`O`. `F` means one finite-parent-line packet, at radius `v`, with the displayed
root count. For `z=0` it is forced by degree exhaustion and D:155–165, with
leading polynomial `f(-w/b0,0)-xi` in the centred coordinate `w`.
R066's `j` refers to its D3 pattern.

| Row | nonzero simple minors | other minor data |
|---|---|---|
| R012 | none | F: 1 × 2 @ 7 |
| R015 | none | F: 1 × 2 @ 8 |
| R016 | 3j × 2 @ 5 | F: 1 × 2 @ 5 |
| R023 | j × 2 @ 9 | F: 1 × 2 @ 9 |
| R024 | j × 2 @ 9 | F: 1 × 2 @ 9 |
| R029 | none | F: 1 × 2 @ 5 |
| R035 | j × 3 @ 7 | F: 1 × 3 @ 7 |
| R038 | j × 2 @ 11 | F: 1 × 2 @ 11 |
| R043 | j × 2 @ 11 | F: 1 × 2 @ 11 |
| R044 | j × 2 @ 5 | F: 1 × 2 @ 5 |
| R045 | none | F: 1 × 3 @ 5 |
| R049 | j × 2 @ 13 | Z alternatives below; each r=2 gives 4 unresolved roots |
| R051 | j × 4 @ 7 | F: 1 × 4 @ 7 |
| R052 | j × 3 @ 8 | F: 1 × 3 @ 8 |
| R053 | none | F: 1 × 3 @ 7 |
| R054 | none | Z alternatives below |
| R055 | j × 2 @ 14 | F: 1 × 2 @ 14 |
| R062 | none | F: 1 × 3 @ 11 |
| R065 | none | Z alternatives below |
| R066 | j × 6 @ 15 | F: 1 × 2 @ 7 |

For the zero simple minor in R049/R054/R065, its common centre is unknown.
The known source final radius `d_m` is respectively `2,2,4`. A first nonzero
common coefficient before it must have integer exponent `k` (a fractional
common coefficient would force a Galois split, contradicting degree one).
If every earlier coefficient vanishes, endpoint Newton inversion applies.
D:145–165 requires this distinction; a principal minor is not a finite-line
packet. The full necessary numerical alternatives for this remainder are:

| Row | first support | transported zero minor | finite-line packet |
|---|---|---|---|
| R049 | endpoint 2 | 1×4@6 | none |
| R049 | 1 | 1×2@7 | 1×2@7 |
| R054 | endpoint 2 | 1×4@4 | none |
| R054 | 1 | 1×2@5 | 1×2@5 |
| R065 | endpoint 4 | 1×8@33/4 | none |
| R065 | 1 | 1×2@15 | 1×6@9 |
| R065 | 2 | 2×2@21/2 | 1×4@9 |
| R065 | 3 | 3×2@9 | 1×2@9 |

Equal-radius entries in separate columns have centres separating earlier.
The missing datum is the first nonzero common-centre coefficient. R049's patterns
containing `r=2` leave each four-root minor group's final subdivision and radii
undetermined; the missing input is its first split support and leading
distribution-detector polynomial. No finite depth cap fills that datum.
The R049 pattern `(1;1^2 5^2)` contains no such heavy minor group.

For other rows, choosing the top alternative fixes the numerical minor
partition; coefficients and terminal characteristic support remain unspecified.
The principal parent minor maps above finite `gamma=0` (D:138–143).

**Row verdicts and the u factor.** `P/C` counts reduced top candidates and
those passing the printed final-major gate. All retained rows have status
`COMPLETE_MAJOR_LIST_BY_PRINTED_FIXED_LIST`; this does not assert a fully
specified parent minor partition. The braces are exact finite necessary
sum sets, with correlations stored per pattern in the JSON. Possible future
minor/coefficient constraints may shrink them. SURVIVES means an integral
alternative for this integrality test, under the radius condition above.

| Row | `u` | P/C | parent `I_M` | child `I'_M=u I_M` | verdict |
|---|---:|---:|---|---|---|
| R012 | 2 | 1/1 | {21} | {42} | SURVIVES |
| R015 | 3 | 1/1 | {16} | {48} | SURVIVES |
| R016 | 2 | 2/1 | {9} | {18} | SURVIVES |
| R023 | 2 | 14/7 | {8,12,13,16,17,21,22} | {16,24,26,32,34,42,44} | SURVIVES |
| R024 | 2 | 11/7 | {9,13,17,18,21,22,27} | {18,26,34,36,42,44,54} | SURVIVES |
| R029 | 3 | 1/1 | {10} | {30} | SURVIVES |
| R035 | 2 | 5/2 | {9,18} | {18,36} | SURVIVES |
| R038 | 4 | 3/1 | {16} | {64} | SURVIVES |
| R043 | 3 | 5/1 | {21} | {63} | SURVIVES |
| R044 | 2 | 1/1 | {8} | {16} | SURVIVES |
| R045 | 2 | 1/1 | {15} | {30} | SURVIVES |
| R049 | 2 | 11/3 | {10,20} | {20,40} | SURVIVES |
| R051 | 2 | 2/1 | {25} | {50} | SURVIVES |
| R052 | 3 | 1/1 | {21} | {63} | SURVIVES |
| R053 | 3 | 1/1 | {28} | {84} | SURVIVES |
| R054 | 2 | 1/1 | {16} | {32} | SURVIVES |
| R055 | 5 | 11/1 | {16} | {80} | SURVIVES |
| R062 | 4 | 1/1 | {33} | {132} | SURVIVES |
| R065 | 3 | 1/1 | {22} | {66} | SURVIVES |
| R066 | 2 | 1/1 | {16} | {32} | SURVIVES |

Thus `I'_M/u` is integral on **every** retained alternative. Factor frequencies
are `u=2:11`, `3:6`, `4:2`, `5:1`. No row forces a nonintegral parent sum.

There are fractional preliminary parent alternatives on exactly nine rows:
R016, R023, R024, R035, R038, R043, R049, R051, R055. **Every one fails
the parent's printed final-major Galois gate.** For example R016's `35/3`
is rejected while `9` remains. R055 even has an integral preliminary value
`20` rejected by that gate; only `16` remains. Full rational sets and rejection
reasons are recorded in `audit.json`. These are failed pattern completions,
not complete parent rows that may be killed from a representative sum.
Across the twenty rows there are 75 reduced top candidates, 40 such gate
rejections, and 35 retained patterns. Another 119 enumerated shapes are
excluded earlier by the entirely zero-major reduced-source rule.

**Verification and FALLACY-v2.** Run
`PYTHONDONTWRITEBYTECODE=1 python3 box/child-integrality-prefixes-20260906/audit.py`,
then `build_report.py` in the same directory. Arithmetic uses `Fraction`;
the driver checks all own vectors, M prefixes and local radii against the
frozen roster, asserts degree conservation through `inverse_top`, and checks
every major group both by transported order and by the ell-shifted formula.
An independent enumeration reproduced all 35 patterns and all twenty sum
sets. R012 negative controls put an erroneous u in the disc count (84 instead
of 42), or omit the ell shift (42/5 instead of 42). Both are detected.

One frozen-input discrepancy is kept explicit: the older structure report
says 38 ES leaves, but summing both `leaf_count` and the actual leaf arrays
of these twenty frozen roster lines gives **36**. Every row still has at least
one ES leaf and `forced=false`; the radius remains unlicensed. No old count
was substituted for the frozen roster and no residual/ledger was changed.

FALLACY-v2 distinctions remain explicit: configuration/pair, prefix/partition,
finite alternatives/attainment, zero coefficient/stabilizer denominator.
The sum is complete because the printed list exhausts parent majors and
transport excludes other child poles. Minor order zero uses generic targets.
All child conclusions retain the radius condition. No new exit-price assertion
is made, so no `charge_basis` line applies.

<!-- BODY-END -->

**Seal.** Body = all bytes through the unique standalone BODY-END marker,
including its terminating newline. Body bytes: `17475`.
Body SHA-256: `0e0fe1a8a31ac6166db47ac4c99e8373c567545bbb68e0f99ae23aa88e3ecbcf`.
JSON SHA-256: `1acfcb2703b548ae124a9e7a49a9ac43361c5f62340228f87918e562f212e2c9`.
