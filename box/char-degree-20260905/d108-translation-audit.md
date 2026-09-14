# D108: the frozen three-jet chart does not support a jet0=0 translation slice

**Conclusion:** no generic diagonal-translation coverage proof is
available for setting D108 jet0=0 in this engine. The (99,66) translation
proof must not be transferred to it by analogy. No engine was changed
for this audit.

The actual frozen engine and this lane's copied snapshot have identical
SHA-256 `8f6c34f6dbc4407e0deb599fe2061a1a23f93f16dcda2d7dbe30184e1cd82ee1`.
Its `symbols_jet()` at line 244 declares only jet0, jet1 and jet2.
`minor_local_rows()` at line 224 and `local_rows()` at line 443 use

\[
y=j_0+u t+v t^2+\pi t^3.
\]

`minor_incidence()` at line 247 imposes the actual h3 target
`K3=-t^8(pi^2-c)+O(t^9)`. Its coefficient at pi is zero. The
F/G leading-pole targets at lines 489–496 are likewise fixed powers
of pi^2-c. There is no jet3 or at-level mean in these functions or
their returned coordinate sets.

For the diagonal source translation
`(x_old,y_old)=(x_new+q,y_new+q)`, the old parameter is
`t_old=t_new/(1+q*t_new)`. Expanding the old root series gives

\[
j_0'=j_0-q,\qquad u'=u,\qquad v'=v-qu,
\]
\[
\pi_{\rm new}=\pi_{\rm old}+A,\qquad A=q^2u-2qv.
\]

Thus on the new **strict** three-jet arc, the transformed leading
polynomial is

\[
-\bigl((\pi-A)^2-c\bigr),
\]

whose linear coefficient is 2A. The leading normalization factor
introduced by translating x is a unit with constant term 1, so it
does not alter this leading face. Setting q=j0 generally gives
`A=j0^2*u-2*j0*v`, which is not zero. No change in c can remove the
linear coefficient.

A generic pi reparameterization restores an even face only if the
arc is transported as well. Writing the new centered parameter as
pi requires

\[
y=j_0'+u't+v't^2+(A+\pi)t^3.
\]

That is precisely the at-level mean absent from the current engine.
Dropping A from the arc while retaining the even target changes the
coefficient equations. A generic-disc coordinate choice is not a
physical source translation and cannot justify this omission.

The exact control `d108-translation-audit.py/.json` imports the
frozen engine, uses its own raw incidence rows and rational pivots
to construct a point with `j0=u=v=1,c=2`, and verifies every old
raw h3 incidence row at that point. It then translates the actual
normalized h3 coefficient polynomial by

\[
\sum c_{r,p}t^rz^p\longmapsto
\sum c_{r,p}t^rz^p(1+qt)^{9-r-p}.
\]

At q=1 the new strict jets are `(0,1,0)`. The engine's own minor
coefficient extraction gives `-pi^2-2*pi+1`, with a nonzero linear
residual **-2** against the even target. The required at-level mean
is -1. Substituting `pi -> pi-1` restores `2-pi^2`, verifying both
the failure and its exact source.

For a transportable enlargement one could retain a mean j3 in the
arc and use
`j3'=j3+q^2*u-2*q*v`; then q=j0 gives a legitimate jet0=0 slice
while j3 remains represented. Such an enlargement also requires
transporting every incidence and leading-pole target. This audit
does not implement it or claim that the existing engine already
does so.

Keeping jet0 free avoids the additional unsupported slice. It does
not itself prove that the original physical mean-zero condition
covers every realized D108 datum: that condition needs its own
printed necessity or a complete chart-coordinate justification.
This audit finds no hidden mean parameter or such transport in the
frozen code. It establishes the concrete covariance failure above,
not a theorem that the source D108 branch is empty or realizable.

The distinction with the audited sibling is material: (99,66)
delta2 carries its at-level `minor_a2`; at delta5/2 the next
translation-generated integer term lies strictly above that level.
Neither fact holds for the three-jet D108 substitution at delta3.
