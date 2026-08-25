# Hostile different-model source review — corrected AS post-D10 D9/D8 package

| Field | Value |
|---|---|
| Claim under review | Frozen corrected producer: from `det J-1=3L+9(K+C_x+D_y)+27M+81N`, the next D9/D8 residual is `M` plus the single-Frobenius part of `K/3 mod 3`; the double-Frobenius part vanishes; all six degree-six Frobenius directions enter. Vertical D9 is unchanged and has the displayed global section. After the six licensed D8 pivots and the invertible triangular coordinates, the `7 x 5` core is the displayed Sylvester matrix and the affine column is the exact next AS source column in `(fua,fa,fb,fc,fd,fvb)`, with literal-F3 census `314127/1594323`. The localized `g!=0` endpoint after the three D10 pivots is a `17 x 14` system with census `918/354294`. Four next-carry controls are pointwise only. No `Fbar_3`, all-depth, characteristic-zero, counterexample, or JC2 claim |
| Overall verdict | **CONFIRMED** |
| Smallest failing identity | none |
| Smallest missing hypothesis | none that breaks a numbered claim (non-blocking remarks below; degree-seven of `E1+M` is not this gate; the `g`-endpoint keeps `fvb` as a free spectator rather than an occurring monomial; next divided carry, algebraic-closure classification, all-depth lift/no-lift, characteristic zero, a counterexample, and JC2 are correctly *not* claimed) |
| Evidence tier | independent integer Jacobian expansion over `Z` (400 random samples, zero remainder) and constructive `(det J-1)/27=E1+M+3N` after `L=3L1` and `E=3E1` (80 constructed families, zero remainder); independent integer `(K(U0+UF,V0+VF)-K(U0,V0))/3 mod 3` versus formula (3) on both licensed branches; empty double-Frobenius class; both erratum witnesses rebuilt; independent regeneration of vertical D9, the `7 x 5` core, and the affine column from the integer residual, matched termwise to the displayed matrix and to the frozen generator's column; independent `g!=0` `17 x 14` system, named degree-nine terms, structural census, and full `354294`-point exhaustion; independent integer determinants of the two mod-81 maps and lex-zero `N_12` on the four fibres; registered `./replay_all.sh` as regression only |
| Reviewer / model | Grok 4.6 (xAI). Different model family from the producer. The prior Claude attempt wrote no report and supplies no evidence |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD at launch | `2e6104a417cfe15a93a901aa0a9129094a2ae11b` (the charged freeze basis) |
| Git HEAD at close | `2e6104a417cfe15a93a901aa0a9129094a2ae11b` (unchanged) |
| Review window (UTC) | 2026-08-24T21:40:00Z – 2026-08-24T21:56:07Z |
| Python | host CPython 3.14.6 (hashes, integer identities, independent row reconstruction, F3 structural/exhaustive censuses, next-carry attacks, registered replay) |
| Singular | 4.4.1 (present; used only inside the registered replay as regression, not as mathematical evidence) |
| Host | `dc-mbp-m2.local`, Darwin arm64 |

Producer, freeze, and named payloads reread in full before any verdict:

