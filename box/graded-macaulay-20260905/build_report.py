#!/usr/bin/env python3
from pathlib import Path
import json,hashlib,datetime,sys
BASE=Path('box/graded-macaulay-20260905')
OUT=Path('xmodel/graded-macaulay-astra-20260905.md') if '--seal' in sys.argv else BASE/'report-draft.md'
A={x['parameters']:x for x in json.loads((BASE/'counts/ambient-counts.json').read_text())['fibres']}
R={n:json.loads((BASE/f'reduced/{n}/reduced-counts.json').read_text()) for n in (77,111,129,136)}
N=(77,111,129,136)
parts=[]
def add(s):parts.append(s.strip()+'\n\n')
def table(headers,rows):
 add('| '+' | '.join(headers)+' |\n|'+'|'.join(['---']*len(headers))+'|\n'+'\n'.join('| '+' | '.join(map(str,r))+' |' for r in rows))
def num(v):return f'{v:,}'
add('''**Graded Macaulay computation — Astra — 2026-09-05**

**Disposition: exact N=2,3 sizes are computed for all four full fibres and the licensed s′=4 control. Every requested target matrix exceeds the proposed 10⁷-column threshold, including after a proved minimal-variable polynomial presentation. The smallest reduced N=2 matrix has 6,782,152,172 columns. Exact rational sparse linear algebra supplies full-ideal Hilbert truncations in smaller degrees; target ranks, c²/c³ membership, and class emptiness remain OPEN. Zero class kills are certified. No Gröbner basis was computed and no fleet instance was launched.**''')
add('''**Custody and scope.** Work began at 15:19:17 UTC, with receipt basis `4536d3fff7d8a13898168dbe430d163b1a0be731`. Before reading charged mathematical contents, awk joined the six numbered `charged_input_<i>_sha256` and `_basename` fields of `xmodel/graded-macaulay-astra-20260905.run.v2`; `sha256sum -c` returned six OK results against `/tmp/jc2-lane.f1FF7T/inputs/`. The first manifest write into the frozen directory was rejected as read-only; moving only the manifest into this lane succeeded. There was no content mismatch. `inputs.sha256` and `inputs-check.log` retain the receipt-derived manifest and check. All abbreviated artifact paths below are relative to `box/graded-macaulay-20260905/`.

The consumable family remains `box/moh14-charts-20260905/hsupport-gate-20260905/source-complete/classes/`, with independent union supports D_i∪G_i, β₁=0, and the stated terminal constant gauges. The JSON outputs bind source/metadata hashes, ring and generator orders, and degrees. No source parameter is specialized in the new full-ideal computations.

The gate §8 permits a class kill only after an actual exact-Q UNIT or rational original-ring identity on one completed fibre, using its common G_i embedding. This lane consumes that source-support theorem and the frozen census/descent dependencies; it does not re-prove or strengthen them. The closeout’s remaining named source obligations are not silently discharged by these counts. No new exit-price assertion is made, so no charge_basis line is due. No ledger, jc2-lean, or ideation file was edited.''')
add('''**Four rings and the target degrees.** Write B(z)=b, w(z)=iK−a, p=ℓ+1, D=n+m−1, C=(p,D). Variables include c, with degree C, and exclude the inverse variable T. The first charge negates the earlier signed convention. The source Jacobian ordering is the audited native Q,P ordering. Switching to P,Q changes c’s sign, which must also be reflected in any identity. We preserve the native target equation F−c throughout.''')
table(['Parameters','Completed fibre M/V','K','(p,D)','δ₂','δ₃','Direct generators'],[
[77,'m12_m2_5/V1_1_6, s′=4',8,'(2,39)','(4,78)','(6,117)',150],
[111,'2_9/V3_8',6,'(3,29)','(6,58)','(9,87)',167],
[129,'m15_14/V1_9',6,'(2,41)','(4,82)','(6,123)',177],
[136,'2_9/V1_8',6,'(3,29)','(6,58)','(9,87)',348]])
add('''Direct rows mean every ordinary x,y coefficient of the audited completed Jacobian. Their ideal agrees with the native h-adic coefficient ideal by the invertible monic triangular coefficient transformation established in the frozen report. The 77 fibre IS the s′=4 control; it is not an additional fifth fibre. Its licensed alternate native list has 425 rows and SHA-256 `af3cf058c7e949d7e9958b1c9120b9350436c6eca7a952afbc8ea32f9794ef58`. The builder-identity custody is inherited and checked against the gate’s actual union control. Header-only files are never counted as empty ideals.''')
add('''**Finite linear system and exact counting method.** For a coefficient row g at native position (j,b,a), deg(g)=(b+1,D−a−jK). Every monomial multiple of that degree contributes one generated row. Set

    h(X,Y) = [u^X v^Y] ∏_(z including c) (1−u^B(z) v^w(z))^(−1),
    columns(M_(X,Y)) = h(X,Y),
    generated_rows(M_(X,Y)) = Σ_g h(X−B(g),Y−w(g)).

A negative complementary coordinate contributes zero. The count is by the declared ordered generator presentation: dependent or repeated rows are still rows. Within each row, distinct original terms remain distinct after monomial multiplication, so the exact sparse input nnz count is Σ_g size(g)·h(δ−deg(g)). It is an input count, not a rank or a prediction of elimination fill.

The variable-by-variable unbounded-knapsack recurrence starts at h(0,0)=1 and adds h(X−B(z),Y−w(z)) in increasing indices. Its integers have arbitrary precision. An independent grouped convolution uses the coefficient binomial(k+t−1,t) for t copies of a degree occurring k times. These methods agree at EVERY entry of the rectangles through 3C, not merely the target entries. The count driver also verifies 1,618 source rows and 2,357,809 distinct nonzero terms across all counted presentations. N=1 reproduces 67,177,159 / 5,667,097 / 31,667,827 / 24,153,138 original columns in fibre order.

Bihomogeneity gives c^N∈I exactly when its vector lies in this row space. All omitted higher-degree rows or variables have no monomial capable of reaching δ_N; omission from a component assigns them no value. This is the complete original-ideal degree block, rather than a parameter specialization.''')
rows=[]
for n in N:
 pr=next(x for x in A[n]['presentations'] if x['name']=='direct')
 for t in pr['powers'][1:]:rows.append([n,t['N'],str(tuple(t['delta'])),num(t['columns']),num(t['rows']),num(t['nonzero_entries'])])
