# External artifact intake — SuperMind and Ziwei Guo

- **Producer/session:** OpenAI Codex, Bacon lane (`/root/compute_audit`)
- **Parent round:** consolidated candidate 1 from round
  `20260824T0035Z-2386780`
- **Audit window:** 2026-08-23/24 UTC
- **Host:** Darwin 23.6.0 arm64; Python 3.14.6; SymPy 1.14.0;
  Singular 4.4.1 (44105, 2025-11-11)
- **Workspace:** fresh private temporary directory
  `/tmp/jc2-external-intake-20260824.iNiGQL`, outside the repository
- **State:** **FROZEN BOUNDED INTAKE** at `2026-08-24T01:38:39Z`
- **Overall verdict:** **SUPERMIND EXACT TERMINAL REPLAY PASS; GUO PARTIAL
  EXACT REPLAY PASS WITH SAGE-ONLY GAPS; SAME TWO MATHEMATICAL SYSTEMS;
  DERIVATIONAL INDEPENDENCE UNRESOLVED**

This is an intake and lineage report, not a new global theorem.  It supersedes
the discovery-only status in `xmodel/websweep-2026-08-23.md:136-142`: both
artifacts were pinned, safety-inspected, hash-checked, and exercised through
bounded paths.  It does **not** edit the campaign's shared proof or priority
ledgers.

## 1. Executive decision

1. **SuperMind's finite residual-support certificates survive local exact
   replay.**  The exact first-layer and smaller-support computations passed in
   Python, and the primary larger-support certificate passed in Singular: the
   characteristic-zero closed-chart lift, 52-dimensional core, preservation of
   all 52 standard monomials modulo 67, and rank-52 multiplication witness all
   checked.  The terminal is a valid good-specialization nonvanishing argument,
   not a finite-field inference that a rational ideal is the unit ideal.
2. **Ziwei Guo's public bundle is intact and several central exact paths pass,
   but this machine did not complete the advertised full theorem replay.**  A
   fresh extraction matched all 790 authoritative manifest entries; logical
   coverage, the conditional global audit, three regression tests, the
   standalone degree-21 verifier, the exact characteristic-zero Singular FGLM
   calculation, and both row-split identities passed.  SageMath and Docker were
   absent, so the Sage-only terminal expansions for the smaller lift and the
   larger `V(c)`, `D!=0`, and `D=E=0` branches remain a declared replay gap.
3. **The objects are exactly the campaign's two Proposition-4.3 systems.**  The
   four polygons, bracket convention, right-hand side, and lattice counts agree
   with `jc72108/CROSSCHECK.md:7-16,29-49`.  SuperMind's and Guo's Laurent models
   are literally related by a variable-and-slice rename given below.
4. **The common degree-five field relation is now exact, not merely
   probabilistic.**  The simple quintic used by SuperMind and Guo is exactly
   isomorphic to both the Helali quintic and Suzuki's large-coefficient quintic;
   exact substitutions reduce to zero.  This upgrades the factor-shape evidence
   recorded in `jc72108/CROSSCHECK.md:79-88` for this comparison.
5. **Do not turn these two repositories into two new independent votes.**  Their
   terminal methods differ, and no byte-identical non-PDF source file was found,
   but they share the same GGV reduction, degree-21/five-dessin core, exact
   quintic, publication neighborhood, and Sol/Codex model family.  Neither gives
   enough provenance to decide social or derivational independence from the
   Suzuki--Roy line.
6. **The campaign conclusion does not change perimeter.**  Together with the
   already replayed exact Helali and Suzuki artifacts
   (`jc72108/CROSSCHECK.md:90-172`), the intake further supports emptiness of
   both residual systems.  The exclusion of the full `(72,108)` counterexample
   case remains conditional on the faithfulness/exhaustiveness of the cited GGV
   reduction and its transcription.  It is not an unconditional degree-125
   theorem and is not a proof of the plane Jacobian conjecture.

## 2. Intake protocol and safety boundary

The temporary root was created with the shape

```sh
mktemp -d /tmp/jc2-external-intake-20260824.XXXXXX
```