- `xmodel/as-fonly-d7-postd10-d98-f3-corrected-20260824.md` (SHA-256 `9cc39af35e1d52c9673755b79392e62bb265f78dc38bd9110cd37a992115c2d8`)
- `cases/as_fonly_d7_postd10_d98_f3_corrected_20260824/FREEZE.txt` (SHA-256 `bf7ce39ae1cf7cc6338c006cd2cd59d11a387d8644d740e6faee2cb63229a264`)
- `cases/as_fonly_d7_postd10_d98_f3_corrected_20260824/MANIFEST.sha256` (SHA-256 `a5480d2e3d7c36db4fee735ef8f2262c3454e3e35eb348c7f097c45c59aa2cfb`)
- `cases/as_fonly_d7_postd10_d98_f3_corrected_20260824/README.md` (SHA-256 `e80ef06e4e729578bdfa20b93291abe340712374036d15d9a8a54d63d153a83a`)
- `cases/as_fonly_d7_postd10_d98_f3_corrected_20260824/generate_corrected.py` (SHA-256 `a71daa0cb525bac229afb91c76987c8f25c1e2d63683caa10ff45d3364c658e5`)
- `cases/as_fonly_d7_postd10_d98_f3_corrected_20260824/audit_corrected_frobenius_rows.py` (SHA-256 `77485e9d583dd621c8ae412fa70bab3c2aa5b7605bebe03e0b74a3c4dc87689c`)
- `cases/as_fonly_d7_postd10_d98_f3_corrected_20260824/audit_vertical_d9_section.sing` (SHA-256 `10bee490139f99a806b8b988b73e9f26eccf028bcb2b30c2d3e9b21f7a90c00b`)
- `cases/as_fonly_d7_postd10_d98_f3_corrected_20260824/audit_vertical_core_rank.sing` (SHA-256 `d6add03d9545fb12bbf101a633d994c9cb2d45b971855b1578092c8d363635b3`)
- `cases/as_fonly_d7_postd10_d98_f3_corrected_20260824/reconstruct_representatives.py` (SHA-256 `9dfc726d859c5eb275638e3b9cd74d166e0ca2e95daef099de3f41453a2e3bf1`)
- `cases/as_fonly_d7_postd10_d98_f3_corrected_20260824/replay_next_carry_controls.py` (SHA-256 `0f4c01b359d7bd73db1adeb38437be85ba3c163547ec586d5c0a29b8b16e1026`)
- `cases/as_fonly_d7_postd10_d98_f3_corrected_20260824/replay_all.sh` (SHA-256 `b3564b4e34f60bba751f00de3e30420050c1e6537db3a137001b89d0ca16e5ff`)

Confirmed omitted-carry erratum, D10 producer/review, and the already-completed vertical state review, consumed for the preservation/retraction boundary and to refuse repeating the abstract-matrix census:

- `xmodel/as-fonly-d7-postd10-d98-f3-erratum-20260824.md` (SHA-256 `26dd0908295bfbcc36ad2f0efe59b645ce1dd11411fd88ab8e37337a74fc0d7d`)
- `xmodel/as-fonly-d7-postd10-d98-f3-erratum-review-grok-20260824.md` (SHA-256 `c97330558a53ad3caa82d1bf53f642f68139d453edbe96f541a55eece331ad8a`), overall **CONFIRMED**
- `xmodel/as-fonly-d7-degree10-pointwise-20260824.md` (SHA-256 `e4311a80aef2d3617c7b449e16cb19d34cfe25d31c558bb68f78ddc02fcae4ab`)
- `xmodel/as-fonly-d7-degree10-pointwise-review-grok-20260824.md` (SHA-256 `8ccaa15fd9180660d5ab7e2957737c028a96bb5b28508378e0a3ca93964089b5`), overall **CONFIRMED**
- `xmodel/as-fonly-d7-vertical-state-sufficiency-review-grok-20260824.md` (SHA-256 `6ab373bf9214c54f506cd368473aff02ed472a20e9797037f83a9745c384bc17`), overall **CONFIRMED** for the displayed `7 x 5` matrix and its literal-F3 comparison against this column, not as an AS-successor theorem

Quarantined predecessor, consumed only to police byte-preservation and to refuse reuse of old columns/counts:

- `xmodel/as-fonly-d7-postd10-d98-f3-20260824.md` (SHA-256 `ff85614982fb26a7d8aba2859c7d1be6e3274ff8170114f23b247b5172fd0fc9`)
- `cases/as_fonly_d7_postd10_d98_f3_20260824/FREEZE.txt` (SHA-256 `f03fc06930c12398f714d5af60ed93374ffa80226bf1504d9429747cbdd6fa60`)
- `cases/as_fonly_d7_postd10_d98_f3_20260824/MANIFEST.sha256` (SHA-256 `1efda261bcd531fd4352c8b3f27ee2cafd77b7bf36dd31a9379d9083733a8f2b`)
- `cases/as_fonly_d7_postd10_d98_f3_20260824/generate_and_enumerate.py` (SHA-256 `243c357c18dbbe445f665621ceb5c748f96aa026cb73947fe38dd8b7af8e365e`)

The charged freeze basis is `2e6104a417cfe15a93a901aa0a9129094a2ae11b`. Review started and closed there. Named producer artifacts remain uncommitted. Recomputed producer hashes at close match the launch table. No producer, case, canonical, coordination, prompt, log, run, predecessor, or other review file was edited. No AWS call was made. Independent reconstruction lived only in `/tmp/as_d7_d98_corrected_source_review/` and in ephemeral interpreters. `generate_corrected.py` and the case audits were not imported as mathematical evidence; they were used only as frozen bytes to compare against independently regenerated rows, and as the registered replay.

