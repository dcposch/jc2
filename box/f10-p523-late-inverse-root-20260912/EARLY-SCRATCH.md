# Additional early determinant scratch — NOT REVIEWED OR PROMOTED

ROOT manual scratch after the four-late-node report was sealed03:51:55UTC.
No scientific subprocess. This is a provisional worksheet, not a scalar
certificate, changed source, qualified place or report amendment. The sealed
report accurately retains six unchecked early determinants at its cutoff.

Same pinned produce.py5078142850c5f4d2e4f08da18fad01ea0271bf36c18740df372884747535280a
and conditional leading C,D from report46f254c123e9b1ea9b30e2758e8229a739b603fb431dba076054bde90c90bb2c.
Let a=381,d=159,b=465,k=17-h,s=10-h,qj=10j-3k.
For a forcing polynomial E=(10-h)A D'-17A'D-target and B=sum b_j*T^j,
the upper recurrence at n=6,...,2 is

    b_(n-2)=-(E_n+a*(10*n-k)*b_n+10*a*(n+1)*b_(n+1))/q_(n-2).

Indices outside0..4 vanish. Residual low rows are

    r1=E1+a*(10-k)*b1+20*a*b2,
    r0=E0-k*a*b0+10*a*b1,
    rho=10*a*b0-17*b*A0.

Column A=1,T,T², in that order. At h4 ONLY, the third target is-2T6,
so E6 includes+2. This target correction is essential.

Hand-generated coefficient arrays (b0,b1,b2,b3,b4):

| h | A=1 | A=T | A=T² |
|---|---|---|---|
| 1 | (173,0,95,0,0) | (450,448,0,234,0) | (405,223,262,0,459) |
| 4 | (335,0,442,0,0) | (470,509,0,292,0) | (446,191,36,0,2) |

Resulting completed matrices (rows r1,r0,rho):

    M1=[[315,381,176],[337,206,481],[90,106,200]],
    M4=[[259,246,449],[260,432,331],[170,471,33]].

First-row signed-minor calculations:

    det M1=315*151-381*52+176*446=106249=203*523+80,
    det M4=259*88-246*426+449*381=89065=170*523+155.

These two residues are advisory and need independent reconstruction; no
inverse products or full scalar-registry certificate supplied here. The
uncomputed h2,h3,h5,h6 matrices remain open, and this scratch does NOT lower
the canonical six-remaining count before complete checked publication.
No follow-on determinant farm, code bypass, runtime or mathematical
conclusion follows. Stop this manual extension at the original03:58 reserve;
do not reset the clock to expand another finite-field worksheet.