The repositories were cloned into it, and only Guo's flat release ZIP plus its
release checksum file were downloaded.  Before execution I inspected the
Python/Sage/Singular entry points, imports, process-launch sites, and write
sites.  The bounded paths have no network or credential access.  SuperMind's
only process launch is an explicit local Singular invocation.  Guo's global
audit can launch Sage for a requested recomputation; it was run with
`--skip-small-recompute`, so it launched no child.  Generators that write JSON
or generated code were either not invoked or wrote only inside the disposable
temporary extraction.  No credentials were passed.  The primary Singular run
used a minimal environment:

```sh
env -i PATH=/opt/homebrew/bin:/usr/bin:/bin Singular -q INPUT.sing
```

The Guo tar member list was checked before extraction: no absolute path and no
`..` traversal component was present.  Python runs used
`PYTHONDONTWRITEBYTECODE=1` where practical; unavoidable pytest cache material
stayed in the disposable extraction.  No verifier wrote to the repository.

Static searches over both source trees and the extracted Guo release found no
`msolve`, `libmsolve`, or `-g 2` invocation.  The msolve characteristic-zero
unit-basis short circuit is therefore not exposed by either proof path; see
section 8.

Evidence labels in this report mean:

- **HASH PASS:** locally recomputed bytes match a pinned manifest or digest.
- **EXACT REPLAY PASS:** the local engine performed exact arithmetic and reached
  the advertised mathematical marker.
- **REGRESSION PASS:** code compared frozen outputs/invariants; this is not an
  independent certificate expansion.
- **STATIC/ARCHIVED:** inspected source or author-supplied output, not locally
  recomputed.
- **GAP:** a required advertised path was not executed here.

## 3. Pinned artifact inventory

### 3.1 SuperMind

| Item | Pin / SHA-256 |
|---|---|
| Repository | `https://github.com/SuperMindAI/Jacobian-Conjecture.git` |
| Audited commit | `8b376296bb8ffeb9a6112d482b9f6b1760d8d1ef` |
| Git tree | `c82d3c05bca2114435ef05023a73ce8dcbfa6684` |
| Commit metadata | `2026-08-05T13:00:02+08:00`, xingchengxu, `Add individual paper essays and new-tab links` |
| Releases | GitHub API returned zero releases; repository commit is the pin |
| Root `README.md` | `6aaf773a760dc8ef91ea8ce049cfec93d6e36d959895ac76a02161e65fd2626d` |
| Degree-125 `main.tex` | `9d757f2461f2b6c88292bd76e82131b493b22a2a6061054a609e032824d5a1a2` |
| Supplement manifest | `b7265df86a22030edab92d9a63a795a52b94e79bc11dc6571306d4e802485e01` |
| `code/verify.py` | `2a88f31056363a385790339f72c69d6c9d8b43cc1318d305a7a3aa79b9cd6adc` |
| `code/case_ii.py` | `3dcf5e29e98149d5aa4ceb3ea11daa90f3ad4243b64d3e29ce026b0d3e5990d8` |
| Primary Case-I Singular input | `6722623b82dd61bad90e53c55881a353727a51d3d1c6263d59c78fc2bd82ebae` |
| Archived quick transcript | `620da511d29f48ddeb2c79dc1ca87f71bf6f3e87a5f7a62effa14d5e9bd164f7` |
| Archived Singular transcript | `03e46255ca52c3d4fad69167d033f03e734f65d8f764cee35834f9ff743ec497` |

The relevant package is
`manuscripts/04-plane-jacobian-degree-125/`.  Its sole Python dependency is
`sympy==1.14.0`; Singular is the external exact-CAS engine.  All 26 entries in
`supplement/CHECKSUMS.sha256` passed with:

```sh
env LC_ALL=C shasum -a 256 -c CHECKSUMS.sha256
```

The authorship disclosure is explicit in the pinned root `README.md:62-67`:
the displayed author is SuperMind, the work is attributed to autonomous
GPT-5.6-Sol Max, and human involvement is described as limited feedback.

### 3.2 Ziwei Guo