Tried hard, and failed, to keep a double-Frobenius monomial alive after `/3` mod 3; to drop `fua` or `fvb` from the vertical D8 column; to make the frozen column a Groebner/module-remainder or representative-dependent surrogate of `M+KFdiv`; to change D9 by the single-cross; to restore the retracted `g f_c=g f_d=0` rows or the `13 x 14` system after adjoining formula (3); to cancel `2x^8` in `(det J-1)/81` by a cap-seven correction that preserves Keller modulo 81; to make `N_12` the unique degree-twelve class of a whole fibre rather than of the lex-zero representative; to reuse `50939/177147` or `954/4374`; and to leak an `Fbar_3`, all-depth, characteristic-zero, counterexample, or JC2 inference out of the stated scope.

The prior Claude attempt `xmodel/as-fonly-d7-postd10-d98-f3-corrected-review-claude-20260824.log` is a two-line launcher plus an output-token failure. It wrote no report and was not consumed.

---

## Promotion

**Accept `FROM THE INTEGER IDENTITY det J(P,Q)-1=3L+9(K+C_x+D_y)+27M+81N, AFTER THE REVIEWED FIRST-DIGIT EQUATIONS AND THE ACCEPTED DEGREE-FIVE/SIX ROWS, THE NEXT D9/D8 RESIDUAL IS M PLUS THE SINGLE-FROBENIUS PART OF K/3 MOD 3. THE DOUBLE-FROBENIUS PRODUCT VANISHES AFTER /3. ALL SIX DEGREE-SIX FROBENIUS DIRECTIONS ENTER THE VERTICAL REGENERATED ROWS, WITH CAPS DEGREE EIGHT VERTICALLY AND DEGREE NINE ON THE g ENDPOINT. VERTICAL D9 IS UNCHANGED AND HAS THE DISPLAYED GLOBAL POLYNOMIAL SECTION. AFTER THE SIX LICENSED D8 UNIT PIVOTS AND THE INVERTIBLE TRIANGULAR COORDINATES, THE 7 BY 5 CORE IS THE DISPLAYED SYLVESTER MATRIX AND THE AFFINE COLUMN IS THE EXACT NEXT AS SOURCE COLUMN IN (fua,fa,fb,fc,fd,fvb), NOT AN AMBIENT OR REPRESENTATIVE-DEPENDENT SURROGATE. ITS LITERAL-F3 CENSUS IS 314127/1594323 WITH THE STATED HISTOGRAM, RANK TRIPLES, TWELVE EMPTY BASES, AND BOTH STREAM HASHES. THE LOCALIZED g!=0 ENDPOINT AFTER THE THREE D10 PIVOTS g*c7_0, g*c7_3, g*c7_6 IS A 17 BY 14 SYSTEM RETAINING ALL SIX FROBENIUS DIRECTIONS AS FIBRE VARIABLES; THE TWO NAMED DEGREE-NINE TERMS ARE 2 g fua x^4 y^5 AND g fa x^7 y^2; ITS CENSUS IS 918/354294 WITH THE STATED HASHES. THE FOUR NEXT-CARRY CONTROLS HOLD POINTWISE, INCLUDING (det J-1)/81 = x^4+2x^6+2x^8 MOD 3 ON THE TWO DISPLAYED MOD-81 MAPS.`**

On the map-only aligned deep branch `P=x-x^3+3U+9C`, `Q=y+3V+9D`:

