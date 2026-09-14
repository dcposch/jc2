# Stage-specific D108 front improvement

For D108 delta3 at stages1–8, the full characteristic block and actual
source moments imply

    D_r=0 for r<=33,  C_r=0 for r<=68.

Stage0 retains D<=32,C<=66. This is radical preprocessing with all
original equations transported, not a source gauge or leader pin.

If D has first nonzero band r33, the proved cubic/quartic divisibilities
and source floor4r+5q>=276, degree cap35, force

    D33=tau*z^29*(1+z)^6.

The coefficient at(r,q)=(33,29) is tau and has D2 weight277. At offset1
the source requires order566-2*277=12 at pi=1 for that whole face.
Its possible powers are1,5,...,33; the face is pi*S(pi^4), deg S<=8.
The unit pi and nonzero derivative of pi^4 at1 preserve the order,
so S has order12 and is zero. Therefore tau is zero whenever offset1
has been imposed.

D consequently starts at34. The quotient, bD, and scalar contributions
to C begin at69,70,107 respectively, proving C<=68. The quartic band
used at r33 is133<151, before its scalar terms, as independently
checked in the preceding quartic audit.

`d108-stage-front-audit.py/.json` checks the actual source graph at
stages0,1,8, its SHA-256, and full rank9 of the12-by9 W277 moment
matrix. At stage0 B2c_33_29 is a free coordinate; at stages1 and8 it
maps exactly to zero, as does every W277 position. Prefix monotonicity
covers stages2–7.

No subsequent cutoff is inferred. At r34 the source equality position
q28 has weight276 and is zero, leaving a possible next shape

    D34=tau*z^29*(1+z)^6.

Its q29 coefficient has weight281 and only4 source moments. The actual
stage8 image is nonzero. A separate argument would be required to
exclude that band.

An optional necessary graph retains the next band:

    D34=tau*z^29*(1+z)^6,
    C69=(3/8)*tau^2*z^30*(1+z)^4

at stages>=1. Tau is the actual z35 coefficient of D34, with zero
allowed. The source equality face deletes its q28 coefficient; cubic
and quartic divisibility force (1+z)^6 and exhaust degree35. The C69
formula is the first monic quotient of D34^2 by H0, with bD beginning
only at70. Stage0 instead has the same D shape at33 and C shape at67.
These are necessary graph equations on the actual source positions,
with rational-pivot elimination available and no inversion of tau.
They do not assert that a nonzero-tau full-chart point exists.