| Item | Pin / SHA-256 |
|---|---|
| Repository | `https://github.com/Kakarottoooo/jacobian-2d-research.git` |
| Public-release commit/tag | `624a34a774276bef72b6093af8dd774713f27314` / `public-preprint-v1-2026-08-10` |
| Public-release tree | `fbca91c8b11f5691d3f93014f4054c721065442b` |
| Public commit metadata | `2026-08-10T15:52:50-07:00`, Ziwei Guo, `Publish reproducible public preprint metadata` |
| Theorem-core commit/tag | `7639822e66de9464e141e748088b62d73c388169` / `larger-polygon-logical-proof-2026-08-09` |
| Theorem-core tree | `8cd8f3fde499f0f58f4a2da5b3df54c7aa585ab6` |
| Flat release ZIP | `1bb8228640505e40b1b8813f78df7d7290df6baccb994a1fd92bfdf4acc14448` |
| Release `SHA256SUMS.txt` | `1da82c88a7d03361a174adf64b52a9f240d13b58bab175f813609fe22ba8b437` |
| Release manuscript PDF, manifest value | `43b207e366d053d3724a69062b3449965af404f6af104b26695f760c265ead24` |
| Release reproducibility PDF, manifest value | `0f81d4942695557482de3e9363743c6f10d740ed2a6e056ea59f9dedc407dca1` |
| Inner dependency-closed tar | `bafe29216ed5a502fe507f17b6f67d81d3a5a3811d956d1803b85e83ef6bd7a8` |
| Inner wrapper README | `f187a3b09779c3f460db90c22139ede5ff6d7758d22b3d3da972c84077072091` |
| Authoritative 790-file manifest | `0d4abab2ddeb44af6771c28f689113beb4b6bb2ef55de56a190eaa7c750db6ba` |
| Manifest verifier | `059d6cccdd3b8762bd72b70d2e1877d95af6f4fcb745bebbdda73a2176fc1455` |
| Logical coverage audit | `b4f0f194770fd3aed94203909998cd99b1037220d50d35c97c318c7bfd42bc0d` |
| Global-degree audit | `a6cad997818fc3395175b7d1bef2dedb35d6166ebd79f5baa210688d3814fa34` |
| Standalone Belyi verifier | `8b468f4c4b35ef076801769bc83178756c60de5a9959e5d811639c135ea54421` |
| Primary / independent small terminal JSON | `a00400fce8fed187866f76e27801f959448c245ecb77c22c8f0bcaba7fce9bb7` / `af3cfe5cc7338df418ac7922d55adfc597f6387655217c36680fd58a7d5f4135` |
| Degree-35 lex basis | `cddb0a735a65fc39c0b6431a6edc7929274d36e5322cd7976582077991414d9e` |
| Row-split Singular object | `1fa46d12281933d51bb0152fdaf740e1ad10a514bdcf2ece06f5fa3a3c556f3e` |
| Exceptional unit-certificate JSON (72,672,850 bytes) | `481efe2c46455cda4e4939ad36cd1650c7a8163d8c332b546e7dbcae946f7fe8` |

The release is
`https://github.com/Kakarottoooo/jacobian-2d-research/releases/tag/public-preprint-v1-2026-08-10`.
The ZIP and checksum file were downloaded locally; the two PDF hashes above are
recorded from that signed-off release checksum file, not independently
downloaded bytes.  The project declares Python `>=3.11`, `sympy==1.14.0`, and
optional `pytest==8.4.2`.  The exact proof environment is SageMath 10.9 plus
Singular 4.4.1 in the pinned image
`sagemath/sagemath@sha256:e068670ae5863b54b2550e72437ec637b0283acb0dc712c8584c124dbf44e667`
(`PUBLIC_RELEASE_NOTES.md:55-60`; `REPRODUCE_LARGER_POLYGON.md:7-15`).

The inner wrapper checksum file has CRLF endings.  A raw macOS
`shasum -a 256 -c` interprets the trailing carriage return as part of each
filename and fails.  Normalizing line endings makes both inner entries pass:

```sh
tr -d '\r' < SHA256SUMS.txt | shasum -a 256 -c -
# README_SUPPLEMENT.txt: OK
# jacobian_125_dependency_closed_archive.tar.gz: OK
```

This is a portability defect, not an integrity failure.  In a second fresh
extraction, the authoritative verifier returned:

```text
MATCH=790 MISMATCH=0 MISSING=0 UNLISTED=0 MALFORMED=0
```