table(['Fibre','N','δ_N','Columns','Generated rows','Input nonzeros'],rows)
add('''The number of direct generators with a nonzero multiplier component at N=2/N=3 is respectively 141/150, 135/164, 123/159, and 171/252. Merely testing componentwise degree inequalities can overcount active generators: some nonnegative complementary bidegrees contain no monomial. Every source contribution and complementary degree is retained in `counts/ambient-counts.json`.

The native presentation changes generated row counts while preserving the row space and column space. Its alternate counts are below; columns are exactly those in the preceding table for the same fibre and N. The 425-row control is therefore explicitly counted in its own preserved presentation, not replaced silently by the 150-row direct list.''')
rows=[]
for n in (77,111,129):
 for pr in A[n]['presentations']:
  if pr['name']=='direct':continue
  for t in pr['powers'][1:]:rows.append([n,pr['generators'],t['N'],num(t['rows']),num(t['nonzero_entries'])])
table(['Fibre','Native generators','N','Generated rows','Input nonzeros'],rows)
add('''**Exact N-independent elimination and minimal number of variables.** The phrase “charge-zero eliminations” needs correction. All 27/71 frozen unit pivots have B>0. Every generator has B≥1, hence I_(0,Y)=0 for every Y: no nonzero homogeneous relation can eliminate a B=0 coordinate. The 38/28/40/28 charge-zero coordinates remain a free polynomial subalgebra. Also no non-c coordinate has residual torus character pw−DB equal to zero, since gcd(p,D)=1 and 1≤w≤n<D.

Fresh full-row processing finds every positive-charge A coordinate as a constant-unit pivot. There are 27/57/57/71 such coordinates. For each ordered source equation q_j a_j+P_j=0, q_j∈Q*, the driver verifies that a_j occurs exactly once and every other pivot dependency precedes it. It defines φ(a_j)=−φ(P_j)/q_j, fixing all remaining variables and c. Each equation is homogeneous and every image vanishes at the origin. The recursive map and the inclusion of remaining coordinates into the quotient are inverse algebra maps. Imposing the images of ALL remaining source rows therefore gives the full chart quotient, with no localization or discarded branch.

The frozen 111/129 lists of 42/37 pivots include c and came from N=1 selected rings. Their counts remain in `counts/reduced-ambient-counts.json`. The full positive-A lists here are stronger; 77/136 reproduce the frozen 27/71 lists.

After removing pivot rows, additional identically zero source images number 3/3/0/11. The surviving ordered image lists have 120/107/120/266 nonzero generators. To establish those numbers without expanding enormous nonzero polynomials, the driver evaluates the recursive rational map at two recorded finite-field points, using p=1073741827. A NONZERO value certifies that the rational polynomial is nonzero; this is not modular ideal-membership promotion. Every remaining zero candidate is composed and checked exactly with FLINT rational multivariate polynomials. The source indices, pivot equations, all point values, residues, and exact zero indices are retained in `reduced/<fibre>/reduced-counts.json`. Independent audit confirms the source-index/position correspondence.

One further global unit equation is φ(F)−c. Eliminate c and write S=Q[u] and J for the images of all other rows. Then R/I≅S/J as bigraded Q-algebras, c maps to F̄=φ(F), and the target becomes F̄^N∈J. This is the smallest possible number of polynomial coordinates for the FULL affine algebra, not just a convenient reduction: the independent exact Fraction audit computes the original linear-part ranks, verifies all residual linear parts vanish, and obtains the cotangent dimensions at the rational origin. Any presentation by s polynomial generators induces a surjection Q^s→𝔪/𝔪², so s must be at least that dimension. Our presentations attain the bound.''')
table(['Fibre','A pivots','Linear rank incl c','Coordinates retaining c','Minimal coordinates after c','Nonzero generators of J'],[[n,R[n]['pivot_count'],R[n]['pivot_count']+1,len(R[n]['remaining_variables']),len(R[n]['remaining_variables'])-1,R[n]['nonzero_reduced_generator_count']-1] for n in N])
add('''Minimality here concerns polynomial generators of the full affine Q-algebra. It is not a Krull-dimension assertion and does not bound coordinate counts after localization or on the c=1 section. The generators of J are the ordered nonzero source images; no claim of a minimal ideal-generating list is made. `audit/minimality.json` independently verifies ranks 28/58/58/72 and cotangent dimensions 49/53/71/64 using all 842 direct rows.

Let h_A count the A-pivot quotient with c retained and h_S count the c-free polynomial ring. The exact identity h_S(X,Y)=h_A(X,Y)−h_A(X−p,Y−D) holds throughout every computed rectangle. Applying the same generator×complement rule gives:''')
rows=[]
for n in N:
 for t in R[n]['tests'][1:]:rows.append([n,t['N'],num(t['columns']),num(t['rows']),num(t['c_eliminated_columns']),num(t['c_eliminated_rows'])])