- Over `Z`, `det J-1=3L+9(K+C_x+D_y)+27M+81N` with the displayed signs. After `L=3L1` and `E=L1+K+C_x+D_y=3E1`, the residual is `(det J-1)/27=E1+M+3N`. At total degrees eight and nine, `L1` and `C_x+D_y` do not occur, so the residual is `K_high/3+M`. Split `U=U0+UF`, `V=V0+VF` with the six degree-six directions. Every integer derivative of `(UF,VF)` is divisible by three. The single-cross is formula (3) of the producer. The double-Frobenius Poisson product is divisible by nine, hence vanishes after `/3` mod 3. Against the licensed vertical first-digit layer this reaches total degree eight and not nine. Against `V_5=g x^5` it reaches degree nine and not ten. All six variables occur in the vertical regenerated rows. Independently, `(K(U0+UF,V0+VF)-K(U0,V0))/3 mod 3` equals formula (3) on both branches, and the two erratum witnesses rebuild as `2x^7+2x^8` and `2 x y^6 + 2 x^4 y^5`.
- Vertical D9 has four nonempty rows, coefficient matrix equal to the displayed `4 x 9`, and global polynomial section `ell=(-pr,-qr-pt,-qt,r^2,0,-rt,0,t^2,0)^T`. The single-cross cannot reach vertical degree nine, so D9 is unchanged by the source correction. Six source-typed unit pivots on `d7_0,c7_0,d7_3,c7_3,d7_6,c7_6` leave remaining labels `M_0_9,M_3_6,M_6_3,M_9_0,M_0_8,M_3_5,M_6_2` in unknowns `(d7_1,d7_4,d7_7,d6_1,d6_4)`. The invertible triangular substitution (6) produces the displayed `7 x 5` core, including polynomial entries `-h^3`. The affine column of that reduced system is exactly `M+KFdiv` after those licensed operations: it is affine in all six Frobenius variables, the core matrix is independent of them, and the column matches the frozen generator termwise. It is not a Groebner remainder, not a Fitting surrogate, and not a representative-dependent lift.
- On `g!=0` the three D10 mixed-carry rows remain unit pivots `g*c7_0,g*c7_3,g*c7_6`. After those exact eliminations the regenerated D9/D8/D10 system has 17 rows and 14 current-digit unknowns. The omitted degree-nine classes are `2 g fua x^4 y^5` and `g fa x^7 y^2`. The four-variable fibre and the retracted `13 x 14` system do not survive. All six Frobenius names are retained as fibre variables.
- Four vertical fibres of sizes `3,9,81,729` reconstruct with an exact Gaussian solver. The lex-zero 3-fibre and 81-fibre solutions have `{C,D}_12=x^{12}` and `2x^{12}` respectively; degree twelve of the `/81` residual comes only from `{C7,D7}`, so those particular representatives are obstructed, not their fibres. The two displayed maps of the 729-fibre and 9-fibre are Keller modulo 81 with `(det J-1)/81 ≡ x^4+2x^6+2x^8 (mod 3)`. A cap-seven correction that preserves that divisibility has divergence of degree at most six and cannot cancel `2x^8`. Pointwise terminal modulo 243 at cap seven, not a fibre-wide obstruction.

**Do not promote this to:** an algebraic-closure or Fitting classification of either inhomogeneous family; emptiness or nonemptiness of `FONLY_(3,7)(D=7)`; a completed following integer carry, including the unexamined degree-seven residual of `E1+M`; all-depth lifting or nonlifting; a characteristic-zero lift or no-lift theorem; a counterexample to JC; or any JC2 inference. Do not reuse the quarantined post-D10 column, the counts `50939/177147` or `954/4374`, the rows `g f_c=g f_d=0`, or the four-variable fibre `(f_a,f_b,f_c,f_d)` as complete. Do not read the two mod-81 maps or the two `N_12` classes as fibre-wide. Do not replace polynomial `-h^3` by `-h` outside literal F3 points.

**Smallest honest successor.** Impose the following divided carry on the two capped adjugate quotients of the displayed vertical core (already confirmed as a state theorem) together with the unexamined degree-seven residual of `E1+M`, and separately advance the `17 x 14` `g!=0` system. Neither step is this gate.

---

## Quarantine

The following readings are refused and must not be reused as live mathematics:

- the quarantined post-D10 inhomogeneous column, the counts `50939/177147` and `954/4374`, the hash `d7910730…`, the hash `119580e2…`, the rows `g f_c=g f_d=0`, the `13 x 14` system, or the four-variable Frobenius fibre `(f_a,f_b,f_c,f_d)` as complete;
- this gate as an algebraic-closure/Fitting classification, a next divided carry, a complete D8-to-D7 classification, or emptiness/nonemptiness of `D=7`;
- this gate as all-depth lifting or nonlifting, a characteristic-zero statement, a counterexample, or JC2;
- the two reconstructed `N_12` classes, or the two mod-81 maps, as a fibre-wide obstruction;
- the prior Claude launcher/log as review evidence.