The run took 0.16 s and about 28.6 MB RSS.  The archive itself explains that
the historical 68-entry overlay manifest is retained as provenance and is not
self-consistent against v2.1 (`SUBMISSION_SUPPLEMENT_README.md:24-31`).  Its
expected `57` matches, `9` replacements, and `2` missing diagnostics must not
be reported as release corruption.  A diff from theorem core to public tag does
modify six executable proof/audit scripts to add force-recompute, equality, and
global-audit hardening hooks.  Thus “the theorem-core proof code ... is
unchanged” (`PUBLIC_RELEASE_NOTES.md:45-53`) is safest read as no change to the
passed theorem formulas or conclusion, not as byte identity of every executable
at public HEAD.

Guo discloses Codex assistance for exploration, CAS orchestration, drafting,
and packaging while assigning responsibility to Ziwei Guo and excluding
unverified generative output as a theorem premise
(`PUBLIC_RELEASE_NOTES.md:108-116`).

### 3.3 Existing campaign crosscheck baseline

The comparison used the already present `archive/crosscheck.tgz` (campaign
recorded SHA-256
`754da7677726af519160b5203c09e64251009c29d72cb79af46e3cb51b911466`),
Helali repository pin `c530fe4`, and Suzuki verification package v1.1.4
(recorded release hash `d457fbee...74bd`).  Their exact replay status and trust
boundaries are documented in `jc72108/CROSSCHECK.md:19-25,90-172`.  Roy was
crosswalked through the frozen campaign assessment in
`xmodel/grok-vanrijn.md:31-46,54-76`; no unrecorded Roy terminal calculation was
silently promoted to a local replay.

## 4. Bounded executions and outcomes

### 4.1 SuperMind

The source-supplied quick and Singular transcripts have the expected hashes,
but they are only archived evidence.  The following are this audit's local
executions.

**Python first layer and Case II — EXACT REPLAY PASS.**  With Python 3.14.6 and
SymPy 1.14.0, an unbuffered bounded run of `code/verify.py` printed:

```text
PASS quintic: displayed mod-5 and mod-23 irreducibility certificate
PASS first layer Hurwitz count: exact weighted orbit count = 5
PASS first layer: 18 exact coefficients and nonzero endpoints
PASS Case II: ranks 16,17,11; seven conditions; quartic Bezout identity
```

After that marker it entered the expensive pure-Python Case-I regeneration and
was intentionally interrupted rather than duplicating the separate primary
Singular terminal.  An earlier full attempt under `ulimit -t 600` reached the
same Case-I regeneration but exhausted the CPU cap: exit 152, 604.20 s wall,
598.87 s user, approximately 145.8 MB maximum RSS.  Output from that first run
was buffered.  This is a performance/replay gap for the Python regeneration,
not a failed identity.

**Primary Case-I Singular certificate — EXACT REPLAY PASS.**  From
`supplement/code/`:

```sh
(
  ulimit -t 300
  env -i PATH=/opt/homebrew/bin:/usr/bin:/bin \
    /usr/bin/time -l Singular -q case_i_structural_good_reduction.sing
)
```

It exited 0 after 290.65 s wall / 275.98 s user with maximum RSS 567,443,456
bytes and printed all load-bearing markers:

```text
PASS Case I A1=0 chart: direct characteristic-zero lift identity
PASS Case I structural core: basis=23 quotient=52
PASS Case I lucky reduction: mapped core and specialized ideal have the same 52 standard monomials
PASS Case I multiplication matrix: shape 52 by 52
multiplication_rank_mod_67=52
PASS Case I structural lucky-reduction full-rank witness
```

Therefore the pinned Case-I terminal is locally certified within Singular's
exact-arithmetic trust boundary.  The only unclosed SuperMind replay edge is
fresh Python regeneration of that Singular input all the way from the universal
layer recurrence.  The pinned input is hash-bound, its structural terminal
passes, and the author-supplied regeneration transcript reports a pass, but the
regeneration itself did not fit the registered 600-CPU-second gate here.

This treatment matches the artifact's own logic.  The supplement says a
finite-field unit ideal or modular reconstruction marker is not terminal
evidence (`supplement/README.md:36-40`), and the paper explains why the mod-67
calculation instead certifies nonvanishing of a specified characteristic-zero
determinant (`sections/07-certification-and-scope.tex:40-50`).

### 4.2 Ziwei Guo

All commands below ran from the extracted release archive, not the Git checkout.

