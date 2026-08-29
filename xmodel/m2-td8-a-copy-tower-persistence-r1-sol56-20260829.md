# `td=8` A-copy approximate-root persistence

Author: Sol 5.6 coordinator/primary, incorporating an independent in-product
derivation by Boole the 2nd. Date: 2026-08-29 UTC.
Lifecycle: `PRODUCER_CHECKED`; different-model hostile review required.

## 0. Result

**Theorem (`TD8-A-TOWER-PERSISTS`).** Let `F` be either reviewed A-vertex of
the `td=8` equal-join affine route, with

```text
Q(F)=(14,42,7,3,5),
Phi=(T-A)^2(T-B),  T=eta^7,  B=(3/2)A,
p_{f,F}=C Phi^2,
p_{h,F}=D Phi Psi,  Psi=eta(T-A)(T-B).
```

Assume the reviewed `(2,3)` first approximate-root stage, `mu_F=3/2`, the
exact tower identities, and `J(f,g)=c0 != 0`. Then the two `f` branches in
the `B` orbit cannot separate before `pi(F)+7/kappa_F`. Equivalently their
contact satisfies `theta>=7`, so the exact A-charge is

```text
Delta_A=2.
```

The assertion holds independently at both A-copies and is independent of
the affine parameter `t`.

## 1. Inputs and scope

1. Fable's Statement-3.9 transport primary, full SHA-256
   `910d3216ad7476b743eb920e3d68026f05efc8ffe1a409c476fb90ce277f6ad4`,
   and Opus's review, full
   `e469e94dbf4393fe820345678c2582ca7f7a528695c25d065fb224b4f796cf61`.
   These force the initial `(2,3)` stage and permit only `k=1` shifts before
   the terminal stage.
2. Opus's exact-separation primary, full
   `991e1b350ad2f8b2b82808fdc84dec71154f9ae17250c18953a36ac8f6588508`,
   and Fable's grading-corrected review, full
   `ec3557953c6387ce35dcf4efe1df267fb828771119c479eb00c8f1793e0ee370`.
   These identify `theta>=7` with A-charge two but do not themselves prove
   that inequality.

This report supplies that missing tower implication. It does not cover the
trunk charge, source landing, polynomial realization, or a Keller pair.

## 2. First-band discriminant

Write

```text
P'_0=C(T-A)^4(T-B)^2.
```

The reviewed vanishing and semi-invariance laws force

```text
P'_1=eta^4(T-A)^3(T-B) R_1(T),
P'_2=eta(T-A)^2 R_2(T).
```

For `c^7=B`, direct expansion of the first child quadratic gives

```text
Disc(p_{F*c})
  =(49/64) A^6 c^13 [B R_1(B)^2-4 C R_2(B)].          (2.1)
```

The f-side vanishing and semi-invariance constraints alone leave the bracket
in (2.1) free. The full approximate-root tower forces it to vanish:

```text
B R_1(B)^2=4 C R_2(B).                               (2.2)
```

Thus the earlier nonzero-discriminant first-jet filling does not extend to
the actual tower. The square filling is forced; in the gauge
`A=C=R_1=1`, its coefficient is `R_2(B)=3/8`.

## 3. Tower proof

Because stage zero is `(k_0,l_0)=(2,3)` and `mu_F=3/2`, every later
preterminal stage has `k_j=1`. Strict descent in Proposition 4.2 makes the
shift exponents strictly decrease, with the first shift exponent in
`{1,2}`. Hence the terminal approximate root has the form

```text
h=g^2-s_0 f^3-P(f),  deg P<=2,
J(f,h)=2 c0 g.                                       (3.1)
```

Work on the lattice `K=e*kappa_F`, where `e=1` in the contact case and
`e=2` in the conjugate case. Before separation, at fine step `j`,

```text
D_f=14e-2j,
D_g=21e-3j,
D_h=12e-2j,
kbar=5e-j.                                           (3.2)
```

Since `h` and `P(f)` lie below `3D_f`, the highest part of
`g^2-s_0 f^3=P(f)+h` gives

```text
G_j^2=s_0 F_j^3.
```

With `deg(F_j,G_j)=(2,3)`, unique factorization forces

```text
F_j=a_j L_j^2,  G_j=b_j L_j^3.                       (3.3)
```

The exact Jacobian band is

```text
D_f F_j H_j' - D_h F_j' H_j = gamma G_j,  gamma!=0. (3.4)
```

Write `H_j=v_2 L_j^2+v_1 L_j+v_0`. Equation (3.4) forces
`v_0=v_1=0` unless `j=5e`. At that resonance it still forces
`H_j=L_j(v_2L_j+v_1)`, so the chosen branch loses at least one unit of
`D_h`. Afterwards `D_h<=2e-1`; because `e<=2`, this remains below `3D_f`
through `j=7e-1`, and the cusp argument keeps `F_j` square. The argument
stops exactly at `D_f=0`, `j=7e`. Therefore separation cannot occur before
the cv level `theta=7`, proving the theorem and (2.2).

The endpoint distinction is harmless for budget: a split quadratic at
`theta=7` is allowed and has `Delta_A=2`; a square cv quadratic means
`theta>7` and also has `Delta_A=2`.

## 4. Twin scope and next datum

There is no cross-twin equation between the two copies of the scalar in
(2.1): it vanishes locally at each copy. Their first shared coefficients
remain locally free, for example

```text
R_{1,e}=u_e,
R_{2,e}=B_e u_e^2/(4 C_e),
```

with independent `u_1,u_2`. Common formal Laurent gluing is available by
CRT at the two disjoint merge-orbit ideals; polynomial source landing may
still couple them.

The next A-side datum is the cv discriminant at `theta=7`, one scalar
`Omega_e` per copy. In the original `kappa_F` grading it is obtained from
`P'_0,...,P'_{14}` by the branch recursion

```text
Q_{j,e}(Z)=[h^(2j)] sum_{r>=0} h^r P'_{r,e}
  (c_e + sum_{s<j} a_{s,e} h^s + h^j Z),
```

with `Q_{j,e}` square for `1<=j<=6` and
`Omega_e=Disc Q_{7,e}`. Nonzero `Omega_e` means `theta=7`; zero means
`theta>7`. Neither changes the charge. Consequently the live exact-budget
issue moves to the trunk rather than another A-side first jet.

## 5. Review risks and exclusions

A different model must reconstruct, directly from the printed Puiseux
conventions:

1. the ramified-lattice band equation and exhaustion `e in {1,2}`;
2. terminal value `D_h=12` and the assertion that every preterminal stage
   after `(2,3)` has `k=1`;
3. the resonance calculation at `j=5e` and the strict inequality range used
   to propagate the square factor.

Until then this result is provisional. It proves no trunk charge, exact
total lambda, source landing, polynomial pair, Keller counterexample, degree
ceiling, `G2-PSC`, `G2-BD`, or JC2 conclusion.

## 6. Recommended next discriminator

Review this tower lemma adversarially. If it passes, stop spending A-side
budget work on `P'_2(c)` and compute the first trunk ramification/area-defect
datum instead. The A-side `Omega_e` values remain useful only for contact
type and source-realization tests, not for the route's budget.

No AWS, web access, canonical engine edit, or heavy computation was used.
This note does not access or depend on the separately owned formalization
repository.

---

Report-body SHA-256 (all bytes before the separator line above):
`3b9c8cacb647579e02ca4b37e7950924636c5626909e9f1adf28252da17ed9a0`.
