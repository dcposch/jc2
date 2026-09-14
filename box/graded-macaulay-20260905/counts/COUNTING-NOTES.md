Exact ambient and declared-pivot counts

`exact_counts.py` reads the four complete ordinary coefficient presentations,
the two available complete native presentations, and the preserved licensed
425-generator s'=4 union control. The latter is the same 77-parameter ideal,
with a different homogeneous generator list. It is not another fibre and is
not V3_2. No missing/header-only native source is counted as the zero ideal.

For variable degrees (b,w), define H(X,Y) by

    sum H(X,Y) u^X v^Y = product_z (1-u^b(z) v^w(z))^-1.

The primary algorithm starts H(0,0)=1 and, for each variable, updates in
increasing X and increasing Y. Independent verification groups variables with
equal degree, then convolves with binomial(m+k-1,k) at each multiple k(b,w).
Every table entry in the rectangle 0<=X<=3p, 0<=Y<=3D agrees between the two
algorithms. All counts are arbitrary-precision Python integers, with no
floating-point arithmetic and no modular or Groebner computation. Each frozen
N=1 ambient count is reproduced exactly. Small hand-counted examples and a
deliberately inhomogeneous mutation are checked.

For the declared generator list g_i, the matrix has H(Np,ND) columns and

    sum_i H(Np-deg_1(g_i),ND-deg_2(g_i))

rows, interpreting a negative argument as zero. Both algorithms run on the
full original support. Generators with no complementary monomials contribute
zero rows even when their first charge alone is eligible. The JSON records
every source coordinate, degree, complementary component and multiplier count,
not only summary totals. The total initial matrix nonzero count is also exact:
the multiplier count times the nonzero term count of each g_i, summed over i.
This counts the explicitly generated matrix, before elimination or duplicate
row removal. It is not a rank or quotient Hilbert function.

The term audit independently checks 1,618 source rows and 2,357,809 terms.
Every parsed rational coefficient is nonzero, every source polynomial is
expanded with distinct monomials, and every term has the degree specified by
its extraction coordinate (b+1,D-a-jK). Original generator order, variable
order and input hashes are retained. The ambient driver finished in about
37 seconds. `ambient-counts-table.md` contains all exact dimensions and nnz.

Actual contributing direct-generator counts at N=1,2,3 are respectively:
77: 76/141/150; 111: 72/135/164; 129: 65/123/159; 136: 85/171/252.
All requested N=2 and N=3 ambient blocks exceed ten million columns by many
orders of magnitude. After the inherited pivot reductions the smallest N=2
block has 7,742,886,741 columns (111, with c eliminated). The subsequent full
positive-A reductions improve this to 6,782,152,172 columns (see below). This proves
infeasibility of explicitly materializing these particular matrices under the
stated column criterion. It does not prove impossibility of every structured
module algorithm or further algebraic reduction.

`reduced_counts.py` independently counts the remaining coordinate inventories
of the frozen reductions. The 77/136 DAGs eliminate 27/71 positive-charge
coordinates and retain c. The 111/129 known fast reductions eliminate 42/37
coordinates INCLUDING c, so the target in those rings is phi(c)^N. The JSON
also gives counts when that last c pivot is held out, and counts after the c
pivot for all four. A defensive assert initially rejected the assumption that
all four lists retained c; the corrected script distinguishes these cases.
The reduced driver verifies inventory partitions and independent DP equality.
The original rational pivot replay supplies ideal/ring-map custody; counting
alone does not re-prove that replay or claim these pivot sets are maximal.

The root subsequently completed 27/57/57/71 positive-A pivots, retaining c, and
optionally eliminated c separately. `check_root_reduced.py` independently
checks these NEW complete presentations in `../reduced/<fibre>/reduced-counts.json`.
It verifies original row coordinate degrees, source hashes, the partition into
pivot/extra-zero/nonzero rows, all 2,004 per-source multiplier contributions,
and both independent counting recurrences across the entire c-retained and
c-free degree rectangles. The identity H_cfree(X,Y)=H_withc(X,Y)-H_withc(X-p,Y-D)
passes at every entry, including all requested targets. The exact zero
expansions are consumed without another large expansion. All root counts pass;
`independent-reduced-check.json` records the upgraded results. The NEW 111/129
c-free N=2 counts are 6,782,152,172 and 223,946,470,992, respectively.

There is no charge-zero pivot in any of these lists. Indeed every original
generator has first charge at least one, so I_(0,W)=0 for every W. Consequently
the charge-zero polynomial subring, with 38/28/40/28 variables respectively,
injects into R/I. Its Hilbert series is the product over exactly those variables.
Those parameters cannot be eliminated from the quotient through a nonzero
charge-zero relation in I. Sending them to zero, or to powers of another
parameter, is a specialization with a different role in a negative proof.

The c=1 section does not inherit the positive two-component grading. Retain
the bounded section space induced from R_(NC): writing a column as c^e*m sends
it to m of degree (N-e)C. Since the original c exponent is uniquely recovered
from the degree of m, this is a bijection of monomial bases and gives exactly

    H_R(NC) = sum_(k=0)^N H_Q[z](kC).

Thus removing the coordinate c via the torus section does not by itself reduce
this finite matrix's column count. The unrestricted residual-character-zero
section component is infinite. Eliminating c through its homogeneous relation
F-c is a different exact ring reduction, giving target F^N in Q[z]; its
ambient count is H_Q[z](NC), not the preceding cumulative count.

Both emitted source/artifact manifests passed `sha256sum -c`.