The quarantined predecessor bytes themselves are unchanged. Producer strings `PASS-CORRECTED-POST-D10-D98-ALL`, `PASS-VERTICAL-D98-CORE`, and the enumeration `PASS-` tags were not used as evidence. Independent reconstruction, not the producer scripts, is the evidence for every numbered claim. The registered replay was rerun unmodified as a regression only.

---

## Scope (not enlarged)

One prime `p=3`; one total-degree cap seven; the aligned deep branch of the confirmed 30-row first-digit ideal; the licensed vertical and `g!=0` survivors of the confirmed degree-ten gate; source-exact D9/D8 rows after the omitted-carry correction; literal-F3 finite censuses; pointwise next-carry controls. No rectangular support, no enumerator, no AWS, no gauge cap, and no modular-to-characteristic-zero existence inference are in scope. The already-confirmed vertical state theorem is not re-audited here.

---

## Headline and subclaim table

| # | Exact subclaim | Verdict | What would have flipped it |
|---|---|---|---|
| 1 | From `det J-1=3L+9(K+C_x+D_y)+27M+81N`, the single-Frobenius part of `K/3 mod 3` is formula (3), the double-Frobenius part vanishes, and all six degree-six Frobenius variables enter with caps degree eight vertically and nine on the `g` endpoint | **CONFIRMED** | a leftover sign on `K` or `M`; a double-Frobenius monomial surviving `/3` mod 3; formula (3) unequal to `(Kfull-K0)/3 mod 3`; `fua` or `fvb` absent from the vertical high rows; a vertical degree-nine single-cross; a degree-ten single-cross on either licensed branch |
| 2 | Vertical D9 is the displayed `4 x 9` with global section (5). After the six licensed D8 pivots and coordinates (6), the `7 x 5` core is the displayed Sylvester matrix and the affine column is the exact next AS source column in all six Frobenius variables. Literal-F3 census `314127/1594323` with histogram (10), triples (11), empty-base locus (12), and hashes (12),(14) | **CONFIRMED** | a termwise mismatch of the core or of the column; Frob in the core matrix; the column equal to `M` alone; a Groebner remainder used in place of the source rows; empty bases other than `P=Q=s=h=0,R≠0,w≠0`; a fibre count off by one |
| 3 | After the three D10 pivots `g*c7_0,g*c7_3,g*c7_6`, the `g!=0` system is `17 x 14`, retains all six Frobenius directions as fibre variables, and contains the named terms `2 g fua x^4 y^5` and `g fa x^7 y^2`. Census `918/354294` with (15)–(18) | **CONFIRMED** | remaining shape other than `17 x 14`; those two monomials absent; `g f_c=g f_d=0` still the full D9 residual; fibre names reduced to four; a hash or count mismatch |
| 4 | The four next-carry controls hold in the integer determinant: lex-zero `N_12` on the 3-fibre and 81-fibre; the two displayed maps have `det=1+81x^4+648x^6+1134x^8` and residual `x^4+2x^6+2x^8 mod 3`; `2x^8` is uncancelled by a cap-seven correction that stays Keller mod 81; all four are pointwise, not fibre-wide | **CONFIRMED** | a different `N_12` on those lex-zero solutions; `(det-1)` not divisible by 81 on either displayed map; residual other than `x^4+2x^6+2x^8`; a cap-seven Keller-mod-81 perturbation cancelling `2x^8`; a fibre-wide claim in the producer |
| 5 | Old counts/column remain quarantined. No `Fbar_3`, all-depth, characteristic-zero, counterexample, or JC2 claim is smuggled in | **CONFIRMED** | reuse of `50939`, `954/4374`, `d7910730…`, or `119580e2…` as live mathematics; a sentence asserting compatibility over `Fbar_3`, emptiness of `D=7`, a lift, a no-lift, a counterexample, or JC2 |

All remarks below are non-blocking unless marked otherwise. None changes a numbered verdict.

---

## Replay and hashes

Registered commands, rerun unmodified from the case directory:

```sh
cd cases/as_fonly_d7_postd10_d98_f3_corrected_20260824
./replay_all.sh
```

