# Preregistration: D1 primary-C2 `c=9` two-jet `k6` valuation ladder

Date: 2026-08-26

Status: **PREREGISTERED THREE-CHAMBER PRODUCER; HEAVY CAS AWS ONLY.**

## Exact scope

Work only on the unit-load generic-square primary-`C2` boundary

```text
D(p*k0), ord(C)=9, ord(A)>=9, ord(R)>=8.
```

The terminal grade is 28. The load family `k6*C/L` begins at grade 26, one
and two grades before the pole-two `C^2/L^2` obstruction. Row two's `mu2`
target also begins at grade 28, so no all-seven-row target-free assertion is
permitted there. The decisive pole-two functional must use only rows
`1,3,4`, whose targets start later.

## Mechanically complete source

Independently enumerate every primitive family through grade 28 at the
boundary `(A,C,R)=(9,9,8)`, repeat with padded bounds, and derive all source,
load, moving-`p`, and target jet ceilings mechanically. Compile all seven
literal Faber equations through grades 26--28 and bridge them coefficientwise
to an independent Laurent source. Include one deliberately over-padded jet
of every series and prove that it does not enter before grade 29.

Write

```text
p(sigma)=p+2 sigma ell1+2 sigma^2 ell2+...,
k6=k60+sigma k60_1+sigma^2 k60_2+...,
C=C0+sigma C1+sigma^2 C2+....
```

The preregistered load numerators are

```text
U0 = k60*C0,
U1 = k60_1*C0+k60*C1,
U2 = k60_2*C0+k60_1*C1+k60*C2,

grade 26, denominator L:   (3/4) U0,
grade 27, denominator L^2: (3/4)(U1*L-ell1*U0),
grade 28, denominator L^3: (3/4)(U2*L^2
                              -(ell1*U1+ell2*U0)*L
                              +ell1^2*U0).
```

At grade 28 the complete common pole-three numerator must additionally
contain `L` times

```text
(3/4)A*C*L + (3/8)C^2 + (5/8)k0*R*C*L.
```

Every coefficient and sign, including the `ell1^2` and `ell2` terms, is a
checked assertion rather than imported authority.

## Exhaustive load chambers

Split scheme-theoretically into

```text
D(k60),
V(k60) intersect D(k60_1),
V(k60,k60_1).
```

- On `D(k60)`, the complete grade-26 literal equations must give the unit
  ideal on both exact-`C` charts.
- On `V(k60) intersect D(k60_1)`, the complete grade-27 literal equations
  must give the unit ideal on both exact-`C` charts.
- On `V(k60,k60_1)`, grade 28 has pole ceiling two. On the finite etale root
  cover `lambda^2=-p/2`, the rows-`1,3,4` functional must equal

  ```text
  (3/8)(lambda*c1+c0)^2,
  (3/8)(-lambda*c1+c0)^2.
  ```

  The surviving `k60_2*C/L`, `A*C/L`, and `k0*R*C/L` terms are pole one and
  vanish under this root functional. The two root forms must give unit ideals
  before radicals on `D(c1)` and `V(c1) intersect D(c0)`.

The moving-root/Faber bridge is asserted only after both earlier load jets
vanish. As a negative control it must fail after imposing only `k60=0` while
leaving `k60_1` free.

## Controls and firewall

The compiler must explicitly verify that row two has exactly the grade-28
`-mu2` target while rows `1,3,4` remain target-free; `k20`, `mu4`, `mu6`, and
`J` must not enter through grade 28. Omitting the second moving-connection
correction must break the full grade-28 numerator identity. Omitting `C^2`
must make both final root terminals zero.

Run exact Q and fresh `F_65519`,`F_65521` controls on distinct registered AWS
hosts with frozen inputs, ordinary polynomial rings, explicit reductions,
fail-closed validators, resource custody, and zero swap.

A PASS may close only `c=9,A>=9,R>=8` on `D(p*k0)` after the named frozen
generic-square/D1 source gates. It does not include `c>=10`, another primary
or tied face, positive-order leading load, `p=0`, `k0=0`, the exact-square
zero section, terminal/global charts, fan exhaustiveness, order two, maximum
twelve, or JC2.