table(['Fibre','N','Columns, c retained','Rows, c retained','Columns in minimal S','Rows for J'],rows)
add('''`counts/independent-reduced-check.json` checks all 2,004 source contributions and both dynamic programs throughout the reduced rectangles. Reduced expansion can enlarge row support; original term counts cannot estimate its sparse storage.''')
add('''**The torus section is valid but does not make this finite block smaller by itself.** Setting c=1 identifies the nonzero-c localization with its section times G_m, as proved in the frozen report. On the vector space R_(NC), however, the substitution c↦1 is INJECTIVE. A z-monomial has at most one exponent j making z^α c^j have degree NC. Its image is precisely

    ⊕_(k=0)^N Q[z]_(kC).

Thus the finite section window has exactly the same column count as the homogeneous block, and the target maps to 1. The inherited row images must be kept within this window. If A₀p+B₀D=1, the window is residual character zero with 0≤k=A₀B(z^α)+B₀w(z^α)≤N. Residual character zero alone is infinite-dimensional: there are positive and negative residual weights, whose monomials supply a nonconstant character-zero monomial and all its powers. Dropping the finite window changes the fixed-N question.

The minimal S presentation uses c=F̄ and preserves the bigrading. A section UNIT needs rational lifting and homogenization to certify an exponent. Setting charge-zero coordinates to zero or t^w is a specialization, not a chart isomorphism.''')
add('''**Which degree pieces vanish, and exact Hilbert information.** There is a complete N-independent answer for vanishing of the IDEAL pieces. For nonnegative integers (B,Y),

    I_(B,Y)=0 ⇔ B=0 or Y<λ(B),
    λ_77(B)=B; λ_111(B)=2B;
    λ_129(B)=ceil(13B/3); λ_136(B)=ceil(B/3).

All variable and generator degrees satisfy the displayed lower slope inequalities. For the converse, `hilbert/global_support_vanishing.json` supplies nonzero original generators in the necessary residue classes, a period variable, and a degree-(0,1) coordinate. Multiplying a residue generator by powers of the period coordinate and the (0,1) coordinate constructs a nonzero element of every claimed nonzero ideal piece; the original polynomial ring is a domain. Thus this is an exact support theorem for I, not an extrapolation from a finite numerical table. The corresponding ring component is zero below λ(B); where I_(B,Y)=0, the full quotient Hilbert value equals the ambient count.

In particular, H_(R/I)(0,Y) is exactly the coefficient of v^Y in ∏_(B(z)=0)(1−v^w(z))^−1. At the target second weights, these FULL quotient values are:''')
HA={d['fibre']:d for d in json.loads((BASE/'audit/hilbert-audit.json').read_text())['fibres']}
table(['Fibre','H(0,D)','H(0,2D)','H(0,3D)'],[[n]+[num(x['dimension']) for x in HA[n]['full_R_mod_I_charge_zero_H']] for n in N])
add('''They refer to first charge zero, not to NC. These permanent polynomial directions prohibit any Artinian top-degree shortcut. Also every row of w<D is c-free and is satisfied by z=0,c=1. A strict-low-weight subsystem therefore cannot force c to vanish; if full forcing occurs, the minimum equation-weight threshold is D. Neither fact decides a higher c power.''')
H={}
for n in N:
 fs=list((BASE/'hilbert').glob(f'hilbert_{n}_B*_Y*.json'))
 f=max(fs,key=lambda p:int(p.stem.split('_Y')[1]));H[n]=json.loads(f.read_text())
