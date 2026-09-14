# Stage-specific 99 front improvement

For either 99 branch, stages1–8 satisfy the further necessary cuts

    D_r=0 for r<=30,   C_r=0 for r<=62.

Stage0 retains the previously proved quartic cuts D<=29,C<=60. These
are radical preprocessing consequences, not an additional gauge. Every
original source and characteristic equation remains transported.

By `review/quartic-front-improvement.md`, if the first nonzero D band
has r=30 then H0^3 divides its fourth power. Here H0=z^24(1+z)^9,
so the leading band d is divisible by (1+z)^7. Its actual source floor
3r+4q>=189 gives z-order at least25, and its degree cap is32. Thus

    d=tau*z^25*(1+z)^7.

The coefficient at (r,q)=(30,25) is exactly tau and has D2 weight190.
At offset1 the frozen source D1 equations require order
583-3*190=13 at pi=1 for the whole W190 face. Its allowed exponents
are 1,4,...,31, so it is pi*S(pi^3), with deg S<=10. Since pi is a
unit near1 and pi^3 has nonzero derivative there, S must have a root
of order13 at1 and is therefore zero. The entire W190 face vanishes,
including tau. This excludes r30 at every stage at least1.

Once D starts at r31, the normalized quotient contribution to C starts
at2*31+1=63, the bD term at31+33=64, and the scalar at98. Therefore
C has no bands through62. The quartic band needed for r30 is121,
below the low target cutoff141; all its scalar-term inequalities
remain satisfied.

The exact source map was checked at stages0,1,7,8. The image of
B2c_30_25 is free at stage0 and identically zero at all three tested
positive stages. Monotonicity of the moment prefix establishes every
intermediate stage as well. The W190 moment matrix has rank11 on11
columns, with13 rows. These checks and the source-engine hash are
in `stage-specific-front-audit.json`.

No further cutoff is inferred. At r31 the equality-band coefficient
q24 is already zero, so a possible next shape is

    D31=tau*z^25*(1+z)^7.

Its q25 position has weight193. At stages7/8 its source image is the
nonzero linear expression

    6 B2c_39_19 + 20 B2c_43_16 + 45 B2c_47_13
    + 84 B2c_51_10 + 140 B2c_55_7 + 216 B2c_59_4
    + 315 B2c_63_1.

Thus treating this position as zero merely because earlier equality
positions vanished would be unsupported. Further characteristic rows
might constrain it, but no such conclusion is used here.

An optional necessary graph retains the next band rather than deleting it.
The same quartic argument, including the zero case, gives at stages>=1

    D31=tau*z^25*(1+z)^7,
    C63=(3/8)*tau^2*z^26*(1+z)^5.

Here tau is the actual z32 coefficient of D31 and may be zero. Indeed
D31's q24 coefficient is zero by the equality face, the remaining
z-order is at least25, and the quartic condition supplies (1+z)^7,
exhausting degree32. Squaring this band and dividing by H0 gives the
stated C63; the bD correction starts at64. At stage0 the corresponding
allowed graph is D30 of the same shape and C61 of the same quotient
shape. Each is a necessary algebraic-set consequence, imposable on
actual source position images with rational pivots and no inversion of
tau. It does not assert existence of a full-chart point with tau nonzero.
