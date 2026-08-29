# `td=8` equal-join route: uniform Proposition 8.1(iv) solutions

Date: 2026-08-29 UTC. Producer: Sol 5.6 ultra. Status:
**SOURCE_READY_FOR_DIFFERENT_MODEL_HOSTILE_REVIEW**.

This is a blind primary derivation made while the independent Opus5 and
Grok 4.6 parametric-consumer lanes were still running; neither lane's output
was read. It consumes the already reviewed formal route, not geometric data.

## 1. Frozen charge and sources

Charged route report:
`xmodel/m2-td8-equal-join-route-family-sol56-20260829.md`, full SHA-256
`9a778862816aa96d251c33aac7e98a2fb3bfc1b3fc7c83f4463ac862de31815a`,
body `bd35c43baf91c6306d4bb651a09e4886340ab7eb836ffd41d6b1ba6a85ea02d7`.
Different-model route review:
`xmodel/m2-td8-equal-join-route-family-hostile-review-grok46-20260829.md`,
full `d3f378a1c5ed6a649b53885ce2d965c4fad4acad64b98df96ed2ed71ad6b2d8e`,
body `a53a78dbabaaa6f1c2a30247ad016b99bf2d2011132736a2e8b7c5f098552c49`.

The printed source was read directly: `refs/sigray_full.pdf`, SHA-256
`9bf9f0320497dd8d5da6d7fe68ec900c1879663e6f11c121853482ca7e1623ae`,
printed pp. 39--41, Notation/Proposition 8.1. Comparison derivations were
`ladder/SHEET6-L1.md` (`69e6e4c1...`),
`ladder/SHEET6-A3L1-REVIEW.md` (`dd25e00a...`),
`cases/l1_ode_check.py` (`e766bfe2...`), and the current
`ladder/BOOK-OFFAXIS.md` (`7679db8a...`).

No web, AWS, CAS, canonical edit, commit, push, global status, or
`jc2-lean` access occurred. Computation was bounded sparse rational Python.

## 2. Result

**PROVED at the vertex-local formal-pattern tier.** Every member of the
reviewed affine equal-join family satisfies Proposition 8.1(iv) with an
explicit admissible reduced pattern. Moreover, both identical incoming
`(21,15)` vertices and the fixed `(85,35)` trunk on the recorded route also
have explicit admissible solutions. Thus the whole displayed route survives
the local ODE consumer. This is not cross-vertex coefficient gluing.

For every integer `t>=0`, put

```text
nu = 4+3t,
delta = X = 4nu = 16+12t,
b = 1-u = kbar = 2(2nu+1)/3 = 6+4t.
```

Then, with `eta` the printed variable,

```text
p(eta) = (eta^(2nu)+1)^3,
q(eta) = eta*(eta^(2nu)+1),

delta*p*q' - b*p'*q = delta*p.                 (EJ)
```

The right-hand constant `delta` is nonzero. Degrees are
`(deg p,deg q)=(6nu,2nu+1)=(24+18t,9+6t)`, and

```text
gcd(6nu,2nu+1)=gcd(3,2nu+1)=3
```

because `nu=1 mod 3`. This is exactly the charged `M=3` family.

## 3. Direct proof of (EJ)

Set `R=eta^(2nu)+1`, so `p=R^3`, `q=eta R`,

```text
q' = R + 2nu*eta^(2nu),
p' = 6nu*eta^(2nu-1)*R^2.
```

Therefore

```text
delta*p*q' - b*p'*q
 = R^3 [delta*R + 2nu*delta*eta^(2nu)
                  - 6nu*b*eta^(2nu)]
 = R^3 [delta +
        (delta*(2nu+1)-6nu*b)*eta^(2nu)].
```

The second coefficient vanishes identically because

```text
delta*(2nu+1) = 4nu*(2nu+1)
              = 6nu * 2(2nu+1)/3 = 6nu*b.
```

The result is `delta*R^3=delta*p`.

The top cancellation also recovers the printed ratio:

```text
delta/(1-u) = 4nu / (2(2nu+1)/3)
            = 6nu/(2nu+1) = deg(p)/deg(q).
```

In the charged frame, `delta/deg(p)=2/3` is the book's `rho`, and
`(b-2/3)/nu=4/3` is the reviewed reduced successor `w`.

## 4. Shape and admissibility

Write `T=eta^nu`. Then `R=T^2+1=(T-i)(T+i)`. The two roots are distinct
and nonzero, hence lift to two disjoint nonzero `nu`-orbits. Each is a
root of `p` with multiplicity three, exactly the two equal arrivals
`(mu,w)=(3,2/3)`. Each divides `q` exactly once, as Proposition 8.1(iv)'s
root law requires. The only other q-root is the forced simple `eta` root;
zero is not a p-root. There are no nonchain p-orbits or q-extra orbits.