Exited 0 in 312.83s. Printed `PASS-CORRECTED-DIVIDED-FROBENIUS-ROWS`, the two integer Jacobians and residuals, the four representative `N_12` supports, `PASS-VERTICAL-D9-GLOBAL-SECTION`, `PASS-VERTICAL-CORE-RANK-STRATA`, `PASS-VERTICAL-D98-CORE`, both structural histograms and rank triples, both empty-base hashes, both exhaustive enumerations `314127/1594323` and `918/354294` with rank-stream hashes (14) and (18), manifest OK, and `PASS-CORRECTED-POST-D10-D98-ALL`. These runs were regressions only.

Recomputed SHA-256 (all match the launch prompt and `FREEZE.txt`):

| Artifact | SHA-256 |
|---|---|
| `xmodel/as-fonly-d7-postd10-d98-f3-corrected-20260824.md` | `9cc39af35e1d52c9673755b79392e62bb265f78dc38bd9110cd37a992115c2d8` |
| `cases/as_fonly_d7_postd10_d98_f3_corrected_20260824/MANIFEST.sha256` | `a5480d2e3d7c36db4fee735ef8f2262c3454e3e35eb348c7f097c45c59aa2cfb` |
| `cases/as_fonly_d7_postd10_d98_f3_corrected_20260824/FREEZE.txt` | `bf7ce39ae1cf7cc6338c006cd2cd59d11a387d8644d740e6faee2cb63229a264` |
| `replay_all.sh` | `b3564b4e34f60bba751f00de3e30420050c1e6537db3a137001b89d0ca16e5ff` |
| `generate_corrected.py` | `a71daa0cb525bac229afb91c76987c8f25c1e2d63683caa10ff45d3364c658e5` |
| `audit_corrected_frobenius_rows.py` | `77485e9d583dd621c8ae412fa70bab3c2aa5b7605bebe03e0b74a3c4dc87689c` |
| `README.md` | `e80ef06e4e729578bdfa20b93291abe340712374036d15d9a8a54d63d153a83a` |

Quarantined predecessor hashes, unchanged:

| Artifact | SHA-256 |
|---|---|
| old report | `ff85614982fb26a7d8aba2859c7d1be6e3274ff8170114f23b247b5172fd0fc9` |
| old freeze | `f03fc06930c12398f714d5af60ed93374ffa80226bf1504d9429747cbdd6fa60` |
| old manifest | `1efda261bcd531fd4352c8b3f27ee2cafd77b7bf36dd31a9379d9083733a8f2b` |
| old generator | `243c357c18dbbe445f665621ceb5c748f96aa026cb73947fe38dd8b7af8e365e` |

---

## Independent recomputation

### 1. Integer Jacobian, single-cross, double vanishing, six directions — CONFIRMED

Direct expansion over `Z` with integer derivatives gives

```text
P_x = 1-3x^2+3 U_x+9 C_x,     P_y = 3 U_y+9 C_y,
Q_x = 3 V_x+9 D_x,             Q_y = 1+3 V_y+9 D_y,
```

and `det J-1=3L+9(K+C_x+D_y)+27M+81N` with the displayed signs of `K,M,N`. Four hundred random integer samples of `(U,V,C,D)` of degrees at most seven produced zero remainders. After imposing `L=3L1` and `E=3E1` on eighty constructed families (base pair `(U,V)=(0,x^2 y)` plus 3-divisible noise, with a `C,D` correction cancelling `E` mod 3), `(det J-1)/27=E1+M+3N` in every case.

Write `UF=fua y^6+fa x^3 y^3+fb x^6` and `VF=fc y^6+fd x^3 y^3+fvb x^6`. Integer derivatives are

```text
UF_x = 3 fa x^2 y^3+6 fb x^5,     UF_y = 6 fua y^5+3 fa x^3 y^2,
VF_x = 3 fd x^2 y^3+6 fvb x^5,     VF_y = 6 fc y^5+3 fd x^3 y^2,
```

so `/3 mod 3` is the displayed `(ufx3,ufy3,vfx3,vfy3)`, and `[L/3]_5=fa x^2 y^3+2 fb x^5+2 fc y^5+fd x^3 y^2`. The double Poisson product is divisible by nine, hence `(UF_x VF_y-UF_y VF_x)/3 ≡ 0 (mod 3)`. The 3-divisible extras in integer `U0_x` multiply a Frobenius derivative and vanish after `/3` mod 3, so formal `F3` derivatives of the first-digit layer are legal in formula (3).

