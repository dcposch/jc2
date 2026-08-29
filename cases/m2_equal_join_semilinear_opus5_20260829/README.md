# `m2_equal_join_semilinear_opus5_20260829`

Cap-free exact packet for the **equal-`(mu,w)` nonzero-arrival merge family**,
the last regime in which the merge-local `nu_G` / `kbar` is unbounded after the
searrow, northeast, root-multiplicity, gcd and handshake constraints.

Producer: Opus 5, primary-research lane, 2026-08-29.
Lifecycle: `PROVISIONAL / DIFFERENT-MODEL REVIEW REQUIRED`.
Report: `xmodel/m2-equal-join-semilinear-primary-research-opus5-20260829.md`.

## What it proves (all exact, no caps, no sampling)

1. **(T1-GEN)** The general merge Prop. 8.1(iv) reduction

       (rho - eps)*W + rho*nu*t*W_t - nu*t*S*sum_i n_i*prod_{i'!=i}(t - A_i') = C

   for `p = eta^eps prod_i (t-A_i)^{n_i}`, `q = eta*Rad(t)*S(t)`, `t = eta^nu`.
   It specialises to `xmodel/sol-td7-law.md` eq. (3) and to
   `cases/l1_ode_check.py` families A/B/C.  Verified as a **symbolic identity
   in the unknown pattern coefficients**, not by numeric sampling.

2. **(T1-EQJOIN)** On the `C = 0` equal-arrival family the whole T1 content is
   the single criterion `r*Rad(t) - t*Rad_t(t) = const`, i.e.

       Rad(t) = t^r - A  (A != 0),   C = -nu*r*(mu-eps)*A/dq != 0,

   **uniformly in `nu`**: the family is T1-alive at every member, with a
   codimension-`(r-1)` rigidity on the arrival directions.

3. **Unbounded classification.** `nu_G` is unbounded iff all arrival
   multiplicities are equal, all effective arrival invariants are equal,
   `k = lex = 0`, and no chain arrives at the 0-direction.  Case III is bounded
   under both H5a readings.

4. **Exact family arithmetic.**
   `dp = eps + nu*r*mu`, `dq = 1 + nu*r`, `E = mu - eps`,
   `kbar = mu*w*dq/E`, `X = mu*(kbar - w)`, `M = gcd(mu - eps, nu*r + 1)`,
   trunk child `(w_tr, M) = (mu*w*r/(mu-eps), M)` with `w_tr` **constant** and
   `M` periodic; `lambda_G = 0` if `eps = 0`, else `max(1, ceil(mu*w*r/eps))`.
   Admissible `nu` = an explicit finite union of residue classes.

5. **A worked infinite budget-fitting family** at `td = 12`, `m = 3`,
   `M = [2,2,2]`, type `(2,3)` (entry forced by MP4 + Prop 5.6 + L6).

## Files

| file | role |
|---|---|
| `polyexact.py` | exact sparse multivariate polynomials over `Q` |
| `t1_merge_reduction.py` | (T1-GEN)/(T1-EQ)/(T1-EQJOIN) symbolic verification |
| `eqjoin_semilinear.py` | merge-local arithmetic, unbounded classification, normalized family record |
| `controls.py` | C1–C6 positive/negative controls |
| `emit_eqjoin.py` | fail-closed emitter (`EQJOIN_EMIT_PASS`) |
| `trunk_probe.py` | cap-free P0 chain-step probe for the emitted trunk |
| `test_eqjoin_semilinear.py` | 5810 checks, ordinary and `-O` |

## Controls

* **C1** the `td = 6` promoted residue cell `(r,nu,l) = (2,3,1)`, `(dp,dq) = (6,10)`
  is re-solved from (T1-EQ) and reproduces OBSTRUCTION O's rigid root ratio
  `2 +- sqrt(3)` (as the exact invariant `pi_1^2/pi_0 = 6`).
* **C2** the D9 `nu = 1` reduction `2*p*s' - l*p'*s = c'` and the exact
  even-`l` log residue `(-1)^{n-1} binom(2n-2, n-1) != 0`.
* **C3** the class-B/C recurrence reproduces `sol-td7-law.md` eq. (4) exactly,
  including identity (8) and `dead <=> dp | dq`; the promoted class-B cell
  `(3,9,2,3)` is re-killed.
* **C4** **D9-style duplicate normalization**: `(r,mu,eps,w) = (2,10,0,9)` and
  `(2,9,4,5)` produce an *identical* `(dp,dq,nu,M,kbar,X,w_tr)` tuple at
  `nu = 2` and are separated only by `lambda` (0 vs 23) and by the family key;
  no *whole-family* collision is possible (the `dp` slope in `nu` is `r*mu`).
* **C5** unequal-`mu` false families: 24416 exact configurations, none
  degenerate (the constant half of the consistency residual is load-bearing).
* **C6** case-III index separation: the merge-local bound binds `nu_G` through
  the **effective** invariant, never the incoming `nu_H`.

## Charged replay

```sh
cd cases/m2_equal_join_semilinear_opus5_20260829
python3    emit_eqjoin.py --output /tmp/eqjoin.json
python3 -O emit_eqjoin.py --output /tmp/eqjoin-O.json
cmp /tmp/eqjoin.json /tmp/eqjoin-O.json
python3    test_eqjoin_semilinear.py
python3 -O test_eqjoin_semilinear.py
python3    trunk_probe.py --w 9/2 --M 2 --budget 10 --depth 3 --output /tmp/trunk92.json
```

Observed:

```text
emit_sha256 3914fd3c62bdecc59d250292bd98751054fa4a9ffc9b2e9dcae115745b734da6
t1_identities 13
families 8
EQJOIN_EMIT_PASS
EQJOIN_SEMILINEAR_TEST_PASS checks=5810      (ordinary and -O, byte-identical emission)
one_step_menu 9
terminals_reached 9
states_seen 60 depth 3
```

Cap tokens (`NUCAP`, `MAXNU`, `--cap`) are refused by both `emit_eqjoin.py`
and `trunk_probe.py`.

## Scope firewall

Conditional merge/chain arithmetic over the promoted record only.  Proves no
source landing, no full-configuration cover, no cofinal topological-degree
bound, no realizability (`R4` superset semantics: alive != existent), no
`G2-BD`/`RPMC(C)`, no Keller counterexample, no JC2 consequence.  `lambda`
values are lower bounds (P0 honesty rider (i)).  `jc2-lean` was not accessed.