| Command/path | Result | Evidence meaning |
|---|---|---|
| `python tools/verify_supplement_manifest.py .` in a fresh extraction | `790/790`, all failure counters zero | HASH PASS, including reverse coverage |
| `python -m pytest -q tests/test_larger_polygon_logical_closure.py` | `3 passed in 0.01s` | REGRESSION PASS only |
| `python experiments/larger_polygon_program/logical_coverage_audit.py` | `LARGE_POLYGON_EXCLUDED_BY_LOGICAL_BRANCH_CERTIFICATES`; support `61/125`; 302 equations; exhaustive `V(c)`/`D(c)` split | Exact logical/hash audit of frozen terminal records; not their expansion |
| `python experiments/larger_polygon_program/global_degree_bound_audit.py --skip-small-recompute` | `GLOBAL_DEGREE_BOUND_125`; source hashes pass; `recomputed_during_this_run=false` | Conditional composition audit, explicitly consuming frozen smaller result |
| `python -m breakthrough_program.independent_verifier` | exit 0 in 0.54 s; five degree-21 passport orbits, `A_21` witness, smaller terminal `['1']`, ranks, positive control | Independent enumeration/check implementation, but some terminal data are frozen inputs |
| `Singular -q results/belyi_edge_Q_fglm.sing` | exit 0 in 6.22 s wall; 7 generators, GB size 56, dimension 0, vector-space dimension 35, lex GB size 6; six degree-35 univariates | EXACT characteristic-zero from-scratch edge/FGLM replay |

The FGLM run emitted only harmless loop-variable redefinition warnings.  Its
six univariate lex elements all had degree 35 and an irreducible degree-35
factor, agreeing with the declared edge field.

The historical reproduction note asks for a missing wrapper
`experiments/larger_polygon_program/verify_row_split_branch_identities.sing`
(`REPRODUCE_SUBRESULTANT_BRANCH_CLOSURE.md:57-73`).  The serialized object that
wrapper would consume does exist as
`results/larger_polygon_program/row_split_branches_exact.sing`.  A minimal
read-only Singular harness loaded that object and checked exact zero remainders:

```text
b2*p0-a2*r7-(D*Y+E) == 0       PASS
b2*Q0-a2*Q7 == 0               PASS
```

This independently closes the two advertised row-split polynomial identities,
including the load-bearing exhaustive split
`b2*p0-a2*r7=D*Y+E` used in the authoritative guide
(`REPRODUCE_LARGER_POLYGON.md:105-127`).  It does not expand the later terminal
certificates on each branch.

**Unexecuted Guo terminal paths — GAP, not FAIL.**  Neither `sage` nor `docker`
was installed.  I therefore did not run:

- the primary and independent Sage lift checks for the smaller configuration;
- the Sage reconstruction binding the `61/125` coefficient system through all
  302 equations to the six row-split generators;
- the two 72 MB exceptional-chart unit-identity verifiers;
- the `D!=0` degree-18 denominator/divisibility/determinant checks; or
- the `D=E=0` factorwise terminal checks.

These files are present and covered by the passing authoritative manifest; the
logical audit validates their frozen hashes and status fields.  That is strong
artifact consistency, but it is not a substitute for exact expansion.  A
future replay should use the pinned 30 GB Sage image and the commands in
`REPRODUCE_LARGER_POLYGON.md:46-127`, without force-recomputing the optional
high-degree discovery intermediates.

A second stale historical wrapper,
`experiments/larger_polygon_program/verify_exceptional_unit_certificate.sing`,
refers to a non-distributed
`results/larger_polygon_program/exceptional_subresultant_unit_certificate.sing`.
The authoritative guide uses the present Sage/JSON verifier pair instead.  Both
missing-wrapper defects should be fixed upstream, but neither changes a
polynomial identity or the top-level manifest.

## 5. Exact mathematical and coordinate crosswalk

### 5.1 Same polygons, support semantics, and bracket

An independent integer cross-product enumeration of lattice points in each
closed polygon returned:

| Configuration | `P` lattice points | `Q` lattice points |
|---|---:|---:|
| larger / Case I | 61 | 125 |
| smaller / Case II | 25 | 47 |

The vertices in both new artifacts are literal matches for
`jc72108/CROSSCHECK.md:10-16`.  Both require the displayed Newton polygons,
hence nonzero displayed vertex coefficients, and both use
`[P,Q]=P_x Q_y-P_y Q_x=x^2`.  This is mathematical object identity, not merely
agreement of final verdicts.