add('''**New full-ideal sparse linear algebra.** `hilbert/compute_hilbert.py` constructs finite original-ring Macaulay blocks, keeping every eligible original generator and multiplier, and computes their exact rational ranks with primitive integer Gaussian elimination. Integer cross-multiplication and gcd normalization preserve the rational row span. An independent modular pass uses p=1073741827. No critical-pair completion, polynomial leading-ideal substitution, or Gröbner algorithm is involved.

The exact cutoffs and completion counts are below. All cells are complete, with no component skipped by the configured column cap. Direct rational and modular ranks agree; exactness comes from rational arithmetic. One final cell is derived through the homogeneous unit quotient, as detailed below.''')
table(['Fibre','B range','Y range','Completed components','Elapsed seconds'],[[n,f"0…{H[n]['max_b']}",f"0…{H[n]['max_y']}",len(H[n]['components']),H[n]['total_elapsed_seconds']] for n in N])
rows=[]
for n,b in [(77,2),(77,4),(111,3),(111,6),(129,2),(129,3),(136,3),(136,6)]:
 y=H[n]['max_y'];t=next(x for x in H[n]['components'] if x['B']==b and x['Y']==y)
 assert t['status'] in ('EXACT_Q','EXACT_Q_VIA_HOMOGENEOUS_UNIT_MAP');rows.append([n,str((b,y)),num(t['columns']),num(t['rows']),num(t['rank_Q']),num(t['hilbert_Q'])])