On the licensed vertical compression, formula (3) equals `(K(U0+UF,V0+VF)-K(U0,V0))/3 mod 3` as sparse polynomials, with maximum total degree 8, and support in all six names `fua,fa,fb,fc,fd,fvb`. On the `g` endpoint, the same identity holds with maximum total degree 9. The integer pair `U0=2x^4`, `V0=x^2 y+x^3 y`, `UF=x^6` rebuilds `2x^7+2x^8`. The pair `UF=y^6`, `V0=x^2 y+x^5` rebuilds `2 x y^6+2 x^4 y^5`.

`fua` and `fvb` are invisible to `[L/3]_5` and to `M mod 3`. They enter only through formula (3). That is the omitted carry.

### 2. Vertical D9, D8 core, and exact source column — CONFIRMED

High rows were regenerated from `R=M(U0,V0,C,D)+KFdiv`, after independently solving the degree-five accepted row (six unit pivots `c6_1,c6_2,d6_2,c6_4,c6_5,d6_5`) and the degree-six D10 accepted row (the seven licensed `C7,D7` pivots). Vertical nonempty labels are

```text
M_0_9, M_3_6, M_6_3, M_9_0, M_0_8, M_1_7, M_2_6, M_3_5, M_4_4, M_5_3, M_6_2, M_7_1, M_8_0.
```

The four D9 rows, in the nine free `C7,D7` variables, have coefficient matrix equal to the displayed `4 x 9`. The displayed `ell` satisfies `A9 ell = b9` as a polynomial identity (all four residues empty), including on rank-changing loci. D9 support is independent of the six Frobenius names, as required by the degree bound.

Searching the nine D8 rows for unit coefficients recovers pivots on `M_2_6,M_1_7,M_5_3,M_4_4,M_8_0,M_7_1` for `d7_0,c7_0,d7_3,c7_3,d7_6,c7_6`. Remaining labels are `M_0_9,M_3_6,M_6_3,M_9_0,M_0_8,M_3_5,M_6_2` in `(d7_1,d7_4,d7_7,d6_1,d6_4)`. The F3 inverse of (6) produces a `7 x 5` equal to the displayed Sylvester matrix, including `2 h h h = -h^3`. The core matrix contains none of the six Frobenius names. The affine remainder — the frozen column — is affine in all six, and as a polynomial 7-vector equals the frozen generator's `bC` termwise.

That column is the next AS source row: it is `E1+M` at degrees eight and nine, after exact unit-pivot elimination of licensed current digits and an invertible coordinate change. It is not `M` alone, not a module remainder, and not a chosen representative. The already-confirmed state review therefore compares the displayed matrix to the actual successor column.

Independent structural projection over all `3^7=2187` bases, using that regenerated column, returns compatible total `314127`, histogram `{0:12, 3:36, 9:16, 81:1904, 729:219}`, rank triples (11), empty-base stream `5b66a63af070eff410c1824a6e6f4e73fc254da13eb5445dcb9bdae4c2ece701`, and empty locus exactly `P=Q=s=h=0`, `R≠0`, `w≠0`, `T` arbitrary (twelve bases). The projection is exact because the system is affine in the fibre and the matrix is fibre-free; it agrees with the exhaustive `1594323`-point census of the frozen column (state review plus registered replay). Rank stream `e86fd1ec…b23d` is the frozen exhaustive hash of that same column.

### 3. Localized `g!=0` endpoint — CONFIRMED

On the `g` branch the regenerated residual at degrees 10, 9, 8 has 20 nonempty rows and the same 17 current-digit unknowns. The three degree-ten rows `M_4_6,M_7_3,M_10_0` are the D10 mixed-carry pivots `g*c7_0,g*c7_3,g*c7_6`. Localizing `g≠0` sets those three digits to zero and drops those three rows, leaving 17 rows in 14 unknowns

```text
d7_0, d7_1, d7_3, d7_4, d7_6, d7_7, c6_0, c6_3, c6_6, d6_0, d6_1, d6_3, d6_4, d6_6.
```

KFdiv on this branch contains the monomials `2 g fua x^4 y^5` and `g fa x^7 y^2`, coming from `-(UF_y/3)·(2 g x^4)` with `UF_y/3=2 fua y^5+fa x^3 y^2`. Those terms make the old deletion of four D9 rows, and the old rows `g f_c=g f_d=0`, invalid. Fibre names remain `(fua,fa,fb,fc,fd,fvb)`.

