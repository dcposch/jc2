# m2_td8_first_extra_jet_exact_lambda_opus5_20260829

Primary research packet (Opus 5, 2026-08-29) for the exact first-separation
charge `Delta(F) = kappa_{I(u_0)}(u_0 - 1)` at the three priced steps of the
reviewed td=8 equal-join affine route, and for the freedom of the first
extra-branch jet `(r_*, p_*)`.

Report: `xmodel/m2-td8-first-extra-jet-exact-lambda-primary-opus5-20260829.md`.

## What is computed

1. **Route recomputation.** Pole `Q=(2,4,3,2,5)`, the `(21,15)` A-step, the
   equal-arrival merge (`nu_G = 4+3t`), the `(85,35)` trunk, the terminal
   `j=3, psi=1`, and the St 3.17(i) i-chain `i_A=2`, `i_G=14`,
   `i_trunk=28(4+3t)`.

2. **The descent law.** With `tau := kappa_F (u - pi(F))`,
   `D_F = int_0^{tau_0} deg(p_{I(tau)}) dtau` and
   `kappa_F(pi(H)-1) = tau_0 - kbar_F`,
   `Delta(F) = (kappa_H/kappa_F)(tau_0 - kbar_F)`.
   A constant profile reproduces the corrected St 9.3(24) gap exactly.

3. **A-step menu** (`m = mult(p_F,c*) = 2`): one drop `2 -> 1` is the only
   possibility, so `Delta_A = 2` if the pair separates at
   `theta >= tau_lin = 7`, else `(kappa_H/kappa_F)(9-theta)`. Integrality
   restricts `theta` to `N*` (contact) or `1/2 + N` (conjugate), giving the
   finite menu `{2,3,4,5,6,7,8} u {5,7,9,11,13,15,17}`.

4. **Trunk** (`m = 2 i_F`): `Delta = 2` iff `kappa_H = kappa_F` and
   `tau_0 = 9`, i.e. the branch group sheds exactly one `i_F` unit of
   branch-area over the nine normalized steps. One explicit realization:
   half the group leaves at `tau = 8`.

5. **Budget.** `sum <= td-1-psi = 6` with three integral charges `>= 2` forces
   all three to be exactly `2` (and `lambda_{(0,y)} = 0`). Any single early
   separation at either A-copy kills every member of the affine family.

6. **Jet layer.** Existence of `F*c*` forces `ord_{c*}(p_{n-k}) >= m-k`, and
   `p_{F*c*}(eta) = sum_k c_k eta^{m-k}` with `c_k = [(eta-c*)^{m-k}] p_{n-k}`.
   `c_0` is pinned by St 3.9(ii); `c_1, c_2` are not pinned by anything printed.
   A derived `nu_F`-semi-invariance of the subtop pieces is imposed, with
   weights PINNED by `(kbar_F, nu_F, D_F)` alone: on the A-step
   `(N_1,e_0,e_1,e_2) = (2,0,4,1)`, on the trunk `(10,0,12,7)`, and `e_0 = 0`
   reproduces the printed `l = 0` of St 3.16. The discriminant is still free:
   both `theta = 1` (`Delta = 8`) and `theta >= 7` (`Delta = 2`) survive every
   printed constraint.
   Exact arithmetic in `K = Q[eta]/(eta^7 - 3/2)`.

## Run

```sh
python3 test_first_extra_jet_td8.py      # TD8_FIRST_EXTRA_JET_OPUS5_TEST_PASS checks=411
python3 -O test_first_extra_jet_td8.py   # identical (the packet has no `assert`)
python3 first_extra_jet_td8.py           # charged JSON + certificate
python3 first_extra_jet_td8.py --json
```

## Scope

Nothing here asserts a route kill, exact `lambda = 2`, source landing, Keller
realizability, a counterexample, or JC2. No AWS, no CAS, no network, no
canonical edit. Certificate firewall booleans are all `false`.