table(['Fibre','(B,Y)','Columns','Rows','Exact rank','H_(R/I)(B,Y)'],rows)
add('''For 136 at (6,12), the exact unit quotient has 8,765 columns, 5,554 rows and rank 4,945, hence H=3,820 and original rank 80,415−3,820=76,595. Its (5,12) value H=4,446 independently matches the completed direct calculation. The redundant original (6,12) run was stopped only after this proof; its partial echelon is unused. This final cell is typed EXACT_Q_VIA_HOMOGENEOUS_UNIT_MAP, not an invented original matrix completion.

The JSON files give full rectangular Hilbert tables, source hashes, computation-specific matrix/echelon hashes, pivot counts, and timings. All 718,633 terms in the four original direct files were freshly rechecked for degree and nonzero coefficients before constructing these matrices. Independent FLINT fmpq_mat/nmod_mat calculations reproduce four actual chart blocks and 100 deterministic random-matrix controls. Rational-combination replay passes a positive membership control; ordinary negative membership, a bad-prime false NO, and a bad-prime false YES are also checked.

These low-degree computations do not reach δ₂ or δ₃. No full target rank or exact target Hilbert value is claimed. The reduced counts do give rigorous intervals, since H_(S/J)(δ)=columns−rank and 0≤rank≤rows. The following lower bounds are arithmetic consequences of the c-free full presentation, rather than guessed Hilbert series:''')
rows=[]
for n in N:
 for t in R[n]['tests'][1:]:
  c=t['c_eliminated_columns'];r=t['c_eliminated_rows'];rows.append([n,t['N'],num(max(0,c-r)),num(c),'OPEN'])