Independent structural projection over the 486 bases with `g≠0` returns histogram `{0:360, 3:36, 9:90}`, triples (16), compatible total 918, empty-base hash `2fdb6b61e6a98e9e4b39ce8459f62774cf6dacd161b04c6752e044e87e963b2e`. Independent exhaustion of all `486·3^6=354294` literal points returns rank pairs (17), compatible 918, and rank stream `ce421ac61d73307c3d0bd553af9e23df7f040f6e7b3e85b4d7da06f220935b67`. Structural and exhaustive totals agree.

### 4. Next-carry controls, division by 81, pointwise scope — CONFIRMED

Lex-zero Gaussian solutions of the independently regenerated vertical system:

| fibre | `(P,Q,R,T,s,w,h)` | Frobenius | `N_12` | `N_11` |
|---|---|---|---|---|
| 3 | `(0,0,0,1,1,0,0)` | `fb=2` | `x^{12}` | `2 x^{11}` |
| 9 | `(0,0,0,0,0,1,0)` | `0` | empty | empty |
| 81 | `(0,0,0,0,0,1,1)` | `fvb=1` | `2 x^{12}` | `2 x^{10} y` |
| 729 | `(0,0,0,0,0,0,0)` | `0` | empty | empty |

`{C6,D7}` and `{C7,D6}` produce total degree at most 11; only `{C7,D7}` produces degree 12. A new cap-seven third digit contributes at order 81 through `W_x V_y` of degree at most 11. Thus `N_12≠0` obstructs those two lex-zero representatives and not their fibres, matching (19) and the producer's scope sentence.

The two displayed maps, which reduce to the 729-fibre and 9-fibre first-digit points, have integer Jacobian `1+81x^4+648x^6+1134x^8` (the optional `3x^4` in `Q` has no `y`-derivative and does not change `det`). Both are Keller modulo 81. After division by 81 the residual is `x^4+2x^6+2x^8 mod 3`. Adding `27 a x^7` destroys divisibility by 81 unless `a=0`. Adding an order-81 cap-seven monomial (so that the order-27 divergence vanishes) can cancel the `x^6` class but leaves the `x^8` class equal to 2. That is the precise content of “a cap-seven correction has divergence of degree at most six”. Pointwise terminal modulo 243 at cap seven.

### 5. Quarantine and refusal scope — CONFIRMED

The old generator still emits high rows from `Mfull` alone, does not name `fua` or `fvb`, and does not contain `KFdiv`. Its freeze still records `50939/177147` and `954/4374` with hashes `d7910730…` and `119580e2…`. Those bytes are unchanged and are not cited as live counts in the corrected report, freeze, or case README. The corrected report mentions `13 x 14` only as the retracted system.

Refusal sentences in the corrected report and README name `Fbar_3`, algebraic-closure/Fitting classification, full-D7, all-depth, no-lift, characteristic zero, counterexample, and JC2 as things *not* claimed. No contrary sentence was found.

---

## Non-blocking remarks

1. This gate does not impose degree seven of `E1+M`. That residual exists: formula (3) against the degree-three layer reaches degree seven, and `M_7` involves `C6,D6`. Omitting it is correct scope for a D9/D8 package, not a source error in the D8 column. It is the smallest honest unexamined successor row on the vertical branch.

2. On the specialized `g!=0` 17 rows, `fvb` does not occur as a monomial. After `p=q=0`, the only single-cross in `fvb` is `2 h fvb x^7`, which is degree seven. The producer nevertheless retains `fvb` in the six-variable fibre, so the census counts it as a free spectator (`3^{6+r-c}` still has the extra factor of 3). That is “not discarded”, not “occurs in the 17 rows”. Vertically all six names occur in the column. No numbered claim fails.

3. The two mod-81 maps are particular integer lifts of the 9-fibre and 729-fibre, not the lex-zero `C=D=0` solutions of the D8 system (those fail already at valuation 9). The producer states the control as pointwise. Do not upgrade it.

4. Geometric ranks `0,2,3,5` of the displayed `7 x 5` are reused from the confirmed state review and the preserved erratum matrix-level statement. They were not re-derived here.

---

Close: git HEAD `2e6104a417cfe15a93a901aa0a9129094a2ae11b`, unchanged. Charged hashes unchanged. No producer or predecessor file edited. No AWS.