### 5.2 Literal Laurent-coordinate equivalence

SuperMind sets

```text
t_SM = x*y^2
P = y^-2 A(t_SM) + y^-1 C(t_SM) + D(t_SM)
Q = y^-3 B(t_SM) + y^-2 E(t_SM) + y^-1 F(t_SM) + G(t_SM)
```

(`sections/03-layer-equations.tex:7-18,40-68`).  Guo sets

```text
z_G = x*y^2,  t_G = y^-1
P = A(z_G)t_G^2 + B(z_G)t_G + C(z_G)
Q = D(z_G)t_G^3 + E(z_G)t_G^2 + F(z_G)t_G + G(z_G)
```

(`paper/raising_degree_bound_125.tex:200-250`).  The exact rename is

```text
t_SM = z_G,  y^-1 = t_G,
(A,C,D,B,E,F,G)_SM = (A,B,C,D,E,F,G)_Guo.
```

Under it, all five displayed differential identities agree term for term.  The
same monomial-lattice transformation has determinant `-1`, so this is a
lossless coordinate equivalence, not a projection or generic-chart comparison.

### 5.3 Exact common degree-five field

SuperMind and Guo both reduce the common first layer to

```text
f(T) = T^5 - T^4 - 9*T^3 + T^2 + 24*T - 18.
```

The formula is identical in the two artifacts.  Over `QQ`, SymPy 1.14's exact
`field_isomorphism(..., fast=False)` and an independent substitution/remainder
check gave the following.

For Helali's

```text
h(w) = w^5 - w^4 + 3*w^3 + 3*w^2 + 26,
```

the image

```text
T -> (w^4 + 3*w^2 - 2*w + 6)/8
```

satisfies `f(T) mod h(w) = 0` exactly.  The compact JSON coefficient vector
`["1/8","0","3/8","-1/4","3/4"]` has SHA-256
`db0309143fe13954dcf41d30d5bb0e5a562b6ad1ac459516a88573d3109750b1`.

For Suzuki's quintic

```text
M(X) = 60579126468209266677769*X^5
     - 80998237342608310849530*X^4
     + 43543902955657595554476*X^3
     - 11765268269898790599288*X^2
     + 1597839837356041961472*X
     - 87271593441390231552,
```

the returned degree-four rational image also gives exact zero remainder.  In
falling powers of a root of `M`, its compact JSON coefficient vector has
SHA-256
`488e93978579cb4b1050cf491dc7dcef07bcf75159aca946733e4014550273b2`.
The vector is:

```text
[-197627295269076150723541891287444581218436926200939356087365687/625250110088070719519295375078702500553039990872950431744,
  230841791810962865094385013871927899017402350696626142738679/930431711440581427856094308152831102013452367370461952,
 -21873228781725308229386101721223737405305708090739951267683/354450175786888162992797831677268991243219949474461696,
  5333624183675254529629786916953996548602505415773381601/1406548316614635567431737427290749965250872815374848,
  108140653984420892164529310652276274523072462217151/392452097269708584662873166096749432268658709647]
```

All three defining quintics are irreducible of degree five and have one real
root in the embeddings used for the calculation.  This proves field
isomorphism for the audited objects; it does not by itself identify every
normalized coefficient tuple or terminal ideal across the papers.

### 5.4 Terminal mechanisms: related inputs, different certificates

| Support | SuperMind | Guo | Existing Helali/Suzuki/Roy crosswalk |
|---|---|---|---|
| Smaller | Exact row reduction over the common quintic, ending in a Bézout identity between two quartics | Five dessins, degree-35 edge field, layered lift, terminal compatibility unit ideal | Suzuki shares the five-dessin/quintic lineage; Helali uses a degree-35 field and exact unit identity |
| Larger | Square relation; closed/open chart split; closed exact lift; 52-dimensional open core and mod-67 full-rank determinant witness | `V(c)` / `D(c)` and then `D!=0` / `D=E=0`; factorwise subresultants and fixed 11x11 Sylvester determinant | Helali uses `s=+/-c`, an exact `h=sum T_i E_i`, and involution; Suzuki uses weighted descent and a fixed Macaulay minor |

No coefficient-level isomorphism between the two new **terminal** certificate
systems was established.  Different terminal mechanisms are real evidence
against literal duplication, but they do not make the whole derivations
independent because the reduction, edge object, and first-layer field are
shared.

