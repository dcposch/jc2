**VERDICT: SOUND — NEVER-VANISHES-PROVED holds on the registered Mondello-hull-plus-one-L1-shell stratum: the unrestricted \(W_2\) class is exactly the odd–odd support of \(E_F\), the written L1 shell has no missing lattice point, and \([xy]E_F=1\) is an identity on the complete four-\(P\) classification (1,152/1,152 nonzero, including all eight odd-degree data).**

Reviewer: Grok 4.6 (hostile referee). Date: 2026-08-14.
Target: `xmodel/sol-witt.md` + `cases/witt_check.py` (GPT-5.6-Sol, Witt/Bockstein lane).
Claim under review: **NEVER-VANISHES-PROVED** — every plane Keller pair on the registered Mondello-hull-plus-one-shell stratum has nonzero unrestricted Cartier–Bockstein class, so none lifts to a determinant-one map over \(\mathbf Z/4\).
Attacks: (1) replay the obstruction / Bockstein arithmetic by hand on one example; (2) stratum registration completeness (hull + one shell — boundary cases; a missed shell element is a hole); (3) never-vanishing proof — structural or exhaustive; (4) scope honesty (stratum-only claim); (5) significance: is this where the char-0-lift hope lived?
Method: independent integer Jacobian of Mondello and of the displayed 48-example; independent barycentric / L1-box / L∞ comparison of both Newton hulls; independent \([xy]\) identity and \((2,2)\) bracket row on all 1,152 registered maps; engine reproduction (`py_compile`, `self-test`, `check` Mondello, `search --degrees`, `relaxed --degrees`, `audit-3d`); two extra censuses not in the writeup (L1-shell with linear jet only; L∞-shell with vertex guards); exact Singular degrees on the 1,024 vanishing maps that keep Mondello's three \(P\)-vertices. Citations checked against Franjou math/0404123, Stacks 0FW2 and 00UP, Mondello 2608.02634v1 §10, Huq–Kuruvilla 2607.20968.
No other repo file modified. No git.

---

## Findings (worst first)

### 1. Severity: note — the original lateral spec did not force core vertices; dropping them on the same L1 shell produces 7,680 vanishing maps, all outside the registered cut

- File: `xmodel/sol-witt.md:304-335,468-520`; `xmodel/sol-lateral.md:84-92`; `cases/witt_check.py:470-474,481-578`
- Claim at risk: “the requested lane is closed on its registered tractable stratum.”
- How checked: `sol-lateral.md` registered “Mondello's two Newton hulls plus one lattice shell” with linear jet, three-point collision, and an odd-generic-degree guard. It did **not** require \(p_{21}=p_{40}=p_{62}=q_{50}=q_{83}=1\). The execution added those five core-vertex bits, then proved never-vanishes on that narrower slice.
- Independent census, same engine primitives, linear jet and collision only, supports \(S_P=(\Delta_P\cap\mathbf N^2)^+\) and \(S_Q=(\Delta_Q\cap\mathbf N^2)^+\):

  | slice | Keller collisions | Cartier zero |
  |---|---:|---:|
  | registered (L1 shell + 5 vertices) | 1,152 | **0** |
  | L1 shell, linear jet, **no** vertex guards | 149,504 | **7,680** |
  | unshelled hulls, no vertex guards (their relaxed control) | 288 | **48** |
  | L∞ shell + 5 vertices (diagonal neighbours they omitted) | 14,080 | **0** |

