# Whole-Q5 scalar row-8 Cartier/Fitting discriminator

Consume the complete displayed global Q5/H6,J6 formula at source SHA-256
`2bdf4bb4743a4bf5904c87b5550df6fa7908e779e6c90645ab2e911bda87805d`.
That parent retains all 197 displayed equations, including its 63 terminal
rows, every exact division gate, and all independent predecessor constraints.

The pointwise Q2/Q1 certificates identify one universal candidate obstruction:
row 8, the coefficient `x^2 y`.  For arbitrary low order-27 forms
`W2,Z2`, exact expansion gives

```text
kappa = z2_0 - w2_1 + h*(z2_1 - w2_2).
```

If the two degree-one first-carry equations are written

```text
rx + z2_1 - w2_2 = 0,
ry + w2_1 - z2_0 = 0,
```

then

```text
kappa = omega + h*stage_x - stage_y,
omega = ry - h*rx.
```

The degree-one divergence map is surjective, so eliminating `W2,Z2` from
the five first-carry equations plus `kappa=0` leaves exactly the single scalar
condition `omega=0`.  Constants have zero derivative.  Degree-three low forms
solve the independent degree-two first-carry rows and do not enter kappa.

Compile `rx,ry` from the literal source carry: divide the final `E` degree-one
part exactly by three and add the degree-one part of `M`.  Append `omega=0` to
the complete Q5 parent.  Emit and hash the exact scalar expression.  An UNSAT
formula is a potentially global necessary-condition obstruction but remains
diagnostic without proof/source review.  A SAT formula is an exact point of the
row-8 zero locus only; it still needs Q4/Q3 restoration and direct integer
replay.

Omitting `omega=0` is the positive control.  No Q4/Q3 existence, all-depth,
algebraization, counterexample, or JC2 inference is licensed.  All substantive
execution is AWS-only.
