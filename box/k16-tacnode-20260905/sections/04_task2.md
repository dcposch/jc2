## 4. Task (2): the degenerate case - the dichotomy iterates as the chain [x^j]D, terminates, and forces nothing

**The reduced recursion.** On `Lpivot = 0`, by Prop. 2.3(b), row k (k >= 6) is linear in `l_{k-3}` with the k-independent
coefficient `-[x³]D = -(3/4)piv_2`; row 5 is quadratic in `l_2` and row 6 in `l_3`. On `piv_2 != 0` the charged dual recursion
becomes `l_{k-3} = [rest'_k - (k-3)b²P_k/2]/((3/4)piv_2)` (k >= 7), `l_3` fixed by row 6: the cascade of
`degenerate_pivot.json`, now identified as the coefficients of D.

**Iteration.** On the degenerate locus the weight-(1,2) tangent cone `(3/8)b²(ℓ - l_2x²)(ℓ - l̃_2x²)` is a square and the
branches separate at the first j with `[x^j]D != 0` (`delta = -(D_0/D_1)(1 + ...)`, `D_1(0) = 2b²`). The dichotomy iterates as the chain

```text
level j (j = 2, 3, 4, ...):   [x^j]D = (3/4) b² l_j + f_j(b, B, eta, w_2, l_2, ..., l_{j-1})   is either != 0 (j0 = j)  or  = 0 (go to j+1),
```

a k-independent pivot at every level, linear in the new L-jet `l_j` with the unit coefficient `(3/4)b²`. On the fully
degenerate chain (`[x^2]D = ... = [x^{m}]D = 0`) the L-jets are determined by `(b, B, l_2, w_2)` (eta = -(3/4)bl_2):

```text
l_3 = -2(Bl_2 + bw_2)/b²,   l_4 = (16B²l_2 + 64Bbw_2 - 21b³l_2²)/(4b⁴),   l_5 = (-32B³l_2 - 368B²bw_2 + 123Bb³l_2² + 52b⁴l_2w_2)/(4b⁶)
```

(to `l_9` in `tacnode_involution_K10.json`, key `l_j_on_full_degenerate_chain`; weight N - j each). The infinite chain is the
locus `D ≡ 0`, i.e. `F_0 = (Y - L)²`, a formal family with NO polynomial L (Theorem 3.1(iv)). Hence:

**Proposition 4.1 (termination).** For every polynomial solution with b != 0 the chain terminates at a finite level
`j0 = ord_0 D <= 3N`, and `j0 >= 3` is exactly the tacnode statement. Termination by itself forces nothing about `B*eta`:
the exceptional t = 2 family terminates at `j0 = 3 = N` with `[x³]D = (15/2)b² != 0` (`piv_2 = 10b²`), and its `B = eta = 0`
is the weight-forced vanishing on the axis `c = 0` (charged abel-polysol §5), not a consequence of the termination. The
chain moves in the x-order j, never in N or t: it is a descent on the jet data of ONE solution, not a descent on the index,
and it produces no induction. What it does produce is the reformulation of §5 (the first level in P-only terms).

**Does j0 >= 3 with the truncation force B*eta = 0?** Level j ties `P_j` to `l_2..l_j` (`[x^j]D_0 ∋ 8bP_j + 4b²l_j`), one
P-jet per level; for `j0 - 1 >= N` the chain would fix `l_N = 1/y`, `l_{N+1} = 0` as weight-2N, 2N+1 relations among
`(b, B, l_2, w_2)`; no bound on j0 in terms of N is known (`OPEN[K16-UF-CONTACT-ORDER-BOUND]`; `j0 = N` in the only known
nontrivial solution). At t = 3, 4, 5 the chain is invisible: every `[x^j]D` is nilpotent mod J but not in J (§6): the scheme
`V(J)` has `j0 = 2` to first order and only its reduction has `j0 >= 3`.
