# Degree-bounded D16/D17 sign branches

This packet classifies the two frozen uniform congruences

```text
(3/8)*Bhat^2+J16 = A^2*M,
3*Bhat*C-2*M = 4*A^2*N,
A=X^4-1,
```

under the authoritative degree bounds `deg(Bhat)<=8`, `deg(C)<=7`.

If `J16!=0`, adjoin `rho` with `rho^2=-8*J16/3` and split `A`.  There are
exactly 16 degree-`<8` Hermite sign lifts `E_s` satisfying
`E_s^2=1 mod A^2`, eight modulo simultaneous `E_s,rho` sign.  Every solution
has

```text
Bhat = rho*E_s + lambda*A^2,
C    = rho*rem(E_s*(E_s^2-1)/A^2,A^2)/4 + lambda/2.
```

All 16 lifts are serialized exactly over `Q(i)`, together with `M,N` and the
substitution of `F9[X0]` absence and every live `C13`--`C17` lower-window
equation.  No branch produces an immediate literal unit; that is a reduction
to eight small systems, not evidence of existence.

If `J16=0`, D16 first gives `Bhat=A*L`, and D17 forces `A|L`; hence
`Bhat=lambda*A^2`.  Here `C` remains free within its degree bound and the
lower/later equations.

Replay:

```text
python3 -B classify_sign_branches.py --check
shasum -a 256 -c SOURCE.sha256
shasum -a 256 -c EVIDENCE.sha256
```

Only standard-library exact arithmetic is used.  No cutoff-three transport,
endpoint emptiness, or JC2 conclusion is asserted.