table(['Fibre','N','H(NC) lower bound','H(NC) upper bound','Exact value'],rows)
add('''A positive Hilbert dimension in a target component would not imply that its particular vector c^N survives. Conversely, an ambient column count is never a quotient Hilbert value. The bounds above respect that distinction.

The frozen exact N=1 witness algebras can be counted as well. Rechecking their custody and standard monomials gives witness dimensions at C of 1/2/21/2, with ambient receiver counts 448/190/605/206. Their total graded maps imply only H_(R/I)(C)≥1/2/21/2; the saved normal forms of c separately prove c∉I as already frozen. Those finite receivers have zero pieces at 2C and 3C because of their overflow cutoffs. Such zeros are NOT H_(R/I)(2C) or H_(R/I)(3C), and they prove no original membership. `audit/hilbert-audit.json` explicitly distinguishes these quantities. No old timeout or specialized zero remainder is promoted.''')
add('''**Modular verdicts and the certificate boundary.** For the requested N=2,3 blocks, no modular membership test was executed: even the minimal ring exceeds the stated feasibility threshold. There is therefore no modular YES, modular NO, or rational c-power identity to promote.

For a future finite block M and target e, an unrestricted modular NO is not automatically exact. Clearing original coefficient denominators is insufficient. For example, take the primitive integer rows (1,1) and (1,1+p), and e=(1,0). Over Q the two rows span everything; modulo p they coincide and miss e. The exceptional prime destroys rank despite primitive rows and integral entries. A modular YES is likewise only a signal: the single row (1,p) contains e modulo p and does not contain it over Q.

The correct good-prime negative implication is conditional. Certify rank_Q(M)=rank_Fp(M)=r, for example using a modular nonzero r-minor for the lower bound together with an exact rational row factorization for the upper bound. If rank_Fp([M;e])=r+1, the augmented nonzero minor survives over Q and exact nonmembership follows. Equivalently, verify an exact rational separating vector v with Mv=0 and ev≠0. Agreement over several primes alone supplies no rational rank upper bound. Membership over Q reduces modulo every prime avoiding the denominators of a valid rational solution, but an unknown solution’s exceptional primes cannot be excluded by assertion.

For a positive signal, solve on identified support over Q or reconstruct with CRT, then multiply out the ORIGINAL full-ring identity Σ a_i g_i=c^N. If elimination was used, include the rational-unit pivot identities when transporting it back. If c=1 was used, homogeneous lifting must first give nonnegative c exponents. From an actually verified original c-power identity one obtains

    1 = Σ_i T^N a_i g_i − (Tc−1) Σ_(k=0)^(N−1) (Tc)^k.

Only that exact full-ring identity, with the completed source custody, supplies the requested gate §8 class kill. No saturation in an x-charge overflow ring is admissible: c becomes nilpotent there by construction, so adjoining Tc−1 always creates a false UNIT even for I=0. Projection onto the target degree can justify a lifted membership calculation, but the original identity must still be checked.''')
add('''**Feasibility and operational disposition.** The explicit direct N=2 input for the 77 fibre has 578,249,602,766,164 nonzeros. Even a compact representation with four-byte values and eight-byte column indices needs more than 6.9 petabytes for its entries, before row pointers and elimination fill. After the minimal exact coordinate reduction, the smallest N=2 block is still about 678 times the requested 10⁷-column ceiling. This is an explicit matrix-size obstruction, not a Gröbner timeout, a rank conclusion, or a theorem excluding a future compressed algorithm.

Counts and the exact small blocks ran locally on the existing approximately 123 GiB host. The root reduction driver finished the four full unit-map audits/counts in about 17 seconds total; it expands only exact-zero candidates. Additional RAM was not required. Consequently the conditional fleet launch was not triggered: this lane owns no worker to terminate and touched no other worker. No msolve, Singular basis command, or guided_gb invocation was made. FLINT 0.9.0 was loaded read-only from the existing Python package directory; it was used for rational polynomial composition and matrix verification, not Gröbner computation.

All new drivers, outputs, exact maps, per-generator contributions, run records, and checksum manifests are confined to this lane directory; the sole report is the requested xmodel path. `run-status.json` records final local-job and fleet dispositions. `artifacts.sha256` binds the final lane artifacts and is mechanically checked before sealing. The frozen input manifest is checked again at closeout. No partial target matrix is labeled a completed test.''')
add('''**Reproduction and final typed result.** Run from the repository root:

    python3 box/graded-macaulay-20260905/counts/exact_counts.py
    python3 box/graded-macaulay-20260905/reduced/reduce_counts.py
    python3 box/graded-macaulay-20260905/counts/check_root_reduced.py
    python3 box/graded-macaulay-20260905/audit/audit_minimality.py
    python3 box/graded-macaulay-20260905/hilbert/verify_support.py

The exact Hilbert commands and independently checked linear-algebra controls are retained with their final status records under `hilbert/`; each command preserves the full declared ring and all eligible original rows. `build_report.py` inserts numerical tables directly from the checked JSON results.

Completed: exact original/native/reduced N=2,3 column and row counts; minimal full-affine coordinate presentation; exact ideal support-vanishing theorem; full-ideal rational Hilbert truncations; careful finite torus-section interpretation; complete input/map/artifact custody. **OPEN[c²∈I], OPEN[c³∈I], and OPEN[c∈√I] remain on all four fibres. Exact target Hilbert values remain OPEN. Zero class kills; no ledger promotion.**''')
now=datetime.datetime.now(datetime.timezone.utc)
add(f'Operational closeout time: {now:%Y-%m-%d %H:%M:%S} UTC, within the 180-minute limit measured from 15:19:17 UTC.')
body=''.join(parts)+'<!-- BODY-END -->\n'
assert 12000<=len(body.encode())<=25000,len(body.encode())
seal=f'\nSeal (outside the body):\n\n- Body: every byte through the unique standalone BODY-END marker and its terminating newline.\n- Body bytes: `{len(body.encode())}`.\n- Body SHA-256: `{hashlib.sha256(body.encode()).hexdigest()}`.\n- Frozen basis: `4536d3fff7d8a13898168dbe430d163b1a0be731`.\n'
OUT.write_text(body+seal if '--seal' in sys.argv else body)
print(OUT,'body_bytes',len(body.encode()),'file_bytes',OUT.stat().st_size)