- Every one of the 7,680 loses at least one registered core vertex (histogram exhausts 7,680 with no \(((),())\) bucket). In particular there is no vanishing map that keeps \(p_{21}=q_{83}=1\). The 1,024 vanishing maps that keep all three \(P\)-vertices (they all lose \(q_{83}\)) have exact generic-degree histogram \(\{4:2,8:3,10:4,12:17,14:18,16:41,18:60,20:93,22:177,24:181,26:60,28:130,30:142,32:72,34:24\}\) — **0 odd**. The filed 48 inside-hull vanishing maps are all even, as claimed (`{4:16, 8:17, 10:4, 12:1, 14:6, 16:4}`), rechecked by `relaxed --degrees`.
- This is not a hole in NEVER-VANISHES-PROVED as stated: the writeup defines the registered stratum to include the vertex guards, flags the 48, and never claims the no-vertex shell is empty of vanishing classes. It *is* the one place the original week-scale search is larger than the proof. The extra vanishing maps are even-degree on every slice whose degree was computed, so they fail the Adjamagbo / odd-degree filter that was part of the original spec. Residual uncomputed slice: the 6,656 vanishing maps that also drop a \(P\)-vertex; many are visibly Artin–Schreier (\(P=x+x^2\), \(P=x+x^4\), 256 each).

### 2. Severity: clear — the obstruction is the complete unrestricted \(W_2\) class; Mondello Bockstein replays by hand

- File: `xmodel/sol-witt.md:162-237,284-298`; `cases/witt_check.py:167-218`
- Claim: \(o_2(F)=[E_F\,dx\wedge dy]\in H^2_{dR}(\mathbf F_2[x,y])\) with \(E_F=([\widetilde P,\widetilde Q]-1)/2\bmod 2\), and this vanishes iff \(E_F\) has no odd–odd monomial. Cartier is complete for unrestricted polynomial corrections.
- How checked (Mondello, no engine import for the expansion):

  \[
  \begin{aligned}
  P_x&=1+2xy+4x^3+6x^5y^2,\\
  P_y&=x^2+2x^6y,\\
  Q_x&=5x^4+6x^5y+7x^6y^2+8x^7y^3,\\
  Q_y&=1+x^6+2x^7y+3x^8y^2.
  \end{aligned}
  \]

  Integer Jacobian:

  \[
  \begin{aligned}
  [P,Q]-1
  &=2xy+4x^3+6x^5y^2-4x^6-2x^7y+4x^9\\
  &\quad-2x^9y^3-2x^{10}y+6x^{11}y^2-2x^{12}y^3+2x^{13}y^4.
  \end{aligned}
  \]

  Halving and reducing mod 2 gives support \(\{(1,1),(5,2),(7,1),(9,3),(10,1),(11,2),(12,3),(13,4)\}\). Odd–odd part \(\{(1,1),(7,1),(9,3)\}\), Cartier image \(1+x^3+x^4y\neq0\). The \(xy\) term is visible without the full expansion: it is \(2xy\) from \(P_x\) times the constant \(1\) in \(Q_y\), and \(P_y Q_x\) starts at degree 6, so \([xy]E_M=1\).
- Completeness: \(L_F(A,B)\,dx\wedge dy=d(A\,dQ-B\,dP)\) is the usual Cartan formula (char-2 signs collapse correctly). Because \([P,Q]=1\), \((A,B)\mapsto A\,dQ-B\,dP\) is an \(R\)-module isomorphism \(R^2\simeq\Omega^1_R\), so \(\operatorname{im}L_F=d\Omega^1_R\) and \(\operatorname{coker}L_F\simeq H^2_{dR}(R)\). In char 2 the latter is spanned by \([x^{2a+1}y^{2b+1}\,dx\wedge dy]\). Every \(\mathbf Z/4\) pair is of the form \((\widetilde P+2A,\widetilde Q+2B)\) with \(A,B\in\mathbf F_2[x,y]\), so the class really is the full unrestricted obstruction, not a support-bounded screen. The engine's primitive / \(A,B\) constructor is the inverse of that isomorphism; it is not needed for nonvanishing, and it does verify on all 48 vanishing controls (independent integer Jacobian of the displayed \(P=x+x^2\), \(Q=y+x^2+x^4y^2\), \(A=x^5y\), \(B=xy\) is \(1+4(\cdots)\)).
- Collision rows add nothing to the cokernel: each \(JF(a_i)\) is invertible, so the marked-point corrections \(u_i\) are unique after \(A,B,v\) are chosen. This is the square-zero lifting property of an étale map (Stacks 00UP / 00UQ). Constructed lifts of the 48-example are \((0,1),(3,0),(1,1)\mapsto(0,1)\), matching the writeup; the same arithmetic on the three Huq–Kuruvilla points \((0,1,0),(1,1,0),(1,1,1)\) produces the displayed mod-4 lifts \((0,1,0),(3,1,0),(3,1,3)\).
- Citations: Franjou Prop. 2 is the Frobenius on integral de Rham cohomology and Thm. 3 identifies Bockstein pages with de Rham mod \(p\) via Cartier; the connecting-class formula \(\partial C^{-1}(\overline\omega)=[dF(\omega)/p^{i+1}]\) in the proof of Thm. 3 is exactly \(d\widetilde\alpha=2E_F\,dx\wedge dy\). Stacks 0FW2 is the relative Cartier/Theta lemma — the affine coefficient rule (trace vanishes unless exponents \(\equiv-1\pmod p\)) lives in its proof, not in the lemma statement. Acceptable, slightly fat.