## 6. Correctness, coordinate equivalence, and lineage are separate

### Mathematical correctness

- **SuperMind:** exact terminal replay pass, subject to exact-CAS trust and the
  uncompleted Python regeneration edge stated above.  No incorrect finite
  identity was found.
- **Guo:** every locally run exact identity and audit passed, and the release is
  dependency-complete by its authoritative manifest.  Because the Sage-only
  terminal identities were not expanded here, the strongest honest label is
  **partial exact replay with gaps**, not a full independent validation and not
  a failure.
- **Campaign consequence:** Helali and Suzuki already provide separately
  documented full exact replays of both systems
  (`jc72108/CROSSCHECK.md:90-172`).  The new intake finds no conflict with them.

### Coordinate equivalence

The polygon systems and Laurent differential systems are exactly equivalent by
the explicit rename in section 5.2.  The degree-five fields are exactly
isomorphic by section 5.3.  These are proved mathematical equivalences.

### Social and derivational lineage

- SuperMind's paper is dated August 3 and its repository pin August 5.  Guo's
  theorem core is August 9 and public release August 10.
- Neither artifact cites the other, Helali, Suzuki, or Roy.  Both cite the
  campaign/Santibáñez-Leal.  SuperMind's ratto3423 bibliography entry is wrong:
  `references.bib:88-96` points to answer `513458` (Eremenko); ratto3423's
  answer is `513493`.  This is a citation/provenance defect, not a mathematical
  defect.
- A SHA-256 inventory join found zero byte-identical non-PDF source files
  between the complete SuperMind degree-125 package and Guo release archive.
  That rules out literal file copying at the compared commits, not conceptual
  or model-mediated derivation.
- SuperMind discloses GPT-5.6-Sol Max; Guo discloses OpenAI Codex.  Same-family
  model assistance, the common degree-21 object, and the already public
  Suzuki--Roy quintic core create correlated discovery channels.
- The campaign's Roy assessment (`xmodel/grok-vanrijn.md:31-46,54-66`) treats
  Roy's August 1 closure as a structural reconstruction of the Helali line plus
  a Proposition-4.3 checker, not a clean new theorem lineage.  This intake finds
  no basis to revise that distinction.

**Lineage verdict:** both new repositories are genuine artifacts with distinct
terminal presentations, but an “independent proof count” is not currently
defensible.  Record separate correctness edges, exact-coordinate-equivalence
edges, and unresolved social/derivational edges in any future lineage DAG.

## 7. Optional degree-4 residue-A comparison

The primary replay/crosswalk was already decided, so only the cheapest exact
test was run.  For

```text
beta(u) = u*(u-2/3)^3 / (u^2-u+1/6)^2
```

exact rational arithmetic gives:

```text
gcd(numerator,denominator) = 1
degree(beta) = 4
numerator - denominator = (4*u-3)/108
numerator(beta') = -(3*u-2)^2*(6*u^2-6*u+1)/486
passport = ((3,1),(2,2),(3,1)); monodromy = A4
```

The shared frontier core has degree 21, passport
`((2^10,1),(3^7),(17,1^4))`, and monodromy `A21`.  The maps are not
Möbius-equivalent, and neither is a nontrivial rational composition of the other
because neither degree divides the other (`4` does not divide `21`, and `21`
does not divide `4`).  The portable connection is only methodological:
passport enumeration followed by exact lift certificates.  No coordinate or
factor relation was found or should be claimed.

## 8. msolve `-g` short-circuit audit

Recursive literal searches of the pinned source trees and Guo release archive
found no msolve executable, library binding, or `-g 2` command.  Both proof
stacks use SymPy/Sage/Singular.

SuperMind is especially explicit: a finite-field unit ideal or a modular
reconstruction marker is not accepted as a terminal (`supplement/README.md:36-40`;
`sections/07-certification-and-scope.tex:40-50`).  Its mod-67 step checks
preservation of a characteristic-zero quotient basis and nonvanishing of one
specified multiplication determinant.  Guo likewise describes its finite-field
calculation as a guarded homomorphic image of a fixed characteristic-zero
determinant (`REPRODUCE_LARGER_POLYGON.md:115-127`), while its unit certificates
are explicit characteristic-zero identities.