The searrow/root-multiplicity checks are strict:

```text
3*deg(q)=6nu+3 > 6nu=deg(p),
deg(p) != 3*deg(q).
```

Thus the solution is not a degree-only artifact and the nonzero RHS does not
vanish at a root.

## 5. Rigidity, not merely one lucky example

Let the two T-orbits instead be roots of the general monic quadratic

```text
P(T)=(T-A)(T-B)=T^2-sigma*T+pi,
p=P^3, q=eta*P.
```

Divide Proposition 8.1(iv) by `1-u` and put
`r=delta/(1-u)=6nu/(2nu+1)`. After cancelling `P^3`, the left side is

```text
r*P + nu*(r-3)*T*P'
 = r*(P - T*P'/2)
 = r*(pi - sigma*T/2),
```

since `nu*(r-3)=-r/2`. It is a nonzero constant if and only if
`sigma=A+B=0` and `pi=AB!=0`. Hence within the forced two-orbit/no-extra
shape, all and only opposite nonzero T-roots solve the identity, up to
scale. The displayed `T^2+1` is a convenient rational-coefficient gauge.

## 6. The two fixed consumers also survive

The same one-line calculation handles both neighboring shapes.

### 6.1 Each incoming `(21,15)` vertex

Take `T=eta^7` and

```text
p=(T-2)^2(T-3), q=eta(T-2)(T-3),
(delta,1-u)=(X,kbar)=(7,5).
```

Then

```text
7*p*q' - 5*p'*q = 42*p.
```

The roots are distinct/nonzero, with multiplicities `(2,1)`; degrees are
`(21,15)`, gcd three. In the general gauge the constant condition is
`2B=3A`, reproducing `B/A=3/2` from the promoted L1 calculation.

### 6.2 Fixed `(85,35)` trunk

Take `T=eta^17` and

```text
p=(T-3)^3(T-4)^2, q=eta(T-3)(T-4),
(delta,1-u)=(X,kbar)=(17,7).
```

Then

```text
17*p*q' - 7*p'*q = 204*p.
```

The roots have multiplicities `(3,2)`; degrees are `(85,35)`, gcd five.
In the general gauge the constant condition is `3B=4A`, so the displayed
ratio is forced rather than guessed.

Consequently all four local vertices on the two-input route (two identical
incoming cells, the affine merge, and the trunk) pass the exact printed ODE.
This does not identify their root parameters across vertices or prove the
existence of one global coefficient system realizing all four patterns.

## 7. Packet and verification

Packet: `cases/m2_td8_equal_join_prop81iv_r1_20260829/`.

```text
89d739b09f15e0f03dc82bf1555d195337516b2199e4d0c082ced9e74901b1ed  td8_equal_join_prop81iv_r1.py
d4314f24fdbe375a37de0f66689ba7df341986d79837ce008d0907980acd92ad  test_td8_equal_join_prop81iv_r1.py
6317bc761e99b3bb189efc6ad29a871a15c310d5eda1bf9dfe7af8ea73a980f8  README.md
```

The implementation expands the identities as sparse polynomials over
`Fraction`; it does not sample eta. Ordinary and optimized suites each pass
5,031 checks over `t=0..1000`, `10000`, and `10^6`, plus hostile mutations
of both frame coefficients, both fixed root ratios, the residue class, and
input types. The finite scan is regression evidence only; §§3 and 5 are the
uniform proof.

Replay:

```sh
python3 cases/m2_td8_equal_join_prop81iv_r1_20260829/test_td8_equal_join_prop81iv_r1.py
python3 -O cases/m2_td8_equal_join_prop81iv_r1_20260829/test_td8_equal_join_prop81iv_r1.py
python3 cases/m2_td8_equal_join_prop81iv_r1_20260829/td8_equal_join_prop81iv_r1.py --t 0
```

## 8. Consequence and firewall

The parametric Proposition 8.1(iv) consumer returns **LOCAL ALIVE for every
`t>=0`**, and the two fixed consumer shapes also return LOCAL ALIVE. A
uniform ODE/log-residue obstruction therefore cannot remove this D2 family.
The next honest discriminators are cross-vertex coefficient compatibility,
exact lambda (all three recorded lower bounds must be exact because their
sum already equals the ceiling), source landing, or a global obstruction.

Not proved: exact lambda, compatibility of the four local gauges, a source
configuration, geometric realizability, completeness of all td-8 cells, a
degree ceiling, a Keller map, or JC2. No canonical consumer may use this
report before different-model hostile review.

---
Report-body SHA-256 (bytes through the separator line above): `514a099191a4eb5df6ab8bace742f0d734afd33705132768306ac5600b2622b4`