### 3. Severity: clear — the L1 hull-plus-one-shell registration is complete; no missed shell element

- File: `xmodel/sol-witt.md:302-320`; `cases/witt_check.py:435-468`
- Claim: \(\#(\Delta_P\cap\mathbf N^2)=10\), \(\#(\Delta_Q\cap\mathbf N^2)=18\), one nonnegative Manhattan shell gives 20 and 31; 14 free \(P\)-bits, 26 free \(Q\)-bits.
- How checked: vertices \((0,0),(4,0),(6,2),(2,1)\) and \((0,0),(5,0),(8,3),(0,1)\) are strictly CCW (all four turning cross-products positive). Independent half-plane scan and independent barycentric / shoelace test on the boxes \([0,7]\times[0,4]\) and \([0,9]\times[0,5]\) agree; no miss, no extra. Explicit \(P\)-hull:

  \[
  \{(0,0),(1,0),(2,0),(2,1),(3,0),(3,1),(4,0),(4,1),(5,1),(6,2)\}.
  \]

  Boundary cases that look like holes and are not: \((0,1)\notin\Delta_P\) (fails the \((6,2)\)–\((2,1)\) half-plane) but is L1-adjacent to \((0,0)\), hence in the shell and then killed by the linear jet; \((1,2)\) is at L1-distance 2 from every hull point, hence correctly excluded by the written \(\|\cdot\|_1\le 1\) definition; the edge \((6,2)\)–\((2,1)\) contains no other lattice point; the edge \((5,0)\)–\((8,3)\) contains \((6,1),(7,2)\) and both are in \(\Delta_Q\).
- L1-box scan of \(\{u\in\mathbf N^2:\min_t\|u-t\|_1\le 1\}\) on a generous ambient box reproduces the code's `one_manhattan_shell` exactly (20 and 31). The five L∞-only \(P\)-points \((1,2),(5,3),(6,0),(7,1),(7,3)\) and six L∞-only \(Q\)-points \((3,3),(7,0),(7,4),(8,1),(9,2),(9,4)\) are *not* in the registered definition. Adding them while keeping the five vertex guards still gives 0 vanishing (14,080 Keller collisions). A missed L1 element would have been a hole; these diagonals are not.
- Bit counts: \(|P_{\mathrm{shell}}\setminus P_{\mathrm{fixed}}|=14\), \(|Q_{\mathrm{shell}}\setminus Q_{\mathrm{fixed}}|=26\). Collision-compatible \(P\)-masks \(2^{14}\to 4096\) and the \(2^9+2^9+2^6+2^6=1152\) split both reproduce. Bank SHA-256 `0b2c14602c487418d57adff7d542ae5a3e94e431ad0466b8d25e5c2fffaa701c` (85,504 bytes) recomputes identically.

### 4. Severity: clear — never-vanishing is structural, after an exhaustive four-\(P\) classification

- File: `xmodel/sol-witt.md:396-424`; `cases/witt_check.py:399-407,535-555`
- Claim: \([xy]E_F=1\) for every registered pair, because the classification forces \(q_{12}=0\) and the jet / vertex guards force \(p_{10}=q_{01}=p_{21}=1\), \(p_{01}=0\).
- How checked. Exponent pairs summing to \((2,2)\):

  | \(P\) | \(Q\) | \(iv-ju\) |
  |---|---|---:|
  | \((0,0)\) | \((2,2)\) | 0 |
  | \((0,1)\) | \((2,1)\) | \(-2\) |
  | \((0,2)\) | \((2,0)\) | \(-4\) |
  | \((1,0)\) | \((1,2)\) | \(2\) |
  | \((1,1)\) | \((1,1)\) | 0 |
  | \((1,2)\) | \((1,0)\) | \(-2\) |
  | \((2,0)\) | \((0,2)\) | \(4\) |
  | \((2,1)\) | \((0,1)\) | \(2\) |
  | \((2,2)\) | \((0,0)\) | 0 |

  So over \(\mathbf Z\), \([xy]([P,Q])=2(p_{10}q_{12}+p_{21}q_{01}-p_{01}q_{21}-p_{12}q_{10})+4(\cdots)\). Under the linear jet \(p_{01}=q_{10}=0\) the last two summands die and
  \[
  [xy]E_F=q_{12}+p_{21}\pmod 2.
  \]
  (The writeup's displayed formula omits the already-killed \(p_{12}q_{10}\) and keeps the already-killed \(p_{01}q_{21}\); both are correct on the normalized slice.) The registered cut sets \(p_{21}=1\), so the class vanishes iff \(q_{12}=1\).
- Why \(q_{12}=0\): the \((2,2)\) coefficient of \([P,Q]\) over \(\mathbf F_2\) is fed by the eight odd-\((iv-ju)\) pairs with \(i+u=j+v=3\). On the registered supports the only surviving pair is \(P(2,1)\,Q(1,2)\): \(p_{01}=0\), \(p_{03},p_{12},p_{23}\) are not in the \(P\)-shell, \(q_{23},q_{03}\) are not in the \(Q\)-shell, \(q_{10}=0\), and none of the four surviving \(P\)'s carries the remaining shell bit \(p_{32}\). For each of those four \(P\)'s the entire \(Q\)-shell contributes to the \((2,2)\) row through the single column \(q_{12}\), with zero base term. Keller forces \(q_{12}=0\). Hence \([xy]E_F=1\) identically.
- Classification itself is exhaustive, not structural: 4,096 collision-compatible \(P\)-masks, exactly four admit a \(Q\),
  \[
  P=P_M+s(x^2+x^4y+x^5+x^6y)+t(x^2y^2+x^4y^2),
  \]
  affine dimensions \(9,9,6,6\). Re-ran `primary_search`; the four supports and the stated \(Q\)-bit identities (including \(q_{41}=q_{30}\) etc.) hold on all 1,152 pairs. Direct evaluation: \(q_{12}\) is absent from all 1,152, \(p_{21}\) is present in all 1,152, \((1,1)\in E_F\) for all 1,152. Five odd–odd patterns, multiplicities \(256+256+256+256+128=1152\), every pattern contains \((1,1)\).
- Exact generic degrees (`search --degrees`, Singular `vdim(std(P-U,Q-V))` over \(\mathbf F_2(U,V)\), 351s) reproduce the filed histogram, including the eight odd degrees \(3,7,11,11,15,15,15,15\), all with \(P=P_M\), and odd-bank SHA-256 `9bf54d4677b31e29ebf8ae4e22ea3b19eca6193788f6ca1f2eeb1f6b6de3c9ba`. The eight \(Q\)-supports match the writeup table (engine print order differs). Mondello's degree 3 matches Mondello Thm. 1.2 / the hidden cubic of §§3–5.

### 5. Severity: clear — scope is honest; this *is* the stratum the char-0-lift hope lived on

- File: `xmodel/sol-witt.md:46-56,522-577`; `xmodel/sol-lateral.md:47-92`
- Claim: stratum-only rigidity; a vanishing \(o_2\) is a \(\mathbf Z/4\) lead, not a char-0 counterexample; nonvanishing kills only the unramified \(W_2/\mathbf Z_2\) lane; the 48 are banked and not promoted; the result does not settle JC2.
- How checked: §6 lists the four further steps a vanishing class would still need (compatible \(W_n\) tower, frozen finite support, distinct colliding points over \(\mathbf Z_2\), descent to a char-0 field). None of those are claimed. The ramified mixed-characteristic caveat is stated. The 3D-premise correction is right and load-bearing: Huq–Kuruvilla is \(G=(x+x^2y,\,y+xz+x^2yz,\,z+x^2z^2)\) with collision \(G(0,1,0)=G(1,1,0)=G(1,1,1)=(0,1,0)\) (2607.20968, Thm. 1.2); its top Cartier class vanishes (no all-odd monomial in \(E_G=xy+x^2z+x^4z^2+x^5yz^2\)) and the displayed \(H\) satisfies \(\det D(G+2H)\equiv1\pmod4\). Independent 3-linear-algebra determinant of \(G\) reproduces \(G-1=2xy+2x^2z+4x^3yz+2x^4z^2+2x^5yz^2\). Mondello §10 is the preserved \(c=0\) fibre of the coordinate-permuted \(\Phi=\tau\circ G\circ\sigma\), not a 3D map. The task prompt had this backwards; the writeup does not.
- Significance. The char-0-lift hope for this lane was a nearby odd-degree separable plane Keller collision whose first Witt obstruction vanishes, close enough to Mondello that the Newton shape which kills every even M2/gap-kill pivot in char \(\neq2\) (MONDELLO-CHECK.md: the lattice determinants 2, 4, 6) still survives. That is exactly the registered cut: same two hulls, one shell, core vertices retained, linear jet, Mondello's three \(\mathbf F_2\)-points, odd generic degree. On that cut the obstruction is identically \(xy\,dx\wedge dy\), including on all eight odd-degree members. Closing the unramified \(W_2\) lane there is the correct negative. It does not touch ramified deformations, larger shells without the vertex cut, or a hypothetical odd-degree vanishing map that has already left Mondello's Newton type (none was found on the slices whose degrees were computed).

### 6. Severity: nit — two display / citation loosenesses, neither load-bearing

- File: `xmodel/sol-witt.md:218-226,399-403`
- The displayed \([xy]\) formula keeps \(p_{01}q_{21}\) and drops \(p_{12}q_{10}\); both coefficients are zero on the normalized jet, so the identity used in the proof is \(q_{12}+p_{21}\). Write it that way.
- Stacks 0FW2 is cited for “the affine-space coefficient rule”; the rule is in the proof, not the lemma. Franjou Prop. 2 / Thm. 3 are the right note, with the connecting-class formula in the proof of Thm. 3 rather than in the proposition statement.

---

## Engine reproduction

```
python3 -m py_compile cases/witt_check.py          # ok
python3 cases/witt_check.py self-test               # SELF-TEST PASS
python3 cases/witt_check.py check --p '1,0;2,1;4,0;6,2' --q '0,1;5,0;6,1;7,2;8,3'
    # odd-odd [[1,1],[7,1],[9,3]], vanishes false
python3 cases/witt_check.py search --degrees        # 1152/0, odd=8, histogram and both SHAs match
python3 cases/witt_check.py relaxed --degrees       # 288/48, vanishing degrees all even
python3 cases/witt_check.py audit-3d                # mod-4 Keller+collision lift verified
```

No floating point, no sampling. All arithmetic above is exact.

## Bottom line

NEVER-VANISHES-PROVED is a theorem on the stratum they registered, not a miss count. The obstruction definition is the right complete \(W_2\) class; the L1 shell has no hole; the identity \([xy]E_F=1\) is forced by the jet, the \(p_{21}\) guard, and the \((2,2)\) Keller row on a complete four-\(P\) list. The one extra fact a hostile reading of the original lateral spec would have wanted — vanishing on the same shell with the vertex guards dropped — exists (7,680 maps) and is already excluded by those guards; every such map whose generic degree was computed is even, so it also fails the odd-degree filter that was part of the original hope. The unramified Mondello-shaped \(W_2\) lane is closed. JC2 is not.