Accordingly, neither new artifact is affected by the campaign erratum that an
msolve characteristic-zero `-g` output of `[1]` may be only the first modular
unit basis.  Conversely, these artifacts do not repair any campaign-internal
msolve `[1]` claim by themselves; only their own exact terminal identities and
the already replayed Helali/Suzuki identities may be cited.

## 9. Evidence matrix and hard perimeter

| Claim | Local status | Hard perimeter |
|---|---|---|
| Both artifacts target the campaign's two systems | **EXACT PASS** | Explicit polygons, bracket, counts, and lossless coordinate rename |
| SuperMind smaller terminal | **EXACT REPLAY PASS** | SymPy exact arithmetic / pinned source trust |
| SuperMind larger terminal | **EXACT REPLAY PASS** | Singular exact arithmetic / pinned Singular-input trust; full Python input regeneration capped |
| Guo archive completeness | **HASH PASS** | Authoritative 790-file v2.1 manifest; historical overlay manifests intentionally differ |
| Guo degree-21 edge and FGLM | **EXACT REPLAY PASS** | Exact Singular/Python paths run locally |
| Guo full smaller exclusion | **PARTIAL PASS / GAP** | Frozen primary+independent outputs hash-bound; Sage lift verifiers not run locally |
| Guo full larger exclusion | **PARTIAL PASS / GAP** | Logical split and row identities pass; Sage expansion of all branch certificates not run locally |
| Helali/Suzuki/SuperMind/Guo common degree-five field | **EXACT PASS** | Exact field embeddings; does not identify every terminal ideal |
| New artifacts are socially/derivationally independent | **UNRESOLVED** | Different bytes/methods are insufficient; shared input/model lineage remains |
| Both residual supports are empty | **STRONGLY SUPPORTED** | SuperMind terminal replay plus pre-existing full Helali/Suzuki replays; exact-CAS and transcription trust |
| Every `(72,108)` counterexample is excluded | **CONDITIONAL** | Requires the cited GGV Proposition-4.3 reduction/normalization/transcription bridge |
| Every counterexample has maximum degree at least 125 | **CONDITIONAL** | Also requires the cited GGV small-degree theorem |
| Plane Jacobian conjecture | **NO IMPLICATION** | Degrees 125 and above remain open |

The two new artifacts themselves state much of this perimeter.  SuperMind says
its supplement does not reprove the upstream GGV reduction and does not prove
JC (`supplement/README.md:6-12`); Guo labels the degree bound a dependency-bearing
corollary and the manuscript unreviewed (`README.md:22-28`,
`PUBLIC_RELEASE_NOTES.md:29-43`).  SuperMind's phrase “unconditional once the
cited reduction ... [is] accepted” (`sections/07-certification-and-scope.tex:79-89`)
should be represented in campaign prose as **conditional on that reduction and
the transcription/normalization bridge**.

## 10. Recommended campaign actions

1. **Promote the SuperMind terminal replay as an exact external confirmation,
   with its regeneration edge disclosed.**  Do not spend more compute on its
   optional direct standard-basis paths; the registered bounded gate is already
   decisive.
2. **Close Guo's replay gap once, in the pinned container.**  Run only the fast
   theorem paths in `REPRODUCE_LARGER_POLYGON.md`, with the documented 30 GB
   bound.  Preserve fresh pre-run manifest verification separately from the
   replay-mutated tree.  Do not launch optional resultant rediscovery jobs.
3. **Record the exact field embeddings.**  They replace the old 300-prime
   factor-shape comparison for these quintics and provide a canonical key for a
   future certificate-lineage graph.
4. **Use a three-edge provenance vocabulary:** mathematical correctness,
   coordinate/field equivalence, and social/derivational lineage.  Never infer
   the third from the first two, or independent-vote counts from repository
   counts.
5. **Report upstream packaging defects.**  SuperMind should correct answer
   `513458` to `513493`; Guo should add or remove the two stale Singular wrapper
   references and make the inner checksum file LF-portable.
6. **Keep the public theorem perimeter unchanged.**  The safe campaign statement
   is: exact external certificates exclude both Proposition-4.3 residual
   systems; therefore the `(72,108)` case and the degree-125 lower-bound
   consequence hold conditional on the cited GGV reduction/transcription
   bridge.  No number of these finite-system replications proves JC2.
