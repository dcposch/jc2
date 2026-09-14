# Bounded route diagnostics for the first-principles audit

These are existing `Tree.embeds` witnesses, freshly obtained at selected
operative rows. The scripts do not change Tree or promote a new kill. Numerical
C-TOP failures have no effective-height-2 member, even in the `u_s>=2` block.
No `u_s=1` operative row has `ell=0`: `ell=d_s-3>=1` there. Among the 225
numerical failures with `u_s>=2`, 109 have `ell=0`.

`r2-enum-routes.py/.json/.log` gives ten complete example witnesses. The main
simple structures are listed below; parent M includes `M_1=-m`, and child data
is the effective campaign label.

| Parent (n,m), M; V | Child n', M'; V'; d' | ell | Parent delta_(s-1) |
|---|---|---:|---:|
| (96,72), (-72,36,78,94); (1,3,5) or (4,3,5) | 16, (-12,6,13); (1,3) or (4,3); (16,4,2,1) | 3 | 1/7 |
| (90,60), (-60,10,45,88); (1,8,4) | 18, (-12,2,9); (1,8); (18,6,2,1) | 2 | 8/35 |
| (108,72), (-72,24,78,106); (1,4,5) | 18, (-12,4,13); (1,4); (18,6,2,1) | 3 | 1/6 |
| (108,72), (-72,48,90,106); (1,3,5) | 18, (-12,8,15); (1,3); (18,6,2,1) | 3 | 1/7 |
| (144,96), (-96,-32,104,142); (1,14,7) | 18, (-12,-4,13); (1,14); (18,6,2,1) | 5 | 2/17 |
| (96,72), (-72,-60,56,94); (1,9,3) | 24, (-18,-15,14); (1,9); (24,6,3,1) | 1 | 9/29 |
| (144,96), (-96,-16,72,140,142); (1,10,5,3) | 36, (-24,-4,18); (1,10); (36,12,4,2), dropped tail | 1 | 0 |
| (150,100), (-100,-60,65,148); (1,6,3) or (5,6,3) | 60, (-40,-24,26); (1,6) or (5,6); (60,20,4,2), u_s=2 | 0 | 33/50 |

## Exact existing Tree behavior at the named (96,72) row

At `j=3`, Tree calculates `delta=1/7`, `L=1`, `A=7`, `P=10`, `Q=15`.
Its accepted witness uses zero multiplicity `b=3`, selects that zero branch
(`V_3=3`), and has one nonzero orbit of root multiplicity 1. At `j=2`, it
calculates `delta=2/7`, **`L=7`, `A=1`**, `P=6`, `Q=15`, `b=0`. For `V_2=4`
it selects a nonzero orbit of multiplicity 4, alongside two orbits of
multiplicity 1. For `V_2=1` there are six multiplicity-1 orbits. The final
`A_1` is 3 or 2 respectively.

The implementation at `opus5_probe.py:70` takes `L` to be the lcm of the
denominators of **all higher radii**, regardless of whether a coefficient at
that radius was selected as zero. The recursive key at line 110 is only
`(j,high,danger,need)`. `danger` at lines 125-135 remembers whether the selected
route has had a nonzero, nonremovable coefficient. It carries no integer
stabilizer or denominator of actual nonzero support. A coefficient is
removable exactly when its exponent is integral and <=0. The two named
nonintegral coefficients are not removable. Thus a retained order-7 symmetry
after zero selection at 1/7 is not separately checked by this code when it
counts possible nonzero roots at 2/7.

This observation is a code-state diagnosis. It does not prove that the source
row is impossible: Tree's first witness need not be its only witness, and
unrecorded coefficients may matter. The root/child-math agents must decide the
actual Puiseux symmetry question from first principles.

## Recorded-support diagnostic and candidate rows

`r2-enum-stabilizer.py/.json/.log` inspects the existing accepted selected
routes without changing any transition or invoking a replacement screen. Start
`L_support=1`. At exponent delta, calculate
`A_support=denominator(L_support*delta)`. The Tree witness's old A divides
this A_support. Its list of nonzero orbits can be grouped under this larger
orbit action only when each multiplicity's frequency is divisible by
`A_support/A_tree`. After a selected nonzero coefficient, update L_support to
the lcm with denominator(delta); leave it fixed after a selected zero. The
script also evaluates the printed (12)/(13) congruences at the bottom using
the recorded-support A_1.

This diagnostic knows only **recorded radius coefficients**, not all actual
coefficients of the centre. Failure is not a new kill; passing proves no
existence. Of 1,161 existing numerical C-TOP-failing witnesses, 57 allow the
orbit grouping and 23 also meet the bottom congruence with recorded support.
All 23 are in the `u_s=1` block. These counts are diagnostic, not promoted.

The simplest effective-height-3 passing diagnostic is parent `(180,120)`,
`M=(-120,132,150,178)`, `V=(2,4,5)` or `(3,4,5)`, `d_s=6`, `u_s=1`,
`ell=3`. Child labels are `(n',m')=(30,20)`, `M'=(-20,22,25)`,
`d'=(30,10,2,1)`, `V'=(2,4)` or `(3,4)`, so the claimed C-TOP comparison is
`4<=2`, false. Its parent route is:

* `delta_3=1/6`: A=6, P=10, Q=25, b=4, selected zero, one nonzero orbit of
  multiplicity 1.
* `delta_2=1/5`: both A_tree and A_support are 5, P=20, Q=16, b=0, selected
  nonzero; orbit multiplicities `(2,1,1)` or `(3,1)`.
* `delta_1=2/3` or `1/2`: recorded support denominator is 5, so A_1 is 3 or 2
  respectively, and the corresponding (12) or (13) congruence holds.

An `ell=1` candidate with a shorter existing free-exponent envelope is parent
`(144,96)`, `M=(-96,112,132,142)`, `V=(8,8,3)`, `d_s=4`, `u_s=1`.
Child labels `(36,24)`, `M'=(-24,28,33)`, `d'=(36,12,4,1)`, `V'=(8,8)`
fail `8<=4`. Parent `delta_3=1/4`: A=4, P=12, Q=9, b=8, zero selected, one
nonzero orbit of multiplicity 1. Parent `delta_2=1/3`: A=3, P=24, Q=16, b=0,
one nonzero orbit of multiplicity 8. Parent `delta_1=4/9`: recorded support
denominator 3, A_1=3, and (12) holds. Tree's existing off-radius exponent
envelope is only `{5/12}`. Neither candidate is asserted to be a realized
source or a first-principles counterexample.
